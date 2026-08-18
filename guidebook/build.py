from __future__ import annotations

import html
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote


GUIDEBOOK_DIR = Path(__file__).parent
ROOT_DIR = GUIDEBOOK_DIR.parent
SOURCE_PATH = GUIDEBOOK_DIR / "content.md"
README_PATH = ROOT_DIR / "README.md"


@dataclass(frozen=True)
class Group:
    file: str
    number: str
    title: str
    summary: str
    accent: str
    chapters: tuple[str, ...]


GROUPS = (
    Group(
        "01-foundations.html",
        "01",
        "分析与基础建模",
        "从复杂度和数据表达出发，建立枚举、哈希、有序化与离线处理的基本判断框架。",
        "coral",
        ("复杂度、模拟与枚举", "数组、字符串与哈希表", "排序与分治", "离散化与离线处理"),
    ),
    Group(
        "02-linear-and-interval.html",
        "02",
        "线性与区间技巧",
        "围绕连续区间、有序边界和动态候选集合，组织高频的线性扫描工具。",
        "gold",
        ("双指针", "滑动窗口", "前缀和与差分", "二分查找", "栈、队列与单调结构", "堆与优先队列", "区间问题"),
    ),
    Group(
        "03-recursion-and-state.html",
        "03",
        "递归与状态搜索",
        "从递归契约到状态转移，覆盖链式结构、树、搜索、动态规划与贪心证明。",
        "jade",
        ("链表", "二叉树与树形递归", "DFS 与 BFS", "回溯与搜索剪枝", "动态规划", "贪心"),
    ),
    Group(
        "04-graphs-and-structures.html",
        "04",
        "图与高级数据结构",
        "处理连通性、路径查询、动态区间信息、多模式字符串和组合数据结构。",
        "blue",
        ("图论与最短路", "并查集", "树状数组", "线段树", "字典树与字符串算法", "设计题与数据结构"),
    ),
    Group(
        "05-specialized-tools.html",
        "05",
        "专项工具",
        "集中整理位运算、数论、矩阵与几何中可直接复用的专项方法。",
        "violet",
        ("位运算", "数学与数论", "矩阵与计算几何"),
    ),
)


class Slugger:
    def __init__(self) -> None:
        self.seen: dict[str, int] = {}

    def __call__(self, value: str) -> str:
        base = re.sub(r"[^\w\s-]", "", re.sub(r"<[^>]+>", "", value.lower()), flags=re.UNICODE)
        base = re.sub(r"\s+", "-", base.strip()) or "section"
        count = self.seen.get(base, 0)
        self.seen[base] = count + 1
        return base if count == 0 else f"{base}-{count}"


def extract_sections(markdown: str) -> dict[str, str]:
    matches = list(re.finditer(r"^## (.+)$", markdown, re.MULTILINE))
    return {
        match.group(1).strip(): markdown[
            match.end() + 1 : matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        ].strip()
        for index, match in enumerate(matches)
    }


def local_href(href: str) -> str:
    if re.match(r"^(?:https?:|#|mailto:)", href):
        return href
    anchor = ""
    if "#" in href:
        href, anchor = href.split("#", 1)
        anchor = f"#{quote(anchor)}"
    if "/" not in href and (href == "Problem-Catalog.md" or href.endswith((".py", ".cpp"))):
        href = f"../problems/{href}"
    return f"{quote(href, safe='/()%')}{anchor}"


def inline_markdown(value: str) -> str:
    code_fragments: list[str] = []

    def replace_code(match: re.Match[str]) -> str:
        code_fragments.append(f"<code>{html.escape(match.group(1))}</code>")
        return f"\x00CODE{len(code_fragments) - 1}\x00"

    rendered = re.sub(r"`([^`]+)`", replace_code, value)
    rendered = html.escape(rendered)

    def replace_link(match: re.Match[str]) -> str:
        label, href = match.groups()
        target = local_href(html.unescape(href))
        external = ' target="_blank" rel="noreferrer"' if target.startswith("http") else ""
        return f'<a href="{html.escape(target, quote=True)}"{external}>{label}</a>'

    rendered = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_link, rendered)
    rendered = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", rendered)
    rendered = re.sub(r"\x00CODE(\d+)\x00", lambda match: code_fragments[int(match.group(1))], rendered)
    return rendered


def is_table_divider(line: str) -> bool:
    return bool(re.fullmatch(r"\s*\|?(?:\s*:?-{3,}:?\s*\|)+\s*:?-{3,}:?\s*\|?\s*", line))


def table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def render_markdown(markdown: str, slugger: Slugger, metadata: dict[str, object]) -> str:
    lines = markdown.splitlines()
    output: list[str] = []
    index = 0
    algorithm_open = False

    def close_algorithm() -> None:
        nonlocal algorithm_open
        if algorithm_open:
            output.append("</section>")
            algorithm_open = False

    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue

        if line.startswith("```"):
            language = line[3:].strip() or "text"
            code: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].startswith("```"):
                code.append(lines[index])
                index += 1
            index += 1
            output.append(
                f'<div class="code-shell"><div class="code-label">{html.escape(language)}</div>'
                f'<pre><code>{html.escape(chr(10).join(code))}</code></pre></div>'
            )
            continue

        heading = re.match(r"^(###|####)\s+(.+)$", line)
        if heading:
            level, title = len(heading.group(1)), heading.group(2).strip()
            section_id = slugger(title)
            close_algorithm()
            if level == 3:
                metadata["modules"].append({"title": title, "id": section_id, "algorithms": []})  # type: ignore[union-attr]
                output.append(f'<h3 id="{section_id}">{inline_markdown(title)}</h3>')
            else:
                algorithm = {"title": title, "id": section_id}
                metadata["algorithms"].append(algorithm)  # type: ignore[union-attr]
                modules = metadata["modules"]  # type: ignore[assignment]
                if not modules:
                    raise ValueError(f"Algorithm '{title}' must belong to a knowledge module")
                modules[-1]["algorithms"].append(algorithm)
                output.append(
                    f'<section class="algorithm" data-search="{html.escape(title.lower())}">'
                    f'<h4 id="{section_id}">{inline_markdown(title)}'
                    f'<a class="anchor" href="#{section_id}" aria-label="定位到 {html.escape(title)}">#</a></h4>'
                )
                algorithm_open = True
            index += 1
            continue

        if index + 1 < len(lines) and "|" in line and is_table_divider(lines[index + 1]):
            headers = table_cells(line)
            index += 2
            rows: list[list[str]] = []
            while index < len(lines) and "|" in lines[index] and lines[index].strip():
                rows.append(table_cells(lines[index]))
                index += 1
            head = "".join(f"<th>{inline_markdown(cell)}</th>" for cell in headers)
            body = "".join(
                f'<tr>{"".join(f"<td>{inline_markdown(cell)}</td>" for cell in row)}</tr>' for row in rows
            )
            output.append(f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>')
            continue

        if line.startswith(">"):
            quote_lines: list[str] = []
            while index < len(lines) and lines[index].startswith(">"):
                quote_lines.append(re.sub(r"^>\s?", "", lines[index]))
                index += 1
            output.append(f'<blockquote>{"<br>".join(map(inline_markdown, quote_lines))}</blockquote>')
            continue

        if re.match(r"^[-*]\s+", line):
            items: list[str] = []
            while index < len(lines) and (re.match(r"^\s*[-*]\s+", lines[index]) or re.match(r"^\s{2,}\S", lines[index])):
                item = re.sub(r"^\s*[-*]\s+", "", lines[index])
                if item == lines[index] and items:
                    items[-1] += f" {lines[index].strip()}"
                else:
                    items.append(item)
                index += 1
            output.append(f'<ul>{"".join(f"<li>{inline_markdown(item)}</li>" for item in items)}</ul>')
            continue

        if re.match(r"^\d+\.\s+", line):
            items = []
            while index < len(lines) and re.match(r"^\d+\.\s+", lines[index]):
                items.append(re.sub(r"^\d+\.\s+", "", lines[index]))
                index += 1
            output.append(f'<ol>{"".join(f"<li>{inline_markdown(item)}</li>" for item in items)}</ol>')
            continue

        paragraph = [line.strip()]
        index += 1
        while (
            index < len(lines)
            and lines[index].strip()
            and not re.match(r"^(?:###|####|```|>|[-*]\s+|\d+\.\s+)", lines[index])
            and not (index + 1 < len(lines) and "|" in lines[index] and is_table_divider(lines[index + 1]))
        ):
            paragraph.append(lines[index].strip())
            index += 1
        output.append(f'<p>{inline_markdown(" ".join(paragraph))}</p>')

    close_algorithm()
    return "\n".join(output)


def page_shell(title: str, description: str, body: str, sidebar: str = "", page_class: str = "", accent: str = "coral") -> str:
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{html.escape(description, quote=True)}">
  <title>{html.escape(title)} · LeetCode Guidebook</title>
  <link rel="stylesheet" href="assets/style.css">
  <link rel="preconnect" href="https://cdn.jsdelivr.net">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
</head>
<body class="{page_class}" data-accent="{accent}">
  <a class="skip-link" href="#main-content">跳到正文</a>
  {sidebar}
  {body}
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
  <script defer src="assets/app.js"></script>
</body>
</html>'''


def render_group(group: Group, sections: dict[str, str], group_index: int) -> dict[str, object]:
    slugger = Slugger()
    chapter_metadata: list[dict[str, object]] = []
    chapter_html: list[str] = []

    for chapter_title in group.chapters:
        if chapter_title not in sections:
            raise ValueError(f"Missing chapter: {chapter_title}")
        chapter_id = slugger(chapter_title)
        metadata: dict[str, object] = {"title": chapter_title, "id": chapter_id, "modules": [], "algorithms": []}
        rendered = render_markdown(sections[chapter_title], slugger, metadata)
        chapter_metadata.append(metadata)
        chapter_html.append(
            f'<section class="chapter" id="{chapter_id}" data-search="{html.escape(chapter_title.lower())}">'
            f'<div class="chapter-index">{len(chapter_metadata):02d}</div><h2>{html.escape(chapter_title)}</h2>{rendered}</section>'
        )

    navigation_parts: list[str] = []
    for chapter in chapter_metadata:
        module_parts: list[str] = []
        for module in chapter["modules"]:  # type: ignore[union-attr]
            algorithm_links = "".join(
                f'<a class="side-algorithm" href="#{algorithm["id"]}">{html.escape(algorithm["title"])}</a>'
                for algorithm in module["algorithms"]
            )
            module_parts.append(
                f'<details class="side-module"><summary><span>{html.escape(module["title"])}</span>'
                f'<small>{len(module["algorithms"])}</small></summary>'
                f'<div class="side-algorithms">{algorithm_links}</div></details>'
            )
        navigation_parts.append(
            f'<details class="side-chapter"><summary><span>{html.escape(str(chapter["title"]))}</span>'
            f'<small>{len(chapter["algorithms"])}</small></summary>'  # type: ignore[arg-type]
            f'<div class="side-branch"><a class="side-overview" href="#{chapter["id"]}">章节概览</a>'
            f'{"".join(module_parts)}</div></details>'
        )
    navigation = "".join(navigation_parts)
    sidebar = f'''<aside class="sidebar">
    <a class="brand" href="main.html"><span class="brand-mark">LC</span><span>Algorithm<br>Guidebook</span></a>
    <div class="side-label">本册目录</div><nav>{navigation}</nav>
    <a class="back-map" href="main.html">返回完整思维导图</a>
  </aside>'''
    previous_group = GROUPS[group_index - 1] if group_index > 0 else None
    next_group = GROUPS[group_index + 1] if group_index + 1 < len(GROUPS) else None
    previous_link = (
        f'<a href="{previous_group.file}"><small>上一册</small><strong>{html.escape(previous_group.title)}</strong></a>'
        if previous_group else "<span></span>"
    )
    next_link = (
        f'<a class="next" href="{next_group.file}"><small>下一册</small><strong>{html.escape(next_group.title)}</strong></a>'
        if next_group else ""
    )
    algorithm_count = sum(len(chapter["algorithms"]) for chapter in chapter_metadata)  # type: ignore[arg-type]
    body = f'''<main id="main-content" class="reader">
    <header class="reader-head">
      <div class="reader-actions"><a href="main.html">思维导图</a><label class="search"><span>搜索本册</span><input type="search" data-search-input placeholder="输入算法或知识点"></label></div>
      <div class="edition">VOLUME {group.number}</div><h1>{html.escape(group.title)}</h1><p>{html.escape(group.summary)}</p>
      <div class="reader-stats"><span>{len(group.chapters)} 个题型</span><span>{algorithm_count} 个典型算法</span></div>
    </header>
    <div class="no-results" data-no-results hidden>没有匹配的算法，请尝试更短的关键词。</div>
    {"".join(chapter_html)}
    <nav class="pager" aria-label="分册导航">{previous_link}{next_link}</nav>
  </main>'''
    (GUIDEBOOK_DIR / group.file).write_text(
        page_shell(group.title, group.summary, body, sidebar, "reader-page", group.accent), encoding="utf-8"
    )
    return {"group": group, "chapters": chapter_metadata}


def render_main(rendered_groups: list[dict[str, object]]) -> None:
    total_algorithms = 0
    branches: list[str] = []
    for rendered_group in rendered_groups:
        group: Group = rendered_group["group"]  # type: ignore[assignment]
        chapters: list[dict[str, object]] = rendered_group["chapters"]  # type: ignore[assignment]
        chapter_blocks = []
        for chapter in chapters:
            algorithms: list[dict[str, str]] = chapter["algorithms"]  # type: ignore[assignment]
            modules: list[dict[str, str]] = chapter["modules"]  # type: ignore[assignment]
            total_algorithms += len(algorithms)
            search_text = " ".join(
                [str(chapter["title"]), *(module["title"] for module in modules), *(algorithm["title"] for algorithm in algorithms)]
            ).lower()
            algorithm_links = "".join(
                f'<a class="algorithm-link" href="{group.file}#{algorithm["id"]}">{html.escape(algorithm["title"])}</a>'
                for algorithm in algorithms
            )
            chapter_blocks.append(
                f'<div class="map-chapter" data-search="{html.escape(search_text, quote=True)}">'
                f'<a class="chapter-link" href="{group.file}#{chapter["id"]}"><span>{html.escape(str(chapter["title"]))}</span>'
                f'<b>{len(algorithms)}</b></a><div class="algorithm-links">{algorithm_links}</div></div>'
            )
        branches.append(
            f'<section class="map-branch" data-accent="{group.accent}"><div class="branch-head">'
            f'<span class="branch-number">{group.number}</span><div><h2><a href="{group.file}">{html.escape(group.title)}</a></h2>'
            f'<p>{html.escape(group.summary)}</p></div></div><div class="branch-line" aria-hidden="true"></div>'
            f'<div class="branch-chapters">{"".join(chapter_blocks)}</div></section>'
        )

    body = f'''<header class="map-head">
    <nav><span class="wordmark">LEETCODE / PYTHON</span><a href="../README.md">README</a></nav>
    <div class="map-title"><div><div class="eyebrow">ALGORITHM KNOWLEDGE ATLAS</div><h1>算法学习<br><em>完整思维导图</em></h1></div><p>从问题约束出发，沿五条学习主线定位知识模块、算法模板与本地 LeetCode 题解。点击任意算法即可进入对应分册。</p></div>
    <div class="map-toolbar"><label class="search map-search"><span>筛选知识图谱</span><input type="search" data-map-search placeholder="例如：LCA、滑动窗口、Manacher"></label><div class="map-count"><strong>26</strong><span>题目类型</span><strong>{total_algorithms}</strong><span>典型算法</span></div></div>
  </header>
  <main id="main-content" class="mind-map"><div class="map-root"><span>START</span><strong>约束 → 结构 → 算法</strong></div><div class="map-empty" data-map-empty hidden>没有匹配项，换一个关键词试试。</div>{"".join(branches)}</main>
  <footer><span>LeetCode Algorithm Guidebook</span><span>Python-first · Generated from content.md</span></footer>'''
    (GUIDEBOOK_DIR / "main.html").write_text(
        page_shell("算法学习完整思维导图", "LeetCode Python 算法知识图谱与完整学习手册", body, page_class="map-page"),
        encoding="utf-8",
    )


def main() -> None:
    if not SOURCE_PATH.exists():
        shutil.copyfile(README_PATH, SOURCE_PATH)
    source = SOURCE_PATH.read_text(encoding="utf-8").replace("\r\n", "\n")
    sections = extract_sections(source)
    expected_chapters = {chapter for group in GROUPS for chapter in group.chapters}
    missing = expected_chapters - sections.keys()
    if missing:
        raise ValueError(f"Missing chapters: {', '.join(sorted(missing))}")

    rendered_groups = [render_group(group, sections, index) for index, group in enumerate(GROUPS)]
    render_main(rendered_groups)
    assets_dir = GUIDEBOOK_DIR / "assets"
    missing_assets = [name for name in ("style.css", "app.js") if not (assets_dir / name).exists()]
    if missing_assets:
        raise FileNotFoundError(f"Missing site assets: {', '.join(missing_assets)}")
    algorithm_count = sum(
        len(chapter["algorithms"])  # type: ignore[arg-type]
        for rendered_group in rendered_groups
        for chapter in rendered_group["chapters"]  # type: ignore[union-attr]
    )
    print(f"Generated 6 pages: {len(expected_chapters)} chapters, {algorithm_count} algorithms.")


if __name__ == "__main__":
    main()
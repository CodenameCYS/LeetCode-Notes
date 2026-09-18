# LeetCode 做题笔记

这是我的 LeetCode 算法练习仓库，目前以 **Python** 为主要语言；历史 C++ 代码保留作思路对照。

## 题目与算法考点总表

[problems/Problem-Catalog.md](problems/Problem-Catalog.md) 收录 `problems/` 下全部 **2646 份 Git 已跟踪的 Python / C++ 源码**，按题号与规范化题名合并为 **2642 条记录**。总表中的难易度来自 LeetCode 官方元数据；算法考点以本地源码的实际实现为主，并以官方题目标签补充，而非只套用题目的常见标准解法。

总表负责完整覆盖，Guidebook 负责教学精选：同一道题可以出现在总表中，但只有实现能清晰体现方法、边界和复杂度时，才会作为手册例题。

## 算法学习手册

完整知识体系已整理为可浏览的静态 Guidebook，包含 **26 个题目类型、104 个典型算法**，以及每个算法的核心原理、Python 模板、复杂度、易错点和官方题目链接。

### [打开算法学习完整思维导图 →](guidebook/main.html)

主页面支持按算法名称或知识点筛选；点击思维导图中的节点，可直接进入对应分册和算法位置。

| 学习路径 | 覆盖内容 |
| --- | --- |
| 分析与基础建模 | 复杂度、模拟、数组与哈希、排序与分治、离散化 |
| 线性与区间技巧 | 双指针、滑动窗口、前缀和、二分、单调结构、堆、区间 |
| 递归与状态搜索 | 链表、二叉树、DFS / BFS、回溯、动态规划、贪心 |
| 图与高级数据结构 | 图论（Dijkstra、Floyd-Warshall 等）、并查集、树状数组、线段树、字符串算法、设计题 |
| 专项工具 | 位运算、数学与数论、矩阵与计算几何 |

## 使用方式

- 从 [problems/Problem-Catalog.md](problems/Problem-Catalog.md) 按题号查找全部本地实现及算法考点。
- 从 [guidebook/main.html](guidebook/main.html) 按知识依赖浏览完整思维导图。
- 在各分册顶部搜索算法或概念，例如 `LCA`、`Manacher`、`滑动窗口`。
- 例题链接会打开 LeetCode 官方题目页；文档中的状态标签说明本地实现与模板的对应程度。

## 内容维护

题目总表作为本仓库的整理结果保存在 [problems/Problem-Catalog.md](problems/Problem-Catalog.md)，与 `problems/` 中的源码一同维护。这个干净版本不包含原始目录使用的元数据抓取与总表生成脚本。

Guidebook 的完整 Markdown 源稿位于 [guidebook/content.md](guidebook/content.md)，静态页面由 [guidebook/build.py](guidebook/build.py) 生成：

```powershell
python .\guidebook\build.py
```

修改知识手册时请编辑 `guidebook/content.md`，然后重新运行构建脚本；不要直接修改生成的 HTML。生成结果无需服务器，可直接在浏览器打开。

## 许可

本仓库采用[个人学习非商业许可证](LICENSE)：允许个人学习、研究、修改和非商业分享；未经书面许可，禁止将仓库内容或其衍生内容用于任何商业化用途。
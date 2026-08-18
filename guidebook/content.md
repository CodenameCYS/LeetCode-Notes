# LeetCode 做题笔记

本仓库收录了 2600 余份 Python / C++ 题解，完整清单及源码分析见[题目与算法考点总表](../problems/Problem-Catalog.md)。本文以 **Python 学习与复习**为主线，只选取能清晰体现方法、实现质量和边界条件的代表题；早期 C++ 题解保留作历史实现和思路参考。分类与例题说明均以本地源码的真实实现为依据，不因题号新或提交时间近而自动收录。

> 一道题往往同时涉及多个知识点。例如「滑动窗口最大值」既属于滑动窗口，也使用单调队列；本文将它放在最有辨识度的主分类下。全文统一采用“**题目类型 → 知识模块 → 典型算法**”三级知识结构；典型算法说明包含原理、Python 模板、复杂度、易错点和对应例题。

## 知识地图与选型速查

算法学习不应从背模板开始，而应先完成三次判断：**数据规模允许什么复杂度、题目要求维护什么不变量、数据是否会在线修改**。下面按学习依赖将全文分成五组：

1. **分析与基础建模**：复杂度、模拟与枚举；数组、字符串与哈希表；排序与分治；离散化与离线处理。
2. **线性与区间技巧**：双指针、滑动窗口、前缀和与差分、二分查找、栈与单调结构、堆、区间问题。
3. **递归与状态搜索**：链表、二叉树、DFS / BFS、回溯、动态规划、贪心。
4. **图与高级数据结构**：图论、并查集、树状数组、线段树、Trie 与字符串算法、设计题。
5. **专项工具**：位运算、数学与数论、矩阵与计算几何。

### 约束到复杂度

| 典型规模 | 常见可接受复杂度 | 首先考虑 |
| --- | --- | --- |
| $n \le 20$ | $O(2^n)$、$O(n2^n)$ | 子集枚举、状态压缩 DP、折半搜索 |
| $n \le 10^2$ | $O(n^3)$ | 区间 DP、Floyd-Warshall |
| $n \le 10^3$ | $O(n^2)$ | 二维 DP、枚举分割点 |
| $n \le 10^5$ | $O(n\log n)$ | 排序、二分、堆、树状数组、线段树 |
| $n \le 10^6$ | $O(n)$ 或低常数 $O(n\log n)$ | 双指针、滑窗、前缀和、线性筛 |

规模只是起点，还要结合语言常数、测试组数、状态维度和内存限制；例如 $10^5$ 个节点各保存 26 个整数，空间已经是 $O(26n)$。

### 操作到结构

| 需求 | 优先方法 | 关键前提 |
| --- | --- | --- |
| 静态区间和 / 频次 | 前缀和 | 无在线修改 |
| 多次区间加、最后统一查询 | 差分 | 可离线还原 |
| 单点修改 + 前缀 / 区间和 | 树状数组 | 信息可由前缀作差 |
| 动态区间最值或复杂合并 | 线段树 | 合并满足结合律 |
| 静态区间 `min / max / gcd` | 稀疏表 | 幂等运算，无修改 |
| 第一个可行值 / 最小化最大值 | 二分答案 | 判定函数具有单调性 |
| 动态取得全局最优候选 | 堆 | 只需堆顶，不要求整体有序 |
| 动态前驱、后继与排名 | 平衡树 / 有序集合 | Python `list + bisect` 插入仍为 $O(n)$ |
| 无权 / 0-1 / 非负权最短路 | BFS / 0-1 BFS / Dijkstra | 按边权范围选择 |
| 只增加边的连通性 | 并查集 | 不直接支持在线删边 |

## 目录

- [LeetCode 做题笔记](#leetcode-做题笔记)
  - [知识地图与选型速查](#知识地图与选型速查)
    - [约束到复杂度](#约束到复杂度)
    - [操作到结构](#操作到结构)
  - [目录](#目录)
  - [复杂度、模拟与枚举](#复杂度模拟与枚举)
    - [候选空间建模](#候选空间建模)
      - [按频次枚举去重子集](#按频次枚举去重子集)
      - [分组枚举](#分组枚举)
    - [大索引定位](#大索引定位)
      - [按贡献分段定位第 K 项](#按贡献分段定位第-k-项)
    - [状态模拟](#状态模拟)
      - [显式状态机与边界推进](#显式状态机与边界推进)
      - [新旧状态隔离](#新旧状态隔离)
  - [数组、字符串与哈希表](#数组字符串与哈希表)
    - [哈希键与频次](#哈希键与频次)
      - [规范化键分组](#规范化键分组)
      - [频次统计与排序取 Top K](#频次统计与排序取-top-k)
    - [常数空间扫描](#常数空间扫描)
      - [Boyer-Moore 多数投票](#boyer-moore-多数投票)
  - [双指针](#双指针)
    - [有序数组上的相向指针](#有序数组上的相向指针)
      - [排序后左右夹逼](#排序后左右夹逼)
      - [从两端逆序构造答案](#从两端逆序构造答案)
    - [子序列匹配](#子序列匹配)
      - [左右极限匹配](#左右极限匹配)
    - [原地覆盖](#原地覆盖)
      - [读写指针压缩数组](#读写指针压缩数组)
  - [滑动窗口](#滑动窗口)
    - [固定长度窗口](#固定长度窗口)
      - [入一个、出一个的滚动维护](#入一个出一个的滚动维护)
    - [单调约束窗口](#单调约束窗口)
      - [最长合法窗口](#最长合法窗口)
      - [最短可行窗口](#最短可行窗口)
    - [子数组计数](#子数组计数)
      - [两个边界计数恰好满足](#两个边界计数恰好满足)
  - [前缀和与差分](#前缀和与差分)
    - [静态区间聚合](#静态区间聚合)
      - [一维前缀和](#一维前缀和)
    - [前缀状态计数](#前缀状态计数)
      - [前缀和加哈希表](#前缀和加哈希表)
      - [前缀不等式与有序计数](#前缀不等式与有序计数)
    - [离线区间修改](#离线区间修改)
      - [一维与二维差分](#一维与二维差分)
  - [排序与分治](#排序与分治)
    - [稳定排序与分治合并](#稳定排序与分治合并)
      - [归并排序](#归并排序)
    - [排序规则设计](#排序规则设计)
      - [自定义比较器与排序键](#自定义比较器与排序键)
    - [顺序统计量](#顺序统计量)
      - [快速选择](#快速选择)
  - [离散化与离线处理](#离散化与离线处理)
    - [值域压缩](#值域压缩)
      - [排序去重离散化](#排序去重离散化)
    - [单调事件扫描](#单调事件扫描)
      - [按阈值离线激活](#按阈值离线激活)
  - [二分查找](#二分查找)
    - [有序序列边界](#有序序列边界)
      - [左边界与右边界二分](#左边界与右边界二分)
    - [单调可行性](#单调可行性)
      - [二分最小可行答案](#二分最小可行答案)
    - [局部有序数组](#局部有序数组)
      - [旋转数组二分](#旋转数组二分)
  - [栈、队列与单调结构](#栈队列与单调结构)
    - [后进先出状态](#后进先出状态)
      - [栈模拟与嵌套解析](#栈模拟与嵌套解析)
    - [最近边界与贡献](#最近边界与贡献)
      - [单调栈](#单调栈)
    - [滑动窗口极值](#滑动窗口极值)
      - [单调队列](#单调队列)
  - [堆与优先队列](#堆与优先队列)
    - [有界候选集合](#有界候选集合)
      - [Top K 小顶堆](#top-k-小顶堆)
    - [有序候选扩展](#有序候选扩展)
      - [多路归并](#多路归并)
    - [资源调度](#资源调度)
      - [双堆事件调度](#双堆事件调度)
  - [树状数组](#树状数组)
    - [动态前缀聚合](#动态前缀聚合)
      - [单点增加与区间求和](#单点增加与区间求和)
    - [有序频次统计](#有序频次统计)
      - [离散化加树状数组计数](#离散化加树状数组计数)
  - [线段树](#线段树)
    - [基础动态区间信息](#基础动态区间信息)
      - [单点修改与普通区间查询](#单点修改与普通区间查询)
    - [多字段节点状态](#多字段节点状态)
      - [复杂节点合并](#复杂节点合并)
    - [批量区间修改](#批量区间修改)
      - [懒标记区间加](#懒标记区间加)
  - [链表](#链表)
    - [指针重连](#指针重连)
      - [虚拟头节点与区间反转](#虚拟头节点与区间反转)
      - [成环后断链](#成环后断链)
    - [结构定位与复制](#结构定位与复制)
      - [快慢指针找中点](#快慢指针找中点)
      - [哈希映射复制复杂链表](#哈希映射复制复杂链表)
    - [排序与合并](#排序与合并)
      - [链表归并排序](#链表归并排序)
  - [二叉树与树形递归](#二叉树与树形递归)
    - [树的遍历与递归契约](#树的遍历与递归契约)
      - [前序、中序与后序 DFS](#前序中序与后序-dfs)
      - [层序 BFS](#层序-bfs)
    - [二叉搜索树](#二叉搜索树)
      - [中序有序性与 BST 操作](#中序有序性与-bst-操作)
    - [树形 DP](#树形-dp)
      - [后序状态合并](#后序状态合并)
    - [最近公共祖先 LCA](#最近公共祖先-lca)
      - [二叉树后序递归 LCA](#二叉树后序递归-lca)
      - [最深叶节点集合的 LCA](#最深叶节点集合的-lca)
    - [倍增与 Binary Lifting](#倍增与-binary-lifting)
      - [第 K 个祖先](#第-k-个祖先)
      - [倍增 LCA](#倍增-lca)
  - [图论与最短路](#图论与最短路)
    - [有向无环图](#有向无环图)
      - [Kahn 拓扑排序](#kahn-拓扑排序)
    - [特殊边权最短路](#特殊边权最短路)
      - [BFS 与 0-1 BFS](#bfs-与-0-1-bfs)
    - [多源最短路](#多源最短路)
      - [Floyd-Warshall](#floyd-warshall)
    - [非负权最短路](#非负权最短路)
      - [堆优化 Dijkstra](#堆优化-dijkstra)
    - [全局连通代价](#全局连通代价)
      - [Kruskal 最小生成树](#kruskal-最小生成树)
  - [并查集](#并查集)
    - [动态连通性](#动态连通性)
      - [路径压缩与按大小合并](#路径压缩与按大小合并)
    - [多集合建模](#多集合建模)
      - [坐标映射与多份并查集](#坐标映射与多份并查集)
  - [DFS 与 BFS](#dfs-与-bfs)
    - [网格与连通块](#网格与连通块)
      - [网格 DFS / Flood Fill](#网格-dfs--flood-fill)
    - [同步扩散](#同步扩散)
      - [多源 BFS](#多源-bfs)
    - [隐式状态图](#隐式状态图)
      - [状态图 BFS](#状态图-bfs)
  - [回溯与搜索剪枝](#回溯与搜索剪枝)
    - [选择路径](#选择路径)
      - [选择、递归与撤销](#选择递归与撤销)
    - [重复候选](#重复候选)
      - [排序与同层去重](#排序与同层去重)
    - [可行性边界](#可行性边界)
      - [上下界与对称性剪枝](#上下界与对称性剪枝)
  - [动态规划](#动态规划)
    - [一维依赖](#一维依赖)
      - [线性 DP 与滚动状态](#线性-dp-与滚动状态)
    - [容量选择](#容量选择)
      - [0-1 背包与完全背包](#0-1-背包与完全背包)
    - [序列对齐](#序列对齐)
      - [双序列 DP](#双序列-dp)
    - [区间合并](#区间合并)
      - [区间 DP](#区间-dp)
    - [线性区间扩张](#线性区间扩张)
      - [从起点向两端扩张](#从起点向两端扩张)
    - [子集状态](#子集状态)
      - [状态压缩 DP](#状态压缩-dp)
  - [贪心](#贪心)
    - [区间选择](#区间选择)
      - [最早结束时间贪心](#最早结束时间贪心)
    - [排序配对](#排序配对)
      - [同序配对与交换论证](#同序配对与交换论证)
    - [候选支配](#候选支配)
      - [保留支配候选](#保留支配候选)
    - [连续覆盖](#连续覆盖)
      - [当前可达范围内延伸最远](#当前可达范围内延伸最远)
    - [局部贡献](#局部贡献)
      - [峰谷替换与正增量累加](#峰谷替换与正增量累加)
  - [区间问题](#区间问题)
    - [区间归并](#区间归并)
      - [按左端点排序合并](#按左端点排序合并)
    - [无权区间调度](#无权区间调度)
      - [最早结束时间贪心](#最早结束时间贪心-1)
    - [重叠计数](#重叠计数)
      - [事件扫描线](#事件扫描线)
    - [加权区间选择](#加权区间选择)
      - [二分前驱加动态规划](#二分前驱加动态规划)
  - [字典树与字符串算法](#字典树与字符串算法)
    - [前缀结构](#前缀结构)
      - [Trie 前缀树](#trie-前缀树)
    - [单模式字符串匹配](#单模式字符串匹配)
      - [KMP 前缀函数](#kmp-前缀函数)
      - [Z 函数](#z-函数)
      - [滚动哈希](#滚动哈希)
    - [回文字符串](#回文字符串)
      - [回文中心扩展](#回文中心扩展)
      - [Manacher 算法](#manacher-算法)
    - [多模式匹配](#多模式匹配)
      - [AC 自动机](#ac-自动机)
  - [位运算](#位运算)
    - [异或消元](#异或消元)
      - [异或分组与位状态机](#异或分组与位状态机)
    - [二进制最低位](#二进制最低位)
      - [lowbit 与位计数 DP](#lowbit-与位计数-dp)
    - [小集合状态压缩](#小集合状态压缩)
      - [位掩码与子集枚举](#位掩码与子集枚举)
    - [按位最优选择](#按位最优选择)
      - [01 Trie 最大异或](#01-trie-最大异或)
  - [数学与数论](#数学与数论)
    - [整除关系](#整除关系)
      - [欧几里得与扩展欧几里得](#欧几里得与扩展欧几里得)
    - [幂与模运算](#幂与模运算)
      - [二进制快速幂](#二进制快速幂)
    - [素数预处理](#素数预处理)
      - [埃氏筛](#埃氏筛)
    - [组合计数](#组合计数)
      - [阶乘逆元求组合数](#阶乘逆元求组合数)
  - [设计题与数据结构](#设计题与数据结构)
    - [接口摊还分析](#接口摊还分析)
      - [双栈队列](#双栈队列)
    - [随机访问与删除](#随机访问与删除)
      - [动态数组加哈希索引](#动态数组加哈希索引)
    - [多容器协作](#多容器协作)
      - [堆加多栈与延迟清理](#堆加多栈与延迟清理)
    - [时间版本索引](#时间版本索引)
      - [哈希表加有序时间轴二分](#哈希表加有序时间轴二分)
  - [矩阵与计算几何](#矩阵与计算几何)
    - [坐标顺序建模](#坐标顺序建模)
      - [边界收缩与方向遍历](#边界收缩与方向遍历)
    - [矩形聚合与更新](#矩形聚合与更新)
      - [二维前缀和与二维差分](#二维前缀和与二维差分)
    - [网格状态转移](#网格状态转移)
      - [矩阵 DP](#矩阵-dp)
    - [平面方向判定](#平面方向判定)
      - [叉积与有向面积](#叉积与有向面积)
  - [推荐复习顺序](#推荐复习顺序)
  - [使用说明](#使用说明)

## 复杂度、模拟与枚举

先用约束估算允许的候选数量，再决定模拟、直接枚举还是改变枚举对象。复杂度分析不仅要数循环，还要计入排序、哈希、切片、列表中间插入等隐藏成本。

### 候选空间建模

#### 按频次枚举去重子集

**解决什么**：输入包含重复元素时，生成所有不同子集；也适合“每种物品可选 $0$ 到若干次”的有限选择模型。

**核心原理**：先统计每个值出现次数。处理值 `value` 时，对已有每个子集分别追加 $0,1,\ldots,count[value]$ 个该值，从构造方式上消除重复。候选总数仍决定运行时间，无法比输出规模更快。

```python
from collections import Counter

def subsets_with_duplicates(nums):
  subsets = [[]]
  for value, frequency in Counter(nums).items():
    subsets = [
      subset + [value] * copies
      for subset in subsets
      for copies in range(frequency + 1)
    ]
  return subsets
```

**复杂度**：若不同值频次为 $c_1,\ldots,c_m$，子集数为 $S=\prod(c_i+1)$；构造结果的时间和输出空间均为 $O(nS)$，辅助状态为 $O(S)$。

**易错点**：不能把含重复元素的每个位置独立选或不选后直接返回，否则会产生重复子集；复杂度应包含复制子集列表的成本。

**对应例题**：Python 实证：[90. Subsets II](https://leetcode.com/problems/subsets-ii/)

#### 分组枚举

**解决什么**：多组元素组合、四数计数或可拆成两半的等式，使朴素 $O(n^4)$ 枚举降维。

**核心原理**：分别枚举两半的组合结果，用哈希表记录一侧的和及出现次数，再在另一侧查询补数。关键是选择规模接近的分组，避免某一侧状态数过大。

```python
from collections import Counter

def four_sum_count(first, second, third, fourth, target=0):
  left_sums = Counter(a + b for a in first for b in second)
  return sum(
    left_sums[target - c - d]
    for c in third
    for d in fourth
  )
```

**复杂度**：四个数组长度均为 $n$ 时，时间 $O(n^2)$，空间 $O(n^2)$；实际空间取决于不同两数和的数量。

**易错点**：计数题必须保存频次而非只保存集合；不要漏算重复下标组合；若分组规模不均，应让较小状态空间进入哈希表。

**对应例题**：Python 实证：[454. 4Sum II](https://leetcode.com/problems/4sum-ii/)

### 大索引定位

#### 按贡献分段定位第 K 项

**解决什么**：在由数字、区间或重复块拼接成的超长甚至无限序列中定位第 $k$ 项，而 $k$ 大到不能实际生成前缀。

**核心原理**：把结构相同的元素归为一段，先计算整段贡献并不断跳过；目标落入某段后，再用整除和取模定位段内对象及对象内偏移。若块内顺序会周期性翻转，最后只需把逻辑编号映射到实际编号。

```python
def kth_digit_in_positive_integers(k):
  digits = 1
  count = 9
  start = 1
  while k > digits * count:
    k -= digits * count
    digits += 1
    count *= 10
    start *= 10
  number = start + (k - 1) // digits
  offset = (k - 1) % digits
  return int(str(number)[offset])
```

**复杂度**：十进制整数串中只需跨过 $O(\log k)$ 个长度段，时间 $O(\log k)$，辅助空间 $O(1)$；最终转成字符串需要 $O(\log k)$ 空间。

**易错点**：先把 1-indexed 的 $k$ 转成段内 0-indexed 偏移可减少整除边界错误；段贡献可能溢出定宽整数；块编号与块内方向是两层映射，不要在跳段时混在一起。

**对应例题**：Python 实证：[4022. K-th Digit in Infinite String](https://leetcode.com/problems/k-th-digit-in-infinite-string/)：先按数字长度跳段，再根据十个整数一组的奇偶性反射块内编号。

### 状态模拟

#### 显式状态机与边界推进

**解决什么**：按方向移动、分层遍历矩阵、处理带阶段切换的流程模拟。

**核心原理**：把位置、方向、边界和终止条件都写成状态。以螺旋矩阵为例，每走完一条边就收缩对应边界，从而保证每个位置只处理一次。

```python
def spiral_order(matrix):
  if not matrix or not matrix[0]:
    return []
  top, bottom = 0, len(matrix) - 1
  left, right = 0, len(matrix[0]) - 1
  answer = []
  while top <= bottom and left <= right:
    answer.extend(matrix[top][left:right + 1])
    top += 1
    for row in range(top, bottom + 1):
      answer.append(matrix[row][right])
    right -= 1
    if top <= bottom:
      answer.extend(reversed(matrix[bottom][left:right + 1]))
      bottom -= 1
    if left <= right:
      for row in range(bottom, top - 1, -1):
        answer.append(matrix[row][left])
      left += 1
  return answer
```

**复杂度**：$m\times n$ 矩阵的时间为 $O(mn)$；除返回结果外辅助空间 $O(1)$。

**易错点**：单行或单列矩阵在反向遍历前必须再次检查边界；每轮循环应收缩至少一条边界，防止重复访问或死循环。

**对应例题**：C++ 历史实现：[54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)；本地实现使用方向与访问矩阵，额外空间为 $O(mn)$。

#### 新旧状态隔离

**解决什么**：所有位置需要基于同一轮旧状态同时更新，例如元胞自动机、棋盘演化和多源扩散的一轮转移。

**核心原理**：读取时只能看到旧状态。最直接的方法是写入副本；若状态值很少，也可用编码同时保存旧值与新值，扫描结束后统一还原。

```python
def update_board(board, transition):
  rows, cols = len(board), len(board[0])
  next_board = [[0] * cols for _ in range(rows)]
  for row in range(rows):
    for col in range(cols):
      next_board[row][col] = transition(board, row, col)
  for row in range(rows):
    board[row][:] = next_board[row]
```

**复杂度**：$m\times n$ 网格的一轮更新时间 $O(mn)$，副本空间 $O(mn)$；有限状态原地编码可把辅助空间降为 $O(1)$。

**易错点**：边扫描边覆盖会让后面的格子读到新状态；原地编码时，邻居统计必须提取旧状态位；边界邻居不能越界。

**对应例题**：C++ 历史实现：[289. Game of Life](https://leetcode.com/problems/game-of-life/)；本地实现使用完整下一代副本，并非原地编码。

**补充练习**：

- [2048. Next Greater Numerically Balanced Number](https://leetcode.com/problems/next-greater-numerically-balanced-number/)：Python 本地实现预先列出合法数字组成，再枚举其不同排列。

## 数组、字符串与哈希表

数组题先定义下标与已处理区间的不变量；哈希表则要先定义“哪些对象应视为等价”，再把这个等价关系编码成不可变键。

### 哈希键与频次

#### 规范化键分组

**解决什么**：按异位词、组成成分或其他等价关系给对象分组。

**核心原理**：把每个对象转换成唯一的规范化键。小写英文字母异位词可以使用长度为 26 的频次数组转成元组；同一键下的原对象加入同一组。

```python
from collections import defaultdict

def group_anagrams(words):
  groups = defaultdict(list)
  for word in words:
    frequency = [0] * 26
    for char in word:
      frequency[ord(char) - ord("a")] += 1
    groups[tuple(frequency)].append(word)
  return list(groups.values())
```

**复杂度**：所有字符串总长度为 $L$ 时，时间 $O(L)$，除返回结果外键空间 $O(26g)$，其中 $g$ 为分组数。

**易错点**：列表不可哈希，必须转成元组；字符集不是固定小写字母时，应改用排序串或排序后的 `(字符, 次数)` 元组；键必须保留完整等价信息。

**对应例题**：Python 实证：[49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

#### 频次统计与排序取 Top K

**解决什么**：寻找出现次数最多的元素、按频率排序或输出高频候选。

**核心原理**：先用哈希表完成一次频次统计，再只对不同元素排序。若只需前 $k$ 个且不同元素很多，可进一步改用大小为 $k$ 的堆或桶排序。

```python
from collections import Counter

def top_k_frequent(nums, k):
  frequency = Counter(nums)
  ordered = sorted(frequency, key=frequency.get, reverse=True)
  return ordered[:k]
```

**复杂度**：设数组长度为 $n$、不同元素数为 $u$，时间 $O(n+u\log u)$，空间 $O(u)$。

**易错点**：排序的是不同元素而非原数组；该模板不满足要求严格优于 $O(n\log n)$ 的最强约束，届时应使用堆或桶；并列频率的输出顺序需按题意处理。

**对应例题**：Python 实证：[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)，本地实现正是频次表加全排序。

### 常数空间扫描

#### Boyer-Moore 多数投票

**解决什么**：在线性时间、常数空间内寻找出现次数超过一半的元素。

**核心原理**：不同元素两两抵消。严格多数元素比其余所有元素总数还多，因此抵消结束后必然成为候选；若题目不保证多数元素存在，还需第二次扫描验证。

```python
def majority_element(nums):
  candidate = None
  votes = 0
  for value in nums:
    if votes == 0:
      candidate = value
    votes += 1 if value == candidate else -1
  return candidate
```

**复杂度**：时间 $O(n)$，辅助空间 $O(1)$；需要验证时仍为 $O(n)$ 时间。

**易错点**：投票结果只是候选，只有题目保证多数存在时才能直接返回；“超过一半”与“出现次数最多”不是同一条件；扩展到超过 $n/3$ 时需维护两个候选。

**对应例题**：C++ 历史实现：[169. Majority Element](https://leetcode.com/problems/majority-element/)

**补充练习**：

- [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)：Python 本地实现是以字典存父节点的并查集，不是经典哈希集合起点扩展法。
- [454. 4Sum II](https://leetcode.com/problems/4sum-ii/)：分组枚举与补数频次，主讲见上一章。
- [706. Design HashMap](https://leetcode.com/problems/design-hashmap/)：Python 本地文件直接包装内置 `dict`，不是桶与冲突处理的手写哈希表。
- [3719. Longest Balanced Subarray I](https://leetcode.com/problems/longest-balanced-subarray-i/)：集合频次与区间枚举。

## 双指针

双指针不是“两个循环变量”的同义词，而是利用单调性或覆盖不变量，让每个指针只沿一个方向移动，从而批量排除候选。

### 有序数组上的相向指针

#### 排序后左右夹逼

**解决什么**：有序数组中的两数和、三数和、最接近目标值，以及满足单调关系的数对搜索。

**核心原理**：固定一个元素后，左右端点之和偏小时只能移动左指针增大结果，偏大时只能移动右指针减小结果；一次移动可以排除一整批不可能候选。

```python
def three_sum(nums, target=0):
  nums.sort()
  answer = []
  for first in range(len(nums) - 2):
    if first > 0 and nums[first] == nums[first - 1]:
      continue
    left, right = first + 1, len(nums) - 1
    while left < right:
      total = nums[first] + nums[left] + nums[right]
      if total < target:
        left += 1
      elif total > target:
        right -= 1
      else:
        answer.append([nums[first], nums[left], nums[right]])
        left += 1
        right -= 1
        while left < right and nums[left] == nums[left - 1]:
          left += 1
        while left < right and nums[right] == nums[right + 1]:
          right -= 1
  return answer
```

**复杂度**：排序 $O(n\log n)$，三数枚举总时间 $O(n^2)$；除结果和排序开销外辅助空间 $O(1)$。

**易错点**：去重必须分别处理固定元素、左端和右端；找到答案后两个指针都要移动；只有排序建立了单调性后才能按和的大小移动指针。

**对应例题**：

- Python 实证：[15. 3Sum](https://leetcode.com/problems/3sum/)
- C++ 历史实现：[15. 3Sum](https://leetcode.com/problems/3sum/)
- C++ 历史实现：[16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)
- C++ 历史实现：[167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

#### 从两端逆序构造答案

**解决什么**：输入有序，但变换后最大值可能来自任一端，例如平方、绝对值或按距离重排。

**核心原理**：比较两端变换值，把较大者写入答案末尾，再向内移动对应指针。答案写指针从后向前推进，始终保持未写区域与未处理输入对应。

```python
def sorted_squares(nums):
  answer = [0] * len(nums)
  left, right = 0, len(nums) - 1
  for write in range(len(nums) - 1, -1, -1):
    if abs(nums[left]) > abs(nums[right]):
      answer[write] = nums[left] ** 2
      left += 1
    else:
      answer[write] = nums[right] ** 2
      right -= 1
  return answer
```

**复杂度**：时间 $O(n)$；返回数组空间 $O(n)$，辅助空间 $O(1)$。

**易错点**：比较的是变换后的大小而非原值；写入方向应与每次选择最大值或最小值一致；空数组时右指针为 `-1`，循环应自然跳过。

**对应例题**：C++ 历史实现：[977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

### 子序列匹配

#### 左右极限匹配

**解决什么**：模式串必须按顺序匹配到文本串的一个子序列中，并要最大化某对相邻匹配位置的距离，或判断每个模式位置可达到的最左、最右边界。

**核心原理**：从左向右贪心求每个模式字符的最早匹配位置 `left[i]`，从右向左求最晚匹配位置 `right[i]`。固定相邻断点 $i$ 后，前缀采用最早位置、后缀采用最晚位置会为该断点留下最大距离，因此答案是 $\max(right[i+1]-left[i])$。

```python
def maximum_subsequence_gap(pattern, text):
  size = len(pattern)
  left = [0] * size
  cursor = 0
  for index, char in enumerate(pattern):
    while text[cursor] != char:
      cursor += 1
    left[index] = cursor
    cursor += 1

  right = [0] * size
  cursor = len(text) - 1
  for index in range(size - 1, -1, -1):
    while text[cursor] != pattern[index]:
      cursor -= 1
    right[index] = cursor
    cursor -= 1
  return max((right[i + 1] - left[i] for i in range(size - 1)), default=0)
```

**复杂度**：两次扫描均为单向推进，时间 $O(n+m)$，空间 $O(n)$，其中 $n$ 为模式长度、$m$ 为文本长度。

**易错点**：该结论依赖题目保证模式是文本的子序列；最大间隔跨越的是 `left[i]` 与 `right[i+1]`，不是同一字符的左右位置；模式长度为 1 时答案按定义为 0。

**对应例题**：Python 实证：[4026. Maximum Gap Between Stations](https://leetcode.com/problems/maximum-gap-between-stations/)

### 原地覆盖

#### 读写指针压缩数组

**解决什么**：原地删除、去重、保留至多若干次重复值，或把满足条件的元素压缩到数组前部。

**核心原理**：读指针扫描原数组，写指针表示有效前缀长度。允许每个值最多出现 `limit` 次时，只需把当前值与 `nums[write - limit]` 比较。

```python
def keep_at_most(nums, limit):
  write = 0
  for value in nums:
    if write < limit or value != nums[write - limit]:
      nums[write] = value
      write += 1
  return write
```

**复杂度**：时间 $O(n)$，辅助空间 $O(1)$。

**易错点**：模板依赖相同值连续出现，通常要求数组已有序；返回的是有效前缀长度，后面的旧内容无需清理；`limit=0` 应按题意单独处理。

**对应例题**：C++ 历史实现：[80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

**补充练习**：

- [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)：本地 Python 实现使用哈希集合记录访问节点，时间与空间均为 $O(n)$，并非 Floyd 快慢指针。

## 滑动窗口

滑动窗口适用于“右端加入后，左端只需单向移动”的连续区间问题。写模板前先判断窗口合法性是否单调；负数常会破坏和或乘积约束的单调性。

### 固定长度窗口

#### 入一个、出一个的滚动维护

**解决什么**：定长子串异位词、窗口频次、定长区间统计，以及只需维护增量变化的连续区间问题。

**核心原理**：右端元素进入状态；窗口长度超过 $k$ 时，恰好移出 `right - k` 位置的元素。每次只更新两个元素，而不是重算整个窗口。

```python
from collections import Counter

def fixed_window_frequencies(nums, k):
  frequency = Counter()
  snapshots = []
  for right, value in enumerate(nums):
    frequency[value] += 1
    if right >= k:
      outgoing = nums[right - k]
      frequency[outgoing] -= 1
      if frequency[outgoing] == 0:
        del frequency[outgoing]
    if right >= k - 1:
      snapshots.append(frequency.copy())
  return snapshots
```

**复杂度**：若状态更新为均摊 $O(1)$，扫描时间 $O(n)$，窗口状态空间 $O(k)$；示例复制快照还需计入输出成本。

**易错点**：先加入还是先移出必须与窗口长度判断一致；频次降为零时通常应删除键；`k<=0` 需要按题意拒绝或特判。

**对应例题**：

- C++ 历史实现：[567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)
- Python 实证：[3768. Minimum Inversion Count in Subarrays of Fixed Length](https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/)：本地实现用 `bisect + list` 维护有序窗口，查找 $O(\log k)$，插入删除为 $O(k)$，总时间最坏 $O(nk)$。

### 单调约束窗口

#### 最长合法窗口

**解决什么**：求满足“至多 $k$ 次修改”“至多 $k$ 个不同值”等单调约束的最长连续区间。

**核心原理**：右端持续扩张；一旦窗口不合法，就移动左端直到恢复合法，再更新最大长度。以字符替换为例，窗口长度减去窗口内最高频字符数就是最少替换次数。

```python
from collections import defaultdict

def longest_repeating_after_replacements(text, k):
  frequency = defaultdict(int)
  left = max_frequency = answer = 0
  for right, char in enumerate(text):
    frequency[char] += 1
    max_frequency = max(max_frequency, frequency[char])
    while right - left + 1 - max_frequency > k:
      frequency[text[left]] -= 1
      left += 1
    answer = max(answer, right - left + 1)
  return answer
```

**复杂度**：时间 $O(n)$，空间 $O(|\Sigma|)$，其中 $\Sigma$ 为字符集。

**易错点**：`max_frequency` 可以保留历史最大值，因为它只用于判断是否存在同长度的潜在合法窗口；若改写为必须精确维护当前窗口的题目，收缩后需重新计算或使用其他结构。

**对应例题**：Python 实证：[424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)；本地实现按目标字符的位置列表分别滑窗，是同一约束的另一种 $O(n)$ 建模。

#### 最短可行窗口

**解决什么**：在正数数组中寻找和至少为目标值的最短子数组，或求首次满足单调阈值的最小窗口。

**核心原理**：右端加入元素后，只要当前窗口已可行，就记录答案并持续移出左端，直到刚好不可行；这样枚举了每个右端对应的最短可行左边界。

```python
def min_subarray_length(target, nums):
  left = window_sum = 0
  answer = len(nums) + 1
  for right, value in enumerate(nums):
    window_sum += value
    while window_sum >= target:
      answer = min(answer, right - left + 1)
      window_sum -= nums[left]
      left += 1
  return 0 if answer == len(nums) + 1 else answer
```

**复杂度**：左右指针各移动至多 $n$ 次，时间 $O(n)$，辅助空间 $O(1)$。

**易错点**：和随窗口扩张单调依赖元素为正或非负；含负数时该模板会漏解；答案要在移出左端之前更新。

**对应例题**：C++ 历史实现：[209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

### 子数组计数

#### 两个边界计数恰好满足

**解决什么**：统计恰好 $k$ 个不同值、恰好满足某个频次层级，或直接条件不易单调维护的子数组数量。

**核心原理**：把“恰好”改写成两个具有单调性的累计计数之差，例如 `at_most(k) - at_most(k - 1)`。每个右端对应的合法左端个数可直接累加。

```python
from collections import defaultdict

def subarrays_with_k_distinct(nums, k):
  def at_most(limit):
    if limit < 0:
      return 0
    frequency = defaultdict(int)
    left = answer = 0
    for right, value in enumerate(nums):
      frequency[value] += 1
      while len(frequency) > limit:
        outgoing = nums[left]
        frequency[outgoing] -= 1
        if frequency[outgoing] == 0:
          del frequency[outgoing]
        left += 1
      answer += right - left + 1
    return answer

  return at_most(k) - at_most(k - 1)
```

**复杂度**：两次滑窗均为 $O(n)$，总时间 $O(n)$；频次表空间 $O(u)$，其中 $u$ 为窗口内不同元素数上界。

**易错点**：不是所有“恰好”条件都能直接套 `at_most`；要先证明累计条件单调。累加的是以当前右端结尾的合法左端数量，不是只加一。

**对应例题**：Python 实证：[3859. Count Subarrays With K Distinct Integers](https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/)；本地题还要求每个不同值至少出现 $m$ 次，使用两个收缩阈值之差完成计数。

**补充练习**：

- C++ 历史实现：[713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)：正数乘积约束与以右端结尾的子数组计数。
- C++ 历史实现：[1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)：至多翻转 $k$ 个零的最长窗口。
- [2398. Maximum Number of Robots Within Budget](https://leetcode.com/problems/maximum-number-of-robots-within-budget/)：Python 本地实现以有序列表维护窗口最大值，中间插入删除最坏 $O(n)$；标准线性解法应使用单调队列。

## 前缀和与差分

前缀和把区间信息改写成两个端点状态之差；差分则是它的逆过程，把多次区间修改压缩成端点事件。静态查询优先前缀和，在线修改应转向树状数组或线段树。

### 静态区间聚合

#### 一维前缀和

**解决什么**：数组不再修改时，多次查询区间和、区间计数或可加信息。

**核心原理**：令 `prefix[i]` 表示前 `i` 个元素之和，并设置 `prefix[0] = 0`。闭区间 $[left,right]$ 的和统一为 `prefix[right + 1] - prefix[left]`。

```python
class PrefixSum:
  def __init__(self, nums):
    self.prefix = [0]
    for value in nums:
      self.prefix.append(self.prefix[-1] + value)

  def range_sum(self, left, right):
    return self.prefix[right + 1] - self.prefix[left]
```

**复杂度**：预处理时间和空间均为 $O(n)$；单次查询 $O(1)$。

**易错点**：统一前缀含义和区间开闭，不要混用 `prefix[right]` 与 `prefix[right + 1]`；累计值可能超出 32 位整数；存在在线修改时不能每次重建。

**对应例题**：C++ 历史实现：[303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)

### 前缀状态计数

#### 前缀和加哈希表

**解决什么**：统计和等于目标值的子数组，或寻找两个相同前缀状态之间的最长区间。

**核心原理**：若当前前缀和为 `current`，此前前缀和为 `current - target`，两者之间的子数组和就是 `target`。计数题保存此前状态出现次数；最长区间题保存状态第一次出现位置。

```python
from collections import defaultdict

def count_subarray_sum(nums, target):
  seen = defaultdict(int)
  seen[0] = 1
  current = answer = 0
  for value in nums:
    current += value
    answer += seen[current - target]
    seen[current] += 1
  return answer
```

**复杂度**：期望时间 $O(n)$，空间 $O(n)$。

**易错点**：必须先放入空前缀 `0`；先查询再记录当前前缀，避免把空子数组算入；求最长长度时不能覆盖状态的最早位置。

**对应例题**：

- Python 实证：[525. Contiguous Array](https://leetcode.com/problems/contiguous-array/)：把 `0/1` 映射为 `+1/-1`，本地实现保存同一前缀状态的全部位置后取首尾距离。
- C++ 历史实现：[560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

#### 前缀不等式与有序计数

**解决什么**：统计子数组状态大于、低于某个阈值，或把比例与多数条件转换成前缀值之间的大小关系。

**核心原理**：先给每个元素赋权，把区间条件化为 `prefix[right] > prefix[left]` 或类似不等式；扫描右端时，在有序结构中查询此前前缀值的排名，再插入当前值。

```python
from bisect import bisect_left, insort

def count_positive_sum_subarrays(weights):
  ordered = [0]
  prefix = answer = 0
  for weight in weights:
    prefix += weight
    answer += bisect_left(ordered, prefix)
    insort(ordered, prefix)
  return answer
```

**复杂度**：该简洁 Python 模板使用列表，查询 $O(\log n)$，插入 $O(n)$，总时间最坏 $O(n^2)$、空间 $O(n)$；坐标压缩加树状数组可优化到 $O(n\log n)$。

**易错点**：严格不等式用 `bisect_left`，非严格不等式通常用 `bisect_right`；比例比较应交叉相乘，避免浮点误差；额外条件如“分母大于零”必须单独验证是否已被变换包含。

**对应例题**：

- Python 实证：[3739. Count Subarrays With Majority Element II](https://leetcode.com/problems/count-subarrays-with-majority-element-ii/)：目标值映射为 `+1`、其余映射为 `-1`，本地实现使用 `bisect + list`。
- Python 实证：[4013. Count Subarrays With Even Odd Ratio II](https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/)：比例不等式赋权后统计有序前缀，本地实现同样存在 $O(n)$ 插入。

### 离线区间修改

#### 一维与二维差分

**解决什么**：执行大量区间加或矩形加，最后一次性得到所有位置的值。

**核心原理**：一维闭区间 $[left,right]$ 加 `delta`，只记录 `diff[left] += delta` 与 `diff[right + 1] -= delta`。二维矩形使用四角标记，最后对两个维度做前缀累加还原。

```python
def apply_range_additions(length, updates):
  difference = [0] * (length + 1)
  for left, right, delta in updates:
    difference[left] += delta
    difference[right + 1] -= delta

  values = [0] * length
  running = 0
  for index in range(length):
    running += difference[index]
    values[index] = running
  return values
```

**复杂度**：一维中，$q$ 次修改与还原总时间 $O(q+n)$、空间 $O(n)$；二维 $r\times c$ 网格为 $O(q+rc)$ 时间和 $O(rc)$ 空间。

**易错点**：数组要为 `right + 1` 预留哨兵位置；闭区间与半开区间的撤销端点不同；二维四角符号必须成对，恢复时不要漏掉容斥项。

**对应例题**：

- C++ 历史实现：[1094. Car Pooling](https://leetcode.com/problems/car-pooling/)
- Python 实证：[2536. Increment Submatrices by One](https://leetcode.com/problems/increment-submatrices-by-one/)：四角标记加二维前缀还原。

**补充练习**：

- C++ 历史实现：[304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)：二维前缀和与矩形容斥。

## 排序与分治

排序先建立全局次序，分治则把问题拆成独立子问题后合并答案。只需第 $k$ 个元素时优先选择而非完整排序；链表和需要统计跨区间贡献时，归并通常更自然。

### 稳定排序与分治合并

#### 归并排序

**解决什么**：稳定排序数组或链表，并为逆序对、跨区间贡献等问题提供有序的左右半区间。

**核心原理**：递归排序左右两半，再用双指针线性合并。每层合并总工作量为 $O(n)$，递归深度为 $O(\log n)$。

```python
def merge_sort(nums):
  if len(nums) <= 1:
    return nums
  middle = len(nums) // 2
  left = merge_sort(nums[:middle])
  right = merge_sort(nums[middle:])
  result = []
  i = j = 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  return result + left[i:] + right[j:]
```

**复杂度**：时间 $O(n\log n)$；该数组模板空间 $O(n)$，递归栈 $O(\log n)$。

**易错点**：稳定排序要求相等时先取左侧；链表找中点时要正确断链；统计逆序对时只在右侧元素严格更小时累加剩余左侧数量。

**对应例题**：Python 对照实现：[148. Sort List](https://leetcode.com/problems/sort-list/) 当前将链表值复制到数组后调用 `sorted`，可作为改写链表归并排序的练习，并非归并模板实证。

### 排序规则设计

#### 自定义比较器与排序键

**解决什么**：元素的优先级不能由单个自然值表达，例如拼接后最大、按频率排序或按多个关键字配对。

**核心原理**：先写清第一关键字和并列规则。无法用元组键表示时，用比较器定义任意两个元素的相对次序，并保证比较关系自洽。

```python
from functools import cmp_to_key

def largest_concatenation(nums):
  words = list(map(str, nums))

  def compare(first, second):
    if first + second > second + first:
      return -1
    if first + second < second + first:
      return 1
    return 0

  answer = "".join(sorted(words, key=cmp_to_key(compare)))
  return "0" if answer[0] == "0" else answer
```

**复杂度**：排序进行 $O(n\log n)$ 次比较；若字符串平均长度为 $m$，时间为 $O(nm\log n)$，额外空间 $O(nm)$。

**易错点**：比较器必须返回负数、零或正数；不要写出循环矛盾；多关键字排序要明确升降序；全零拼接结果应规范为单个 `0`。

**对应例题**：Python 实证：[179. Largest Number](https://leetcode.com/problems/largest-number/)

### 顺序统计量

#### 快速选择

**解决什么**：只求第 $k$ 小或第 $k$ 大元素，不需要得到完整有序数组。

**核心原理**：随机选枢轴并原地分区，只继续处理目标下标所在的一侧；与快速排序不同，不递归另一侧。

```python
from random import randint

def kth_smallest(nums, k):
  target = k - 1
  left, right = 0, len(nums) - 1
  while left <= right:
    pivot_index = randint(left, right)
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    store = left
    for index in range(left, right):
      if nums[index] < nums[right]:
        nums[store], nums[index] = nums[index], nums[store]
        store += 1
    nums[store], nums[right] = nums[right], nums[store]
    if store == target:
      return nums[store]
    if store < target:
      left = store + 1
    else:
      right = store - 1
```

**复杂度**：期望时间 $O(n)$，最坏时间 $O(n^2)$；迭代模板额外空间 $O(1)$。

**易错点**：第 $k$ 大对应升序下标 `n - k`；分区后只能缩到不含枢轴的一侧；随机化降低恶意有序输入触发最坏情况的概率。

**对应例题**：C++ 历史实现：[215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)；本地源码使用完整快速排序，并非快速选择实证。

**补充练习**：

- C++ 历史实现：[451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)
- Python 实证：[4014. Minimum Total Price After Applying Discounts](https://leetcode.com/problems/minimum-total-price-after-applying-discounts/)：排序配对与交换论证。

## 离散化与离线处理

离散化压缩值域但保留次序；离线处理则改变查询顺序，把反复变化的条件变成单向扫描。两者常与并查集、堆、树状数组或线段树组合。

### 值域压缩

#### 排序去重离散化

**解决什么**：坐标很大或为负数，但算法只关心相对大小、排名或实际出现的位置。

**核心原理**：将所有可能参与操作的坐标排序去重，原值映射为连续排名；需要恢复原值时保留反向数组。

```python
def compress(values):
  ordered = sorted(set(values))
  rank = {value: index + 1 for index, value in enumerate(ordered)}
  return [rank[value] for value in values], ordered
```

**复杂度**：预处理时间 $O(n\log n)$，空间 $O(n)$；哈希映射单次期望 $O(1)$。

**易错点**：离散化只保留顺序，不保留原坐标距离；区间端点、查询值和更新值要一起收集；树状数组通常使用从 `1` 开始的排名。

**对应例题**：Python 实证：[1847. Closest Room](https://leetcode.com/problems/closest-room/)：离线激活后维护房间编号候选；本地实现使用 `bisect + list`，中间插入仍为 $O(n)$。

### 单调事件扫描

#### 按阈值离线激活

**解决什么**：多个独立查询各有阈值，满足条件的元素可随阈值单调加入，且允许改变查询处理顺序。

**核心原理**：数据和查询分别按阈值排序；扫描查询时持续激活新数据，用数据结构回答当前查询，最后按原下标恢复答案。

```python
def offline_threshold(items, queries, activate, answer):
  items = sorted(items, key=lambda item: item[0])
  ordered_queries = sorted(enumerate(queries), key=lambda pair: pair[1][0])
  result = [None] * len(queries)
  item_index = 0
  for query_index, query in ordered_queries:
    threshold = query[0]
    while item_index < len(items) and items[item_index][0] < threshold:
      activate(items[item_index])
      item_index += 1
    result[query_index] = answer(query)
  return result
```

**复杂度**：排序时间 $O((n+q)\log(n+q))$；扫描和数据结构操作另计，常见总复杂度为 $O((n+q)\log n)$。

**易错点**：严格小于与小于等于决定同阈值事件的先后；必须保存查询原下标；查询影响后续输入时不能离线重排。

**对应例题**：Python 实证：[1697. Checking Existence of Edge Length Limited Paths](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/)：按边权激活边，并用并查集回答连通性。

**补充练习**：

- Python 实证：[1851. Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/)：查询排序、区间激活与堆维护候选。

## 二分查找

二分的本质是利用单调性排除一半候选。先写清搜索区间、循环不变量和最终返回值，再选择精确查找、边界查找或二分答案模板。

### 有序序列边界

#### 左边界与右边界二分

**解决什么**：查找目标值、第一处不小于目标的位置，或第一处大于目标的位置。

**核心原理**：在左闭右开区间 `[left, right)` 中维护答案候选；条件成立时保留中点并收缩右边界，否则排除中点。

```python
def lower_bound(nums, target):
  left, right = 0, len(nums)
  while left < right:
    middle = (left + right) // 2
    if nums[middle] >= target:
      right = middle
    else:
      left = middle + 1
  return left
```

**复杂度**：时间 $O(\log n)$，空间 $O(1)$。

**易错点**：整个循环必须统一闭区间或半开区间语义；`lower_bound` 使用 `>=`，`upper_bound` 使用 `>`；返回值可能等于 `len(nums)`。

**对应例题**：C++ 历史实现：[704. Binary Search](https://leetcode.com/problems/binary-search/)、[278. First Bad Version](https://leetcode.com/problems/first-bad-version/)

### 单调可行性

#### 二分最小可行答案

**解决什么**：答案是整数，且 `feasible(value)` 从某个位置开始恒为真，例如最小容量、最短天数或最小阈值。

**核心原理**：先给出覆盖全部答案的闭区间；可行时保留中点并向左找更小答案，不可行时排除中点。

```python
def first_feasible(low, high, feasible):
  while low < high:
    middle = low + (high - low) // 2
    if feasible(middle):
      high = middle
    else:
      low = middle + 1
  return low
```

**复杂度**：若判定一次为 $O(f(n))$，值域大小为 $V$，总时间 $O(f(n)\log V)$，额外空间由判定函数决定。

**易错点**：先证明判定函数单调；上下界必须覆盖答案且 `high` 可行；求最大可行值时要改不变量并防止中点停滞。

**对应例题**：Python 实证：[1482. Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)，本地文件名题号误写为 1480；[3924. Minimum Threshold Path With Limited Heavy Edges](https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/)

### 局部有序数组

#### 旋转数组二分

**解决什么**：在原本有序、经过一次旋转的数组中寻找最小值或目标值。

**核心原理**：将中点与右端比较。若 `nums[middle] > nums[right]`，最小值严格在右侧；否则最小值位于包含中点的左半区间。

```python
def find_rotated_minimum(nums):
  left, right = 0, len(nums) - 1
  while left < right:
    middle = (left + right) // 2
    if nums[middle] > nums[right]:
      left = middle + 1
    else:
      right = middle
  return nums[left]
```

**复杂度**：无重复元素时为 $O(\log n)$ 时间、$O(1)$ 空间；允许重复时最坏退化为 $O(n)$。

**易错点**：不能简单与首元素比较后同时排除两端；有重复且中点等于右端时只能令 `right -= 1`；空数组需按题目契约处理。

**对应例题**：C++ 历史实现：[153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

**补充练习**：

- C++ 历史实现：[875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
- C++ 历史实现：[1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)，本地文件名题号误写为 1014。

## 栈、队列与单调结构

栈适合处理最近未匹配状态和嵌套结构；单调栈把“寻找左右第一个更大或更小”降为线性扫描；单调队列则在线维护滑动窗口极值。

### 后进先出状态

#### 栈模拟与嵌套解析

**解决什么**：括号匹配、路径化简、逆波兰表达式和带括号的嵌套编码。

**核心原理**：栈顶保存最近尚未完成的状态；遇到结束标记时弹出并与当前结果合并。

```python
def evaluate_rpn(tokens):
  stack = []
  for token in tokens:
    if token not in {"+", "-", "*", "/"}:
      stack.append(int(token))
      continue
    right = stack.pop()
    left = stack.pop()
    if token == "+":
      stack.append(left + right)
    elif token == "-":
      stack.append(left - right)
    elif token == "*":
      stack.append(left * right)
    else:
      stack.append(int(left / right))
  return stack[-1]
```

**复杂度**：时间 $O(n)$，空间 $O(n)$。

**易错点**：减法和除法的操作数顺序不能颠倒；Python `//` 对负数向下取整，题目要求向零截断时应使用 `int(left / right)`；弹栈前确保输入合法。

**对应例题**：Python 实证：[150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)、[394. Decode String](https://leetcode.com/problems/decode-string/)

### 最近边界与贡献

#### 单调栈

**解决什么**：在线性时间找到每个元素左右第一个更大或更小元素，或计算元素作为区间最值的贡献。

**核心原理**：栈保存尚未找到右边界的下标；新元素破坏单调性时持续弹栈，并在弹出时结算答案。

```python
def next_greater_distances(nums):
  answer = [0] * len(nums)
  stack = []
  for index, value in enumerate(nums):
    while stack and nums[stack[-1]] < value:
      previous = stack.pop()
      answer[previous] = index - previous
    stack.append(index)
  return answer
```

**复杂度**：每个下标至多入栈、出栈一次，时间 $O(n)$，空间 $O(n)$。

**易错点**：栈中通常存下标而非值；严格与非严格比较决定重复值归属；贡献法的左右边界通常一侧严格、一侧非严格，避免重复计数。

**对应例题**：Python 实证：[2104. Sum of Subarray Ranges](https://leetcode.com/problems/sum-of-subarray-ranges/)；C++ 历史实现：[739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

### 滑动窗口极值

#### 单调队列

**解决什么**：在线性时间维护固定长度窗口的最大值或最小值。

**核心原理**：双端队列保存仍在窗口内且可能成为最优值的下标；队首淘汰过期下标，队尾淘汰不优于新元素的候选。

```python
from collections import deque

def sliding_window_maximum(nums, window_size):
  queue = deque()
  answer = []
  for index, value in enumerate(nums):
    while queue and queue[0] <= index - window_size:
      queue.popleft()
    while queue and nums[queue[-1]] <= value:
      queue.pop()
    queue.append(index)
    if index + 1 >= window_size:
      answer.append(nums[queue[0]])
  return answer
```

**复杂度**：时间 $O(n)$，空间 $O(k)$，其中 $k$ 为窗口长度。

**易错点**：队列必须存下标才能判断过期；先后执行过期清理与队尾清理都要保持同一窗口语义；窗口形成前不要输出答案。

**对应例题**：Python 实证：[239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

**补充练习**：

- Python 实证：[71. Simplify Path](https://leetcode.com/problems/simplify-path/)
- C++ 历史实现：[155. Min Stack](https://leetcode.com/problems/min-stack/)

## 堆与优先队列

堆只保证堆顶是全局最值，适合反复取最优候选，而不适合查找或删除任意元素。Python 的 `heapq` 是小顶堆，大顶堆通常存相反数。

### 有界候选集合

#### Top K 小顶堆

**解决什么**：从静态数组或数据流中持续维护最大的 $k$ 个元素，并快速得到第 $k$ 大。

**核心原理**：维护大小不超过 $k$ 的小顶堆；新元素入堆后若超长就弹出最小值，堆顶始终是当前第 $k$ 大。

```python
import heapq

class KthLargest:
  def __init__(self, k, nums):
    self.k = k
    self.heap = []
    for value in nums:
      self.add(value)

  def add(self, value):
    heapq.heappush(self.heap, value)
    if len(self.heap) > self.k:
      heapq.heappop(self.heap)
    return self.heap[0]
```

**复杂度**：每次加入 $O(\log k)$，空间 $O(k)$；初始化为 $O(n\log k)$。

**易错点**：求最大的 $k$ 个应使用小顶堆；只有至少已有 $k$ 个元素时堆顶才有第 $k$ 大语义；堆内部数组并非整体有序。

**对应例题**：Python 实证：[703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

### 有序候选扩展

#### 多路归并

**解决什么**：合并多个有序序列，或按从小到大的顺序生成二维有序候选中的前 $k$ 个。

**核心原理**：每一路只把当前最小候选放入堆；弹出后再加入同一路的后继，避免一次性枚举全部组合。

```python
import heapq

def merge_sorted_lists(sequences):
  heap = []
  for sequence_index, sequence in enumerate(sequences):
    if sequence:
      heapq.heappush(heap, (sequence[0], sequence_index, 0))
  result = []
  while heap:
    value, sequence_index, index = heapq.heappop(heap)
    result.append(value)
    next_index = index + 1
    if next_index < len(sequences[sequence_index]):
      next_value = sequences[sequence_index][next_index]
      heapq.heappush(heap, (next_value, sequence_index, next_index))
  return result
```

**复杂度**：合并总计 $n$ 个元素、$k$ 路序列时，时间 $O(n\log k)$，空间 $O(k)$。

**易错点**：堆元素要带来源和后继位置；初始只放每一路首项；元组前项相同时，后续字段必须可比较且不破坏业务语义。

**对应例题**：Python 实证：[373. Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

### 资源调度

#### 双堆事件调度

**解决什么**：任务按时间到达，需要优先复用已释放资源，并在无空闲资源时等待最早结束的任务。

**核心原理**：空闲堆按资源编号排序，占用堆按结束时间排序；处理新任务前先释放所有已结束资源，必要时从最早结束事件推进时间。

```python
import heapq

def assign_resources(tasks, resource_count):
  available = list(range(resource_count))
  heapq.heapify(available)
  busy = []
  assignment = []
  for start, end in sorted(tasks):
    duration = end - start
    while busy and busy[0][0] <= start:
      _, resource = heapq.heappop(busy)
      heapq.heappush(available, resource)
    if not available:
      start, resource = heapq.heappop(busy)
    else:
      resource = heapq.heappop(available)
    heapq.heappush(busy, (start + duration, resource))
    assignment.append(resource)
  return assignment
```

**复杂度**：$n$ 个任务、$m$ 个资源时，时间 $O(n\log n+n\log m)$，空间 $O(m)$。

**易错点**：延迟任务时必须保留原持续时间；结束时间相同要按题意处理资源编号；释放条件是 `< start` 还是 `<= start` 取决于端点语义。

**对应例题**：Python 实证：[2402. Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/)

**补充练习**：

- Python 实证：[1642. Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/)：用堆把稀缺资源留给更大的高度差。

## 树状数组

树状数组（Fenwick Tree）用紧凑数组维护可差分的前缀信息。它的功能比线段树窄，但代码短、常数小，是动态前缀和与计数问题的常用结构。

### 动态前缀聚合

#### 单点增加与区间求和

**解决什么**：数组频繁单点修改，同时反复查询前缀和或任意区间和。

**核心原理**：`index & -index` 是节点管辖区间长度。更新时向更大的父区间跳转，查询时向前拆分成互不重叠区间；区间和由两个前缀和作差。

```python
class FenwickTree:
  def __init__(self, size):
    self.size = size
    self.tree = [0] * (size + 1)

  def add(self, index, delta):
    index += 1
    while index <= self.size:
      self.tree[index] += delta
      index += index & -index

  def prefix_sum(self, right):
    total = 0
    while right > 0:
      total += self.tree[right]
      right -= right & -right
    return total

  def range_sum(self, left, right):
    return self.prefix_sum(right + 1) - self.prefix_sum(left)
```

**复杂度**：单点增加、前缀查询和区间查询均为 $O(\log n)$；空间 $O(n)$，逐点建树为 $O(n\log n)$。

**易错点**：内部下标必须从 `1` 开始；模板的 `prefix_sum(right)` 计算半开区间 `[0, right)`；赋值更新要保存原值并加入 `new_value - old_value`。

**对应例题**：C++ 历史实现：[307. Range Sum Query - Mutable - Fenwick Tree](https://leetcode.com/problems/range-sum-query-mutable/)

### 有序频次统计

#### 离散化加树状数组计数

**解决什么**：扫描过程中统计此前严格更小、更大或落在某个值域区间内的元素数量。

**核心原理**：先把值映射为排名，再让树状数组维护每个排名出现次数；前缀查询得到更小元素数，总数减去不大于当前值的数量得到更大元素数。

```python
def count_smaller_before(nums):
  ordered = sorted(set(nums))
  rank = {value: index for index, value in enumerate(ordered)}
  bit = FenwickTree(len(ordered))
  answer = []
  for value in nums:
    index = rank[value]
    answer.append(bit.prefix_sum(index))
    bit.add(index, 1)
  return answer
```

**复杂度**：离散化 $O(n\log n)$，扫描 $O(n\log n)$，空间 $O(n)$。

**易错点**：严格更小查询不应包含当前排名；重复值必须映射到同一排名；先查询再插入可避免把当前元素统计进去。

**对应例题**：Python 对照实现：[1649. Create Sorted Array through Instructions](https://leetcode.com/problems/create-sorted-array-through-instructions/) 当前使用 `bisect + list`，可按本模板优化到 $O(n\log n)$，但本地源码不是树状数组实证。

**补充练习**：

- C++ 历史实现：[307. Range Sum Query - Mutable - Naive](https://leetcode.com/problems/range-sum-query-mutable/)：$O(1)$ 赋值、$O(n)$ 区间遍历的朴素基线。

## 线段树

线段树把数组递归划分为若干区间，用树节点保存区间信息，适合处理**频繁修改后仍要反复查询区间结果**的问题。只要区间答案能够由左右子区间合并，就可以考虑线段树。

### 基础动态区间信息

#### 单点修改与普通区间查询

**解决什么**：数组会单点变化，需要在线查询任意区间的和、最大值或最小值。

**核心原理**：叶子保存单个位置，父节点由两个子节点合并。单点修改沿祖先链重新计算；区间查询将目标拆成 $O(\log n)$ 个树节点并合并。

```python
class MaxSegmentTree:
  def __init__(self, nums):
    self.size = 1
    while self.size < len(nums):
      self.size *= 2
    self.tree = [float("-inf")] * (2 * self.size)
    self.tree[self.size:self.size + len(nums)] = nums
    for node in range(self.size - 1, 0, -1):
      self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

  def update(self, index, value):
    node = self.size + index
    self.tree[node] = value
    node //= 2
    while node:
      self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])
      node //= 2

  def query(self, left, right):
    result = float("-inf")
    left += self.size
    right += self.size
    while left < right:
      if left & 1:
        result = max(result, self.tree[left])
        left += 1
      if right & 1:
        right -= 1
        result = max(result, self.tree[right])
      left //= 2
      right //= 2
    return result
```

**复杂度**：建树 $O(n)$；单点修改和区间查询 $O(\log n)$；空间 $O(n)$。

**易错点**：模板查询的是半开区间 `[left, right)`；最大值查询单位元是负无穷；值域线段树的下标是数值排名，不一定是原数组位置。

**对应例题**：Python 实证：[2407. Longest Increasing Subsequence II](https://leetcode.com/problems/longest-increasing-subsequence-ii/)：查询值域最大 DP 值后单点更新。

### 多字段节点状态

#### 复杂节点合并

**解决什么**：区间答案不是单个和或最值，而要同时维护前缀、后缀、边界特征和区间最优值。

**核心原理**：先定义节点不变量，再设计满足结合律的 `merge`。父节点的内部最优值来自左子树、右子树或跨越中点的组合。

```python
def merge(left, right):
  if left[0] == 0:
    return right
  if right[0] == 0:
    return left
  left_length, left_char, left_right_char, left_prefix, left_suffix, left_best = left
  right_length, right_left_char, right_char, right_prefix, right_suffix, right_best = right
  prefix, suffix = left_prefix, right_suffix
  best = max(left_best, right_best)
  if left_right_char == right_left_char:
    best = max(best, left_suffix + right_prefix)
    if left_prefix == left_length:
      prefix += right_prefix
    if right_suffix == right_length:
      suffix += left_suffix
  return (
    left_length + right_length,
    left_char,
    right_char,
    prefix,
    suffix,
    best,
  )
```

**复杂度**：若节点字段数固定，合并 $O(1)$，建树 $O(n)$，单点修改与区间查询 $O(\log n)$，空间 $O(n)$。

**易错点**：空节点必须有明确合并语义；跨中点前先检查两侧边界能否连接；只有整个左段同字符时前缀才能延伸，后缀同理；字段顺序要保持一致。

**对应例题**：Python 实证：[2213. Longest Substring of One Repeating Character](https://leetcode.com/problems/longest-substring-of-one-repeating-character/)：本地实现维护区间长度、左右字符、同字符前后缀和最长段，并在每次字符修改后沿祖先链执行 `pull`。

### 批量区间修改

#### 懒标记区间加

**解决什么**：大量区间整体增加，同时查询区间和、最小值或最大值，不能逐个更新叶子。

**核心原理**：完整覆盖时直接更新当前节点并累积懒标记；只有继续访问子节点时才下推。父节点始终反映已包含标记后的真实区间信息。

```python
class LazyRangeSumTree:
  def __init__(self, size):
    self.size = size
    self.tree = [0] * (4 * size)
    self.lazy = [0] * (4 * size)

  def _apply(self, node, left, right, delta):
    self.tree[node] += (right - left + 1) * delta
    self.lazy[node] += delta

  def _push(self, node, left, right):
    if self.lazy[node] == 0 or left == right:
      return
    middle = (left + right) // 2
    self._apply(node * 2, left, middle, self.lazy[node])
    self._apply(node * 2 + 1, middle + 1, right, self.lazy[node])
    self.lazy[node] = 0

  def add(self, query_left, query_right, delta, node=1, left=0, right=None):
    if right is None:
      right = self.size - 1
    if query_right < left or right < query_left:
      return
    if query_left <= left and right <= query_right:
      self._apply(node, left, right, delta)
      return
    self._push(node, left, right)
    middle = (left + right) // 2
    self.add(query_left, query_right, delta, node * 2, left, middle)
    self.add(query_left, query_right, delta, node * 2 + 1, middle + 1, right)
    self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

  def query(self, query_left, query_right, node=1, left=0, right=None):
    if right is None:
      right = self.size - 1
    if query_right < left or right < query_left:
      return 0
    if query_left <= left and right <= query_right:
      return self.tree[node]
    self._push(node, left, right)
    middle = (left + right) // 2
    return self.query(query_left, query_right, node * 2, left, middle) + self.query(
      query_left, query_right, node * 2 + 1, middle + 1, right
    )
```

**复杂度**：建树 $O(n)$；区间修改和区间查询均为 $O(\log n)$；空间 $O(n)$。

**易错点**：区间和应用标记时必须乘区间长度，最值则不乘；访问子节点前先下推；区间赋值与区间加的标记复合有先后顺序，不能照搬单一加法标记。

**对应例题**：Python 实证：[3362. Zero Array Transformation III](https://leetcode.com/problems/zero-array-transformation-iii/)：本地 `SegmentTree` 使用区间加懒标记并维护区间最小值。

**补充练习**：

- Python 实证：[3161. Block Placement Queries](https://leetcode.com/problems/block-placement-queries/)：线段树维护障碍物间距最大值并处理在线查询。
- Python 实证：[3479. Fruits Into Baskets III](https://leetcode.com/problems/fruits-into-baskets-iii/)：维护可用篮子的区间最大容量，动态选择并删除位置。

## 链表

### 指针重连

#### 虚拟头节点与区间反转

**解决什么**：删除或插入头节点、反转整条链表或区间，以及需要统一处理首节点边界的链表修改。

**核心原理**：虚拟头节点让真实头节点也拥有前驱。反转时先保存 `current.next`，再修改指向；区间反转额外保存区间前驱和后继，最后一次性接回。

```python
def reverse_between(head, left, right):
  dummy = ListNode(0, head)
  before = dummy
  for _ in range(left - 1):
    before = before.next
  current = before.next
  for _ in range(right - left):
    moved = current.next
    current.next = moved.next
    moved.next = before.next
    before.next = moved
  return dummy.next
```

**复杂度**：时间 $O(n)$，额外空间 $O(1)$。

**易错点**：改写 `next` 前必须保存后继；循环次数是 `right - left`；返回 `dummy.next` 而不是原 `head`。

**对应例题**：C++ 历史实现：[92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)、[206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

#### 成环后断链

**解决什么**：把链表向右轮转 $k$ 位，或把首尾关系转换成更容易定位的切分问题。

**核心原理**：先求长度并把尾节点连到头节点形成环，令 $k\mathrel{\%=}n$，再从尾节点向前走 $n-k$ 步找到新尾并断开。

```python
def rotate_right(head, k):
  if head is None or head.next is None:
    return head
  tail, length = head, 1
  while tail.next:
    tail = tail.next
    length += 1
  tail.next = head
  for _ in range(length - k % length):
    tail = tail.next
  answer = tail.next
  tail.next = None
  return answer
```

**复杂度**：时间 $O(n)$，额外空间 $O(1)$。

**易错点**：空链表不能取模；必须先对 $k$ 取模；断环位置是新尾节点之后。

**对应例题**：C++ 历史实现：[61. Rotate List](https://leetcode.com/problems/rotate-list/)

### 结构定位与复制

#### 快慢指针找中点

**解决什么**：找链表中点、判断回文，或把链表拆成长度接近的两段。

**核心原理**：快指针每次走两步、慢指针每次走一步；快指针到尾部时，慢指针位于中点。回文判断可反转后半段并与前半段逐项比较。

```python
def middle_node(head):
  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  return slow
```

**复杂度**：时间 $O(n)$，额外空间 $O(1)$。

**易错点**：偶数长度时模板返回第二个中点；若要切断前半段，应保存 `slow` 的前驱；回文比较后是否恢复链表取决于接口约定。

**对应例题**：C++ 历史实现：[234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

#### 哈希映射复制复杂链表

**解决什么**：复制同时含 `next` 与随机指针的链表，保证新节点之间的引用不指回原链表。

**核心原理**：第一遍为每个原节点建立副本，第二遍通过 `copies[old.next]` 和 `copies[old.random]` 重建边；给 `None` 预置映射可统一边界。

```python
def copy_random_list(head):
  copies = {None: None}
  current = head
  while current:
    copies[current] = Node(current.val)
    current = current.next
  current = head
  while current:
    copies[current].next = copies[current.next]
    copies[current].random = copies[current.random]
    current = current.next
  return copies[head]
```

**复杂度**：时间 $O(n)$，额外空间 $O(n)$。

**易错点**：字典键必须是节点对象而不是可能重复的节点值；必须创建完全部副本后再连随机指针。

**对应例题**：Python 本地实现：[138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)

### 排序与合并

#### 链表归并排序

**解决什么**：在不能随机访问的链表上实现稳定的 $O(n\log n)$ 排序。

**核心原理**：快慢指针切分链表，递归排序左右两半，再用虚拟头节点线性合并。该算法是标准链表排序模板，但本地 148 源码实际把值复制到数组排序后写回，并非此实现。

```python
def sort_list(head):
  if head is None or head.next is None:
    return head
  slow, fast = head, head.next
  while fast and fast.next:
    slow, fast = slow.next, fast.next.next
  right = slow.next
  slow.next = None
  return merge(sort_list(head), sort_list(right))

def merge(first, second):
  dummy = tail = ListNode()
  while first and second:
    if first.val <= second.val:
      tail.next, first = first, first.next
    else:
      tail.next, second = second, second.next
    tail = tail.next
  tail.next = first or second
  return dummy.next
```

**复杂度**：时间 $O(n\log n)$；递归栈 $O(\log n)$，自底向上版本可把额外栈空间降为 $O(1)$。

**易错点**：切分前必须断开左半段；合并后要接上剩余节点；若题目严格要求常数额外空间，应改用自底向上归并。

**对应例题**：Python 对照实现：[148. Sort List](https://leetcode.com/problems/sort-list/) 当前使用数组排序并回写节点值，时间 $O(n\log n)$、额外空间 $O(n)$，不是链表归并实证。

## 二叉树与树形递归

树题的统一视角是：把整棵树的问题定义为“一个节点从子树接收什么信息、向父节点返回什么信息”。先写清递归契约，再选择前序、后序、中序或层序，通常比记忆题型模板更可靠。

### 树的遍历与递归契约

#### 前序、中序与后序 DFS

**解决什么**：前序遍历适合把路径、深度等状态从父节点传给子节点；中序遍历可以利用 BST 的有序性；后序遍历适合先取得左右子树结果，再计算当前节点答案。

**核心原理**：三种遍历的区别只是“处理当前节点”相对于左右子树递归的位置。递归函数应明确输入、返回值和副作用，例如 `dfs(node) -> 子树高度`，不要让返回值同时承担全局答案。

```python
def preorder(node):
	if node is None:
		return
	visit(node)
	preorder(node.left)
	preorder(node.right)

def inorder(node):
	if node is None:
		return
	inorder(node.left)
	visit(node)
	inorder(node.right)

def postorder(node):
	if node is None:
		return
	postorder(node.left)
	postorder(node.right)
	visit(node)
```

**复杂度**：时间 $O(n)$；递归栈为 $O(h)$，其中 $h$ 是树高，退化树最坏为 $O(n)$。

**易错点**：Python 递归深度默认有限，长链形树应改用显式栈；前序 + 中序重建通常要求节点值唯一；递归前必须定义空节点返回什么。

**对应例题**：

- Python 实证：[99. Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/)
- C++ 历史实现：[105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

#### 层序 BFS

**解决什么**：按深度访问节点、求最短层数、连接同层节点或逐层聚合结果。

**核心原理**：队列中始终保存下一批待处理节点。每轮先记录当前队列长度，只弹出这一层的节点，再把下一层加入队尾。

```python
from collections import deque

def level_order(root):
	if root is None:
		return []
	queue = deque([root])
	answer = []
	while queue:
		level = []
		for _ in range(len(queue)):
			node = queue.popleft()
			level.append(node.val)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		answer.append(level)
	return answer
```

**复杂度**：时间 $O(n)$；队列空间最坏为树的最大宽度 $O(n)$。

**易错点**：必须在处理本层前固定 `len(queue)`；Python 使用 `deque.popleft()`，不要使用列表 `pop(0)`。

**对应例题**：C++ 历史实现：[102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

### 二叉搜索树

#### 中序有序性与 BST 操作

**解决什么**：在 BST 中查找、插入、删除、验证顺序、寻找第 $k$ 小元素或修复错位节点。

**核心原理**：若 BST 约定左子树严格小于节点、右子树严格大于节点，则中序遍历得到严格递增序列。搜索时比较目标值与当前值，每次只进入一棵子树。

```python
def search_bst(root, target):
	node = root
	while node:
		if node.val == target:
			return node
		node = node.left if target < node.val else node.right
	return None
```

**复杂度**：搜索、插入和删除均为 $O(h)$；平衡树中为 $O(\log n)$，退化树中为 $O(n)$。

**易错点**：题目允许重复键时必须明确相等值放左边还是右边；验证 BST 不能只比较父子节点，应传递整个祖先范围。

**对应例题**：

- Python 实证：[99. Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/)
- C++ 历史实现：[230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

### 树形 DP

#### 后序状态合并

**解决什么**：树上路径、选或不选、安装设备、子树贡献等需要汇总子树状态的问题。

**核心原理**：为每个节点设计一个规模固定的返回状态，再由左右子节点状态合并。以“打家劫舍 III”为例，返回 `(不选当前节点, 选择当前节点)`：

```python
def rob_tree(root):
	def dfs(node):
		if node is None:
			return 0, 0
		left_skip, left_take = dfs(node.left)
		right_skip, right_take = dfs(node.right)
		skip = max(left_skip, left_take) + max(right_skip, right_take)
		take = node.val + left_skip + right_skip
		return skip, take

	return max(dfs(root))
```

**复杂度**：通常时间 $O(n)$、递归栈 $O(h)$；每个节点的状态数若为 $k$，合并成本还需乘以状态转移复杂度。

**易错点**：区分“可以向父节点延伸的值”和“当前子树内的全局最优值”；不要让父节点读取已经混入兄弟子树的信息。

**对应例题**：

- [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)：向上贡献与全局路径答案
- [337. House Robber III](https://leetcode.com/problems/house-robber-iii/)：选 / 不选状态
- [968. Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/)：多状态覆盖

### 最近公共祖先 LCA

#### 二叉树后序递归 LCA

**解决什么**：在普通二叉树中寻找两个节点最深的公共祖先，适合单次或少量查询。

**核心原理**：`dfs(node)` 返回当前子树中找到的目标节点或它们的 LCA。若左右子树都返回非空，说明两个目标分居两侧，当前节点就是 LCA；若只有一侧非空，直接向上传递。

```python
def lowest_common_ancestor(root, first, second):
	if root is None or root is first or root is second:
		return root
	left = lowest_common_ancestor(root.left, first, second)
	right = lowest_common_ancestor(root.right, first, second)
	if left is not None and right is not None:
		return root
	return left if left is not None else right
```

**复杂度**：时间 $O(n)$；递归栈 $O(h)$。

**易错点**：该简洁模板通常默认两个目标都存在；若题目不保证存在，需要额外统计找到的目标数。比较节点应使用对象身份，而不是仅比较可能重复的节点值。

**对应例题**：Python 标准实现：[236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

#### 最深叶节点集合的 LCA

**解决什么**：目标不是预先给定的两个节点，而是所有最深叶节点的公共祖先。

**核心原理**：后序返回 `(子树最大深度, 对应 LCA)`。左右深度相等时当前节点是两侧最深叶的汇合点；否则继承更深一侧的候选。

```python
def lca_deepest_leaves(root):
  def dfs(node):
    if node is None:
      return 0, None
    left_depth, left_lca = dfs(node.left)
    right_depth, right_lca = dfs(node.right)
    if left_depth == right_depth:
      return left_depth + 1, node
    if left_depth > right_depth:
      return left_depth + 1, left_lca
    return right_depth + 1, right_lca

  return dfs(root)[1]
```

**复杂度**：时间 $O(n)$；递归栈 $O(h)$。

**易错点**：它与通用 `LCA(u, v)` 的查询模型不同，不应共用同一个模板标签。

**对应例题**：Python 实证：[1123. Lowest Common Ancestor of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/)

### 倍增与 Binary Lifting

#### 第 K 个祖先

**解决什么**：静态树上大量“向上跳 $k$ 步”查询，也是倍增 LCA 的基础。

**核心原理**：预处理 `up[bit][node]` 表示节点的 $2^{bit}$ 级祖先。查询时把 $k$ 按二进制拆分，只执行置位对应的跳跃。

```python
class BinaryLifting:
	def __init__(self, parent):
		self.levels = max(1, len(parent).bit_length())
		self.up = [parent[:]]
		for _ in range(1, self.levels):
			previous = self.up[-1]
			self.up.append([
				-1 if ancestor == -1 else previous[ancestor]
				for ancestor in previous
			])

	def kth_ancestor(self, node, steps):
		bit = 0
		while steps and node != -1:
			if steps & 1:
				if bit >= self.levels:
					return -1
				node = self.up[bit][node]
			steps >>= 1
			bit += 1
		return node
```

**复杂度**：预处理时间和空间均为 $O(n\log n)$；单次查询 $O(\log n)$。

**易错点**：层数应由 `n.bit_length()` 动态计算；祖先不存在时保持 `-1`，不能继续把它当数组下标；根节点的父亲定义要统一。

**对应例题**：Python 实证：[1483. Kth Ancestor of a Tree Node](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/)

#### 倍增 LCA

**解决什么**：静态树上大量 LCA 或路径长度查询。

**核心原理**：先把较深节点提升到相同深度；若两点尚未相同，再从最高位到最低位同步上跳到“祖先不同但父祖先相同”的位置，最后返回共同父节点。

```python
def lowest_common_ancestor(first, second, depth, up):
  if depth[first] < depth[second]:
    first, second = second, first

  difference = depth[first] - depth[second]
  for bit in range(len(up)):
    if difference >> bit & 1:
      first = up[bit][first]

  if first == second:
    return first

  for bit in range(len(up) - 1, -1, -1):
    if up[bit][first] != up[bit][second]:
      first = up[bit][first]
      second = up[bit][second]
  return up[0][first]
```

**复杂度**：预处理 $O(n\log n)$；每次查询 $O(\log n)$；空间 $O(n\log n)$。

**易错点**：建表前必须确定树根和深度；同步上跳时只在两者的 $2^j$ 祖先不同且有效时移动；森林需要分别处理连通分量。

**对应例题**：

- Python 实证：[3553. Minimum Weighted Subgraph With the Required Paths II](https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/)
- Python 实证：[3559. Number of Ways to Assign Edge Weights II](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/)

## 图论与最短路

### 有向无环图

#### Kahn 拓扑排序

**解决什么**：课程依赖、任务先后关系、DAG 上的动态规划，以及检测有向图是否存在环。

**核心原理**：把所有入度为零的节点入队；每取出一个节点就删除它的出边，并把新出现的零入度节点入队。最终处理数少于节点总数就说明存在环。

```python
from collections import deque

def topological_order(node_count, edges):
  graph = [[] for _ in range(node_count)]
  indegree = [0] * node_count
  for source, target in edges:
    graph[source].append(target)
    indegree[target] += 1
  queue = deque(node for node in range(node_count) if indegree[node] == 0)
  order = []
  while queue:
    node = queue.popleft()
    order.append(node)
    for neighbor in graph[node]:
      indegree[neighbor] -= 1
      if indegree[neighbor] == 0:
        queue.append(neighbor)
  return order if len(order) == node_count else []
```

**复杂度**：时间 $O(V+E)$，空间 $O(V+E)$。

**易错点**：边方向必须与依赖含义一致；不能只从一个零入度节点开始；DAG DP 应在节点出队时转移。Python 队列要用 `deque`。

**对应例题**：Python 实证：[1857. Largest Color Value in a Directed Graph](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/) 使用反向边与出度归零的等价 Kahn 过程，并叠加 26 维 DAG DP；本地队列为 `list.pop(0)`，可改为 `deque`。Python 对照实现：[207. Course Schedule](https://leetcode.com/problems/course-schedule/) 使用依赖集合传播检测环，并非拓扑排序。

### 特殊边权最短路

#### BFS 与 0-1 BFS

**解决什么**：无权图最少步数，以及边权只为 $0/1$ 时的最短路。

**核心原理**：普通 BFS 按层扩展；0-1 BFS 松弛后把权重为 0 的节点放队首、权重为 1 的节点放队尾，使弹出顺序保持非降距离。

```python
from collections import deque

def zero_one_bfs(graph, start):
  distance = [float("inf")] * len(graph)
  distance[start] = 0
  queue = deque([start])
  while queue:
    node = queue.popleft()
    for neighbor, weight in graph[node]:
      candidate = distance[node] + weight
      if candidate < distance[neighbor]:
        distance[neighbor] = candidate
        if weight == 0:
          queue.appendleft(neighbor)
        else:
          queue.append(neighbor)
  return distance
```

**复杂度**：时间 $O(V+E)$，空间 $O(V)$；每条边权必须属于 $\{0,1\}$。

**易错点**：0 权边放队首、1 权边放队尾；不能用普通 FIFO BFS 处理不同边权；允许重复松弛时应以更短距离为准。

**对应例题**：Python 对照实现：[2290. Minimum Obstacle Removal to Reach Corner](https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/) 采用 0-1 BFS 的两端入队逻辑，但以列表头删、头插实现，最坏复杂度高于标准 `deque` 模板。

### 多源最短路

#### Floyd-Warshall

**解决什么**：求稠密图中任意两点之间的最短距离；也可把距离改成布尔可达性，求有向图的传递闭包。它允许负权边，但不能正确处理最短路经过负权环的情况。

**核心原理**：动态规划状态 `distance[source][target]` 表示当前允许经过指定中间点集合时的最短距离。依次把节点 `middle` 加入可用中间点，转移为“保持原路径”与“经过 `middle`”二者的较小值。`middle` 必须放在最外层循环，才能保证本轮读取的是只使用前一阶段中间点的闭包结果。

```python
def floyd_warshall(node_count, edges):
  infinity = float("inf")
  distance = [[infinity] * node_count for _ in range(node_count)]
  for node in range(node_count):
    distance[node][node] = 0
  for source, target, weight in edges:
    distance[source][target] = min(distance[source][target], weight)

  for middle in range(node_count):
    for source in range(node_count):
      if distance[source][middle] == infinity:
        continue
      for target in range(node_count):
        candidate = distance[source][middle] + distance[middle][target]
        if candidate < distance[source][target]:
          distance[source][target] = candidate
  return distance
```

**复杂度**：时间 $O(V^3)$，空间 $O(V^2)$；通常适合 $V \le 400$ 左右的稠密图或大量两点查询，具体边界取决于语言与常数。

**易错点**：中间点循环必须在最外层；重边初始化要取最小值；无向图需要同时写入两个方向；不可达状态不能参与加法。运行结束后若存在 `distance[node][node] < 0`，说明该节点可达某个负权环。

**对应例题**：Python 对照实现：[1462. Course Schedule IV](https://leetcode.com/problems/course-schedule-iv/) 求课程依赖的传递闭包，但本地代码采用集合传播而非标准 Floyd 三重循环；将距离矩阵替换为布尔矩阵并使用 `reachable[source][target] |= reachable[source][middle] and reachable[middle][target]`，即可得到 Floyd-Warshall 的可达性版本。

### 非负权最短路

#### 堆优化 Dijkstra

**解决什么**：边权非负的单源最短路，以及把乘积概率等可单调扩展目标改写为“每次确定当前最优节点”的路径问题。

**核心原理**：小顶堆始终弹出当前距离最小的状态；若堆中距离已落后于 `distance[node]`，就是过期状态。非负边保证节点以最短距离出堆后无需被更短路径推翻。

```python
from heapq import heappop, heappush

def dijkstra(graph, start):
  distance = [float("inf")] * len(graph)
  distance[start] = 0
  heap = [(0, start)]
  while heap:
    current, node = heappop(heap)
    if current != distance[node]:
      continue
    for neighbor, weight in graph[node]:
      candidate = current + weight
      if candidate < distance[neighbor]:
        distance[neighbor] = candidate
        heappush(heap, (candidate, neighbor))
  return distance
```

**复杂度**：邻接表加二叉堆为 $O((V+E)\log V)$ 时间、$O(V+E)$ 空间。

**易错点**：存在负权边时不能使用 Dijkstra；同一节点可多次入堆，必须跳过过期状态；带方向、剩余资源等约束时，完整状态才是图节点。

**对应例题**：Python 实证：[1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) 使用最大堆式概率松弛。Python 对照实现：[743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) 实际使用 FIFO 队列反复松弛，类似 SPFA，并非 Dijkstra。

### 全局连通代价

#### Kruskal 最小生成树

**解决什么**：用最小总边权连接无向图全部节点；目标是整棵生成树的总成本，不是从某个源点到各点的最短距离。

**核心原理**：按边权从小到大扫描，只有当边的两端属于不同连通分量时才选边并合并集合。交换论证中的割性质保证跨越任意割的最轻安全边可进入某棵 MST。

```python
def kruskal(node_count, edges):
  dsu = DSU(node_count)
  total = used = 0
  for weight, first, second in sorted(edges):
    if dsu.union(first, second):
      total += weight
      used += 1
      if used == node_count - 1:
        return total
  return -1
```

**复杂度**：排序 $O(E\log E)$，并查集操作总计 $O(E\alpha(V))$，空间 $O(V+E)$。

**易错点**：无向边只需参与一次排序；必须选到恰好 $V-1$ 条边才连通；最小生成树与最短路径树的优化目标不同。

**对应例题**：Python 对照实现：[1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) 按边权执行 Kruskal 思路，但以集合列表线性查找、合并连通分量，并非并查集实现。

**补充练习**：

- Python 本地实现：[133. Clone Graph](https://leetcode.com/problems/clone-graph/)：图遍历与复制。
- Python 本地实现：[785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)：递归染色判断二分图。
- Python 本地实现：[332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)：欧拉路径。
- Python 本地实现：[3970. Shortest Path With At Most K Consecutive Identical Characters](https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/)：把连续字符限制并入路径状态。
- Python 本地实现：[4003. Minimum Cost Path with Alternating Directions III](https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/)：网格位置、方向奇偶状态与加权最短路。

## 并查集

### 动态连通性

#### 路径压缩与按大小合并

**解决什么**：只增加连接时，快速判断两个元素是否连通、合并集合、统计连通分量或检测新增边是否成环。

**核心原理**：`find` 把查询路径上的节点直接指向根；`union` 总把较小树挂到较大树根下。两种优化共同避免父指针链退化。

```python
class DSU:
  def __init__(self, size):
    self.parent = list(range(size))
    self.size = [1] * size
    self.components = size

  def find(self, node):
    while node != self.parent[node]:
      self.parent[node] = self.parent[self.parent[node]]
      node = self.parent[node]
    return node

  def union(self, first, second):
    first_root, second_root = self.find(first), self.find(second)
    if first_root == second_root:
      return False
    if self.size[first_root] < self.size[second_root]:
      first_root, second_root = second_root, first_root
    self.parent[second_root] = first_root
    self.size[first_root] += self.size[second_root]
    self.components -= 1
    return True
```

**复杂度**：初始化 $O(n)$；任意 $m$ 次合并与查找总计 $O(m\alpha(n))$，空间 $O(n)$。

**易错点**：按大小比较的是根节点；`union` 应返回是否真的合并，便于识别冗余边；普通并查集不直接支持在线删边。

**对应例题**：Python 对照实现：[684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) 使用路径压缩并通过 `union` 返回值检测环，但未按大小合并。

### 多集合建模

#### 坐标映射与多份并查集

**解决什么**：元素不是连续整数、不同类型实体需要落在同一连通模型，或多组用户共享部分边但各自维护连通性。

**核心原理**：先把邮箱、行列坐标等实体映射到并查集节点；共享边优先合并，再复制或分别维护多份 DSU。答案通常由成功合并次数、剩余分量数或根节点分组得到。

```python
def removable_shared_edges(node_count, edges):
  alice, bob = DSU(node_count), DSU(node_count)
  used = 0
  for edge_type, first, second in sorted(edges, reverse=True):
    first -= 1
    second -= 1
    if edge_type == 3:
      merged = alice.union(first, second)
      bob.union(first, second)
      used += merged
    elif edge_type == 1:
      used += alice.union(first, second)
    else:
      used += bob.union(first, second)
  if alice.components != 1 or bob.components != 1:
    return -1
  return len(edges) - used
```

**复杂度**：排序按边类型可用三次线性扫描；一般写法为 $O(E\log E+E\alpha(V))$ 时间、$O(V)$ 空间。

**易错点**：共享边必须先处理；行和列编号空间要避免冲突；按根分组前应再次 `find` 完成压缩；两份 DSU 都必须最终连通。

**对应例题**：Python 本地实现：[1579. Remove Max Number of Edges to Keep Graph Fully Traversable](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/) 使用共享边优先与双并查集，但本地 DSU 只有路径压缩、没有按大小合并。

**补充练习**：

- Python 本地实现：[547. Friend Circles](https://leetcode.com/problems/number-of-provinces/)：连通分量计数。
- Python 本地实现：[721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)：邮箱到账户的集合合并。
- Python 本地实现：[947. Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/)：行列坐标连通建模。
- Python 本地实现：[990. Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/)：先合并等式，再检查不等式。

<a id="深度优先搜索与广度优先搜索"></a>

## DFS 与 BFS

### 网格与连通块

#### 网格 DFS / Flood Fill

**解决什么**：统计网格连通块、判断路径存在、从边界反向标记可达区域，或遍历隐式图中的一个完整分量。

**核心原理**：每个格子是节点，相邻方向是边。进入格子时立即标记，避免沿无向边回到父节点；若一次搜索中的访问状态要供下一条候选路径复用，则返回前撤销。

```python
def flood_fill(grid, start_row, start_col):
  rows, columns = len(grid), len(grid[0])
  stack = [(start_row, start_col)]
  visited = {(start_row, start_col)}
  while stack:
    row, column = stack.pop()
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      nr, nc = row + dr, column + dc
      if 0 <= nr < rows and 0 <= nc < columns and (nr, nc) not in visited:
        if can_enter(grid, nr, nc):
          visited.add((nr, nc))
          stack.append((nr, nc))
  return visited
```

**复杂度**：每个格子至多访问一次，时间 $O(mn)$，栈与访问集合空间 $O(mn)$。

**易错点**：深网格递归 DFS 可能超过 Python 递归深度，显式栈更稳妥；永久访问标记与回溯临时标记语义不同；必须先判边界再访问网格。

**对应例题**：Python 本地实现：[417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) 使用从海岸反向搜索的建模；C++ 历史实现：[79. Word Search](https://leetcode.com/problems/word-search/)、[200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

### 同步扩散

#### 多源 BFS

**解决什么**：求每个位置到最近源点的距离、模拟多个起点同时扩散，或确定所有目标完成传播的最早时刻。

**核心原理**：把全部源点以距离 0 同时入队，相当于添加一个连接所有源点的虚拟超级源。队列按层推进，第一次到达即是最近源点距离。

```python
from collections import deque

def multi_source_distance(rows, columns, sources):
  distance = [[-1] * columns for _ in range(rows)]
  queue = deque()
  for row, column in sources:
    distance[row][column] = 0
    queue.append((row, column))
  while queue:
    row, column = queue.popleft()
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      nr, nc = row + dr, column + dc
      if 0 <= nr < rows and 0 <= nc < columns and distance[nr][nc] == -1:
        distance[nr][nc] = distance[row][column] + 1
        queue.append((nr, nc))
  return distance
```

**复杂度**：时间 $O(mn)$，空间 $O(mn)$。

**易错点**：所有源点必须在搜索开始前一起入队；入队时就标记，不能等出队；若源点有不同优先级或边权，普通多源 BFS 可能要改成堆或分桶。

**对应例题**：Python 本地实现：[3905. Multi Source Flood Fill](https://leetcode.com/problems/multi-source-flood-fill/) 含颜色优先级；C++ 历史实现：[994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

### 隐式状态图

#### 状态图 BFS

**解决什么**：字符串变换、密码锁、带钥匙或资源限制的最少操作次数，其中节点不是输入显式给出的图节点，而是一个完整状态。

**核心原理**：定义 `neighbors(state)` 生成一步可达状态；BFS 首次到达目标时层数最小。位置相同但附加资源不同通常是不同节点，`visited` 必须保存完整状态。

```python
from collections import deque

def shortest_steps(start, is_target, neighbors):
  queue = deque([(start, 0)])
  visited = {start}
  while queue:
    state, steps = queue.popleft()
    if is_target(state):
      return steps
    for next_state in neighbors(state):
      if next_state not in visited:
        visited.add(next_state)
        queue.append((next_state, steps + 1))
  return -1
```

**复杂度**：设可达状态数为 $S$、每个状态最多生成 $B$ 个邻居，时间 $O(SB)$，空间 $O(S)$。

**易错点**：状态必须可哈希且包含影响未来转移的全部信息；无权边才能用首次到达作为最短路；先检查禁用状态还是先检查目标要按题意决定。

**对应例题**：Python 本地实现：[127. Word Ladder](https://leetcode.com/problems/word-ladder/)、[752. Open the Lock](https://leetcode.com/problems/open-the-lock/)、[1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

## 回溯与搜索剪枝

### 选择路径

#### 选择、递归与撤销

**解决什么**：枚举组合、排列、分割方案，以及所有答案都对应搜索树中一条根到叶路径的问题。

**核心原理**：递归状态由当前路径、下一层候选和终止条件组成。做选择后递归，返回时撤销，使兄弟分支看到相同现场；组合用起始下标避免顺序重复，排列用 `used` 区分位置。

```python
def combinations(nums, target):
  answer, path = [], []

  def backtrack(start, remaining):
    if remaining == 0:
      answer.append(path.copy())
      return
    for index in range(start, len(nums)):
      value = nums[index]
      if value > remaining:
        break
      path.append(value)
      backtrack(index, remaining - value)
      path.pop()

  backtrack(0, target)
  return answer
```

**复杂度**：由搜索树规模决定，通常为指数级；输出 $A$ 个平均长度为 $L$ 的方案至少需要 $O(AL)$ 时间与空间，递归栈深度等于路径长度。

**易错点**：可重复选择时递归传 `index`，每个元素限用一次时传 `index + 1`；加入答案必须复制路径；候选未排序时不能按数值提前 `break`。

**对应例题**：Python 本地实现：[17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)、[39. Combination Sum](https://leetcode.com/problems/combination-sum/)

### 重复候选

#### 排序与同层去重

**解决什么**：输入含重复元素时生成不重复的组合或排列，避免先生成全部答案再用集合去重。

**核心原理**：先排序，让相同值相邻。同一递归层中，若当前值等于前一个值且前一个候选没有在本层被选择，就跳过；不同层仍可按题意使用相同值。

```python
def unique_permutations(nums):
  nums.sort()
  answer, path = [], []
  used = [False] * len(nums)

  def backtrack():
    if len(path) == len(nums):
      answer.append(path.copy())
      return
    for index, value in enumerate(nums):
      if used[index] or (index > 0 and value == nums[index - 1] and not used[index - 1]):
        continue
      used[index] = True
      path.append(value)
      backtrack()
      path.pop()
      used[index] = False

  backtrack()
  return answer
```

**复杂度**：最坏生成 $n!$ 个排列，时间 $O(n\cdot n!)$，结果外空间 $O(n)$；重复值会减少实际叶节点数。

**易错点**：去重条件约束的是同层，不是禁止不同层选择同值；排序是该判断成立的前提；组合去重常用 `index > start`，排列去重还要结合 `used`。

**对应例题**：Python 本地实现：[40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)、[47. Permutations II](https://leetcode.com/problems/permutations-ii/)

### 可行性边界

#### 上下界与对称性剪枝

**解决什么**：括号合法性、等和分桶、单词方阵等约束密集搜索，尽早排除不可能完成或与已搜索分支对称的状态。

**核心原理**：排序后优先放置约束最强的候选；维护剩余容量上下界；多个桶容量相同时只尝试第一个；一旦空桶尝试失败，其他空桶完全对称，可立即停止。

```python
def can_partition_k_subsets(nums, bucket_count):
  total = sum(nums)
  if total % bucket_count:
    return False
  target = total // bucket_count
  nums.sort(reverse=True)
  buckets = [0] * bucket_count

  def backtrack(index):
    if index == len(nums):
      return True
    value = nums[index]
    seen = set()
    for bucket in range(bucket_count):
      if buckets[bucket] in seen or buckets[bucket] + value > target:
        continue
      seen.add(buckets[bucket])
      buckets[bucket] += value
      if backtrack(index + 1):
        return True
      buckets[bucket] -= value
      if buckets[bucket] == 0:
        break
    return False

  return nums[0] <= target and backtrack(0)
```

**复杂度**：最坏仍为 $O(k^n)$ 时间、$O(n+k)$ 空间；排序和对称性剪枝只减少实际搜索量，不改变最坏指数级上界。

**易错点**：剪枝必须证明不会删掉唯一解；等容量桶是可交换的，桶有标签时不能套对称剪枝；重复状态很多时应考虑记忆化或状态压缩 DP。

**对应例题**：Python 本地实现：[22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) 使用合法前缀剪枝；[698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) 使用降序、目标和与分桶搜索；[3799. Word Squares II](https://leetcode.com/problems/word-squares-ii/) 使用位掩码记录选择并按前缀约束候选。

**补充练习**：

- Python 本地实现：[131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)：分割型回溯；可预处理回文区间减少重复判断。

## 动态规划

动态规划先写清状态含义、转移、初值和计算顺序；不可达状态不能参与转移。树上选或不选等模型见[树形 DP](#树形-dp)，此处不重复。

### 一维依赖

#### 线性 DP 与滚动状态

**解决什么**：数组前缀上的最优选择、相邻元素不能同时选择、路径逐层转移，以及当前状态只依赖固定数量前项的问题。

**核心原理**：令 `dp[i]` 表示处理前 $i$ 个元素的最优值。若只依赖 `dp[i-1]`、`dp[i-2]`，用两个变量滚动；压缩前必须确认本轮不会读取已覆盖状态。

```python
def rob_linear(values):
  previous_two = previous_one = 0
  for value in values:
    current = max(previous_one, previous_two + value)
    previous_two, previous_one = previous_one, current
  return previous_one
```

**复杂度**：时间 $O(n)$，额外空间 $O(1)$；需要还原方案时通常保留 $O(n)$ 的前驱信息。

**易错点**：状态是“前 $i$ 个”还是“必须选第 $i$ 个”会产生不同转移；环形序列通常拆成不选首项与不选末项；空输入初值要有定义。

**对应例题**：C++ 历史实现：[198. House Robber](https://leetcode.com/problems/house-robber/)；Python 本地实现：[120. Triangle](https://leetcode.com/problems/triangle/) 使用逐层路径 DP；Python 本地实现：[3840. House Robber V](https://leetcode.com/problems/house-robber-v/) 扩展了颜色约束。

### 容量选择

#### 0-1 背包与完全背包

**解决什么**：每件物品最多选一次或可无限次，在容量限制下判断可达性、最大化价值或最小化物品数。

**核心原理**：一维压缩时，0-1 背包容量倒序，防止同一物品在本轮被重复使用；完全背包容量正序，允许读取本轮刚更新的状态来复用当前物品。

```python
def can_partition(nums):
  total = sum(nums)
  if total % 2:
    return False
  target = total // 2
  reachable = [False] * (target + 1)
  reachable[0] = True
  for value in nums:
    for capacity in range(target, value - 1, -1):
      reachable[capacity] |= reachable[capacity - value]
  return reachable[target]
```

**复杂度**：$n$ 件物品、容量 $C$ 时，时间 $O(nC)$，空间 $O(C)$。

**易错点**：遍历方向决定物品能否复用；最小化问题应以 $+\infty$ 初始化不可达状态；计数、排列数和组合数的循环顺序不同。

**对应例题**：Python 本地实现：[322. Coin Change](https://leetcode.com/problems/coin-change/)、[416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

### 序列对齐

#### 双序列 DP

**解决什么**：最长公共子序列、编辑与匹配、两个字符串前缀之间的转换代价。

**核心原理**：`dp[i][j]` 表示两个序列前缀 `first[:i]`、`second[:j]` 的答案；末尾元素相等时继承左上角，否则从删去一侧末尾的状态中选择。

```python
def longest_common_subsequence(first, second):
  previous = [0] * (len(second) + 1)
  for left in first:
    current = [0]
    for column, right in enumerate(second, 1):
      if left == right:
        current.append(previous[column - 1] + 1)
      else:
        current.append(max(previous[column], current[-1]))
    previous = current
  return previous[-1]
```

**复杂度**：时间 $O(mn)$，滚动数组空间 $O(n)$；交换两个序列可令空间为 $O(\min(m,n))$。

**易错点**：为空前缀预留第 0 行和第 0 列；子序列不要求连续；正则匹配等特殊问题的转移不能直接等同于 LCS。

**对应例题**：Python 本地实现：[583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) 使用记忆化 LCS；C++ 历史实现：[1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)；Python 本地实现：[3995. Minimum Cost to Convert String III](https://leetcode.com/problems/minimum-cost-to-convert-string-iii/) 使用字符串分段 DP。

### 区间合并

#### 区间 DP

**解决什么**：合并、切分、括号化或选择区间中最后一个操作，使大区间答案可由两个独立小区间合并。

**核心原理**：按区间长度从短到长计算。以戳气球为例，枚举区间内最后被戳的气球 `middle`，此时左右区间已独立完成，边界贡献确定。

```python
def burst_balloons(nums):
  values = [1] + nums + [1]
  size = len(values)
  dp = [[0] * size for _ in range(size)]
  for length in range(2, size):
    for left in range(size - length):
      right = left + length
      dp[left][right] = max(
        dp[left][middle] + values[left] * values[middle] * values[right] + dp[middle][right]
        for middle in range(left + 1, right)
      )
  return dp[0][-1]
```

**复杂度**：该模板时间 $O(n^3)$，空间 $O(n^2)$。

**易错点**：先明确区间是开区间还是闭区间；必须保证子区间已计算；枚举“最后一步”常比枚举“第一步”更容易让左右子问题独立。

**对应例题**：Python 本地实现：[312. Burst Balloons](https://leetcode.com/problems/burst-balloons/)

### 线性区间扩张

#### 从起点向两端扩张

**解决什么**：目标点位于一条线上，从起点出发逐个访问；访问过的目标必然形成连续区间，移动时所有未完成目标还会同时累积等待代价。

**核心原理**：排序目标并插入起点。状态 `dp[left][right][side]` 表示已访问排序后区间 `[left, right]`，当前位置在左端或右端时的最小总代价。区间外只可能先访问 `left-1` 或 `right+1`；移动距离乘以当前未完成目标数，就是这段移动对总完成时间之和的贡献。

```python
def minimum_total_completion_time(start, requests):
  request_set = set(requests)
  points = sorted(request_set | {start})
  size = len(points)
  origin = points.index(start)
  weights = [int(point in request_set) for point in points]
  prefix = [0]
  for weight in weights:
    prefix.append(prefix[-1] + weight)

  infinity = float("inf")
  left_dp = [[infinity] * size for _ in range(size)]
  right_dp = [[infinity] * size for _ in range(size)]
  left_dp[origin][origin] = right_dp[origin][origin] = 0
  for length in range(1, size + 1):
    for left in range(max(0, origin - length + 1), origin + 1):
      right = left + length - 1
      if right >= size or right < origin:
        continue
      unfinished = len(request_set) - (prefix[right + 1] - prefix[left])
      if left > 0:
        left_dp[left - 1][right] = min(
          left_dp[left - 1][right],
          left_dp[left][right] + unfinished * (points[left] - points[left - 1]),
          right_dp[left][right] + unfinished * (points[right] - points[left - 1]),
        )
      if right + 1 < size:
        right_dp[left][right + 1] = min(
          right_dp[left][right + 1],
          left_dp[left][right] + unfinished * (points[right + 1] - points[left]),
          right_dp[left][right] + unfinished * (points[right + 1] - points[right]),
        )
  return min(left_dp[0][-1], right_dp[0][-1])
```

**复杂度**：排序 $O(n\log n)$，区间状态时间和空间均为 $O(n^2)$。

**易错点**：路程对目标函数的贡献是“距离乘未完成数量”，不是只加本次到达时间；起点若本身是请求应在时刻 0 计为完成；只有目标在线上且越过目标即可顺便完成时，已访问集合才压缩成连续区间。

**对应例题**：Python 实证：[4023. Elevator Requests II](https://leetcode.com/problems/elevator-requests-ii/)：本地递归状态保存未访问区间两端与当前楼层，转移使用相同的剩余请求数加权。

### 子集状态

#### 状态压缩 DP

**解决什么**：$n$ 通常不超过 20，状态由一个已选择集合决定，并需要枚举剩余元素或子集转移的问题。

**核心原理**：用位掩码 `mask` 表示集合，`dp[mask]` 保存到达该集合的最优值。若后续代价还取决于当前位置，则扩展成 `dp[mask][last]`；在相同集合和终点下，只保留最早时间或最小代价，因为更差状态不会让后续转移更优。只有前置条件全部包含在 `mask` 中的元素才可加入；需要批量选择时可枚举非空子集。

```python
def minimum_semesters(prerequisites, limit):
  node_count = len(prerequisites)
  full = (1 << node_count) - 1
  dp = [float("inf")] * (1 << node_count)
  dp[0] = 0
  for mask in range(1 << node_count):
    available = 0
    for node, required in enumerate(prerequisites):
      if not (mask >> node & 1) and required & mask == required:
        available |= 1 << node
    subset = available
    while subset:
      if subset.bit_count() <= limit:
        dp[mask | subset] = min(dp[mask | subset], dp[mask] + 1)
      subset = (subset - 1) & available
  return dp[full]
```

**复杂度**：枚举所有状态及其子集最坏为 $O(3^n)$ 时间，空间 $O(2^n)$；`mask + last` 并逐个添加元素时通常为 $O(2^n n^2)$ 时间、$O(2^n n)$ 空间。

**易错点**：位编号与元素编号要统一；不可达状态不能参与转移；若转移代价依赖终点，不能只保留 `dp[mask]`；若只选固定数量，可只枚举满足 `bit_count` 的子集。数位 DP 虽也常用掩码记录已用数字，但还需 `position/tight/started` 状态。

**对应例题**：Python 对照实现：[1494. Parallel Courses II](https://leetcode.com/problems/parallel-courses-ii/) 当前按解锁数量启发式选课，并非状态压缩 DP 实证；Python 本地实现：[2376. Count Special Integers](https://leetcode.com/problems/count-special-integers/) 使用数位状态与已用数字集合。

**补充练习**：

- C++ 历史实现：[300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)：序列 DP。
- Python 本地实现：[3700. Number of ZigZag Arrays II](https://leetcode.com/problems/number-of-zigzag-arrays-ii/)：状态转移矩阵与快速幂。

## 贪心

贪心成立的关键是证明局部选择具有安全性。常用论证是交换论证、支配关系和反证法；若无法把任意最优解改造成包含当前选择的最优解，就应保留多个状态并考虑 DP。

### 区间选择

#### 最早结束时间贪心

**解决什么**：选择最多个互不重叠区间，或等价地删除最少区间使剩余区间互不重叠。

**核心原理**：按右端点升序选择第一个兼容区间。正确性用交换论证：任意最优解的第一个区间都可换成结束更早的贪心区间，后续可用空间只会增大，不会减少可选数量。

```python
def maximum_non_overlapping(intervals):
  end = float("-inf")
  selected = 0
  for left, right in sorted(intervals, key=lambda interval: interval[1]):
    if left >= end:
      selected += 1
      end = right
  return selected
```

**复杂度**：排序 $O(n\log n)$，扫描 $O(n)$，额外空间取决于排序实现。

**易错点**：按开始时间排序不能保证留出最大后续空间；端点接触是否冲突决定使用 `>=` 还是 `>`；加权区间调度不能套此贪心，应使用 DP。

**对应例题**：Python 本地实现：[435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

### 排序配对

#### 同序配对与交换论证

**解决什么**：两个序列一一配对，收益形如乘积，或要把更稀缺、更高收益的资源分配给价值更大的对象。

**核心原理**：将两侧同序排序后配对。对 $a\ge b$、$x\ge y$，有 $ax+by\ge ay+bx$，因为两式之差为 $(a-b)(x-y)\ge0$；反复消除逆序配对即可得到全局最优。

```python
def minimum_discounted_price(prices, discounts):
  prices.sort(reverse=True)
  discounts.sort(reverse=True)
  answer = sum(prices)
  for price, discount in zip(prices, discounts):
    answer -= price * discount / 100
  return answer
```

**复杂度**：排序时间 $O(n\log n+m\log m)$，额外空间由排序实现决定。

**易错点**：先确认目标可写成独立配对收益；存在容量、依赖或位置约束时交换可能不可行；浮点金额按题目要求处理精度与舍入。

**对应例题**：Python 实证：[4014. Minimum Total Price After Applying Discounts](https://leetcode.com/problems/minimum-total-price-after-applying-discounts/)；Python 本地实现：[1710. Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/)；C++ 历史实现：[455. Assign Cookies](https://leetcode.com/problems/assign-cookies/)

### 候选支配

#### 保留支配候选

**解决什么**：多个候选可重复使用且没有容量耦合，其中一个候选对每个输入都不劣于另一个候选，可以先删除所有被支配候选再求解。

**核心原理**：若候选 $A$ 对任意任务的代价都不大于候选 $B$，则任何使用 $B$ 的方案都能把它替换为 $A$ 而不变差。同步交通灯中，绿灯时长更大的灯覆盖更短灯的全部零等待时刻；红灯等待又只由到达余数决定，因此只保留最大绿灯时长即可。

```python
def minimum_maximum_wait(period, green_lengths, arrivals):
  longest_green = max(green_lengths)

  def wait(arrival):
    remainder = arrival % period
    return 0 if remainder < longest_green else period - remainder

  return max(map(wait, arrivals))
```

**复杂度**：寻找支配候选并扫描任务，时间 $O(n+m)$，辅助空间 $O(1)$。

**易错点**：支配必须对所有可能输入成立；候选有容量、费用、不同相位或任务间冲突时，不能独立替换；最小化最大值仍需检查每个任务在支配候选下的代价。

**对应例题**：Python 实证：[4025. Minimize the Maximum Waiting Time at Synchronized Traffic Lights](https://leetcode.com/problems/minimize-the-maximum-waiting-time-at-synchronized-traffic-lights/)

### 连续覆盖

#### 当前可达范围内延伸最远

**解决什么**：用最少区间覆盖目标范围，或在当前位置之前选择能把边界推进最远的候选。

**核心原理**：扫描所有左端点不超过当前边界的区间，只保留最远右端点；必须做选择时才增加次数。支配论证：任何更短的可用区间都不能提供贪心区间之外的新后续候选，因此可被最远者替换。

```python
def minimum_cover(intervals, target):
  intervals.sort()
  used = index = current = 0
  while current < target:
    farthest = current
    while index < len(intervals) and intervals[index][0] <= current:
      farthest = max(farthest, intervals[index][1])
      index += 1
    if farthest == current:
      return -1
    current = farthest
    used += 1
  return used
```

**复杂度**：排序 $O(n\log n)$，扫描 $O(n)$，额外空间由排序实现决定。

**易错点**：必须在同一当前边界下看完所有候选再选择；无法推进时立即无解；最大不相交区间应按结束时间，而覆盖问题按当前可达范围延伸最远。

**对应例题**：Python 本地实现：[1024. Video Stitching](https://leetcode.com/problems/video-stitching/)；C++ 历史实现：[134. Gas Station](https://leetcode.com/problems/gas-station/) 使用“区间总和为负则该段起点全部失败”的批量排除思想。

### 局部贡献

#### 峰谷替换与正增量累加

**解决什么**：收益可拆成相邻增量，或只需保留最有利峰谷而中间选择可被支配的问题。

**核心原理**：股票无限次交易中，每段上涨总利润等于所有正相邻差之和；波动序列中，同方向连续变化只保留更极端端点。交换论证说明把中间点替换为更高峰或更低谷不会减少后续选择空间。

```python
def sum_positive_gains(values):
  return sum(
    max(0, current - previous)
    for previous, current in zip(values, values[1:])
  )
```

**复杂度**：时间 $O(n)$，额外空间 $O(1)$。

**易错点**：只有交易次数不限且无手续费、冷冻期等跨期约束时才能直接累加正增量；峰谷贪心要忽略零差并正确处理最后趋势。

**对应例题**：Python 本地实现：[376. Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/)；C++ 历史实现：[122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

**补充练习**：

- Python 本地实现：[763. Partition Labels](https://leetcode.com/problems/partition-labels/)：扫描字符最后出现位置，当前下标到达最远边界时切分。

## 区间问题

### 区间归并

#### 按左端点排序合并

**解决什么**：合并重叠区间、求覆盖并集，或先把零散区间规范化后再查询。

**核心原理**：按左端点排序后，尚未合并的区间只可能与结果末尾相交；相交时扩展右端点，否则开启新区间。闭区间中 `left <= last_right` 表示接触也合并，半开区间需按题意调整。

```python
def merge_intervals(intervals):
  merged = []
  for left, right in sorted(intervals):
    if not merged or left > merged[-1][1]:
      merged.append([left, right])
    else:
      merged[-1][1] = max(merged[-1][1], right)
  return merged
```

**复杂度**：排序时间 $O(n\log n)$，扫描时间 $O(n)$；除返回结果外辅助空间取决于排序实现。

**易错点**：先明确端点开闭和“接触是否重叠”；新区间要复制成可修改对象；当前区间被包含时不能缩短已有右端点。

**对应例题**：Python 本地实现：[1288. Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/)，本地题解同样先排序，但执行的是包含区间计数而非直接套用合并模板。

### 无权区间调度

#### 最早结束时间贪心

**解决什么**：选择最多个互不重叠区间、求最少删除数，或用最少的点命中所有区间。

**核心原理**：按右端点升序选择第一个与已选区间兼容的候选。最早结束的区间给后续留下最大空间；交换论证可将任一最优解的首个区间替换为它而不变差。

```python
def max_non_overlapping(intervals):
  chosen = 0
  last_end = float("-inf")
  for left, right in sorted(intervals, key=lambda interval: interval[1]):
    if left >= last_end:
      chosen += 1
      last_end = right
  return chosen
```

**复杂度**：时间 $O(n\log n)$，排序外辅助空间 $O(1)$。

**易错点**：`>=` 还是 `>` 由接触是否算重叠决定；不要按左端点贪心；“最少删除”应返回 `n - chosen`。

**对应例题**：Python 本地实现：[435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)；C++ 历史实现：[452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

### 重叠计数

#### 事件扫描线

**解决什么**：求最大同时重叠数、最少分组数，或统计每个坐标处的活动区间数量。

**核心原理**：把每个区间拆成开始增量和结束减量，按坐标累加。闭区间 $[left,right]$ 可在 `right + 1` 处减一；一般坐标则必须把同点事件优先级编码进排序键。

```python
def maximum_overlap_closed(intervals):
  events = []
  for left, right in intervals:
    events.append((left, 1))
    events.append((right + 1, -1))
  active = answer = 0
  for _, delta in sorted(events):
    active += delta
    answer = max(answer, active)
  return answer
```

**复杂度**：事件排序时间 $O(n\log n)$，扫描时间 $O(n)$，空间 $O(n)$。

**易错点**：只有整数闭区间才能无条件使用 `right + 1`；半开区间同点先结束再开始；闭区间接触算重叠时同点先开始再结束。

**对应例题**：Python 本地实现：[2406. Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/)

### 加权区间选择

#### 二分前驱加动态规划

**解决什么**：每个区间带收益时，选择互不重叠区间使总收益最大；普通最早结束贪心不再保证最优。

**核心原理**：按结束时间排序，令 `dp[i]` 为前 `i` 个任务的最大收益。对第 `i` 个任务二分最后一个结束时间不晚于其开始时间的前驱，在“不选”和“选并接前驱最优值”之间取最大值。

```python
from bisect import bisect_right

def weighted_interval_scheduling(jobs):
  jobs = sorted(jobs, key=lambda job: job[1])
  ends = [end for _, end, _ in jobs]
  dp = [0] * (len(jobs) + 1)
  for index, (start, _, profit) in enumerate(jobs, 1):
    previous = bisect_right(ends, start, hi=index - 1)
    dp[index] = max(dp[index - 1], dp[previous] + profit)
  return dp[-1]
```

**复杂度**：排序和全部二分为 $O(n\log n)$，DP 空间 $O(n)$。

**易错点**：前驱兼容条件决定使用 `bisect_right` 还是 `bisect_left`；二分范围不能包含当前任务；按开始时间递归和按结束时间迭代是两种不同但等价的状态设计。

**对应例题**：Python 本地实现：[1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)，本地源码采用按开始时间排序、二分下一个可选任务的记忆化 DP。

**补充练习**：

- Python 本地实现：[729. My Calendar I](https://leetcode.com/problems/my-calendar-i/)：在线检查新区间冲突。
- C++ 历史实现：[986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)：两个有序区间列表双指针求交。

## 字典树与字符串算法

字符串算法的关键不是背诵函数名，而是先判断查询模型：单模式还是多模式、只匹配一次还是大量比较、是否要求确定性、是否关心前缀或回文结构。不同模型决定应使用 Trie、KMP、Z、哈希还是回文算法。

### 前缀结构

#### Trie 前缀树

**解决什么**：动态插入单词，查询完整单词或公共前缀；也可扩展到通配符搜索、网格多词搜索和 01 Trie。

**核心原理**：每条根到节点的路径代表一个前缀，相同前缀共享节点。节点必须额外记录是否为某个完整单词的结尾。

```python
class TrieNode:
  def __init__(self):
    self.children = {}
    self.is_word = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    node = self.root
    for char in word:
      node = node.children.setdefault(char, TrieNode())
    node.is_word = True

  def search(self, word):
    node = self.root
    for char in word:
      if char not in node.children:
        return False
      node = node.children[char]
    return node.is_word
```

**复杂度**：长度为 $L$ 的字符串，插入和查询均为 $O(L)$；空间与所有互异前缀的字符总数成正比。

**易错点**：到达路径末端不代表单词存在，必须检查 `is_word`；字符集固定且较小时可用数组换取更低常数；回溯搜索应直接携带当前 Trie 节点，避免每步从根重复查询。

**对应例题**：

- Python 实证：[208. Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/)
- Python 实证：[211. Add and Search Word](https://leetcode.com/problems/design-add-and-search-words-data-structure/)：通配符 DFS
- Python 实证：[212. Word Search II](https://leetcode.com/problems/word-search-ii/)：Trie + 网格回溯

### 单模式字符串匹配

#### KMP 前缀函数

**解决什么**：在线性时间内寻找模式串出现位置、计算最长相等真前后缀、判断字符串周期。

**核心原理**：`prefix[i]` 表示 `text[:i + 1]` 的最长相等真前后缀长度。失配时令 `matched = prefix[matched - 1]`，沿已经计算出的边界继续尝试，因此文本指针不会回退。

```python
def prefix_function(text):
  prefix = [0] * len(text)
  for right in range(1, len(text)):
    matched = prefix[right - 1]
    while matched > 0 and text[right] != text[matched]:
      matched = prefix[matched - 1]
    if text[right] == text[matched]:
      matched += 1
    prefix[right] = matched
  return prefix

def kmp_search(text, pattern):
  if not pattern:
    return 0
  prefix = prefix_function(pattern)
  matched = 0
  for index, char in enumerate(text):
    while matched > 0 and char != pattern[matched]:
      matched = prefix[matched - 1]
    if char == pattern[matched]:
      matched += 1
    if matched == len(pattern):
      return index - len(pattern) + 1
  return -1
```

**复杂度**：预处理与匹配总时间 $O(n + m)$；空间 $O(m)$。

**易错点**：前缀必须是真前缀，不能等于整个字符串；失配跳转使用 `prefix[matched - 1]`；找到一次匹配后若要继续寻找，应把 `matched` 退到 `prefix[matched - 1]`。

**对应例题**：

- Python 标准实现：[1392. Longest Happy Prefix KMP](https://leetcode.com/problems/longest-happy-prefix/)
- 近似 / 非标准实现：[1392. Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/) 当前为切片枚举，最坏 $O(n^2)$

#### Z 函数

**解决什么**：计算每个后缀与原串的最长公共前缀，适合模式匹配、前缀贡献、周期判断和“模式串 + 文本”建模。

**核心原理**：维护当前最靠右的匹配区间 `[left, right]`。位置落在区间内时先复用对应的 Z 值，只有可能越过右边界时才继续逐字符扩展。

```python
def z_function(text):
  size = len(text)
  z = [0] * size
  left = right = 0
  for index in range(1, size):
    if index <= right:
      z[index] = min(right - index + 1, z[index - left])
    while index + z[index] < size and text[z[index]] == text[index + z[index]]:
      z[index] += 1
    if index + z[index] - 1 > right:
      left = index
      right = index + z[index] - 1
  return z
```

**复杂度**：时间 $O(n)$；空间 $O(n)$。

**易错点**：`z[0]` 取 `0` 还是 `n` 要在调用方统一；拼接模式与文本时应选不会出现在输入中的分隔符；命中位置需扣除模式和分隔符的偏移。

**对应例题**：

- Python 实证：[2223. Sum of Scores of Built Strings](https://leetcode.com/problems/sum-of-scores-of-built-strings/)
- Python 实证：[3008. Find Beautiful Indices in the Given Array II](https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/)
- Python 实证：[3036. Number of Subarrays That Match a Pattern II](https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/)

#### 滚动哈希

**解决什么**：大量比较定长或任意子串、二分最长公共前缀、查找重复子串。

**核心原理**：把字符串视为多项式，预处理前缀哈希与底数幂，使任意子串哈希可以 $O(1)$ 取得。

```python
class RollingHash:
  def __init__(self, text, base=911382323, mod=1_000_000_007):
    size = len(text)
    self.base = base
    self.mod = mod
    self.prefix = [0] * (size + 1)
    self.power = [1] * (size + 1)
    for index, char in enumerate(text):
      self.prefix[index + 1] = (self.prefix[index] * base + ord(char)) % mod
      self.power[index + 1] = self.power[index] * base % mod

  def get(self, left, right):
    return (self.prefix[right] - self.prefix[left] * self.power[right - left]) % self.mod
```

**复杂度**：预处理 $O(n)$；单次半开区间 `[left, right)` 查询 $O(1)$；空间 $O(n)$。

**易错点**：哈希碰撞无法从理论上消除；双哈希只能降低概率。要求确定性正确时应验证原串，或改用 KMP、Z、后缀结构。区间开闭和字符编码必须统一。

**对应例题**：Python 实证：[2156. Find Substring With Given Hash Value](https://leetcode.com/problems/find-substring-with-given-hash-value/)

### 回文字符串

#### 回文中心扩展

**解决什么**：枚举回文子串、求最长回文，或把回文区间与 DP 组合；适合数据规模允许 $O(n^2)$ 的场景。

**核心原理**：每个回文都有一个中心。分别以单个字符和相邻字符间隙为中心向两侧扩展，即可覆盖奇数和偶数长度回文。

```python
def longest_palindrome_expand(text):
  best_left = best_right = 0
  for center in range(len(text)):
    for left, right in ((center, center), (center, center + 1)):
      while left >= 0 and right < len(text) and text[left] == text[right]:
        if right - left > best_right - best_left:
          best_left, best_right = left, right
        left -= 1
        right += 1
  return text[best_left:best_right + 1]
```

**复杂度**：时间最坏 $O(n^2)$；除结果外空间 $O(1)$。

**易错点**：必须分别处理奇偶中心；与 DP 组合时要明确发现回文区间的顺序是否满足状态依赖。

**对应例题**：Python 实证：[2472. Maximum Number of Non-overlapping Palindrome Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/)

#### Manacher 算法

**解决什么**：在线性时间内计算所有位置的回文半径，进而求最长回文子串或统计回文信息。

**核心原理**：插入分隔符统一奇偶回文。维护当前最右回文区间的中心和右边界；区间内的位置先复用关于中心对称的镜像半径，再尝试向外扩展。

```python
def manacher(text):
  transformed = "^#" + "#".join(text) + "#$"
  radius = [0] * len(transformed)
  center = right = 0
  for index in range(1, len(transformed) - 1):
    mirror = 2 * center - index
    if index < right:
      radius[index] = min(right - index, radius[mirror])
    while transformed[index + radius[index] + 1] == transformed[index - radius[index] - 1]:
      radius[index] += 1
    if index + radius[index] > right:
      center = index
      right = index + radius[index]
  return radius
```

**复杂度**：时间 $O(n)$；空间 $O(n)$。

**易错点**：哨兵字符必须不与输入冲突；`right` 通常表示当前回文覆盖的开区间右端；映射回原串时，起点为 `(center - radius[center]) // 2`。

**对应例题**：当前仓库暂无 Manacher 本地实现；可将本节模板用于 5. Longest Palindromic Substring。

### 多模式匹配

#### AC 自动机

**解决什么**：在同一文本中同时匹配大量模式串，例如敏感词扫描；它将 Trie 的多模式共享与 KMP 的失配跳转结合起来。

**核心原理**：先建立 Trie，再用 BFS 为每个节点构造失败指针 `fail`，指向当前前缀失配后可接续的最长后缀状态。扫描文本时沿字符边和失败指针移动，并汇总当前节点输出。

```python
from collections import deque

class AhoCorasick:
  def __init__(self):
    self.next = [{}]
    self.fail = [0]
    self.output = [[]]

  def add(self, word, word_id):
    node = 0
    for char in word:
      if char not in self.next[node]:
        self.next[node][char] = len(self.next)
        self.next.append({})
        self.fail.append(0)
        self.output.append([])
      node = self.next[node][char]
    self.output[node].append(word_id)

  def build(self):
    queue = deque(self.next[0].values())
    while queue:
      node = queue.popleft()
      self.output[node].extend(self.output[self.fail[node]])
      for char, child in self.next[node].items():
        fallback = self.fail[node]
        while fallback and char not in self.next[fallback]:
          fallback = self.fail[fallback]
        self.fail[child] = self.next[fallback].get(char, 0)
        queue.append(child)

  def find(self, text):
    matches = []
    node = 0
    for index, char in enumerate(text):
      while node and char not in self.next[node]:
        node = self.fail[node]
      node = self.next[node].get(char, 0)
      for word_id in self.output[node]:
        matches.append((index, word_id))
    return matches
```

**复杂度**：设模式总长度为 $S$、最长模式长度为 $L$、文本长度为 $T$。当前稀疏字典模板的建树为 $O(S)$，朴素失败跳转建表最坏为 $O(SL)$，扫描为均摊 $O(T + \text{匹配数})$，空间为 $O(S + \text{匹配数})$。固定字符集下补全所有转移可用 $O(SC)$ 建表，换取严格的常数时间状态转移。

**易错点**：输出需要沿失败指针继承；调用匹配前必须完成 `build()`；[1032. Stream of Characters](https://leetcode.com/problems/stream-of-characters/) 使用的是反向 Trie，没有失败指针，因此不是 AC 自动机。

**对应例题**：模板待补；当前仓库暂无使用 AC 自动机的本地题解。

## 位运算

### 异或消元

#### 异或分组与位状态机

**解决什么**：其余元素成对或成固定次数出现时找异常值，以及把每一位的出现次数压缩进有限状态。

**核心原理**：异或满足 `value ^ value = 0` 且交换、结合律成立。两个异常值时先异或得到差异位，再用 `xor_sum & -xor_sum` 分组；出现三次的问题可对每一位计数模 $3$。

```python
def two_single_numbers(nums):
  xor_sum = 0
  for value in nums:
    xor_sum ^= value
  lowbit = xor_sum & -xor_sum
  first = second = 0
  for value in nums:
    if value & lowbit:
      first ^= value
    else:
      second ^= value
  return first, second
```

**复杂度**：时间 $O(n)$，辅助空间 $O(1)$。

**易错点**：分组位必须来自两个答案的差异位；Python 处理负数逐位计数时要限定字长；“出现三次”不能直接用整体异或消去。

**对应例题**：Python 本地实现：[137. Single Number II](https://leetcode.com/problems/single-number-ii/)；C++ 历史实现：[260. Single Number III](https://leetcode.com/problems/single-number-iii/)

### 二进制最低位

#### lowbit 与位计数 DP

**解决什么**：统计二进制中 $1$ 的个数、枚举置位位置，或批量计算 `0..n` 的位计数。

**核心原理**：`value & -value` 只保留最低位的 $1$，`value & (value - 1)` 删除最低位的 $1$。批量计数可复用 `bits[value >> 1] + (value & 1)`。

```python
def count_bits(limit):
  bits = [0] * (limit + 1)
  for value in range(1, limit + 1):
    bits[value] = bits[value >> 1] + (value & 1)
  return bits
```

**复杂度**：生成全部答案的时间和空间均为 $O(n)$；单个整数用消位法为 $O(\operatorname{popcount}(x))$ 时间、$O(1)$ 空间。

**易错点**：`value & value - 1` 应加括号表达意图；Python 负数没有有限的前导零，直接循环清位不会按固定字长结束；`lowbit(0)` 为 `0`。

**对应例题**：Python 本地实现：[338. Counting Bits](https://leetcode.com/problems/counting-bits/)；C++ 历史实现：[191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

### 小集合状态压缩

#### 位掩码与子集枚举

**解决什么**：元素种类较少时表示集合、枚举一个集合的所有子集，或记录字符出现次数的奇偶状态。

**核心原理**：第 `bit` 位表示一种元素是否存在。`subset = (subset - 1) & mask` 会按降序遍历 `mask` 的所有非空子集；前缀异或掩码可让两前缀之间的奇偶状态直接相消。

```python
def enumerate_subsets(mask):
  subsets = []
  subset = mask
  while subset:
    subsets.append(subset)
    subset = (subset - 1) & mask
  subsets.append(0)
  return subsets
```

**复杂度**：单个掩码含 $k$ 个置位时枚举时间和输出空间均为 $O(2^k)$；枚举所有 $n$ 位掩码的全部子集总量为 $O(3^n)$。

**易错点**：循环通常不包含空集，要在循环后单独处理；状态种类过多时掩码 DP 会指数爆炸；字符到位下标的映射必须稳定。

**对应例题**：Python 本地实现：[1915. Number of Wonderful Substrings](https://leetcode.com/problems/number-of-wonderful-substrings/)，本地源码使用前缀奇偶掩码计数，并非显式枚举全部子集。

### 按位最优选择

#### 01 Trie 最大异或

**解决什么**：从一组非负整数中寻找与查询值异或最大的元素，或附带上界条件回答离线查询。

**核心原理**：把整数从最高位到最低位插入二叉 Trie。查询时优先走与当前位相反的分支，使答案的当前位为 $1$；高位贡献始终优先于所有低位贡献。

```python
def maximum_xor_pair(nums, width=31):
  root = {}
  for value in nums:
    node = root
    for bit in range(width - 1, -1, -1):
      node = node.setdefault((value >> bit) & 1, {})
  answer = 0
  for value in nums:
    node = root
    current = 0
    for bit in range(width - 1, -1, -1):
      digit = (value >> bit) & 1
      chosen = digit ^ 1 if (digit ^ 1) in node else digit
      current |= (chosen ^ digit) << bit
      node = node[chosen]
    answer = max(answer, current)
  return answer
```

**复杂度**：设固定字长为 $W$，建树和查询总时间 $O(nW)$，空间 $O(nW)$。

**易错点**：字长要覆盖最大输入；有查询上界时可按上界排序后增量插入，避免在 Trie 中回溯筛值；负数需要先规定补码位宽。

**对应例题**：Python 本地实现：[1707. Maximum XOR With an Element From Array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/) 使用 01 Trie，但在 Trie 内按上界回溯；[421. Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

**补充练习**：

- C++ 历史实现：[201. Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)：寻找区间端点的公共二进制前缀。

## 数学与数论

### 整除关系

#### 欧几里得与扩展欧几里得

**解决什么**：计算最大公约数、最小公倍数，求解裴蜀等式 $ax+by=\gcd(a,b)$，以及在互质条件下求模逆元。

**核心原理**：`gcd(a, b) = gcd(b, a % b)` 不断缩小问题。递归回代余数关系即可同时得到系数 `x, y`；当 `gcd(a, mod) == 1` 时，`x % mod` 是 `a` 的逆元。

```python
def extended_gcd(a, b):
  if b == 0:
    return abs(a), 1 if a >= 0 else -1, 0
  gcd, next_x, next_y = extended_gcd(b, a % b)
  return gcd, next_y, next_x - (a // b) * next_y

def lcm(a, b):
  gcd, _, _ = extended_gcd(a, b)
  return 0 if gcd == 0 else abs(a // gcd * b)
```

**复杂度**：时间 $O(\log \min(|a|,|b|))$，递归栈空间同阶。

**易错点**：模逆元只在互质时存在；负数的商和余数约定会影响回代系数；计算最小公倍数应先除后乘以降低定宽整数溢出风险。

**对应例题**：Python 本地实现：[1979. Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) 使用库函数 `gcd`；C++ 历史实现：[1250. Check If It Is a Good Array](https://leetcode.com/problems/check-if-it-is-a-good-array/) 使用裴蜀定理。仓库例题没有扩展欧几里得实证。

### 幂与模运算

#### 二进制快速幂

**解决什么**：高效计算 $base^{exponent}$ 或模幂，并作为矩阵快速幂、组合数逆元等算法的基础。

**核心原理**：把指数按二进制拆分；当前位为 $1$ 时乘入答案，每轮将底数平方、指数右移一位。

```python
def fast_power(base, exponent, mod=None):
  result = 1
  while exponent > 0:
    if exponent & 1:
      result = result * base if mod is None else result * base % mod
    base = base * base if mod is None else base * base % mod
    exponent >>= 1
  return result
```

**复杂度**：时间 $O(\log exponent)$，辅助空间 $O(1)$。

**易错点**：负指数需转为倒数后处理正指数；模意义下不能直接做普通除法；底数乘法可能溢出的语言要使用更宽类型或安全乘法。

**对应例题**：Python 本地实现：[1922. Count Good Numbers](https://leetcode.com/problems/count-good-numbers/) 使用模快速幂；C++ 历史实现：[50. Pow(x, n)](https://leetcode.com/problems/powx-n/)、[372. Super Pow](https://leetcode.com/problems/super-pow/)

### 素数预处理

#### 埃氏筛

**解决什么**：批量判断不超过上界的素数、枚举区间素数，或为质因数分解和计数预处理。

**核心原理**：从小到大扫描；发现素数 `prime` 后，从 `prime * prime` 开始标记其倍数。更小倍数已经被更小质因子处理。

```python
def eratosthenes(limit):
  is_prime = bytearray(b"\x01") * (limit + 1)
  if limit >= 0:
    is_prime[0] = 0
  if limit >= 1:
    is_prime[1] = 0
  for prime in range(2, int(limit ** 0.5) + 1):
    if is_prime[prime]:
      start = prime * prime
      is_prime[start:limit + 1:prime] = b"\x00" * (((limit - start) // prime) + 1)
  return is_prime
```

**复杂度**：时间 $O(n\log\log n)$，空间 $O(n)$。

**易错点**：`0` 和 `1` 不是素数；切片赋值长度必须与左侧完全一致；单个大数判素时建整张筛表未必合适，应考虑试除或更强判素法。

**对应例题**：Python 本地实现：[2523. Closest Prime Numbers in Range](https://leetcode.com/problems/closest-prime-numbers-in-range/)，本地筛从 `prime` 而非 `prime * prime` 开始，结论正确但重复标记更多；C++ 历史实现：[204. Count Primes](https://leetcode.com/problems/count-primes/)

### 组合计数

#### 阶乘逆元求组合数

**解决什么**：在质数模数下多次计算组合数 $\binom{n}{k}$，并用于排列计数、路径计数和容斥。

**核心原理**：预处理阶乘与逆阶乘，利用 $\binom{n}{k}=n!/(k!(n-k)!)$；质数模数下由费马小定理用快速幂求阶乘逆元。

```python
def combination_table(limit, mod):
  factorial = [1] * (limit + 1)
  for value in range(1, limit + 1):
    factorial[value] = factorial[value - 1] * value % mod
  inverse_factorial = [1] * (limit + 1)
  inverse_factorial[limit] = pow(factorial[limit], mod - 2, mod)
  for value in range(limit, 0, -1):
    inverse_factorial[value - 1] = inverse_factorial[value] * value % mod

  def choose(total, selected):
    if selected < 0 or selected > total:
      return 0
    return factorial[total] * inverse_factorial[selected] % mod * inverse_factorial[total - selected] % mod
  return choose
```

**复杂度**：预处理时间和空间均为 $O(n)$，单次查询 $O(1)$。

**易错点**：该逆元写法要求模数为质数且阶乘不为模数的倍数；`k` 越界应返回零；“至少一个”等限制常需容斥，不能只套一次组合数。

**对应例题**：Python 本地实现：[1569. Number of Ways to Reorder Array to Get Same BST](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/) 使用组合数递推；C++ 历史实现：[878. Nth Magical Number](https://leetcode.com/problems/nth-magical-number/) 使用容斥与最小公倍数，并非组合数模板。

**补充练习**：

- Python 本地实现：[29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)：倍增与二进制除法。
- C++ 历史实现：[319. Bulb Switcher](https://leetcode.com/problems/bulb-switcher/)：由因数配对推出仅完全平方数保留。

## 设计题与数据结构

### 接口摊还分析

#### 双栈队列

**解决什么**：只用后进先出的栈实现先进先出队列，并让一系列入队、出队操作保持常数均摊成本。

**核心原理**：新元素压入输入栈；只有输出栈为空时才把输入栈全部倒入。每个元素至多进入、移出两个栈各一次，因此偶尔的线性搬运可摊到整个操作序列。

```python
class AmortizedQueue:
  def __init__(self):
    self.in_stack = []
    self.out_stack = []

  def push(self, value):
    self.in_stack.append(value)

  def pop(self):
    if not self.out_stack:
      while self.in_stack:
        self.out_stack.append(self.in_stack.pop())
    return self.out_stack.pop()
```

**复杂度**：`push` 为 $O(1)$；`pop` 单次最坏 $O(n)$、均摊 $O(1)$；空间 $O(n)$。

**易错点**：输出栈非空时不能重复搬运；空队列行为要遵循接口契约；摊还 $O(1)$ 不等于每次最坏 $O(1)$。

**对应例题**：Python 本地实现：[232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)；[225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) 是反向模拟，复杂度取舍不同。

### 随机访问与删除

#### 动态数组加哈希索引

**解决什么**：平均 $O(1)$ 插入、删除和等概率随机取元素；允许重复值时仍按元素出现次数采样。

**核心原理**：动态数组负责 $O(1)$ 随机访问，哈希表把值映射到其下标集合。删除中间元素时与数组末尾交换再弹出，并同步修正两个值的索引集合。

```python
import random
from collections import defaultdict

class RandomizedCollection:
  def __init__(self):
    self.values = []
    self.indices = defaultdict(set)

  def insert(self, value):
    self.indices[value].add(len(self.values))
    self.values.append(value)

  def remove(self, value):
    if not self.indices[value]:
      return False
    remove_index = self.indices[value].pop()
    last_value = self.values[-1]
    if remove_index != len(self.values) - 1:
      self.values[remove_index] = last_value
      self.indices[last_value].remove(len(self.values) - 1)
      self.indices[last_value].add(remove_index)
    self.values.pop()
    return True

  def get_random(self):
    return random.choice(self.values)
```

**复杂度**：插入、删除、随机读取期望 $O(1)$，空间 $O(n)$。

**易错点**：删除值恰好等于末尾值时也要正确更新索引；交换数组后必须同步反向索引；空集合随机读取的行为应明确。

**对应例题**：Python 本地实现：[381. Insert Delete GetRandom O(1) - Duplicates allowed](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/)，本地源码用列表保存索引并调用 `remove`，最坏为 $O(n)$，不是上述集合版的期望 $O(1)$ 实证。

### 多容器协作

#### 堆加多栈与延迟清理

**解决什么**：在多个有容量限制的栈中，总是向最左未满栈写入、从最右非空栈弹出，并支持指定栈操作。

**核心原理**：数组保存各个栈，最小堆保存可能未满的栈下标。堆中允许暂时存在过期下标，使用前持续弹出已越界或已满项；尾部空栈则立即裁剪。

```python
import heapq

class PlateStacks:
  def __init__(self, capacity):
    self.capacity = capacity
    self.stacks = []
    self.available = []

  def push(self, value):
    while self.available and (self.available[0] >= len(self.stacks) or len(self.stacks[self.available[0]]) == self.capacity):
      heapq.heappop(self.available)
    if not self.available:
      heapq.heappush(self.available, len(self.stacks))
      self.stacks.append([])
    self.stacks[self.available[0]].append(value)

  def pop_at(self, index):
    if index >= len(self.stacks) or not self.stacks[index]:
      return -1
    heapq.heappush(self.available, index)
    return self.stacks[index].pop()
```

**复杂度**：每个有效或过期堆项至多进出一次，操作均摊 $O(\log n)$；全部栈与堆空间 $O(n)$。

**易错点**：标准完整实现还需在普通 `pop` 后裁剪右侧空栈；堆中重复下标要靠校验或额外集合控制；延迟删除的复杂度应按一系列操作分析。

**对应例题**：Python 本地实现：[1172. Dinner Plate Stacks](https://leetcode.com/problems/dinner-plate-stacks/)，本地源码使用有序列表和 `pop(0)`，单次更新最坏 $O(n)$，并非堆版实证。

### 时间版本索引

#### 哈希表加有序时间轴二分

**解决什么**：按键写入多个时间版本，并查询不晚于指定时间的最新值；也适合单调追加的历史统计。

**核心原理**：哈希表隔离不同键，每个键对应按时间递增的 `(timestamp, value)` 数组。查询使用右边界二分定位最后一个 `timestamp <= target` 的版本。

```python
from bisect import bisect_right

class TimeMap:
  def __init__(self):
    self.history = {}

  def set(self, key, value, timestamp):
    self.history.setdefault(key, []).append((timestamp, value))

  def get(self, key, timestamp):
    versions = self.history.get(key, [])
    index = bisect_right(versions, (timestamp, chr(0x10FFFF))) - 1
    return "" if index < 0 else versions[index][1]
```

**复杂度**：时间戳单调写入时 `set` 为 $O(1)$，`get` 为 $O(\log n)$，总空间 $O(n)$。

**易错点**：模板依赖同一键的时间戳递增；二分必须找不大于目标的最后一个版本；元组哨兵需覆盖值的比较范围，工程代码也可单独二分时间戳数组。

**对应例题**：Python 本地实现：[981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)、[3709. Design Exam Scores Tracker](https://leetcode.com/problems/design-exam-scores-tracker/)

**补充练习**：

- C++ 历史实现：[155. Min Stack](https://leetcode.com/problems/min-stack/)：同步维护栈内最小值。
- C++ 历史实现：[307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)：树状数组维护动态区间和。
- Python 本地实现：[622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)：固定容量循环队列。
- Python 本地实现：[3885. Design Event Manager](https://leetcode.com/problems/design-event-manager/)：字典维护优先级，`bisect + list` 更新最坏 $O(n)$。

## 矩阵与计算几何

### 坐标顺序建模

#### 边界收缩与方向遍历

**解决什么**：螺旋、对角线或按指定方向访问矩阵，并把二维位置映射为稳定的一维顺序。

**核心原理**：螺旋遍历维护上、下、左、右四条未访问边界；每完成一条边就收缩对应边界。一般方向移动则统一用 `(row_delta, column_delta)` 并在访问前检查范围。

```python
def spiral_order(matrix):
  if not matrix:
    return []
  top, bottom = 0, len(matrix) - 1
  left, right = 0, len(matrix[0]) - 1
  order = []
  while top <= bottom and left <= right:
    order.extend(matrix[top][left:right + 1])
    top += 1
    for row in range(top, bottom + 1):
      order.append(matrix[row][right])
    right -= 1
    if top <= bottom:
      order.extend(reversed(matrix[bottom][left:right + 1]))
      bottom -= 1
    if left <= right:
      for row in range(bottom, top - 1, -1):
        order.append(matrix[row][left])
      left += 1
  return order
```

**复杂度**：时间 $O(rows\cdot columns)$；除返回结果外辅助空间 $O(1)$。

**易错点**：单行或单列时反向遍历前必须再次检查边界；行列下标不要混用；原地标记不能覆盖后续仍需读取的信息。

**对应例题**：Python 本地实现：[2326. Spiral Matrix IV](https://leetcode.com/problems/spiral-matrix-iv/)；C++ 历史实现：[54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

### 矩形聚合与更新

#### 二维前缀和与二维差分

**解决什么**：静态矩形和查询，或批量对多个矩形加值后一次性还原完整矩阵。

**核心原理**：二维前缀用四块容斥回答矩形和；二维差分对矩形四角做 `+ - - +` 标记，最后沿两个维度累加恢复每个格子的增量。

```python
def build_prefix(matrix):
  rows, columns = len(matrix), len(matrix[0])
  prefix = [[0] * (columns + 1) for _ in range(rows + 1)]
  for row in range(rows):
    for column in range(columns):
      prefix[row + 1][column + 1] = (matrix[row][column] + prefix[row][column + 1]
        + prefix[row + 1][column] - prefix[row][column])
  return prefix

def rectangle_sum(prefix, top, left, bottom, right):
  return (prefix[bottom + 1][right + 1] - prefix[top][right + 1]
    - prefix[bottom + 1][left] + prefix[top][left])
```

**复杂度**：预处理时间和空间均为 $O(rows\cdot columns)$，单次矩形查询 $O(1)$；二维差分的每次更新 $O(1)$、最终恢复 $O(rows\cdot columns)$。

**易错点**：用额外首行首列统一边界；闭区间右下角查询要加一；差分数组需为撤销位置预留哨兵，四角符号不能写反。

**对应例题**：Python 本地实现：[2536. Increment Submatrices by One](https://leetcode.com/problems/increment-submatrices-by-one/)、[1895. Largest Magic Square](https://leetcode.com/problems/largest-magic-square/)；C++ 历史实现：[304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)

### 网格状态转移

#### 矩阵 DP

**解决什么**：统计全 $1$ 正方形、求网格路径最优值，或处理只依赖左、上、对角线等已计算邻居的状态。

**核心原理**：以格子 `(row, column)` 为右下角的最大全 $1$ 正方形边长，等于三个前驱状态最小值加一。遍历顺序必须保证所有依赖已经计算。

```python
def count_square_submatrices(matrix):
  rows, columns = len(matrix), len(matrix[0])
  dp = [[0] * (columns + 1) for _ in range(rows + 1)]
  answer = 0
  for row in range(1, rows + 1):
    for column in range(1, columns + 1):
      if matrix[row - 1][column - 1] == 1:
        dp[row][column] = 1 + min(dp[row - 1][column], dp[row][column - 1], dp[row - 1][column - 1])
        answer += dp[row][column]
  return answer
```

**复杂度**：时间和空间均为 $O(rows\cdot columns)$；只依赖上一行时可滚动为 $O(columns)$ 空间。

**易错点**：最大边长、最大面积和正方形总数是三个不同答案；原地 DP 会修改输入；含负数的乘积路径必须同时维护最大值和最小值。

**对应例题**：Python 本地实现：[1594. Maximum Non Negative Product in a Matrix](https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/) 使用双状态矩阵 DP；C++ 历史实现：[221. Maximal Square](https://leetcode.com/problems/maximal-square/)、[1277. Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)

### 平面方向判定

#### 叉积与有向面积

**解决什么**：判断三点方向、共线、线段相交和多边形面积，避免使用浮点斜率。

**核心原理**：向量 $AB$ 与 $AC$ 的叉积为 $(B_x-A_x)(C_y-A_y)-(B_y-A_y)(C_x-A_x)$；正负分别表示逆时针和顺时针，零表示共线，其绝对值是三角形面积的两倍。

```python
def cross(origin, first, second):
  return ((first[0] - origin[0]) * (second[1] - origin[1])
    - (first[1] - origin[1]) * (second[0] - origin[0]))

def segments_strictly_cross(a, b, c, d):
  return (cross(a, b, c) * cross(a, b, d) < 0
    and cross(c, d, a) * cross(c, d, b) < 0)
```

**复杂度**：单次方向或严格相交判定时间 $O(1)$，辅助空间 $O(1)$。

**易错点**：上面相交模板不含共线端点接触，完整线段相交还需包围盒与 `on_segment`；定宽整数要防坐标乘法溢出；不要用浮点斜率直接判等。

**对应例题**：Python 本地实现：[2280. Minimum Lines to Represent a Line Chart](https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/) 当前使用浮点斜率，并非叉积实证；C++ 历史实现：[1232. Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/)

**补充练习**：

- C++ 历史实现：[593. Valid Square](https://leetcode.com/problems/valid-square/)：平方距离判定。
- Python 本地实现：[835. Image Overlap](https://leetcode.com/problems/image-overlap/)：坐标偏移频次统计。
- Python 本地实现：[3882. Minimum XOR Path in a Grid](https://leetcode.com/problems/minimum-xor-path-in-a-grid/)：网格路径与异或状态搜索。
- Python 本地实现：[4016. Maximum Area of Two Non-Overlapping Square Submatrices](https://leetcode.com/problems/maximum-area-of-two-non-overlapping-square-submatrices/)：二维前缀和、二分边长与不相交约束。

## 推荐复习顺序

1. **复杂度与基本功**：复杂度 → 模拟 / 枚举 → 数组与哈希 → 排序。目标是能从 $n$ 判断复杂度上限，并准确分析语言容器操作成本。
2. **线性扫描**：双指针 → 滑动窗口 → 前缀和 / 差分 → 栈 / 队列。目标是能写出循环不变量，区分窗口单调性和前缀状态。
3. **有序性与区间**：二分查找 → 堆 → 区间问题 → 离线处理。目标是能识别单调判定、事件顺序与查询是否允许重排。
4. **递归与搜索**：链表 → 二叉树 → DFS / BFS → 回溯。目标是能定义递归契约、访问状态和剪枝边界。
5. **决策优化**：贪心 → 动态规划。先能证明局部选择，再系统掌握线性、背包、区间、树形、状态压缩和数位 DP。
6. **图论主干**：拓扑排序 → 最短路 → 最小生成树 → 并查集 → 二分图 / 强连通分量。目标是根据边权、方向和查询方式选算法。
7. **动态区间结构**：树状数组 → 线段树。先掌握前缀可差分信息，再学习节点合并、单位元、懒标记与值域建树。
8. **专项提高**：Trie / KMP / Z / 哈希 → 位运算 → 数学数论 → 矩阵与计算几何 → 综合设计题。

建议每章按“读核心知识点 → 独立完成 2 道典型题 → 解释复杂度与边界 → 一周后重写”的循环复习。能说明**为什么选它、何时失效、替代方案是什么**，比仅记住模板更重要。

## 使用说明

- 点击题目名称可直接打开当前仓库中的对应源码。
- 同一题存在 Python 和 C++ 两种实现时，本页通常只链接其中一种，另一种可按题号在目录中查找。
- 文件名以题号开头，使用编辑器按题号搜索是定位题解最快的方式。
- 新增题解时，可按其主要思想补充到对应分类；若一题具有多个鲜明标签，也可以在多个分类中交叉引用。
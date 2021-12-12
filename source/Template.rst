
==================================================================
Prefix Sum
==================================================================

for ``arr[]`` with length ``n``, and ``s[]`` with length ``n + 1``,

``s[i] = arr[0] + ... + arr[i - 1]``

sum of ``arr[i]`` to``arr[j]`` is ``s[j + 1] - s[i]``


==================================================================
Counting Array
==================================================================
.. list-table:: Counting Array

    * - **arr**
      - X
      - 0
      - 1
      - ...
      - i - 1
      - i
      - ...
      - j
      - ...
      - n
    * - **sum**
      - 0
      - 1
      - 2
      - ...
      - i
      - i + 1
      - ...
      - j + 1
      - ...
      - n + 1

==================================================================
All Subset
==================================================================

.. code-block:: python

   def subsets(nums: list[int]) -> list[list[int]]:
       ans = []
       stack = []

       def find(k: int) -> None:
           if k == len(nums):
               ans.append(stack.copy())
               return

           find(k + 1)

           stack.append(nums[k])
           find(k + 1)
           stack.pop()

       find(0)
       return ans

==================================================================
Set with Fixed Length
==================================================================

.. code-block:: python

   def combine(nums: list[int], k: int) -> list[list[int]]:
       ans = []
       stack = []

       def find(i: int) -> None:
           if len(stack) == k:
               ans.append(stack.copy())
               return
           if len(stack) + (len(nums) - i) < k:
               return

           find(i + 1)

           stack.append(nums[i])
           find(i + 1)
           stack.pop()

       find(0)
       return ans

==================================================================
Permutation
==================================================================

.. code-block:: python

   def permute(nums: list[int]) -> list[list[int]]:
       selected = [False] * len(nums)
       ans = []
       stack = []

       def find() -> None:
           if len(stack) == len(nums):
               ans.append(stack.copy())
               return

           for i in range(len(selected)):
               if not selected[i]:
                   selected[i] = True
                   stack.append(nums[i])
                   find()
                   stack.pop()
                   selected[i] = False
       find()
       return ans


==================================================================
Topology
==================================================================

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

.. code-block:: python

   from collections import deque

   def findOrder(numCourses: int, prerequsites: list[list[int]]) -> list[int]:
       edges = [[] for _ in range(numCourses) ]
       indegree = [0] * numCourses
       ends = deque()
       ans = []

       for a, b in prerequsites:
           edges[b].append(a)
           indegree[a] += 1

       for i in range(len(indegree)):
           if indegree[i] == 0:
               ends.append(i)

       while ends:
           first = ends.popleft()
           ans.append(first)
           for second in edges[first]:
               indegree[second] -= 1
               if indegree[second] == 0:
                   ends.append(second)

       if len(ans) == numCourses:
           return ans
       return []

==================================================================
BFS Map
==================================================================

.. code-block:: python

   from collections import deque

   def numIslands(grid: list[list[str]]) -> int:
       ans = 0
       m = len(grid)
       n = len(grid[0])
       visited = [[False] * n for _ in range(m)]
       q = deque()

       offsets = [(-1,0), (1,0), (0,-1), (0,1)]

       for i in range(m):
           for j in range(n):
               if visited[i][j] or grid[i][j] == "0":
                   continue

               #print("start from", i, j)
               q.append((i,j))
               visited[i][j] = True
               while q:
                   x, y = q.popleft()
                   #print("connecting", x, y)
                   for o_x, o_y in offsets:
                       n_x, n_y = x + o_x, y + o_y
                       if n_x < 0 or n_y < 0 or n_x >= m or n_y >= n:
                           continue
                       if grid[n_x][n_y] == "1" and not visited[n_x][n_y]:
                           q.append((n_x, n_y))
                           visited[n_x][n_y] = True
                           #print("append",n_x, n_y)

               ans += 1

       return ans

   grid = [
     ["1","1","0","0","0"],
     ["1","1","0","0","0"],
     ["0","0","1","0","0"],
     ["0","0","0","1","1"]
   ]

   print(numIslands(grid))

==================================================================
DFS Find circle in Undirected Map
==================================================================

.. code-block:: python

   def has_circle_undirected(nums: int, edges: list[list[int]]) -> list[int]:
       connections = [[] for _ in range(nums)]

       for a, b in edges:
           connections[a].append(b)
           connections[b].append(a)

       ans = []
       visited = set()
       line = set()

       def dfs(x: int, fa: int):
           visited.add(x)
           line.add(x)

           for y in connections[x]:
               if y in visited:
                   if y != fa and y in line:
                       ans.append(x)
                       ans.append(y)
                       return
               else:
                   dfs(y, x)
                   if ans:
                       return

           line.remove(x)

       for point in range(nums):
           if point in visited:
               continue
           dfs(point, None)
           if ans:
               break
       return ans

   # print(has_circle_undirected(10, [ [1,2],[2,3],[3,4],[1,5],[4,5] ] ))


   def has_circle_undirected_uf(nums: int, edges: list[list[int]]) -> list[int]:
       search = [i for i in range(nums + 1)]

       for a, b in edges:
           ori_a, ori_b = a, b

           while search[a] != a:
               search[a] = search[search[a]]
               a = search[a]

           while search[b] != b:
               search[b] = search[search[b]]
               b = search[b]

           if a == b:
               return [ori_a, ori_b]

           search[a] = b

       return []

   # print(has_circle_undirected_uf(10, [ [1,5], [2,1], [3,2], [5,4], [4, 6], [2,7] ] ))

   def has_circle_directed(nums: int, edges: list[list[int]]) -> bool:
       connections = [[] for _ in range(nums)]

       for a, b in edges:
           connections[a].append(b)

       ans = False
       visited = set()
       line = set()

       def dfs(x: int):
           nonlocal ans
           visited.add(x)
           line.add(x)

           for y in connections[x]:
               if y in visited:
                   if y in line:
                       ans = True
                       return
               else:
                   dfs(y)
                   if ans:
                       return

           line.remove(x)

       for point in range(nums):
           if point in visited:
               continue
           dfs(point)
           if ans:
               break
       return ans

==================================================================
Binary Search Tree (BST)
==================================================================


==================================================================
Binary Search
==================================================================

.. code-block:: python

   from typing import List

   # Okay
   # index of v that v is first value that larger equal than key
   # n means not found
   def bisect_left(arr: List[int], key: int) -> int:
       i = 0
       j = len(arr)
       ####
       while i < j:
           mid = i + (j - i) // 2
           if arr[mid] >= key:
               #####
               j = mid
           else:
               i = mid + 1
       #####
       return i

   #Okay
   def bisect_right(arr: List[int], key: int) -> int:
       i = 0
       j = len(arr)
       while i < j:
           mid = i + (j - i) // 2
           if arr[mid] > key:
               j = mid
           else:
               i = mid + 1

       return i

==================================================================
Merge Sort
==================================================================

.. code-block:: python

   def merge_sort(nums: list[int], left: int, right: int) -> None:
       if left == right:
           return

       mid = (left + right) // 2
       i = left
       j = mid + 1

       merge_sort(nums, left, mid)
       merge_sort(nums, mid + 1, right)

       tmp = [0] * (right - left + 1)
       k = 0
       while i <= mid and j <= right:
           if nums[i] <= nums[j]:
               tmp[k] = nums[i]
               k += 1
               i += 1
           else:
               tmp[k] = nums[j]
               k += 1
               j += 1
       while i <= mid:
           tmp[k] = nums[i]
           k += 1
           i += 1

       nums[left: left + k] = tmp[:k]

   def merge_sort_no_recursive(nums: list[int]) -> None:
       size = 1
       tmp = [0] * len(nums)

       def merge(low: int, mid: int, high: int):
           i = low
           j = mid
           k = 0
           while i < mid and j < high:
               if nums[i] <= nums[j]:
                   tmp[k] = nums[i]
                   k += 1
                   i += 1
               else:
                   tmp[k] = nums[j]
                   k += 1
                   j += 1
           while i < mid:
               tmp[k] = nums[i]
               k += 1
               i += 1
           nums[low: low + k] = tmp[:k]

       while size < len(nums):
           low = 0
           while low + size < len(nums):
               mid = low + size
               high = mid + size
               if high > len(nums):
                   high = len(nums)
               merge(low, mid, high)
               low = high
           size = size + size


==================================================================
Quick Sort
==================================================================

.. code-block:: python

   from typing import List
   from random import randint, seed

   def quick_sort(arr: List[int]) -> None:
       if not arr:
           return

       def find(start: int, end: int) -> int:
           i = start + 1
           j = end
           p = randint(i, j)
           arr[start], arr[p] = arr[p], arr[start]

           while i <= j:
               while i < end and arr[i] < arr[start]:
                   i += 1
               while start < j and arr[j] > arr[start]:
                   j -= 1
               if i < j:
                   arr[i], arr[j] = arr[j], arr[i]
                   i += 1
                   j -= 1
               else:
                   break

           arr[start], arr[j] = arr[j], arr[start]

           return j

       def sort(start: int, end: int) -> None:
           if start >= end:
               return
           mid = find(start, end)
           sort(start, mid - 1)
           sort(mid + 1, end)

       sort(0, len(arr) - 1)

   def quick_sort_inc_pivot(arr: list[int]) -> None:

       def partition(low: int, high: int) -> int:
           p_index = randint(low, high)
           p_val = arr[p_index]
   #         p_val = arr[low]
           print("rand", p_val)

           i,j = low, high
           # < ??
           while i <= j:
               while i < j and arr[i] < p_val:
                   i += 1
               while i < j and arr[j] > p_val:
                   j -= 1
               if i < j:
                   arr[i], arr[j] = arr[j], arr[i]
                   i += 1
                   j -= 1
               if i == j:
                   break
           return j

       def sort(start: int, end: int) -> None:
           print(start, end)
           if start >= end:
               return
           # 0 - pivot: less than
           # pivot + 1 - end: larger than or equal to
           pivot = partition(start, end)
           print(pivot, arr)
           sort(start, pivot)
           sort(pivot + 1, end)

       sort(0, len(arr) - 1)
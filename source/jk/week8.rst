==================================================================
W8 (Graph, String)
==================================================================

******************************************************************
Examples
******************************************************************

For shortest path, ``Dijkstra`` algorithm applies to no negative edges only.
``Bellman-Ford`` applies to negative edges, but not negative cyclic (sum(edges) < 0)


------------------------------------------------------------------------------------------------------------------------------------
`743. Network Delay Time <https://leetcode.com/problems/network-delay-time/>`_ (Medium)
------------------------------------------------------------------------------------------------------------------------------------
This is a solution with ``Dijkstra`` algorithm

.. literalinclude:: /problems/743. Network Delay Time/solution.py

This is a solution with ``Bellman-Ford`` algorithm

.. literalinclude:: /problems/743. Network Delay Time/solution2.py

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
`1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance Network Delay Time <https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/>`_ (Medium)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. literalinclude:: /problems/1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance/solution.py

******************************************************************
Homework
******************************************************************




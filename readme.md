# Task 2: Comparison of DFS and BFS Algorithms

## Overview
In this task, we implemented two pathfinding algorithms:
1.  **BFS (Breadth-First Search)** using a Queue.
2.  **DFS (Depth-First Search)** using a Stack.

The graph was designed with two possible routes from **Station A** to **Station Z**:
* A "Short" route via `Station M` (2 steps).
* A "Long" route via `Station B` (5 steps).

## Results

| Algorithm | Path Found | Length |
| :--- | :--- | :--- |
| **BFS** | `['Station A', 'Station M', 'Station Z']` | **2 steps** |
| **DFS** | `['Station A', 'Station B', 'Station C', 'Station D', 'Station E', 'Station Z']` | **5 steps** |

## Analysis of Differences

### Why BFS found the short path?
**Breadth-First Search** explores the graph layer by layer.
1.  It starts at `Station A`.
2.  It checks all immediate neighbors (`Station B` and `Station M`).
3.  In the next step, it finds that `Station M` is directly connected to the goal `Station Z`.
4.  Since BFS guarantees finding the path with the minimum number of edges in an unweighted graph, it returned the shortest route.

### Why DFS found the long path?
**Depth-First Search** explores as far as possible along each branch before backtracking.
1.  At `Station A`, the algorithm had to choose between neighbors.
2.  Due to the implementation logic (stack order), it prioritized `Station B`.
3.  It continued deeper into that branch (`B -> C -> D -> E`) until it finally reached `Station Z`.
4.  DFS does not look for the shortest path; it returns the first path it successfully completes based on its traversal order.
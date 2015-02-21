To trick our enemies we will use the ancient Chess-Knight manoeuvre.
If our robots will drive their craft along a tricky path which the enemy cannot hit.

Chess is played on a square board of eight rows (called ranks and denoted with numbers 1 to 8) and eight columns
(called files and denoted with letters a to h) of squares.

The knight moves to any of the closest squares that are not on the same rank, file, or diagonal,
thus the move forms an "L"-shape: two squares vertically and one square horizontally, or two squares horizontally
and one square vertically.

You are given the start and end squares as chess coordinates separated by a hyphen.
You should find the length of the shortest path for the knight from one point to another on the chessboard.

[!short-knight-path](short-knight-path.svg)

You can learn more about chess here on [Wikipedia](http://en.wikipedia.org/wiki/Chess).

**Input:** Squares coordinates as a string. 

**Output:** The number of moves in the shortest path the knight can take as an integer.

**Example:**

```python
knight("b1-d5") == 2, "First"
knight("a6-b8") == 1, "Second"
knight("h1-g2") == 4, "Third"
knight("h8-d7") == 3, "Fourth"
knight("a1-h8") == 6, "Fifth"
```
**How it is used:**

Let's think about chess and how we can use pathfinding and computer science to play this awesome game.
The game structure and nature of chess is related to several branches of mathematics.
Many combinatorial and topological problems connected to chess have been known for hundreds of years.

**Precondition:**

An input string satisfies regexp "[a-h][1-8]-[a-h][1-8]".
```python
start_cell != end_cell
```

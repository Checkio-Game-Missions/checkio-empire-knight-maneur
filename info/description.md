Chess is played on a square board of eight rows (called ranks and denoted with numbers 1 to 8) and eight columns
(called files and denoted with letters a to h) of squares.

The knight moves to any of the closest squares that are not on the same rank, file, or diagonal,
thus the move forms an "L"-shape: two squares vertically and one square horizontally, or two squares horizontally
and one square vertically.

You are given the start and end squares as chess coordinates separated by a hyphen.
You should find the length of the shortest path for the knight from one point to another on the chessboard.

```

   |---|---|---|---|---|---|---|---|
8  |   |   |   | ↓ ← ← ← ♘ ← ← | ♞ |
   |---|---|---|-↓-|---|---|-↑-|-↓-|
7  |   |   |   | ♞ |   |   | ↑ | ↓ |
   |---|---|---|---|---|---|-↑-|-↓-|
6  |   |   |   |   |   |   | ♘ ← ← |
   |---|---|---|---|---|---|---|---|
5  |   |   | → → ♞ |   |   | → → ♘ |
   |---|---|-↑-|---|---|---|-↑-|-↓-|
4  |   |   | ↑ |   |   | ♘ ← ↑ ← ← |
   |---|---|-↑-|---|---|-↓-|-↑-|---|
3  |   | → → ♘ |   |   | ↓ | ♘ ← ← |
   |---|-↑-|---|---|---|-↓-|---|-↑-|
2  |   | ↑ |   |   |   | → → ♞ | ↑ |
   |---|-↑-|---|---|---|---|---|-↑-|
1  |   | ♞ |   |   |   |   |   | ♞ |
   |---|---|---|---|---|---|---|---|
     a   b   c   d   e   f   g   h

b1-d5 -> 2 moves
h8-d7 -> 3 moves
h1-g2 -> 4 moves
```

You can learn more about chess here on [Wikipedia](http://en.wikipedia.org/wiki/Chess).

# water-jug-problem-ai
Water Jug Problem implemented in Python with pseudocode, explanation, and example output. Suitable for AI course projects and learning search techniques.


The Water Jug Problem is a famous example in Artificial Intelligence (AI) that demonstrates how search algorithms can be used to solve constraint satisfaction problems.
The task is to measure exactly 4 liters of water using a 3-liter jug and a 5-liter jug.

 * Problem Statement

We have two jugs:

Jug A: 4 liters capacity

Jug B: 3 liters capacity

There is no measuring scale.

The goal is to get exactly 2 liters of water in Jug A.


Pseudocode
1. Start with both jugs empty.
2. Fill Jug B (3 liters).
3. Pour water from Jug B into Jug A until Jug A is full or Jug B is empty.
4. If Jug A reaches the desired amount → Goal reached.
5. Otherwise:
   - If Jug B becomes empty, refill it.
   - If Jug A becomes full, empty it.
6. Repeat steps until solution is found.

  The Knapsack problem (also known as the bag problem) is a combinatorial optimization problem. The problem gets its name from the problem of choosing what's important to fit in a bag (with a weight limit) to take with you on a trip. Similar problems often appear in business, combinatorics, computational complexity theory, cryptography, and applied mathematics.
  
  In this report, I present the results of running the GoogleORTools tool with the Knapsack solver to evaluate the test sets on the Knapsack problem. And I will show you how I prepare the source code to run this experiment.
  
  ![k](https://user-images.githubusercontent.com/106755542/192469324-9c509738-c91d-4648-9132-fd4e27066b83.jpg)
  
  There are a total of 13 groups of test cases (00-12) for the knapsack problem. In each group, we need to select at least 5 test cases of different sizes. In this lesson, choose 50 items, 100 items, 200 items, 500 items, 1000 items and all choose the file "s005.kp". My computer is quite weak so I only run R01000.
  
  In the .kp file, line 1 is the quantity, line 2 is capacities and from line 4 to the end are values, weights.

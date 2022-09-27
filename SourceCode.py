from ortools.algorithms import pywrapknapsack_solver 
import time 
import pandas as pd
import csv
import os
from posixpath import split
import json
import glob
import os
from tqdm import tqdm
import subprocess

with open("data.csv", encoding="utf8", mode="w", newline='') as file_csv:
    header = ["Group", "Trường hợp", "Tổng giá trị", "Tổng trọng lượng", "Thời gian chạy", "Tối ưu"]
    writer = csv.writer(file_csv)
    writer.writerow(header)

TestCases = ['n00050/R01000/s005', 'n00100/R01000/s005' ,'n00200/R01000/s005', 
             'n00500/R01000/s005', 'n01000/R01000/s005']
groups = ['00Uncorrelated','01WeaklyCorrelated','02StronglyCorrelated',
              '03InverseStronglyCorrelated', '04AlmostStronglyCorrelated', '05SubsetSum', 
              '06UncorrelatedWithSimilarWeights', '07SpannerUncorrelated', 
              '08SpannerWeaklyCorrelated','09SpannerStronglyCorrelated', 
              '10MultipleStronglyCorrelated','11ProfitCeiling', '12Circle']
# Create the solver.
solver = pywrapknapsack_solver.KnapsackSolver(
    pywrapknapsack_solver.KnapsackSolver.
    KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

data = [] 
for group in groups: 
    for TestCase in TestCases: 
        path_id = group+'/'+TestCase+'.kp' 

        kp = open(path_id, 'r')
        kpfile = kp.read()
        kpfile = kpfile.split("\n")

        # print(kpfile)

        n = str(kpfile[1])
        capacities = []
        values = []
        weights = [[]]
        capacities.append(int(kpfile[2]))
        x = kpfile[4:len(kpfile)]
    
        for i in range(len(x)):
        # print(x[i])
            for j in range(len(x[i])):
                if x[i][j] == " ":
                    values.append(int(x[i][0:j]))
                    # print(x[i][0:j],' + ',s,'  ',j)
                    # print(type(x[i][0:j]))
                # if ((x[i][j] == " ") & (s == 1)):
                    weights[0].append(int(x[i][j:len(x[i])+1]))
                    # print(x[i][j:len(x[i])+1])
                    break

        solver.Init(values, weights, capacities)
        time_limit = 180.0
        solver.set_time_limit(time_limit)
        
        time_start = time.time()
        computed_value = solver.Solve()  
        time_end = time.time()
        
        packed_items = []
        packed_weights = []
        total_weight = 0
        for i in range(len(values)):
            if solver.BestSolutionContains(i):
                packed_items.append(i)
                packed_weights.append(weights[0][i])
                total_weight += weights[0][i]
                

        data.append([str(group)+'.kp', TestCase, computed_value, total_weight, (time_end-time_start), str(round((time_end-time_start<=time_limit),3))])
        outputPath = 'ketqua/' + group + '/' + TestCase +'.txt' 
        with open(outputPath,encoding="utf8",mode='w') as f: 
            f.write('Total value: ' + str(computed_value) + '\n')
            f.write('Total weight: ' + str(total_weight) + '\n') 
            f.write('>>Packed items:'+ str(packed_items) + '\n')
            f.write('>>Packed weights:'+ str(packed_weights) + '\n')
            f.write('Thời gian chạy: ' + str(time_end-time_start) + '\n') 
            f.write('Tối ưu: ' + str(time_end-time_start<=time_limit) + '\n') 

    print(group)

with open("data.csv", "a", encoding='utf-8', newline='') as file_csv:
    writer = csv.writer(file_csv)
    writer.writerows(data)



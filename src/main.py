import math

from aco import ACO, Graph
import sys


def main():
    if len(sys.argv) != 2:
        print("Wrong!")
        print("Pass number of iterations as argument!")
        return

    num_itr = int(sys.argv[1])
    cities = []
    points = []
    cost_matrix = []
    with open('./data/gr17.txt') as f:                 # importing the dataset file
        for line in f.readlines():                     # reading matrix from the dataset file and putting into cost_matrix 
            city = line.split(' ')
            row = []
            for i in city:
                row.append(float(i))
            cost_matrix.append(row)                                   

    rank = len(row)

    print('No. of cities:' ,rank)
    #print(rank)
    print("\nCost Matrix:") 
    for i in range(rank):
        print(cost_matrix[i])                         # printing the cost matrix given in the dataset

    alpha = []
    beta = []
    rho = []

    #for varying alpha
    with open('./input/alpha.txt') as f1:
        for line in f1.readlines():
            a = line.split(' ')
            for i in range(len(a)):
                alpha.append(float(a[i]))
    print(alpha)

    #for varying beta
    with open('./input/beta.txt') as f1:
        for line in f1.readlines():
            a = line.split(' ')
            for i in range(len(a)):
                beta.append(float(a[i]))
    print(beta)

    #for varying rho
    with open('./input/rho.txt') as f1:
        for line in f1.readlines():
            a = line.split(' ')
            for i in range(len(a)):
                rho.append(float(a[i]))
    print(rho)


    total_cost1 = [0.0 for j in range(len(alpha))]
    total_cost2 = [0.0 for j in range(len(beta))]
    total_cost3 = [0.0 for j in range(len(rho))]

    print('\n\nNumber of iterations: ' , num_itr)


    # for varying alpha
    print('Keeping  β=1 and ρ=0.1 and varying α\n') 
    for j in range(len(alpha)):
        aco = ACO(rank, num_itr,alpha[j],1,0.1, 10, 2)
        graph = Graph(cost_matrix, rank)
        path, cost = aco.solve(graph)
        total_cost1[j] = cost
        print('α = {} , Total Cost = {}'.format(alpha[j] ,total_cost1[j]))
        print('Path: ', path)
    print('\n')

    # for varying beta
    print('Keeping  α = 0.5 and ρ=0.1 and varying β\n') 
    for j in range(len(beta)):
        aco = ACO(rank, num_itr,0.5,beta[j],0.1,10, 2)
        graph = Graph(cost_matrix, rank)
        path, cost = aco.solve(graph)
        total_cost2[j] = cost
        print('β = {} , Total Cost = {}'.format(beta[j] ,total_cost2[j]))
        print('Path: ', path)
    print('\n')


 # β=1, ρ=0.1 and varying values of  α
    #for varying rho
    print('Keeping  α = 0.5 and β=1 and varying ρ\n') 
    for j in range(len(rho)):
        aco = ACO(rank, num_itr,0.5,1,rho[j], 10, 2)
        graph = Graph(cost_matrix, rank)
        path, cost = aco.solve(graph)
        total_cost3[j] = cost
        print('ρ= {} , Total Cost = {}'.format(rho[j] ,total_cost3[j]))
        print('Path: ', path)
    print('\n')


if __name__ == '__main__':
    main()

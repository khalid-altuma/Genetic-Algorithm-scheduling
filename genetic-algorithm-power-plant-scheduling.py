#******** Please Execute at online-python.com ********

import random

#define arrays to avoid errors
capacity = [0] * 100
intervals = [0] * 100
scheduled_capacity = [0] * 100
max_load = [0] * 4
total_capacities = 0
net_reserve = [0] * 4

# declare possible genes 
maintenance_once = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
maintenance_twice = [[1,1,0,0], [0,1,1,0], [0,0,1,1]]
maintenance_thrice = [[1,1,1,0], [0,1,1,1]]

# Get the number of units and the total installed capacity
units = int(input("How many Units? "))

# Loop through each unit
for i in range(units):
    # Get the unit capacity and number of intervals
    capacity[i], intervals[i] = map(int, input(f"Unit {i + 1} Capacity in (MW) & intervals required for maintenance? ").split())
    total_capacities += capacity[i]
    
for i in range(4):
    max_load[i] = int(input(f"Max load of Interval {i + 1} ? (MW) "))


#generate 4 individuals, which means population is 4
gene_pool1 = [[0] * 4 for _ in range(units)]
gene_pool2 = [[0] * 4 for _ in range(units)]
gene_pool3 = [[0] * 4 for _ in range(units)]
gene_pool4 = [[0] * 4 for _ in range(units)]
parent1 = [[0] * 4 for _ in range(units)]
parent2 = [[0] * 4 for _ in range(units)]
best = [[0] * 4 for _ in range(units)]

for i in range(units):
    if intervals[i] == 1:
        gene_pool1 [i] = maintenance_once[random.randrange(4)]
        gene_pool2 [i] = maintenance_once[random.randrange(4)]
        gene_pool3 [i] = maintenance_once[random.randrange(4)]
        gene_pool4 [i] = maintenance_once[random.randrange(4)]
    elif intervals[i] == 2:
        gene_pool1 [i] = maintenance_twice[random.randrange(3)]
        gene_pool2 [i] = maintenance_twice[random.randrange(3)]
        gene_pool3 [i] = maintenance_twice[random.randrange(3)]
        gene_pool4 [i] = maintenance_twice[random.randrange(3)]
    elif intervals[i] == 3:
         gene_pool1 [i] = maintenance_thrice[random.randrange(2)]
         gene_pool2 [i] = maintenance_thrice[random.randrange(2)]
         gene_pool3 [i] = maintenance_thrice[random.randrange(2)]
         gene_pool4 [i] = maintenance_thrice[random.randrange(2)]

#Print first generation 1st individual Gene Pool
print("\n Initial individual 1 = ", end="")
for i in range(units):
    for j in range(4):
        print(gene_pool1[i][j], end="")
    print(" ", end="")

#print first generation 2nd individual gene pool
print("\n Initial individual 2 = ", end="")
for i in range(units):
    for j in range(4):
        print(gene_pool2[i][j], end="")
    print(" ", end="")
    
#Print first generation 1st individual Gene Pool
print("\n Initial individual 3 = ", end="")
for i in range(units):
   
    for j in range(4):
        print(gene_pool3[i][j], end="")
    print(" ", end="")

#print first generation 2nd individual gene pool
print("\n Initial individual 4 = ", end="")
for i in range(units):
    for j in range(4):
        print(gene_pool4[i][j], end="")
    print(" ", end="")

#loop should start here 
for x in range(100):
    scheduled_capacity1 = [0] * 4
    scheduled_capacity2 = [0] * 4
    scheduled_capacity3 = [0] * 4
    scheduled_capacity4 = [0] * 4
    #calculate scheduled_capacity for each gene pool
    for i in range(units):
        for j in range(4):
            if gene_pool1[i][j] == 1:
                # If the gene is a 1, add the unit capacity to the scheduled capacity for the interval
                scheduled_capacity1[j] += capacity[i]
    for i in range(units):
        for j in range(4):
            if gene_pool2[i][j] == 1:
                # If the gene is a 1, add the unit capacity to the scheduled capacity for the interval
                scheduled_capacity2[j] += capacity[i]
    for i in range(units):
        for j in range(4):
            if gene_pool3[i][j] == 1:
                # If the gene is a 1, add the unit capacity to the scheduled capacity for the interval
                scheduled_capacity3[j] += capacity[i]
    for i in range(units):
        for j in range(4):
            if gene_pool4[i][j] == 1:
                # If the gene is a 1, add the unit capacity to the scheduled capacity for the interval
                scheduled_capacity4[j] += capacity[i]
                
    net_reserve1 = [0] * 4
    net_reserve2 = [0] * 4
    net_reserve3 = [0] * 4
    net_reserve4 = [0] * 4
    # calculate net_reserve of each individual
    for i in range(4):
        net_reserve1[i] += total_capacities - scheduled_capacity1[i] - max_load[i]
        net_reserve2[i] += total_capacities - scheduled_capacity2[i] - max_load[i]
        net_reserve3[i] += total_capacities - scheduled_capacity3[i] - max_load[i]
        net_reserve4[i] += total_capacities - scheduled_capacity4[i] - max_load[i]
        
    #calculate fitness of each individual 
    fitness1 = min(net_reserve1)
    fitness2 = min(net_reserve2)
    fitness3 = min(net_reserve3)
    fitness4 = min(net_reserve4)
    fitness_values = [[fitness1], [fitness2], [fitness3], [fitness4]]
    #decide the parent1 by choosing the maximum fitness
    if fitness1 == max(fitness_values):
        parent1 = gene_pool1
    elif fitness2 == max(fitness_values):
        parent1 = gene_pool2
    elif fitness3 == max(fitness_values):
        parent1 = gene_pool3
    else:
        parent1 = gene_pool4
    #decide parent2 by choosing the 2nd maximum fitness
    if fitness1 == sorted(fitness_values)[-2]:
        parent2 = gene_pool1
    elif fitness2 == sorted(fitness_values)[-2]:
        parent2 = gene_pool2
    elif fitness3 == sorted(fitness_values)[-2]:
        parent2 = gene_pool3
    else:
        parent2 = gene_pool4
    
    #*** Crossover and Mutation ****
    offspring1 = [[0]*4 for _ in range(units)]
    offspring2 = [[0]*4 for _ in range(units)]
    offspring3 = [[0]*4 for _ in range(units)]
    offspring4 = [[0]*4 for _ in range(units)]
    #copy parents to next generation ELITES
    offspring3 = parent1
    offspring4 = parent2
    #Crossover the first 2 genes of parents
    for j in range(2):
        for i in range(4):
            offspring1[j][i] = parent2[j][i]
            offspring2[j][i] = parent1[j][i]
    
    #fill the rest of the offsprings with their parents
    for j in range(2, units):
        for i in range(4):
            offspring1[j][i] = parent1[j][i]
            offspring2[j][i] = parent2[j][i]
    
    #Mutation
    rand_gene = random.randrange(units)
    rand_bit = 0
    
    #calculate sum of the gene to determin if its maintance is once or twice or thrice
    sumofpool1 = 0
    for i in range(4):
        sumofpool1 += offspring1[rand_gene][i]
    
    #Mutate by changing a random gene
    if sumofpool1 == 1:
        #mutation probability = 0.75
        rand_bit = random.randrange(4)
        offspring1[rand_gene] = maintenance_once[rand_bit]
    elif sumofpool1 == 2:
        #mutation probability = 0.66
        rand_bit = random.randrange(3)
        offspring1[rand_gene] = maintenance_twice[rand_bit]
    elif sumofpool1 == 3:
        #mutation probability = 0.50
        rand_bit = random.randrange(2)
        offspring1[rand_gene] = maintenance_thrice[rand_bit]
    
    #same for offspring2
    sumofpool2 = 0
    for i in range(4):
        sumofpool2 += offspring2[rand_gene][i]
    
    if sumofpool2 == 1:
        rand_bit = random.randrange(4)
        offspring2[rand_gene] = maintenance_once[rand_bit]
    elif sumofpool2 == 2:
        rand_bit = random.randrange(3)
        offspring2[rand_gene] = maintenance_twice[rand_bit]
    elif sumofpool2 == 3:
        rand_bit = random.randrange(2)
        offspring2[rand_gene] = maintenance_thrice[rand_bit]
        
    #same for offspring3
    sumofpool3 = 0
    for i in range(4):
        sumofpool3 += offspring3[rand_gene][i]
    
    if sumofpool3 == 1:
        rand_bit = random.randrange(4)
        offspring3[rand_gene] = maintenance_once[rand_bit]
    elif sumofpool3 == 2:
        rand_bit = random.randrange(3)
        offspring3[rand_gene] = maintenance_twice[rand_bit]
    elif sumofpool3 == 3:
        rand_bit = random.randrange(2)
        offspring3[rand_gene] = maintenance_thrice[rand_bit]
    
    #same for offspring4
    sumofpool4 = 0
    for i in range(4):
        sumofpool4 += offspring4[rand_gene][i]
    
    if sumofpool4 == 1:
        rand_bit = random.randrange(4)
        offspring4[rand_gene] = maintenance_once[rand_bit]
    elif sumofpool4 == 2:
        rand_bit = random.randrange(3)
        offspring4[rand_gene] = maintenance_twice[rand_bit]
    elif sumofpool4 == 3:
        rand_bit = random.randrange(2)
        offspring4[rand_gene] = maintenance_thrice[rand_bit]
    
    #make offsrings the new population but check if its fitness is legal
    if fitness1 >= 0:
        gene_pool1 = offspring1
    if fitness2 >= 0:
        gene_pool2 = offspring2
    if fitness3 >= 0:
        gene_pool3 = offspring3
    if fitness4 >= 0:
        gene_pool4 = offspring4
    #dont allow illegal 
    minfitness = min(fitness_values)
    if (minfitness[0] < 0 ) and (x == 99):
        x = x-1
#print the best offspring in the 100th generation
if fitness1 == max(fitness_values):
    best = gene_pool1
    scheduled_capacity = scheduled_capacity1
    net_reserve = net_reserve1
elif fitness2 == max(fitness_values):
    best = gene_pool2
    scheduled_capacity = scheduled_capacity2
    net_reserve = net_reserve2
elif fitness3 == max(fitness_values):
    best = gene_pool3
    scheduled_capacity = scheduled_capacity3
    net_reserve = net_reserve3
else:
    best = gene_pool4
    scheduled_capacity = scheduled_capacity4
    net_reserve = net_reserve4

print("\n\n After 100 generations, the best Result is = ", end="")
for i in range(units):
    for j in range(4):
        print(best[i][j], end="")
    print(" ", end="")

print("\n\n*******The Optimum Schedule is: *******")
# Print the table header
print("Unit | Capacity (MW) | Intervals | Gene Pool")
print("-----|---------------|-----------|----------")

# Loop through each unit and print the information
for i in range(units):
    print(f"{i + 1:4} | {capacity[i]:13} | {intervals[i]:9} | {best[i]}")

# Print the scheduled capacity for each interval
print("\n Interval | Scheduled Capacity (MW) | Net Reserve (MW)")
print("----------|-------------------------|-----------------")

for i in range(4):
    print(f"{i + 1:9} | {scheduled_capacity[i]:23} | {net_reserve[i]} ")


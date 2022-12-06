#Sudoku is a logic-based, combinal number-placement puzzle. In classic Sudoku, the objective is to fill a 9 × 9 grid 
#with digits so that each column, each row, and each of the nine 3 × 3 subgrids that compose the grid contain all of the digits from 1 to 9.

fitness = 81 # we initialize the fitness variable as the individuals number nd if fitness is 0 so there's no more duplication and the grid is complete
base  = 3 # initialization of the number of the small grid 3*3
side  = base*base # initialization of the number of all the grid 9*9

#The stochastic algorithm is a very powerful optimization tool, used to deal with difficult problems using numerical simulation techniques.
#It is used in many genetic algorithms:
#   -> Cultural genetics algorithm:
#   -> Optimization by particle test:
#This algorithm reproduces evolutionary or learning processes according to physical rules or from natural evolution.
#It relies on random processes.

#Individuals : {"1":1  , "2":2 , "3":3 , "4":4 , "5":5 , "6":6 , "7":7 ,"8":8 ,"9":9 }

# pattern for a baseline valid solution
def pattern(r,c): return (base*(r%base)+r//base+c)%side # cross over: Iterating through the values of the domain of the variable, then we compare the existants values with the no-existants values by counting the number of legal variables on the other unassigned variables then updating the domain of the variable by sorting them by those that allow the most legal moves.

#the first step is selection of individuals randomly
# randomize rows, columns and numbers (of valid base pattern)
from random import sample
def shuffle(s): return sample(s,len(s)) 
rBase = range(base)  # initial population
rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] # fill the rows
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ] # fill the columns
nums  = shuffle(range(1,base*base+1)) # mutation: it is able to replace a large portion of the population (worst performing chromosomes) with completely randomized boards, but this seems to have a minimal effect.

# produce board using randomized baseline pattern
board = [ [nums[pattern(r,c)] for c in cols] for r in rows] # final population: a grid with 81 individuals such as for each row, each column and each grid of 3*3 has no duplicates.

for c in cols: # fitness function
    for r in rows:
        fitness=fitness-1


#the display function
def expandLine(line):
    return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]
line0  = expandLine("╔═══╤═══╦═══╗")
line1  = expandLine("║ . │ . ║ . ║")
line2  = expandLine("╟───┼───╫───╢")
line3  = expandLine("╠═══╪═══╬═══╣")
line4  = expandLine("╚═══╧═══╩═══╝")

symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums   = [ [""]+[symbol[n] for n in row] for row in board ]
print(line0)
for r in range(1,side+1):
    print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
    print([line2,line3,line4][(r%side==0)+(r%base==0)]) 
    
print("____________________________________________")  
print("____________________________________________")  
print("fitness function:")
print(fitness)
print("____________________________________________")  
print("____________________________________________")  
print("Sudoku Complete")

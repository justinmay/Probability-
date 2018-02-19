#Created by Justin May 

import matplotlib.pyplot as omega #importing plotting library 
import random #importing random function

p = .6388 #last 4 digits of my RUID divided by 36, probability of heads 

print "Probability and Random Proc. Assignment 1\nJustin May RUID:170003686 \n\np=.6388 \n" #printing user data to terminal

n = int(input("please enter an 'n':")) #taking in input for n

howManyHeads = 0 #initalizing inital heads count to 0
table = [] #initalizing a python list of n probabilities 

for i in range(0,n): #will iterate the following code n times
	if(random.randint(1,101)>(p*100)): #generates a random variable between 1 and 100 and compares it with 100*p 
		table.append(float(howManyHeads) / (i+1)) #if it's greater than, then the simulated fliop is tails and divide the #heads by current # tosses
	else:
		howManyHeads += 1 #updatig howManyHeads by 1
		table.append(float(howManyHeads) / (i+1)) #if it's less than, then the simulated fliop is heads and divide the #heads by current # tosses
		
omega.plot(table,'r.',ms = 2.0) #creates a plot using data table 
omega.ylabel('Probability of Heads') #sets y axis label 
omega.xlabel('Coin Toss Number') #sets x axis label
omega.axis([0,n,0,1]) #determines axis domains and ranges
omega.show() #produces the plot 
import timeit
import matplotlib.pyplot as plt
import numpy as np


def originalfib(n):
    if n == 0 or n == 1:
        return n
    else:
        return originalfib(n-1) + originalfib(n-2)

def testslowfib():
    averageTime=[]
    testsizes=[]
    for j in range(0,35):
        testsizes.append(j)
        totalTime = timeit.timeit(lambda: originalfib(j), number = 1000)
        averageTime.append(totalTime/1000)

    slope, intercept = np.polyfit(testsizes, averageTime, 1)

    line_values = [slope * x + intercept for x in testsizes]

    # plot
    plt.scatter(testsizes, averageTime, color='blue', label='Measured Time')
    plt.plot(testsizes, line_values, color='red', linestyle='dashed', label='Linear Fit')
    plt.title("Slow Fibonacci sequence")
    plt.xlabel("Fibonacci number")
    plt.ylabel("Average Processing Time")
    plt.savefig("ex1.6.1.png")
    plt.show()

    
def fastfib(n):
    prepopulated = [0,1]
    for i in range(2,n+1) :
        prepopulated.append(prepopulated[i-1]+prepopulated[i-2])


def testfastfib():
    averageTime=[]
    testsizes=[]
    for j in range(0,35):
        testsizes.append(j)
        totalTime = timeit.timeit(lambda: fastfib(j), number = 1000)
        averageTime.append(totalTime/1000)

    slope, intercept = np.polyfit(testsizes, averageTime, 1)

    line_values = [slope * x + intercept for x in testsizes]

    # plot
    plt.scatter(testsizes, averageTime, color='blue', label='Measured Time')
    plt.plot(testsizes, line_values, color='red', linestyle='dashed', label='Linear Fit')
    plt.title("Fast Fibonacci sequence")
    plt.xlabel("Fibonacci number")
    plt.ylabel("Average Processing Time")
    plt.savefig("ex1.6.2.png")
    plt.show()



if __name__=="__main__":
    testfastfib()
    testslowfib()


#1) The code snippet is a Fibonacci sequence generator 
#2) Yes, it can be considered a divide and conquer as it simplifies each calculation by calling itself.
#3) The time complexity of recursive Fibonacci is O(n^2)
 

#5)The time complexity Fibonacci sequence using memoization is O(n)

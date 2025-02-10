import timeit
import random
import scipy
import numpy as np
from matplotlib import pyplot as plt



def linear_search(array, value):
    for i, num in enumerate(array): # create new array of value with the index
        if (num == value):
            return i                # Return index
    return -1                       # when not found

# this function is taken from lecture 9 of week 3
def binary_search(array, value):
    min = 0
    max = len(array) - 1
    while (min <= max):
        mid = (min + max) // 2 # Integer divition to ensure it is an index
        if (value < array[mid]):
            max = mid - 1
        elif (array[max] < value ):
            min = mid + 1
        else:
            return mid
    return -1                  # when not found

def log(x, a, b):
    return a * np.log(x) + b

def search_average_time(func,array,value):
    return timeit.timeit(lambda:func(array, value), number = 100) / 100

def main():
    array_sizes = [1000, 2000, 4000, 8000, 16000, 32000]
    trial_runs = 1000
    
    binary = []
    linear = []
        
    x = []

    
    for size in array_sizes:
        array = list(range(size)) # create a sorted list depending on the size given
        
        total_linear = 0
        total_binary = 0 
        
        for _ in range(trial_runs):
            target_value = random.choice(array)
            
            total_binary += search_average_time(binary_search, array, target_value)
            total_linear += search_average_time(linear_search, array, target_value)
                    
        avg_time_lin = total_linear/trial_runs
        avg_time_bin = total_binary/trial_runs
        
        binary.append(avg_time_bin)
        linear.append(avg_time_lin)
            
        x.append(size)
        
        print(f"Array size: {size}")
        print(f"The average time for 100 runs across {size} elements for linear search is: {avg_time_lin}")
        print(f"The average time for 100 runs across {size} elements for binary search is: {avg_time_bin}")
        print(" ")
        
    linearInterp = scipy.interpolate.interp1d(x=x, y=linear, kind='linear')
    binaryPopT, _ = scipy.optimize.curve_fit(f=log , xdata=x, ydata=binary)
    
    newX = [i for i in range(1000, 32001, 500)]
    
    newLinear = [linearInterp(i) for i in newX]
    
    plt.figure(figsize=(10, 5))
    plt.scatter(x, linear, label= "Linear Average Times")
    plt.plot(newX, newLinear, '--', label="Linear Fit")
    plt.legend()
    plt.xlabel('X Value')
    plt.ylabel('Average Time for Linear Search')
    plt.title('Linear Data')
    plt.show()
    plt.close()
    
    plt.figure(figsize=(10, 5))
    plt.scatter(x, binary, label= "Binary Average Times")
    plt.plot(newX, [log(i, *binaryPopT) for i in newX], '--',  label="Binary Fit")
    plt.legend()
    plt.xlabel('X Value')
    plt.ylabel('Average Time for Binary Search')
    plt.title('Binary Data')
    plt.show()
    plt.close()
    
    
        

if __name__ == "__main__":
    main()
            
            
#The interpolation of the linear search algorithm is predicted to take the form of a O(n). The data we aquired is consistent with this prediction.
#The interpolation of the linear search algorithm is predicted to take the form of a O(log(n)). The data we aquired is consistent with this prediction.
#The linear interpolation required only the sizes and the average times from our linear search algorithm
#The binary interpolation required the sizes, the average times from our binary search, and a log function
#The results are consistent with our predictions. The data points from our average search times are similar to the interpolated data.
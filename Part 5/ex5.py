import timeit
import random

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

def search_average_time(func,array,value):
    return timeit.timeit(lambda:func(array, value), number = 100) / 100

def main():
    array_sizes = [1000, 2000, 4000, 8000, 16000, 32000]
    trial_runs = 1000
    
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
        
        print(f"Array size: {size}")
        print(f"The average time for 100 runs across {size} elements for linear search is: {avg_time_lin}")
        print(f"The average time for 100 runs across {size} elements for binary search is: {avg_time_bin}")
        print(" ")

if __name__ == "__main__":
    main()
            
            

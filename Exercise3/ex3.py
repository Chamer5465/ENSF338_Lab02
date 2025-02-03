import timeit
import cProfile
import re

def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
    
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

def main():
    test_function()
    third_function()

if __name__ == '__main__':
    main()
    cProfile.run('main()')

#Question 1: A profile is a set of statistics describing how often and how long parts of a program are executed.
#Profiles provide programmers with important about length and use frequency of sections of code.

#Question 2: Profilling gives much more data than simply benchmarking. 
#Also, the statistics given by profiling can easily generated into a report using the pstats module.

#Question 3:
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    7.955    7.955 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 ex3.py:12(test_function)
#        1    0.000    0.000    7.166    7.166 ex3.py:18(third_function)
#        1    7.166    7.166    7.166    7.166 ex3.py:20(<listcomp>)
#        1    0.789    0.789    7.955    7.955 ex3.py:22(main)
#    55/10    0.000    0.000    0.000    0.000 ex3.py:5(sub_function)
#        1    0.000    0.000    7.956    7.956 {built-in method builtins.exec}
#       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#Question 4: The majority of the time is spent doing the list comprehention in the sub function.
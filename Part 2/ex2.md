1. Mention at least two aspects that make interpolation search better 
than binary search [0.1 pts]
    - Interpolation search is more efficient when handling data which is 
    uniformly distributed
    - interpolation search tends to have a faster performance time compared
    to binary search when dealing with uniformly distributed data

2. Interpolation search assumes that data is uniformly distributed.
What happens this data follows a different distribution? Will the
performance be affected? Why? [0.2 pts]
    - yes, interpolation search estimates the position of the target based
    on the value of surrounding elements. If the data is not uniformly distributed
    it may cause interpolation search to be slower as the target may be much
    further than the estimated location

3. If we wanted to modify interpolation search to follow a different
distribution, which part of the code would be affected? [0.1 pts]
    - To modify interpolation search to follow a different distribution the line
    pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))
    will have to be reflected on and changed

4. When is linear search your only option for searching data as
binary and interpolation search may fail? [0.2 pts]
    - when the data is randomly distributed, both interpolation and binary
    search need sorted data to work

5. In which case will linear search outperform both binary and
interpolation search, and why? [0.2 pts]
    - When the search target is at the beginning of the list

6. Is there a way to improve binary and interpolation search to solve
this issue? [0.2 pts]
    - Have binary and interpolation search have an implementation of linear
    search
    For binary: it can have a linear search for the first few elements before 
    starting the binary search.
    For interpolation: interpolation search can switch to a linear search if the
    estimated position is near the start of the array

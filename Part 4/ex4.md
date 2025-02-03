1. Describe the algorithm you will use to find the room. Assume all the
information you have is the one given by the sign; you have no
knowledge of the floor plan [0.5 pts]
    -   solely from the sign given, there are 2 conditions to either
    go left or right 
    to go left: the desired room is any number in range from
    100 - 130
    to go right: the desired room is every other number

2. How many ”steps” it will take to find room EY128? And what is a “step” in
this case? [0.25 pts]
    -   Lets define "steps" as 1 step = 1 room for simplicity. to get to room 28
    will be 15 "steps". Following the algorithm, 128 would signify to go left
    and it would be 15 steps from 100 to 128 

3. Is this a best-case scenario, worst-case scenario, or neither? [0.25 pts] 
    -   I would say it is a worst case scenario as it takes 15 steps when taking the 
    left path but would only take 6 steps when taking a right

4. With this particular sign and floor layout, explain what a worst-case or best-
case scenario would look like [0.5 pts]
    -   with no knowledge of the floor plan,
    best case scenarios: 
    when the desired rooms is 100 or 138 as it would only take 1 step
    to each room 
    worst case scenario: 
    when desired room is 130, using the previous described algorithm it would
    take 16 steps to reach this room

5. Suppose after a few weeks in the term you memorize the layout of the floor.
How would you improve the algorithm to make it more efficient? [0.5 pts]
    -   I would divide this floor plan into half where rooms 100-118 would
    prompt to go left and 120-138 would prompt to go right

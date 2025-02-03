# TASK 39: Write a program to create a custom iterator that iterates from 1 to 10 in 0.5 intervals.

import numpy as np # type: ignore

numbers=[num for num in np.arange(1,10.5,0.5)]

iterator=iter(numbers)

for i in iterator:
    print(i,end=' ')
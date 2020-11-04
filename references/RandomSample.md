### What is a Random Sample?

Technically, a simple random sample is a set of n objects in a population of 
N objects where all possible samples are equally likely to happen. 

*random.sample(population, k)*

#### Arguments

The random.sample() function has two arguments, and both are required.

1. The population can be any sequence such as list, set from which you want to select a **k** length number.

2. The **k** is the number of random items you want to select from the sequence.  **k** must be less than the size of the specified list.

*Note:  A random.sample() function raises a type error if you miss any of the required arguments.*


### Example

    import random
    
    aList = [20, 40, 80, 100, 120]
  
    sampled_list = random.sample(aList, 3)
    
    print(sampled_list)

*Output*

    [40, 120, 100]
    
#####[Link to Pynative.com](https://pynative.com/python-random-sample/)
#####[Statisticshowto.com](https://www.statisticshowto.com/simple-random-sample/)


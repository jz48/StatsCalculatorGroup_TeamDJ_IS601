### What is a Cochran's Sample Size Formula?
Cochran Formula is used to calculate an ideal sample size given a *desired level of precision*, and the estimated proportion of the attribute present in the population.

The *desired level of precision* is also known as the "Margin of Error".


### Cochran's Formula

![Cochran's Formula](https://www.statisticshowto.com/wp-content/uploads/2018/01/cochran-1.jpeg)

 * q = 1 - p
 * e = Margin of Error (the desired level of precision)
 * p = the estimated proportion of the population which has the attribute

The z-value is found in a Z Table

### Example Equation

You are performing a study on students at a university, and want to determine how many students workout 

We can assume half of the students serve workout, which gives us the "maximum variability".

    p = 0.5
    q = 1 - 0.5
    
We want to have 95% confidence, and at least +/- 5% (0.05) precision.

*95% Confidence Level gives a Z-Value of **1.96**.*
 
    = ((Z-Value)^2 * (p) * (q)) / (e)^2
    = ((1.96)^2) * (0.5) * (1 - 0.5)) / (0.05)^2
    = ((3.84) * (0.5) * (0.5)) / (0.0025)
    = 0.96 / 0.0025
    = 384

A random sample of **384** students in the target population would be enough to give you the confidence levels needed.


### All Functions Used in Cochran's Formula:


   * Subtraction
   * Multiplication
   * Division
   * Square
 



[Link to Statisticshowto.com](https://www.statisticshowto.com/probability-and-statistics/find-sample-size/#Cochran)

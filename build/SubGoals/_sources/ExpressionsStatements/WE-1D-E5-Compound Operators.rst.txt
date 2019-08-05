WE-1D-E5-Compound Operators
===========================
**Assume the following given declarations:**

.. code-block:: cpp

    int alpha = 2, beta = 1, delta = 3, eta, gamma;
    double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho; 


Evaluate these statements. If invalid, give the reason. If valid, what value is assigned to the variable? Note any possible side effects.

::
    
    gamma = 5;
    gamma += delta / alpha + beta % alpha; 



.. topic:: SG1: Determine whether data type of expression is compatible with data type of variable

    gamma += delta / alpha + beta % alpha;
    Is the identifier on the lefthand side of the assignment statement a variable? What data type is it?
    gamma is declared as an int
    Look at the righthand side of the assignment statement and determine the resultant data type.
    delta / alpha + beta % alpha contains only int s so the result is an int 
    Can the data type of the righthand side be assigned to the data type on the lefthand side?
    Yes, an int can be assigned to an int.

.. topic:: SG2: Update variables for any pre-increment or pre-decrement operators (side effects)
    
    NOT USED IN THIS EXAMPLE
 
.. topic:: SG3: Solve arithmetic equation

    gamma += delta / alpha + beta % alpha;
    Replacing the variables with their values, you get:
    gamma += 3 / 2 + 1 % 2;
    Based on order of operations, the division and modulus are evaluated first:
    gamma += 3 / 2 + 1 % 2 = (3 / 2) + (1 % 2) = 1 + 1 = 2
    The compound addition operator (+=)can be re-written as: 
    gamma = gamma + 2 = 5 + 2 = 7; 

.. topic:: SG4: Check data type of copied value against data type of variable
    
    Yes, 7 can be assigned to an int variable.
 
.. topic::SG5: Update variable for post based on side effect
    
    NOT USED IN THIS EXAMPLE
 
    Answer:  Valid, 7 assigned to variable gamma.
 
 

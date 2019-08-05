W2-2-E7-Prefix Operators
========================


**Assume the following given declarations:**

.. code-block:: cpp

    int alpha = 2, beta = 1, delta = 3, eta, gamma;
    double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho; 


Evaluate this statement. If invalid, give the reason. If valid, what value is assigned to the variable?   Note any possible side effects.

.. code-block:: cpp

    eta = delta / beta + delta % ++alpha;

.. topic::SG1: Determine whether data type of expression is compatible with data type of variable
    
    eta = delta / beta + delta % ++alpha;
    
    Is the identifier on the lefthand side of the assignment statement a variable? What data type is it?
    
    eta is declared as an int
    
    Look at the righthand side of the assignment statement and determine the resultant data type.
    
    
    delta / beta + delta % ++alpha contains only ints so the result is an int 

    Can the data type of the righthand side be assigned to the data type on the lefthand side?

    Yes, an int can be assigned to an int.
 
.. topic:: SG2: Update variables for any pre-increment or pre-decrement operators (side effects)

    alpha has a value of 2, with pre-increment operator, the value becomes 3
 
.. topic:: SG3: Solve arithmetic equation

    eta = delta / beta + delta % ++alpha;

    Replacing the variables with their values, you get:
    eta = 3 / 1 + 3 % 3 = (3/1) + (3%3) = 3 + 0 = 3
    Remember than an int divided by an int is always an int (1 goes into 3 3 times).

.. topic:: SG4: Check data type of copied value against data type of variable

    Yes, 4 can be assigned to an int variable.
 
.. topic:: SG5: Update variable for post based on side effect
    
    NOT USED IN THIS EXAMPLE
 
    Answer:  Valid, 3 assigned to variable eta. alpha now has a value of 3.


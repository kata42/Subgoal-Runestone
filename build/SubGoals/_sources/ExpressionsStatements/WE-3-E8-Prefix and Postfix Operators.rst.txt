WE3: E8 Prefix and Postfix Operators
====================================

**Assume the following given declarations:**

.. code-block:: cpp

    int alpha = 2, beta = 1, delta = 3, eta, gamma;
    double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho; 



Evaluate this statement. If invalid, give the reason. If valid, what value is assigned to the variable?  Note any possible side effects.
    
.. code-block::cpp

    lambda = ++beta / delta-- * alpha;

.. topic:: SG1: Determine whether data type of expression is compatible with data type of variable

    lambda = ++beta / delta-- * alpha;
    Is the identifier on the lefthand side of the assignment statement a variable? What data type is it?
    lambda is declared as a double 
    Look at the righthand side of the assignment statement and determine the resultant data type.
    ++beta / delta-- * alpha contains only int s so the result is an int 
    Can the data type of the righthand side be assigned to the data type on the lefthand side?
    Yes, an int can be assigned to a double.
    
    
.. topic:: SG2: Update variables for any pre-increment or pre-decrement operators (side effects)
    
    beta has a value of 1, with pre-increment operator, the value becomes 2
 
.. topic:: SG3: Solve arithmetic equation

    lambda = ++beta / delta-- * alpha;
    Replacing the variables with their values, you get:
    lambda = 2 / 3-- * 2 = (2 / 3-- ) * 2 = 0 * 2 = 0
    Remember than an int divided by an int is always an int (3 goes into 2 0 times).
    SG4: Check data type of copied value against data type of variable
    Yes, 0 can be assigned to a double variable, it becomes 0.0.
 
.. topic:: SG5: Update variables for any post-increment or post-decrement operators (side effects)

    delta has a value of 3, with post-increment operator, the value becomes 2
 
    Answer:  Valid, 0.0 assigned to variable lambda. beta has a value of 2, and delta has a value of 2

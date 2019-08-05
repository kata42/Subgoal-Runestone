WE-1E-E6-Method Calls
=====================

**Assume the following given declarations:**

.. code-block:: cpp

    int alpha = 2, beta = 1, delta = 3, eta, gamma;
    double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho; 

Evaluate these statements. If invalid, give the reason. If valid, what value is assigned to the variable? Note any possible side effects.

::

    rho = beta + Math.pow(delta, alpha);



.. topic:: SG1: Determine whether data type of expression is compatible with data type of variable


    rho = beta + Math.pow(delta, alpha);
    
    Is the identifier on the lefthand side of the assignment statement a variable? What data type is it?
    rho is declared as a double
    
    Look at the righthand side of the assignment statement and determine the resultant data type.
    beta + Math.pow(delta, alpha) contains only int s, but we must also check the API (application programming interface) of the Math.pow method: 
    
    static double	pow(double a, double b)
    
    It returns a double, so the expression would be a double.
    
    Can the data type of the righthand side be assigned to the data type on the lefthand side?
    
    Yes, a double can be assigned to a double.

.. topic:: SG2: Update variables for any pre-increment or pre-decrement operators (side effects)
    
    NOT USED IN THIS EXAMPLE

.. topic:: SG3: Solve arithmetic equation

    rho = beta + Math.pow(delta, alpha);
    Replacing the variables with their values, you get:
    rho = 1 + Math.pow(3, 2);
    Based on order of operations, the method call is evaluated first. According to the API:
    Returns the value of the first argument raised to the power of the second argument.
    rho = 1 + Math.pow(3, 2) = 1 + 9.0 = 10.0;
    (Three squared is 9).

.. topic:: SG4: Check data type of copied value against data type of variable
    
    Yes, 10.0 can be assigned to a double variable.

.. topic:: SG5: Update variable for post based on side effect
    
    NOT USED IN THIS EXAMPLE

    Answer:  Valid, 10.0 assigned to variable rho.

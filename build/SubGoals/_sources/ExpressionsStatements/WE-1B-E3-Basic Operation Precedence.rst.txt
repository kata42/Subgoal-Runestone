WE1B: E3 Basic Operation Precedence
===================================


**Assume the following given declarations:**

.. code-block:: cpp

    int alpha = 2, beta = 1, delta = 3, eta, gamma;
    double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho; 

Evaluate this statement. If invalid, give the reason. If valid, what value is assigned to the variable? Note any possible side effects.

::
  
  lambda = alpha / kappa + delta ;
  
 
.. topic:: SG1:

   **Given**
     
        .. code-block:: cpp
      
            int alpha = 2, delta = 3;
            double kappa = 3.0, lambda; 
            lambda = alpha / kappa + delta ;


   Determine whether data type of expression is compatible with data type of variable
    
    ::
      
      lambda = alpha / kappa + delta;
      
   **Is the identifier on the lefthand side of the assignment statement a variable? What data type is it?**
    
    .. reveal:: we1bans1
       :showtitle: Show answer
         
         lambda is declared as a double
    
   **Look at the righthand side of the assignment statement and determine the resultant data type.**
      
    .. reveal:: we1bans2
       :showtitle: Show answer
    
          alpha / kappa + delta is evaluated as: (int / double) + int which is: double + int which is a double
    
   **Can the data type of the righthand side be assigned to the data type on the lefthand side?**
      
    .. reveal:: we1bans3
       :showtitle: Show answer
    
         Yes, a double can be assigned to a double.
 
.. topic:: SG2: Update variables for any pre-increment or pre-decrement operators (side effects)
    
    NOT USED IN THIS EXAMPLE
    
    

.. topic:: SG3: Solve arithmetic equation

   **Given**
     
        .. code-block:: cpp
      
            int alpha = 2, delta = 3;
            double kappa = 3.0, lambda; 
            lambda = alpha / kappa + delta ; 
   

   - lambda = alpha / kappa + delta;
    
     Replacing the variables with their values, you get:
      
     lambda = 2 / 3.0 + 3 = (2/3.0) + 3 = 0.66667 + 3 = 3.66667
 
.. topic:: SG4: Check data type of copied value against data type of variable

   **Given**
     
        .. code-block:: cpp
      
            int alpha = 2, delta = 3;
            double kappa = 3.0, lambda; 
            lambda = alpha / kappa + delta ; 
      
    .. reveal:: we1bans4
       :showtitle: Show answer

        Yes, 3.66667 can be assigned to a double variable.
 
.. topic:: SG5: Update variable for post based on side effect

        .. code-block:: cpp
      
            int alpha = 2, delta = 3;
            double kappa = 3.0, lambda; 
            lambda = alpha / kappa + delta ; 

      
    .. reveal:: we1bans5
       :showtitle: Show answer
 
       Answer:  Valid, 3.66667 assigned to variable lambda.

 

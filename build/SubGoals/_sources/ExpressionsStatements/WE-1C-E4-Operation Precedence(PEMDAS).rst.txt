WE1C: E4 Operation Precedence (PEMDAS)
======================================

Assume the following given declarations:

.. code-block:: cpp

    int alpha = 2, beta = 1, delta = 3, eta, gamma;
    double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho; 
    

Evaluate this statement. If invalid, give the reason. If valid, what value is assigned to the variable? Note any possible side effects.

::
  
  gamma = delta / (alpha + beta) % alpha;


.. topic:: SG1

    **Given**

        ::
    
            int alpha = 2, beta = 1, delta = 3, gamma;

            gamma = delta / (alpha + beta) % alpha;



   **Determine whether data type of expression is compatible with data type of variable**

        .. reveal:: we1cans1
           :showtitle: Show answer
       
            gamma = delta / (alpha + beta) % alpha;

   **Is the identifier on the lefthand side of the assignment statement a variable? What data type is it?**
    
        .. reveal:: we1cans2
           :showtitle: Show answer
        
            gamma is declared as an int
        
   **Look at the righthand side of the assignment statement and determine the resultant data type.**
        
        .. reveal:: we1cans3
           :showtitle: Show answer    
        
            delta / (alpha + beta) % alpha contains only int s so the result is an int 
            Remember, an int divided by an int is always an int.
    
   **Can the data type of the righthand side be assigned to the data type on the lefthand side?**
    
        .. reveal:: we1cans4
           :showtitle: Show answer
        
            Yes, an int can be assigned to an int.
        
.. topic:: SG2: Update variables for any pre-increment or pre-decrement operators (side effects)

    NOT USED IN THIS EXAMPLE
 
.. topic:: SG3: Solve arithmetic equation
    
    ::
      
      gamma = delta / (alpha + beta) % alpha;
      
    **Given**
    
    ::
        
        int alpha = 2, beta = 1, delta = 3, gamma;

        gamma = delta / (alpha + beta) % alpha;

      
    - Replacing the variables with their values, you get:
      gamma = 3 / (2 + 1) % 2;
      Based on order of operations, the parentheses are evaluated first:
    - gamma = 3 / (3) % 2;
      Because division (/) and modulus (%) have the same precedence, they are evaluated left to right:
    - gamma = (3 / 3) % 2 = 1 % 2 = 1;
      Reminder:  % gives you the remainder (how much remains after you divide 1 by 2?).


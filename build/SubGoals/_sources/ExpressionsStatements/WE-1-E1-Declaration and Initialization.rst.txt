Worked Example1:(declaration and initialization)
================================================



.. topic:: Subgoals


   E1 - Evaluate an assignment statement
   
   1.Determine whether data type of expression is compatible with data type of variable
        
   2.Update variable for pre based on side effect
        
   3.Solve arithmetic equation
        
   4.Check data type of copied value against data type of variable
        
   5.Update variable for post based on side effect



Evaluate these statements. If invalid, give the reason. If valid, what are the values of the variables? 

::
    
  int alpha, beta = 1, gamma;
  double omega = 2.5, theta, lambda; 
  alpha = 42;
  theta = 4;
  gamma = 0.0;

.. topic:: SG1: Determine whether data type of expression is compatible with data type of variable

   - First let’s look at the declarations:
     ::
       
       int alpha, beta = 1, gamma;
       double omega = 2.5, theta, lambda; 
     

   - alpha, beta, and gamma are all declared as integers. beta is assigned the value of 1, which is an integer and legal.
     omega, theta, and lambda are declared as doubles (decimal numbers). omega is assigned the value of 2.5, which is a double and legal.
  
   - Now let’s evaluate each of the next statements:
     alpha = 42;
     alpha is assigned the value of 42, which is an integer and legal.
     theta = 4;
     theta is assigned the value of 4, which is an integer. However, by adding a “.0” to it (so it becomes 4.0) it is now a decimal and a legal assignment. This process of the computer adding the “.0” to an integer to convert it into a decimal is known as promotion, and is done automatically.
  
   - gamma = 0.0;
     gamma is assigned the value of 0.0, which is a double. A double cannot be assigned to an integer variable and there is no automatic process to convert it. This results in a compilation error (incompatible types).
 
   - What about lambda? What is it’s value?  Because there is no assignment to the variable, its contents is considered “unknown”. There are       some compilers that will do automatic initialization of variables (and a double is initialized to 0.0), but you can’t always count on it,     so it’s best to consider it “unknown” or “garbage” and not to use that variable until you assign a value to it.
    
    
 .. reveal:: ans
            :showtitle: Show answer
           
         

             Answer:  
             alpha is 42, beta = 1, omega is 2.5, theta is 4.0, lambda is unknown;
             gamma results in a compilation error
   

.. topic:: SG2: Update variables for any pre-increment or pre-decrement operators (side effects)

  NOT USED IN THIS EXAMPLE
  

.. topic:: SG3: Solve arithmetic equation

  NOT USED IN THIS EXAMPLE
  

.. topic:: SG4: Check data type of copied value against data type of variable
  
  See the above discussion.
  

.. topic:: SG5: Update variable for post based on side effect

  NOT USED IN THIS EXAMPLE


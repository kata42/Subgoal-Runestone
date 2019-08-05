
PP1A-C-E2-PP3 
--------------


.. topic:: SubGoals


    E1 - Evaluate an assignment statement

    1.	Determine whether data type of expression is compatible with data type of variable
    2.	Update variable for pre based on side effect
    3.	Solve arithmetic equation
    4.	Check data type of copied value against data type of variable
    5.	Update variable for post based on side effect

-----------------------------------------------

.. topic:: PP1A-C-E2-PP3


   Assume the following given declarations:

.. code-block:: cpp

   int alpha = 2, beta = 1, delta = 3, eta, gamma;
   double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho;
   
      
**Question a** 
  
  Use same variable on lhs and rhs
      

   
.. code-block:: cpp
         
    beta = beta * alpha;
        
        
.. shortanswer:: short-PP1A-C-E2-PP3-a
            
    answer here

          
     
----------------------------------------------------------------------------------------------------------------


.. activecode:: assignactivecode-PP1A-C-E2-PP3-a
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }
       



---------------------------------------------------------------------------------------------------------------------

.. topic:: PP1A-C-E2-PP3

   Assume the following given declarations:

.. code-block:: cpp

   int alpha = 2, beta = 1, delta = 3, eta, gamma;
   double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho;

**Question b** 

  Use same variable on lhs and rhs
      

.. code-block:: cpp

    alpha = beta + delta;
        
        
.. shortanswer:: short-PP1A-C-E2-PP3-b
            
    answer here

          
     
----------------------------------------------------------------------------------------------------------------


.. activecode:: assignactivecode-PP1A-C-E2-PP3-b
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }
       

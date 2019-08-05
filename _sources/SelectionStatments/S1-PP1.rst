S1-PP1
::::::

Subgoals for assignment statements:

1.	Determine whether data type of expression is compatible with data type of variable
2.	Update variable for pre based on side effect
3.	Solve arithmetic equation
4.	Check data type of copied value against data type of variable
5.	Update variable for post based on side effect



**Given** 

.. code-block:: cpp

    int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;
    double omega = 2.5, theta = -1.3, kappa = 3.0, rho = 0; 
    


1. Evaluate this statements and determine the value of all variables used. 


.. code-block:: cpp

    if (theta > omega)
       rho = kappa + 2;

.. shortanswer:: short-S1-PP1-1
            
    answer here

.. activecode:: assignactivecode-S1-PP1-1
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }
    

2. Evaluate this statements and determine the value of all variables used. 


.. code-block:: cpp

   if (beta < alpha)
	  eta = 42;

.. shortanswer:: short-S1-PP1-2
            
    answer here

.. activecode:: assignactivecode-S1-PP1-2
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }

3. Evaluate this statements and determine the value of all variables used. 


.. code-block:: cpp

   if (kappa < delta)
      eta = 42;
      beta = 22;
    
.. shortanswer:: short-S1-PP1-3
            
    answer here

.. activecode:: assignactivecode-S1-PP1-3
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }


4. Evaluate this statements and determine the value of all variables used. 


.. code-block:: cpp

    if (gamma < kappa)
     { 
	   beta = 22;    
     }
       eta = 42;

.. shortanswer:: short-S1-PP1-4
            
    answer here

.. activecode:: assignactivecode-S1-PP1-4
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }

WE1 S1 If Only
::::::::::::::

.. topic:: Subgoal Labels for Selection

    1. Diagram which statements go together
    2. For if statement, determine whether expression is true or false
    3. If true – follow true branch, if false –follow else branch or do nothing if no else branch





Assume the following given declarations:

.. code-block:: cpp

    int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;
    double omega = 2.5, theta = -1.3, kappa = 3.0, lambda = 0.0, rho = 0; 
    
    
Evaluate these statements and determine the value of all variables used. 
    
    
.. code-block:: cpp

    if (kappa > omega)
        rho = kappa + 2;


.. topic:: SG1: Diagram which statements go together

    If no { } are present, then by default all if and else branches have only a single statement:
    
   .. figure:: Figures/Slide7.png



.. topic:: SG2: For if statement, determine whether true or false


    **Given**
    
    .. code-block:: cpp
    
        int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;
        double omega = 2.5, theta = -1.3, kappa = 3.0, lambda = 0.0, rho = 0; 

    First we evaluate (kappa > omega):
    
    (3.0 > 2.5)   TRUE
 
.. topic:: SG3: If true – follow true branch, if false – do nothing or follow else branch

    **Given**
    

    .. code-block:: cpp
       
       int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;
       double omega = 2.5, theta = -1.3, kappa = 3.0, lambda = 0.0, rho = 0; 
    
    .. figure:: Figures/Slide8.png

    The condition is TRUE  so we execute the true branch:
    
    ::
        
        rho = kappa + 2 = 3.0 + 2 = 5.0
 
 
    **Answer:**  
    omega = 2.5, kappa = 3.0, rho = 5.0;

WE 1A S2 If/Else
::::::::::::::::

**Assume the declarations:**


.. code-block:: cpp

    int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;
    double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho; 
    
Evaluate these statements and determine the value of all variables used. 

.. code-block:: cpp

    if (alpha > delta)
        eta = alpha + 2;
    else
        gamma = alpha + 5;


.. topic:: SG1: Diagram which statements go together

    **Given**

    .. code-block:: cpp

        int alpha = 2, delta = 3, eta = 0, gamma = 0;


    If no { } are present, then by default all if and else branches have only a single statement

    .. figure:: Figures/Slide11.png
    

.. topic:: SG2: For if statement, determine whether true or false

    **Given**
    
    ::
    
        int alpha = 2, delta = 3, eta = 0, gamma = 0;

    First we evaluate (alpha > delta):
    (2 > 3)   FALSE

    .. figure:: Figures/Slide12.png

.. topic:: SG3: If true – follow true branch, if false – do nothing or follow else branch

    **Given**
    
    ::
    
        int alpha = 2, delta = 3, eta = 0, gamma = 0;


 

    .. figure:: Figures/Slide13.png
            
    The condition is FALSE  so we execute the else branch:
    gamma = alpha + 5 = 2 + 5 = 7 
    
    ::
      
      Answer:  
      
        alpha = 2, beta = 1, delta = 3, 
        
        eta = 0, gamma = 7



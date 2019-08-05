WE 1B S3 Sequential Ifs
:::::::::::::::::::::::

**Assume the following declarations**

.. code-block:: cpp

    int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;
    double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho; 


Evaluate these statements and determine the value of all variables used. 

.. code-block:: cpp

    if (alpha > beta)
        eta = alpha + 2;
    if (alpha > delta)
        gamma = alpha + 5;



.. topic:: SG1: Diagram which statements go together

    **Given**

    ::
    
        int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;


    If no { } are present, then by default all if and else branches have only a single statement

    .. figure:: Figures/Slide16.png


.. topic:: SG2: For if statement, determine whether true or false

    .. code-block:: cpp
        
        int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;


    First we evaluate (alpha > beta):
    
    (2 > 1)   TRUE



.. topic:: SG3: If true – follow true branch, if false – do nothing or follow else branch

    The condition is TRUE  so we execute the true branch:
    
    eta = alpha + 2 = 2 + 2 = 4


    .. figure:: Figures/Slide17.png
            
-----------------------------------------------------------------------------------------------

Next sequential statement is another selection statement so we will repeat:

.. topic:: SG1: Diagram which statements go together

    If no { } are present, then by default all if and else branches have only a single statement

    **Given**
    
    .. code-block:: cpp
    
        int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;

    .. figure:: Figures/Slide18.png


.. topic:: SG2: For if statement, determine whether true or false


    **Given**
    .. code-block:: cpp
    
        int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;


    First we evaluate (alpha > delta):
    (2 > 3)   FALSE


.. topic:: SG3: If true – follow true branch, if false – do nothing or follow else branch
    
    **Given**
    
    .. code-block:: cpp
    
       int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;
       
       
    The condition is FALSE so we do nothing (no else branch).


    .. figure:: Figures/Slide19.png
    
            
    ::
    
        Answer:  
        alpha = 2, beta = 1, delta = 3, 
        eta = 4, gamma = 0







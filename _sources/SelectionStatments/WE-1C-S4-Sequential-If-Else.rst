WE 1C S4 Sequential If/Else
:::::::::::::::::::::::::::


int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;
Evaluate these statements and determine the value of all variables used. 
if (alpha > beta)
{
eta = alpha + 2;
gamma = alpha + 5;
}
else
{
eta = alpha – 1;
gamma = beta - 1;
}
if (alpha > delta)
gamma = alpha + 5;
else
gamma = beta + 5;
eta = beta + 2;

SG1: Diagram which statements go together:

**Given**

.. code-block:: cpp


    int alpha = 2, beta = 1,        delta = 3, eta = 0, gamma = 0;


If no { } are present, then by default all if and else branches have only a single statement


.. figure:: Figures/Slide22.png

if (alpha > delta)
gamma = alpha + 5;
else
gamma = beta + 5;
eta = beta + 2;


SG2: For if statement, determine whether true or false

**Given**

int alpha = 2, beta = 1,        delta = 3, eta = 0, gamma = 0;


First we evaluate (alpha > beta):
(2 > 1)   TRUE




SG3: If true – follow true branch, if false – do nothing or follow else branch
The condition is TRUE  so we execute the true branch:
eta = alpha + 2 = 2 + 2 = 4
gamma = alpha + 5 = 2 + 5 = 7


.. figure:: Figures/Slide23.png


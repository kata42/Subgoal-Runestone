WE1B-A3-Initializer List Reverse
================================

**Lecture Overview**

* Printing arrays
* Summing up the elements of an array
* Reading data into an array
* Averaging elements of an array
* Finding the minimum and maximum of an array









.. topic:: Subgoal Labels For Arrays 

    1. Set up array from 0 to size-1
    2. Evaluate data type of statements against array
    3. Trace statements, updating slots as you go


Evaluate these statements and determine the value of all variables used.

If any error occurs, give the reason. 

.. code-block:: cpp

   int [] beta = {2, 4, 6, 8, 10};
   for (int i = 4; i > 0; i--)
   beta[i] = beta[i-1] + 5;
   
   
-------------------------------------------------------------------------------------------------------------------    
   
.. topic:: SG1

   Set up array from 0 to size-1
   
   ::
      
      int [] beta = {2, 4, 6, 8, 10};
     
   beta is declared as an array of ints AND is initialized (instantiated) with the values given. 
   Notice that no keyword new is needed, and no size is given as the computer can count the number of values.
   This statement allocates 5 slots for integers (first line are values, second line are indexes):

   Notice that the largest index is 4 (size of 5 minus 1).
   
   .. figure:: Figures/WE1B-1.png
   
------------------------------------------------------------------------------------------------------------------- 

.. topic:: SG2

   Evaluate data type of statements against array
   
   ::
     
     for (int i = 4; i > 0; i--)
     beta[i] = beta[i-1] + 5;
   
   This loop has index i go from 4 to 1 (>0) by decrements of 1. 
   Then the value beta[i-1] is placed into the position beta[i].  
   So for every iteration of the loop:

   .. figure:: Figures/WE1B-2.png
   
   
   
-------------------------------------------------------------------------------------------

.. topic:: SG3


   Trace statements, updating slots as you go
    
   ::
   
     for (int i = 4; i > 0; i--)
    
     beta[i] = beta[i-1] + 5;
      
   The resulting array is:
   
   .. figure:: Figures/WE1B-3.png
   
   
   
.. activecode:: assignactivecode-WE1B-A3
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }
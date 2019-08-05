WE1: A1 1D Instantiate, Alter
=============================


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








**Assume the following given declarations:**
   
.. code-block:: cpp
    
    int [] alpha;
        
          
Evaluate these statements and determine the value of all variables used.
If any error occurs, give the reason. 

   
      ::
      
         alpha = new int[5];
         alpha[4] = 22;
         alpha[0] = 10;
         alpha[1] = alpha[4] – alpha[0];
         alpha[2] = alpha[1] – alpha[0];
         alpha[3] = alpha[alpha[2] - 1];
         alpha[4] = alpha[alpha[3]];
    
        
   
---------------------------------------------------------------------------
         
    
**Assume the following given declarations:**
int [] alpha;


Evaluate these statements and determine the value of all variables used.
If any error occurs, give the reason.
          
     
   
      .. code-block:: cpp
         
         alpha = new int[5];

  
         
------------------------------------------------------------------------------------------
   

.. topic:: SG1
 
   .. figure:: Figures/Arrays1.png

      2 dimensional array.




   ``Set up array from 0 to size-1``
   
   ::
   
     alpha = new int[5];
   
   
   alpha is declared as an array of ints
   This statement allocates 5 slots for integers (first line are indexes, second line are values/content):
   Notice in the figure above that the largest index is 4 (size of 5 minus 1).



--------------------------------------------------------------------------------------------------------------------------------------



.. topic:: SG2


    Evaluate data type of statements against array

    ::
    
      alpha[4] = 22;
    
      alpha[0] = 10;
    
      alpha[1] = alpha[4] – alpha[0];
    
      alpha[2] = alpha[1] – alpha[0];
    
      alpha[3] = alpha[alpha[2] - 1];
    
      alpha[4] = alpha[alpha[3]];
    
    

   Each of these statements only involve integers. 
   Notice that for every [ ] in the statements the result will be an integer because we have an integer array.  
   All of the array indexes on the left hand side of the assignment statements are within the bounds of the array (0 – 4). We can see that some of the index values on the right hand side of the array are within bounds, but we will need to evaluate them all to see if all are valid.

    
----------------------------------------------------------------------------------------------------------------------


.. topic:: SG3


   Trace statements, updating slots as you go
   
   We will evaluate the first two statements:
   
   ::
   
      alpha[4] = 22;
      alpha[0] = 10;
     
   The resulting array is:
   
   .. figure:: Figures/Arrays2.png
   

   
   ::
     
     alpha[1] = alpha[4] – alpha[0];
     

   .. figure:: Figures/Arrays4.png
   
   
   ::
     
     alpha[2] = alpha[1] – alpha[0];
     
     
   .. figure:: Figures/Arrays5.png     
   
   
   
   ::
   
     alpha[3] = alpha[alpha[2] - 1];

   First determine the value of alpha[2] which is 2. 
   Then look at  alpha[2 - 1] which is alpha[1], or 12
   
   
   .. figure:: Figures/Arrays6.png
    
    
   ::
    
      alpha[4] = alpha[alpha[3]];
      

   First determine the value of alpha[3] which is 12. 
   Now we try to get alpha[12] which is out of bounds.

    ``IndexOutOfBounds exception occurs with this statement.``
    
   .. figure:: Figures/Arrays7.png
   
   
-------------------------------------------------------------------------

.. activecode:: assignactivecode-WE1:A11DInstantiateAlter
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }
       
   
   

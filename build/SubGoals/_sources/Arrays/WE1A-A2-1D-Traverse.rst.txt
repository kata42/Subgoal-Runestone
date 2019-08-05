WE1A-A2-1D-Traverse
===================

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



Assume the following given declarations:

::
  
  int [] alpha;
  
Evaluate these statements and determine the value of all variables used.
If any error occurs, give the reason. 

.. code-block:: cpp
  
   alpha = new int[10];
   for (int i = 0; i < 10; i++)
    alpha[i] = i * 1;
    
------------------------------------------------------------------------------------------

.. topic:: SG1


   Set up array from 0 to size-1
   ::
   
     alpha = new int[10];
     
   alpha is declared as an array of ints
   This statement allocates 10 slots for integers (first line are values, second line are indexes):
   Notice that the largest index is 9 (size of 10 minus 1).


  .. figure:: Figures/Traversal1.png   
   
-------------------------------------------------------------------------------------------------------------------


.. topic:: SG2


    Evaluate data type of statements against array
    
   :: 
     
     for (int i = 0; i < 10; i++)
     alpha[i] = i * 10;
      
   This loop has index i go from 0 to 9 (< 10) by increments of 1. 
   
 
   
   Then the value i * 10 is placed into the position alpha[i].  
   
   So for every iteration of the loop:
   All of the array indexes are within the bounds of the array (0 – 9) and all values being assigned (10-90) are valid integers and can be stored in an integer array.
    
  .. figure:: Figures/Traversal2.png
     :height: 450px
     :width: 250px
     :align: center
     :alt: traversal image2
     :scale: 55%

-------------------------------------------------------------------------------------------------------------------     


.. topic:: SG3

   Trace statements, updating slots as you go
   
   ::
     
     for (int i = 0; i < 10; i++)
     alpha[i] = i * 10;
     
   The resulting array is:
   
   .. figure:: Figures/Traversal3.png
   
------------------------------------------------------------

.. activecode:: assignactivecode-WE1A-A2-1D-Traverse
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }
       
   
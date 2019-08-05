WE2b_A8-1D-Shift
================


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



Assume that the integer array alpha has been properly declared, has a length greater than or equal to 1, and is full of data values.
Evaluate these statements and determine the values in  alpha.
If any error occurs, give the reason. 

.. code-block:: cpp
   
   int start = alpha[0]; 
   for (int i = 0; i < alpha.length - 1; i++)
   {
    alpha[i] = alpha[i+1])
   }
   alpha[length - 1] = start;
   
-------------------------------------------------------------------------------------------------------------------------------------

.. topic:: SG1

   Set up array from 0 to size-1
   alpha is an array of ints and has values, but we don’t know what those values are…

   .. figure:: Figures/size-1.png
   
   Notice that the largest index is size -1. Remember that alpha.length  will give you the array size.
   
-----------------------------------------------------------------------------------------------------------------------------------------

.. topic:: SG2

   Evaluate data type of statements against array
   
   .. code-block:: cpp
   
      int start = alpha[0];
      for (int i = 0; i < alpha.length - 1; i++)
      {
       alpha[i] = alpha[i+1])
      }
      alpha[length - 1] = start;

   All indexes into the array are valid, and all assignments are valid.
   
   The variable start is assigned the value from alpha[0].  We know this array has size >=1, so there will be an element at index 0.  This loop has index i go from 0 to size - 2 (<length) by increments of 1. In it, the value at alpha[i] is set to the value alpha [i+1]. Will i+1 ever be out of bounds of the array?  No, because the largest value of i is size-2 and adding 1 will give the value size-1, (<length).  Finally, alpha[length-1] is assigned the value stored in start, which is an integer.  The index length-1 is a valid array index for alpha.

.. topic:: SG3

   Trace statements, updating slots as you go
   
   .. code-block:: cpp
   
      int start = alpha[0];
      for (int i = 0; i < alpha.length - 1; i++)
      {
      alpha[i] = alpha[i+1])
      }
      alpha[length - 1] = start;

   What is this code doing? Let’s trace it with one sample array:
   
   **start = 12**

   
   .. figure:: Figures/WEshift-1.png
   
   .. code-block:: cpp
      
      int start = alpha[0];
      for (int i = 0; i < alpha.length - 1; i++)
      {
       alpha[i] = alpha[i+1])
       }
      alpha[length - 1] = start;


--------------------------------------------------------------------------------------------------------------------

.. activecode:: assignactivecode-WE2b_A8-1D-Shift
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }
      

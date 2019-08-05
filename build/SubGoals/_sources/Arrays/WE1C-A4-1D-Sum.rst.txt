WE1C-A4-1D-Sum
==============

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
    

Assume that the integer array alpha has been properly declared and is full of data values.

Evaluate these statements and determine the value of sum.
If any error occurs, give the reason. 

.. code-block:: cpp

   int sum = 0;
   for (int i = 0; i < alpha.length; i++)
   {
    sum += alpha[i];
   }
   
------------------------------------------------------------------------------------------------------   

.. topic:: SG1

   Set up array from 0 to size-1
   
   alpha is an array of ints and has values, but we don’t know what those values are…
   
   Notice that the largest index is size -1. Remember that alpha.length  will give you the array size.
   
   .. figure:: Figures/WE1C-1.png

-----------------------------------------------------------------------------------------------------

.. topic:: SG2

    Evaluate data type of statements against array
    
    .. code-block:: cpp
    
        for (int i = 0; i < alpha.length; i++)
        {
        sum += alpha[i];
        }
        
    This loop has index i go from 0 to size - 1 (<length) by increments of 1. Then the value at alpha[i] is added to sum.  
    All indexes into the array are valid, and all assignments are valid.


-----------------------------------------------------------------------------------------------------------

.. topic:: SG3

    Trace statements, updating slots as you go
   
   .. code-block::cpp
   
        int sum = 0;
        for (int i = 0; i < alpha.length; i++)
        {
            sum += alpha[i];
            }



   What is this code doing? Let’s trace it with one sample array:
    
    
    
   .. figure:: Figures/WE1C-2.png
    
    
    
   First, sum = 0;
    


   .. figure:: Figures/WE1C-3.png
   
   
   This code finds the sum of all the values in the array.
   
   .. reveal:: WE1c
      :showtitle: Show answer
      :modal:
      :modaltitle: Answer is

       sum contains the sum of all the values in array alpha.
       
----------------------------------------------------------------------------


.. activecode:: assignactivecode-WE1C-A4-1D-Sum
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }
       
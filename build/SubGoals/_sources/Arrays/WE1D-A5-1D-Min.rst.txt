WE1D-A5-1D-Min
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
Evaluate these statements and determine the value of min.
If any error occurs, give the reason. 

.. code-block:: cpp

    int min = alpha[0];
    for (int i = 1; i < alpha.length; i++)
    {
        if (alpha[i] < min)
       min = alpha[i];
       }
       
       
       
--------------------------------------------------------------------


.. topic:: SG1

   Set up array from 0 to size-1
   
   
   
   alpha is an array of ints and has values, but we don’t know what those values are…
   Notice that the largest index is size -1. Remember that alpha.length  will give you the array size.
   
   
   .. figure:: Figures/WE1D-1.png
   
   
-------------------------------------------------------------------------------

.. topic:: SG2



   Evaluate data type of statements against array
   int min = alpha[0];
   This statement stores the first value in alpha in an int variable min.
   alpha stores integers, and 0 is a valid index. You can assign an int to an int .
   
   .. code-block:: cpp
   
      for (int i = 1; i < alpha.length; i++)
      {
      if (alpha[i] < min)
       min = alpha[i];
       }
       
   This loop has index i go from 1 to size - 1 (<length) by increments of 1. Then the value at alpha[i] is compared to min.  If the value at alpha[i] is less than min, then alpha[i] is copied into min.
   
   All indexes into the array are valid, and all assignments are valid.
   
   
-------------------------------------------------------------------------------------------------------

.. topic:: SG3

    Trace statements, updating slots as you go
    
    .. code-block:: cpp
    
       int min = alpha[0];
       for (int i = 1; i < alpha.length; i++)
       {
       if (alpha[i] < min)
       min = alpha[i];
       }


    What is this code doing? Let’s trace it with one sample array:
    
    .. figure:: Figures/WE1D-2.png
    
    First, min = alpha[0] = 12
    We can see that each time a smaller value is located in the array, that value is stored in  min.
    
    .. figure:: Figures/WE1D-3.png
    
    
    This code finds the minimum value in the array.
    
    
    .. reveal:: WE1d-1
      :showtitle: Show answer
      :modal:
      :modaltitle: Answer is

       min contains the smallest value in array alpha.
       
-------------------------------------------------------------------------------------------------

.. activecode:: assignactivecode-WE1D-A5-1D-Min
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }
       
WE2-A6-Calculate Average
========================

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
Evaluate these statements and determine the value of avg.

If any error occurs, give the reason. 

.. code-block:: cpp

   int sum = 0;
   double avg = 0.0;
   for (int i = 0; i < alpha.length; i++)
   sum = sum + alpha[i];
   if (alpha.length != 0)
   avg = (sum * 1.0)  / alpha.length;

       
       
---------------------------------------------------------------

.. topic:: SG1
   
   Set up array from 0 to size-1
   alpha is an array of ints and has values, but we don’t know what those values are…

   Notice that the largest index is size -1. Remember that alpha.length  will give you the array size.
   
   .. figure:: Figures/size-1.png
   
   
--------------------------------------------------------------------------------------------------------------
   
.. topic:: SG2

   Evaluate data type of statements against array
   Only references to the array are in the loop and selection statements:
   
   .. code-block:: cpp
   
      for (int i = 0; i < alpha.length; i++)
      sum = sum + alpha[i];
      if (alpha.length != 0)
      avg = (sum * 1.0) / alpha.length;
      
   The loop has index i go from 0 to size - 1 (<length) by increments of 1. 
   Then the value at alpha[i] is added to sum, an int.  
   If the size of the array is not 0, then it is divided by the number of values in alpha.
   All indexes into the array are valid, and all assignments are valid.
   
---------------------------------------------------------------------------------------------------------------------
   
.. topic:: SG3

   Trace statements, updating slots as you go
   
   .. code-block:: cpp
   
      int sum = 0;
      double avg = 0.0;
      for (int i = 0; i < alpha.length; i++)
      sum = sum + alpha[i];
      if (alpha.length != 0)
      avg = (sum * 1.0) / alpha.length;
  
   What is this code doing? Let’s trace it with one sample array:
   
   
   .. figure:: Figures/WEavg-1.png
   
   First, sum and avg are both initialized to 0 values. Let’s calculate sum.


   .. figure:: Figures/WEavg-2.png

   We can see that all the values in the array are added to sum.
   Now look at the selection statement:
   
   .. code-block:: cpp
   
      if (alpha.length != 0)
      avg = (sum * 1.0) / alpha.length;
      
   Why have the selection statement? What if the array has been declared, but has no values? Then its size is 0 – and we would be dividing by 0! An exception! So we guard against this.
   As long as the array has some values, then we will calculate the average:
   
   .. code-block:: cpp
     
      avg = (sum * 1.0) / alpha.length;
      
      
   Why do we need to multiply sum by 1.0? Remember, an int divided by an int is always an int! So we need to make sure that either the divisor or dividend is a double; and one way to do this without affecting the value is to multiply it by 1.0. Another way would be to add 0.0 to the value. Still another way would be to cast the value as a double:
   
   ::
     
     avg = (double)sum / alpha.length;
     
   The average is the sum of all the elements divided by the number of elements in the array.
   
   
   .. reveal:: WEavg
      :showtitle: Show answer
      :modal:
      :modaltitle: Answer is

   
       avg contains the average of the values in the array alpha or 0 if alpha is empty.
       

------------------------------------------------------------------------------------------------------------------------

   
.. activecode:: assignactivecode-WE2-A6-Calculate Average
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }
       
       
       
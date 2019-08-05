WE2A-A7-Find  Value
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

Assume that the integer array alpha has been properly declared and is full of data values and that the variable target is an int with a value in it.
Evaluate these statements and determine the value of loc.
If any error occurs, give the reason. 

.. code-block:: cpp

    int loc = -1;
    for (int i = 0; i < alpha.length; i++)
    {
    if (alpha[i] == target)
	  loc = i;
      }

-----------------------------------------------------------------------------------------------------------------------------------------------

Assume that the integer array alpha has been properly declared and is full of data values and that the variable target is an int with a value in it.
Evaluate these statements and determine the value of loc.
If any error occurs, give the reason. 

.. code-block:: cpp

    int loc = -1;
    boolean found = false;
    for (int i = 0; i < alpha.length && !found; i++)
    {
    if (alpha[i] == target)
	{
       loc = i;  found = true;  }
       }

------------------------------------------------------------------------------------------------------------------------------------

.. topic:: SG1
   
   Set up array from 0 to size-1
   alpha is an array of ints and has values, but we don’t know what those values are…

   .. figure:: Figures/size-1.png
   
   Notice that the largest index is size -1. Remember that alpha.length  will give you the array size.
 

------------------------------------------------------------------------------------------------------------------

.. topic:: SG2

   Evaluate data type of statements against array
   
   .. code-block:: cpp
   
      for (int i = 0; i < alpha.length; i++)
       {
      if (alpha[i] == target)
       loc = i;
       } 
    
   This loop has index i go from 0 to size - 1 (<length) by increments of 1. 
   Then the value at alpha[i] is compared to target.  If the value at alpha[i] is equal to target, then the value i is copied into loc.
   All indexes into the array are valid, and all assignments are valid.
   
   
---------------------------------------------------------------------------------------------------------------------------------

.. topic:: SG3

   Trace statements, updating slots as you go
   
   .. code-block:: cpp
   
      int loc = -1;
      for (int i = 0; i < alpha.length; i++)
      {
      if (alpha[i] == target)
       loc = i;
       }
      
   What is this code doing? Let’s trace it with one sample array:
   
   .. figure:: Figures/WEfind-1.png
   
   
   Let’s assume that target = 15
   loc = -1
   
   .. figure:: Figures/WEfind-2.png
   
   
   We can see that when we find the target value in the array, we store the index (location) of where it is in the array. 
   What would happen if the target value is not in the array? Then the selection statement is never true, and loc ends up with its initial value of -1. Why is -1 a good initial value for loc? Because it isn’t a valid index value! If loc is -1 after this code, then you know the target value isn’t in the array.
   What would happen if there were 2 occurrences of the target value in the array? Yes, loc would store the index of the last occurrence.
   
   
   .. reveal:: WEfind
      :showtitle: Show answer
      :modal:
      :modaltitle: Answer is
      
       loc contains the index of the last occurrence of target  in array alpha or -1 if target is not in the array.

----------------------------------------------------------------

.. activecode:: assignactivecode-WE2A-A7-Find  Value
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }

WE2C-A9-Reverse
===============

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



.. topic:: Worked Examples – write your own


    What would the code be to "reverse" the elements of an array?


.. topic:: Reverse

   .. code-block:: cpp
   
      int [] original = {2, 4, 6, 8, 10};
      int [] copy = new int [original.length];
      int place = 0;
      for (int i = original.length-1; i >= 0; i++)
	  copy[place++] = original[i];
      
      for(int i=0; i<array.length/2; i++)
      {   int temp = array[i]; 
          array[i] = array[array.length -i -1]; 
          array[array.length -i -1] = temp; 
      }
      
-------------------------------------------------------------------------------------------------
     
.. topic:: Reverese

   .. shortanswer:: WEReverse
      
      Give the answer here
      
      
--------------------------------------------------------------------------------------------------------

.. activecode:: assignactivecode-WE2C-A9-Reverse
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }
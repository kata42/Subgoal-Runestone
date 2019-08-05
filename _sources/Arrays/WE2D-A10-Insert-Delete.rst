WE2D-A10-Insert-Delete.rst
==========================

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

    How about inserting an element into an array?

    How about deleting an element from an array?

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
      
------------------------------------------------------------------------------------------------------------

.. topic:: Insert, position given


   .. code-block:: cpp
      
      int [] original = {2, 4, 6, 8, 0, 0, 0};
      int value = 5, position = 2;

      for (int i = position; i < original.length-1; i++)
      {
	   original[i+1] = original[i];	
      }
      original[position] = value;
      
------------------------------------------------------------------------------------------------------------      

.. topic:: Insert, find position

   .. code-block:: cpp
   
       int [] original = {2, 4, 6, 8, 0, 0, 0};
       int insert = 5;
       boolean found = false;
       for (int i = 0; i < original.length && !found ; i++)
       {
	     if (original[i] > insert)
	     found = false;	
       }
     
       if (found)
       {
       }
     
     
------------------------------------------------------------------------------------------------------------     
     
.. topic:: Delete, position given

   .. shortanswer:: WEdelete-posistion
      
      Give the answer here


------------------------------------------------------------------------------------------------------------


.. topic:: Delete, find first

   
   .. shortanswer:: WEdelete-find
      
      Give the answer here

-------------------------------------------------------------------------------------------------------

.. activecode:: assignactivecode-WE1: WE2D-A10-Insert-Delete.rst
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }
       



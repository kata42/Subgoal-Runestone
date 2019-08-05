A2-PP1
======

.. topic:: Subgoals for Evaluating Array statements:

    1.	Set up array from 0 to size-1
    2.	Evaluate data type of statements against array
    3.	Trace statements, updating slots as you go



Assume the following given declarations:

.. code-block:: cpp

    int [] alpha;


Evaluate these statements and determine the value of all variables used.

.. code-block:: cpp

    alpha = new int[10];
    for (int i = 0; i < 10; i++)
    alpha[i] = i * i;

.. shortanswer:: short-A1-PP1-a
            
    answer here
    
.. activecode:: assignactivecode-A1-PP2-a
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }

----------------------------------------------------------------------------------------------------------------

.. code-block:: cpp

    alpha = new int[10];
    alpha[0] = 50;
    for (int i = 1; i < 10; i++)
    alpha[i] = alpha[i-1];

.. shortanswer:: short-A1-PP1-b
            
    answer here
    

.. activecode:: assignactivecode-A1-PP2-b
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }

----------------------------------------------------------------------------------------------------------------
    
.. code-block:: cpp

    alpha = new int[10];
    alpha[0] = 50;
    for (int i = 1; i < 10; i++)
    alpha[i] = alpha[i-1] - 5;
    
.. shortanswer:: short-A1-PP1-c
            
    answer here


.. activecode:: assignactivecode-A1-PP2-c
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }
    
----------------------------------------------------------------------------------------------------------------


.. code-block:: cpp

    alpha = new int[5];
    for (int i = 0; i <= 5; i++)
    alpha[i] = i + 1;

    
.. shortanswer:: short-A1-PP1-d
            
    answer here
    
.. activecode:: assignactivecode-A1-PP2-d
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }

          





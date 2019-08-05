A1-PP1
======




.. topic:: Subgoals for Evaluating Array statements:

    1.	Set up array from 0 to size-1
    2.	Evaluate data type of statements against array
    3.	Trace statements, updating slots as you go



Assume the following given declarations:

.. code-block::cpp

    String [] alpha;

Evaluate these statements and determine the value of all variables used.
If any error occurs, give the reason.

.. code-block:: cpp

    alpha = new String[8];
    alpha[0] = "apple";
    alpha[1] = "Banana";
    alpha[2] = alpha[0].substring(2);
    alpha[7] = 'a';
    alpha[3] = alpha[alpha[1].indexOf('a')];
    
.. shortanswer:: short-A1-PP1
            
    answer here

          
     
----------------------------------------------------------------------------------------------------------------


.. activecode:: assignactivecode-A1-PP1
   :language: java
   
   
    public class main{
    
    public static void main(String args[]){      
  
    }
    }

# processor emulation
the idea of the project is to set some processors up and some tasks in an sqlite table, then the system to automate the running of the tasks

this project has two python files. 

## create_database.py 
- creates an SQLite database, generating and adding tasks to newly created table called SimulationData.
- it populates the table with a task number, a unique ID, task duration and end time

## run_processors.py 
- creates a queue from the self-named module
- adds all the tasks from the previously created table to the queue, ordered by arrival time
- has a System class that utilises 3 instances of the Processor class in the same file
- this cycles through the tasks in the queue based on a Clock that is keeping track of the time
- the system checks whether there are processors free or not to determine whether to assign the task to a processor, if not they are placed on hold
- if there is one free, it will sit running until the end time and then be removed

this was a university project and some point may need refactoring a little.
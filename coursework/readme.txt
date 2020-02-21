create_database creates an sqlite database
it populates the table with a task number, a unique ID, task duration and end time

run processes runs all these tasks in processors
uses classes clock, processor and system
checks the ID and processor availability before processing and loops over the table ordered by start time
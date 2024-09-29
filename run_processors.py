import sqlite3
import re
import queue

DB_FILE = "SimulationData.db"

# Checks for a validID using regular expressions
def validID (IDString) :
    checksPassed = 0
    if re.search(r'[a-z]', IDString) :
        checksPassed += 1
    if re.search(r'[A-Z]', IDString) :
        checksPassed += 1
    if re.search(r'[0-9]', IDString) :
        checksPassed += 1
    if re.search(r'[-@_#*&]', IDString) :
        checksPassed += 1
    if (checksPassed >= 3) :
        return True
    return False

# add all tasks to a queue and return it
def tasks_to_queue (db_file):
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM SimulationData ORDER BY Arrival ASC')
    tasks = cursor.fetchall()
    new_queue = queue.Queue()
    for task in tasks :
        new_queue.put(task)
    cursor.close()
    return new_queue

class Clock() :
    def __init__(self):
        self.time = 0

    def update_time(self, new_time):
        self.time = new_time

    def get_time(self):
        return self.time

class Processor()  :
    def __init__(self,processor_id):
        self.processor_id = processor_id
        self.task_id = 0
        self.end_time = 0

    def add_task(self, task_id, end_time) :
        self.task_id = task_id
        self.end_time = end_time

    def release(self):
        self.task_id = 0
        self.end_time = 0

    def is_free(self):
        return self.task_id == 0

    def get_proc_id(self) :
        return self.processor_id

    def get_task_id(self) :
        return self.task_id

    def get_endtime(self) :
        return self.end_time

class System() :
    def __init__(self):
        self.clock = Clock()
        self.queue = tasks_to_queue(DB_FILE)
        self.hold = queue.Queue()
        self.processors = [Processor(i+1) for i in range(3)]

    # return true if the queue is empty
    def held_empty(self):
        return self.hold.empty()

    # return the length of the queue
    def queue_length(self):
        return self.queue.qsize()

    # return the number of free processors
    def num_free_processors(self):
        count = 0
        for i in range(len(self.processors)):
            if self.processors[i].is_free() :
                count += 1
        return count

    # return the number of free processors
    def num_busy_processors(self):
        count = 0
        for i in range(len(self.processors)):
            if self.processors[i].is_free() == False :
                count += 1
        return count

    # return the first available processor in ascending order
    def first_free_processor(self) :
        for i in range(len(self.processors)):
            if self.processors[i].is_free() :
                return i

    # return true if there is a processor available
    def processor_free(self):
        for processor in self.processors :
            if processor.get_task_id() == 0 :
                return True
        return False

    # return a list containing indexes of all busy processors
    def list_busy_processors(self):
        list = []
        for processor in self.processors:
            if processor.get_task_id() != 0:
                list.append(processor.get_proc_id()-1)
        return list

    # return the id of the next processor to release based on the current end times of each one
    def next_processor_to_release(self):
        processors_to_release = self.list_busy_processors()
        current_earliest_time = self.processors[processors_to_release[0]].get_endtime()
        processor_id = processors_to_release[0]

        for i in processors_to_release[1:] :
            if (self.processors[i].get_endtime() < current_earliest_time) :
                current_earliest_time = self.processors[i].get_endtime()
                processor_id = i
        return processor_id

    # return true if the task arrival time is earlier than the end times of all busy processors
    def task_first(self, task_arrival):
        current_earliest_time = task_arrival

        if self.num_busy_processors() != 0:
            earliest_proc_id = self.next_processor_to_release()
            earliest_proc_time = self.processors[earliest_proc_id].get_endtime()
            if current_earliest_time < earliest_proc_time:
                return True
            return False

        return True

    # update the time to the endtime of the processor being freed and then free that processor
    def release_processor(self):
        processor_to_release = self.processors[self.next_processor_to_release()]
        self.clock.update_time(processor_to_release.get_endtime())
        print("** {} : Task {} completed.".format(self.clock.get_time(), processor_to_release.get_task_id()))
        processor_to_release.release()

    # release the remaining busy processors
    def release_all_processors(self):
        for i in range(self.num_busy_processors()):
            self.release_processor()

    # add a task to the first available processor
    def add_task_to_processor(self, task, end_time):
        freeprocessor = self.processors[self.first_free_processor()]
        freeprocessor.add_task(task[1], end_time)
        print("** {} : Task {} assigned to processor {}".format(self.clock.get_time(), task[1], freeprocessor.get_proc_id()))

    # Start the system
    def start(self):
        print("** SYSTEM INITIALISED **")
        task = 0

        # Keep going until there are no tasks left and the queue/processors are also empty.
        while (self.queue_length() != 0 or self.held_empty() == False or self.num_free_processors() != 3) :
            # Only assign a task from the database if there are any left
            if self.queue_length() != 0 and task == 0:
                task = self.queue.get()

            # only work with a task if there is one left and there are no tasks on hold
            if self.held_empty() and task != 0:
                # If the task arrival time comes before the end times of the processors, task_first evaluates to true
                task_first = (self.task_first(task[2]))
                if task_first :
                    # Check for a validID and accept it if valid.
                    validatedID = validID(task[1])

                    # Update the clock time if the task has an arrival time past the current clock time
                    if self.clock.get_time() < task[2]:
                        self.clock.update_time(task[2])

                    print('** {} : Task {} with duration {} enters the system.'.format(self.clock.get_time(), task[1], task[3]))

                    # If the ID is valid, proceed
                    if validatedID :
                        print("** Task {} accepted.".format(task[1]))
                        # if there is a processor free then add to a processor
                        if self.processor_free() :
                            end_time = task[2] + task[3]
                            self.add_task_to_processor(task, end_time)
                        else :
                            # if there are no processors available, put it on hold.
                            self.hold.put(task)
                            print("** Task {} on hold.".format(task[1]))
                    else :
                        # Otherwise discard the task
                        print("** Task {} unfeasible and discarded.".format(task[1]))
                    # Reset the task now it's been dealt with
                    task = 0
                else :
                    # If there aren't any processors available then release the nearest endtime processor
                    self.release_processor()
            else :
                # if there is a processor free and a task on hold then add that task to the free processor and remove from queue.
                if self.processor_free() and self.held_empty() == False:
                    waiting_task = self.hold.get()
                    end_time = self.clock.get_time()+waiting_task[3]
                    self.add_task_to_processor(waiting_task, end_time)

                # If there isn't a processor free then release the earliest end_time processor
                if self.processor_free() == False :
                    self.release_processor()

                # Once there are no more tasks in the database and no tasks on hold free up the rest of the processors in order of end_times
                if self.queue_length() == 0 and self.held_empty() :
                    self.release_all_processors()

        print("** {} : SIMULATION COMPLETED. **".format(self.clock.get_time()))

# Start the system.
System().start()

class TaskManager():

    def __init__(self): 
        self._task_list = []

    def add_task(self, task):
        if task == "":
            raise Exception("Unable to add task. Input must be a string")
        self._task_list.append(task)

    def display_task(self): 
        if self._task_list == []:
            raise Exception("No tasks to-do!")
            
        result = "To-do: " + ", ".join(self._task_list) + "."
        return result

    def complete_task(self, task): 
        if task not in self._task_list:
                raise Exception("Task not in your current task list.")            
        self._task_list.remove(task)

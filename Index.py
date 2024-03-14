from constants import *


class Task:
    __id_counter = 1

    def __init__(self, header, description, date):
        self._header = header
        self._description = description
        self._date = date
        self._is_completed = False
        self.__id = type(self).__id_counter
        type(self).__id_counter += 1

    def get_id(self):
        return self.__id

    def mission_accomplished(self):
        self._is_completed = True

    def get_status(self):
        if not self._is_completed:
            return "Awaiting execution"
        else:
            return "Done"

    def print_task(self):
        print("{}{}{}:{}{}".format(BOLD_TEXT, BOTTOM_LINE, self._header, CANCEL_BOLD_TEXT, CANCEL_BOTTOM_LINE))
        print("\t{}description:{} {}".format(BOTTOM_LINE, CANCEL_BOTTOM_LINE, self._description))
        print("\t{}date:{} {}".format(BOTTOM_LINE, CANCEL_BOTTOM_LINE, self._date))
        print("\t{}status:{} {}".format(BOTTOM_LINE, CANCEL_BOTTOM_LINE, self.get_status()))


class ListOfTask:
    def __init__(self):
        self.__list_task = []
        self.__num_of_task = 0

    def add_task(self, task):
        self.__list_task.append(task)
        self.__num_of_task += 1

    def remove_task(self, num_of_task):
        try:
            self.__list_task.pop(num_of_task)
            self.__num_of_task -= 1
            return "The task was successfully removed"
        except IndexError:
            return "No match was found for the id you entered"

    def print_list(self):
        i = 1
        for task in self.__list_task:
            print("{}. ".format(i), end="")
            task.print_task()
            i += 1


def main():
    print("Welcome to the todo list")
    to_do_list = ListOfTask()
    tasks_performed = to_do_list = ListOfTask()
    choice = 1
    while choice:
        choice = int(input("Please enter your choise\n1. To print ToDo list\n2. To add a task to be performed\n3. To mark a completed task\n4. Delete a task from the list"))
        if choice == 1:
            to_do_list.print_list()
        elif choice == 2:
            header = input("Please enter a name for the task: ")
            description = input("Please enter a description for the task: ")
            date = input("Please enter a date for the task: ")
            to_do_list.add_task(Task(header, description, date))
        elif choice == 3:
            #TODO complete the transfer from to-do tasks to completed tasks
        elif choice == 4:
            id = input("Which list number would you like to remove?")
            to_do_list.remove_task(id)






if __name__ == "__main__":
    main()

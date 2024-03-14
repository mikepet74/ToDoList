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
    def print_task(self):
        print("{}{}{}:{}{}".format(BOLD_TEXT, BOTTOM_LINE, self._header, CANCEL_BOLD_TEXT, CANCEL_BOTTOM_LINE))
        print("\t{}description:{} {}".format(BOTTOM_LINE, CANCEL_BOTTOM_LINE, self._description))
        print("\t{}date:{} {}".format(BOTTOM_LINE, CANCEL_BOTTOM_LINE, self._date))


def main():



if __name__ == "__main__":
    main()
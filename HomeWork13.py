# 1. Modify the first homework assignment so that when you try to set a negative or zero value for an item, an exception is raised (the type of exception is up to you).

# 2. Modify the Second Homework so that when you try to add more than 10 students to the group, an exception is thrown (the type of exception is up to you).
# The event of adding a new student to the group should be recorded in a log file.

import logging
logger = logging.getLogger('HomeWork12')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
console.setFormatter(formatter)
#
filehandler = logging.FileHandler('example_logger.log')
filehandler.setLevel(logging.DEBUG)
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)
if __name__ == '__main__':
    logger.info('Start')
    logger.warning('Added logging to log')

class ErrorLimitGroup(BaseException):
    def __init__(self, limit_group):
        self.limit_group = limit_group

    def __str__(self):
        return f'Sorry, group is full {self.limit_group}'

class Human:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'



class Student(Human):

    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender


    def __str__(self):
        return f'{super().__str__()},- {self.gender}'


class Group:

    def __init__(self, title, max_group=10):
        self.title = title
        self.max_group = max_group
        self.students_list = []


    def add_to_group(self, student):

        if not isinstance(student, Student):
            raise TypeError('The student must to be instance of classe Student')
        if student not in self.students_list and len(self.students_list) < self.max_group:
            self.students_list.append(student)
            logger.info(f'Student {student} added')
        if len(self.students_list) >= self.max_group:
            raise ErrorLimitGroup('')


    def remove_student(self, student):
        if student in self.students_list:
            self.students_list.remove(student)

    def search_student(self, surname):
        search = []
        for student in self.students_list:
            if student.surname == surname:
                search.append(student)
        return search

    def __str__(self):
        return f"{'Group:'} {self.title} \n{'-' * 30}\n" + \
           '\n'.join(map(str, self.students_list)) + '\n'


my_group = Group('PythonItGeneration')
my_group.add_to_group(Student('Heorhii', 'Karabetskyi', 'male'))
my_group.add_to_group(Student('Hanna', 'Karabetska', 'female'))
my_group.add_to_group(Student('Oleksandr', 'Fedorov', 'male'))
my_group.add_to_group(Student('Ivan', 'Stoianov', 'male'))
my_group.add_to_group(Student('Inna', 'Stoianova', 'female'))
my_group.add_to_group(Student('Marian', 'Stoianov', 'male'))
my_group.add_to_group(Student('Oleksii', 'Leemon', 'male'))
my_group.add_to_group(Student('Maria', 'Cheban', 'female'))
my_group.add_to_group(Student('Viktor', 'Dadisha', 'male'))
# my_group.add_to_group(Student('Mark', 'Karabetskyi', 'male'))
# my_group.add_to_group(Student('Oleksii', 'Fevrov', 'male'))
# my_group.add_to_group(Student('Dmitro', 'Sezonov', 'male'))
# my_group.add_to_group(Student('Vitalyina', 'Zelenska', 'female'))
print(my_group)
print('-' * 30)
for student in my_group.search_student('Stoianov'):
    print(student.name, student.surname, '-', student.gender)

logger.info('Finish')

# import statements
import datetime


class Employee:
    """Class variables are variables that as shared among all instances of a class.
        they should & must be the same for each instance of the class. (e.g. annual raise amount).
    """
    # example1 - class variable
    numb_of_empls = 0

    # example2 of a class variable
    raise_amt = 1.03

    def __init__(self, first, last, pay):
        """You may think of this as 'initialize' or 'constructor'.

            Methods within a class automatically receive the instance as the first argument.
                By conversion this is first argument is called 'self'.
                And then you can add any other arguments as deem fit.

        """
        # Now let's set the 'instance variables' which must be unique for each instance of a class; like
        # our names, pay, email address, etc. using a class method/function

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.numb_of_empls += 1

    # If we have to perform certain 'Actions' which must be repetitive,
    # then we should think of creating functions/methods to do that job
    def fullname(self):
        """function to return Employee class instance
        full name.
        """
        return f'{self.first}, {self.last}'

    def apply_raise(self):
        """An example of a class variable wrapped inside a regular method.
            1. we can either access the class variables via the class itself OR
            2. access them via an instance of the class(self).
                3. using point (2) instead of (1) allows to makes changes to class instances if need be.        """
        # self.pay =  self.pay * Employee.raise_amount # via the class itself
        self.pay = int(self.pay) * self.raise_amt  # via the class instance

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        """Using the @classmethod method as alternative constructors to create objects
        :arg - cls represents the class
            emp_str reprsents the string value that is passed to the method.
        """
        fname, lname, pay, = emp_str.split('-')  # the last comma after pay makes the assignment a list
        return cls(fname, lname, pay)

    @staticmethod
    def is_workday(day):
        """These methods are neither regular nor class methods. They may not depend on any instance or class variables.
            They, but only have some logical connection with the class. They also do not take the instance(self) nor
            class(cls) arguments. Instead, just pass in the arguments that you want to work with.

        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# Inheritance & Sub-classes in Python
class Developer(Employee):
    """This child class inherited from the parent class, Employee.
        we can customize certain things in this class like a different
        raise amount for our developers from 4% to 10%.
    """
    raise_amt = 1.10

    # if we want to give/initiate our Developer sub-class/child class with more information
    # than their parent class can handle, we may need to give our sub-class its own "__init__" method.

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # 1-way to call the parent class' "__init__" method
        # Employee.__init__(self, first, last, pay) # a 2nd way to call the parent class' "__init__" method
        self.prog_lang = prog_lang


# Let's class another sub-class that will inherit from the Employee class
class Manaager(Employee):
    """this class will also have it's own __init__ method"""

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        """This method adds new employee to the manager class
        Args: emp - the newly added employee"""
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        """This method removes an employee from the manager class."""
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            return emp.fullname()

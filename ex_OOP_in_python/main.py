from OOP_script import *


if __name__ == '__main__':
    # create Employee
    emp_1 = Employee('Von', 'Doe', 50000)
    emp_2 = Employee('Test', 'User', 60000)

    # create Developer instance variable
    dev_1 = Developer('Emmanuel', 'Adjavor', 50000, 'Python')
    dev_2 = Developer('Paul', 'Adjavor', 60000, 'Julia')

    # create Manager instance variab
    mgr_1 = Manaager('Clifford', 'Adjavor', 90000, [dev_1])

    # print the Employee instance class
    # print(emp_1)
    # print(emp_2)

    # An example of manual assignation of "instance variables/data/info/" -
    # Instance variables contain DATA that is unique to each instance
    # emp_1.first = 'hayford'
    # emp_1.last = 'adjavor'
    # emp_1.email = 'hayford.adjavor@gmail.com'
    # emp_1.pay = 50000
    #
    # emp_2.first = 'Test'
    # emp_2.last = 'User'
    # emp_2.email = 'Test.User@gmail.com'
    # emp_2.pay = 60000

    # How to create a new employee object/instance when you get the information in the form of a string value
    # using our Employee class: Example below:-
    emp_str_1 = 'kofi-doe-70000'
    emp_str_2 = 'samar-alhihi-80000'
    emp_str_3 = 'alex-adjavor-25000'

    # first we split on the hyphen (-)
    # fname, lname, pay, = emp_str_1.split('-')

    # Then, we create the instance of the new employee using the class, 'Employee'
    new_emp_1 = Employee.from_string(emp_str_1)

    breakingpoint_ = 0

    # print to inspect object
    print(new_emp_1.email)
    print(new_emp_1.pay)

    breaking_point = 1

    print(new_emp_1.apply_raise())

    # Printing Function  calls or instance and/or instance Variable calls
    # print an attribute variable (email) of the Employee instance class
    print(emp_1.email)
    print(emp_2.email)

    # doing a certain actions manually, but
    # this could be done using a class method/function as in above.
    # print(f'{emp_1.first}, {emp_1.last}')

    # print the sane action using the class method creative above
    print(emp_1.fullname())
    print(emp_2.fullname())

    # we can also run the above as follows
    print(emp_1.fullname())  # we can run a method on a class instance OR
    print(Employee.fullname(
        emp_1))  # run method on the Employee class and pass the respective instance of the class to it.

    # accessing the name space of a class instance
    print(emp_1.__dict__)

    # check out the class variable function before and after the raise
    print(emp_1.pay)
    emp_1.apply_raise()
    print(emp_1.pay)

    # let's call the class method to change the "raise_amt" cls variable
    # to a new global value
    Employee.set_raise_amount(1.08)

    # access the class variable(s) via the class or class instance
    print(Employee.raise_amt)
    print(emp_1.raise_amt)
    print(emp_2.raise_amt)
    print(Employee.numb_of_empls)

    # access the @staticmethod function
    my_date = datetime.date(2021, 10, 31)
    print(Employee.is_workday(my_date))

    breaking_point = 2

    # print to inspect the developer class
    # print the Developer instance class: "Method Resolution Order"
    print(dev_1.email)
    print(dev_1.prog_lang)
    print(dev_1.pay)

    # check out Python's "Method Resolution Order"
    # print(help(Developer))
    print(dev_1.pay)
    dev_1.apply_raise()
    print(dev_1.pay)

    breaking_point = 3

    print(f'attributes of mgr_1 is:++++++++> {mgr_1}')
    print(f'attributes of mgr_1 is:++++++++> {mgr_1.email}')
    mgr_1.add_emp(dev_2)
    print(mgr_1.print_emps())

    breaking_point = 4

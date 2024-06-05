import pytest
from Employee import Employee

def test_give_default_raise():
    test_emp = Employee('hqz', '22', '3000')
    test_emp.give_raise()


def test_give_custom_raise():
    test_emp = Employee('hqz', '22', '3000')
    test_emp.give_raise(10000)
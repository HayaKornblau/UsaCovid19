import unittest
from scripts.employee import Employee


# ---------------------
# Author: Haya Kornblau
# Date:  08/08/20 13:30
# ---------------------

# note:
#  in the tests, need to change day/month birthday of emp1 to today(), adjust birthday of emp2
#  for activate, kindly place the cursor after unittest.main()


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('setUp..')
        self.emp1 = Employee(1, 'Joan', 'Collins', 'F', '1935-08-22', 10, 1, 5000)
        print(self.emp1.empId, self.emp1.firstName, self.emp1.lastName, self.emp1.birthDate)
        self.emp2 = Employee(2, 'James', 'Bond', 'M', '1961-11-27', 20, 2, 8000)
        print(self.emp2.empId, self.emp2.firstName, self.emp2.lastName, self.emp2.birthDate)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('Testing email..')
        self.assertEqual(self.emp1.email, 'Joan.Collins@email.com')
        self.assertEqual(self.emp2.email, 'James.Bond@email.com')

    def test_fullname(self):
        print('Testing fullname..')
        self.assertEqual(self.emp1.fullname, 'Joan Collins')
        self.assertEqual(self.emp2.fullname, 'James Bond')

    def test_happy_birthday(self):
        print('Testing happy_birthday..')
        self.assertEqual(self.emp1.happy_birthday, 'Happy birthday!')
        self.assertEqual(self.emp2.happy_birthday, None)

    def test_days_to_birthday(self):
        print('Testing days_to_birthday..')
        self.assertEqual(self.emp1.days_to_birthday, 0)
        self.assertEqual(self.emp2.days_to_birthday, 97)

    def test_apply_salary_raise(self):
        print('Testing apply_salary_raise..')
        self.emp1.apply_salary_raise()
        self.emp2.apply_salary_raise()
        self.assertEqual(self.emp1.salary, 5250)
        self.assertEqual(self.emp2.salary, 8400)

    def test_apply_salary_cut(self):
        print('Testing apply_salary_cut..')
        self.emp1.apply_salary_cut()
        self.emp2.apply_salary_cut()
        self.assertEqual(self.emp1.salary, 4854)
        self.assertEqual(self.emp2.salary, 7766)

    print('Testing employee.. Done!\n')

    # if __name__ == 'test_employee':
    #     unittest.main()

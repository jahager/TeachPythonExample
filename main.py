import importlib
import glob
import unittest
import random


class StudentTestCase(unittest.TestCase):
    def __init__(self, method_name='runTest', student_folder='none'):
        super().__init__(method_name)
        self.student_folder = student_folder

    def setUp(self):
        """
        Imports user folder as library
        """
        self.module = importlib.import_module(self.student_folder)

    @unittest.skipIf(__name__ != '__main__', reason="Tests must be run using runner, use \"python main.py\"")
    def test_add(self):
        """
        Place all tests relating to "add" here
        """
        # Actual tests/asserts occur heere
        a = random.randint(1, 100000)
        b = random.randint(1, 100000)
        response = self.module.add(a, b)
        self.assertEqual(response, a + b, f"Student: {self.student_folder}")

    def tearDown(self) -> None:
        """
        un-imports student folder
        """
        del self.module


def suite():
    # Get all folder without \\
    sum_assignments = [x.replace('\\', '').replace('/','') for x in glob.glob('[!_]*/')]

    suite = unittest.TestSuite()
    # Create a test for each student folder
    for student in sum_assignments:
        suite.addTest(StudentTestCase("test_add", student))
    return suite


if __name__ == '__main__':
    # Run tests
    runner = unittest.TextTestRunner()
    runner.run(suite())

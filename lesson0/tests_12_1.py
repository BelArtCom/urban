import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner1 = Runner('Ivan')
        for walk in range(1, 11):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    def test_run(self):
        runner2 = Runner('Stepan')
        for run in range(1, 11):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    def test_challenge(self):
        runner3 = Runner('Oleg')
        runner4 = Runner('Petr')
        for walk_and_run in range(1, 11):
            runner3.walk()
            runner4.run()
        self.assertNotEqual(runner3.distance, runner4.distance)

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest import TestCase

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner('Tamerlan')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('Roman')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner('Artem')
        runner2 = Runner('Dima')
        for i in range(10):
            runner1.run()
            runner1.walk()
        for j in range(10):
            runner2.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, 120)
        self.assertNotEqual(runner2.distance, 120)


if __name__ == "__main__":
    unittest.main()
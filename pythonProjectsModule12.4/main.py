import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding="UTF-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

def skip_if_frozen(test_func):

    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            raise unittest.SkipTest("Тесты в этом кейсе заморожены")
        return test_func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    def test_run(self):
        try:
            runner = Runner(123, 5)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner")

    def test_walk(self):
        try:
            runner = Runner('Ivan', -10)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning("Неверная скорость для Runner")


if __name__ == "__main__":
    unittest.main()
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding="UTF-8",
                        format="%(levelname)s | %(message)s")
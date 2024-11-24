import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создаем тестовый набор (TestSuite)
def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))  # Используем loadTestsFromTestCase
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))  # Используем loadTestsFromTestCase
    return suite

# Запускаем тесты с verbosity=2
if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)  # Установим verbosity=2 для подробного вывода
    runner.run(suite())
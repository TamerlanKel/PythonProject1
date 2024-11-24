import unittest

def skip_if_frozen(test_func):
    # Декоратор для пропуска теста, если is_frozen = True
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            raise unittest.SkipTest("Тесты в этом кейсе заморожены")
        return test_func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Указываем, что тесты не заморожены

    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    def test_run(self):
        self.assertTrue(True)

    def test_walk(self):
        self.assertIsNone(None)


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Указываем, что тесты заморожены

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertEqual(1 + 1, 2)

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertIsNone(None)
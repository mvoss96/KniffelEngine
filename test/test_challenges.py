import unittest
import challenges


class TestChallenges(unittest.TestCase):
    def test_only_number(self):
        for i in range(1, 7):
            ch = challenges.ch_only_number(i)
            for n in range(0, 6):
                test_input = [i] * n + [i + 1 if i < 6 else i - 1] * (5 - n)
                points = ch.set_result(test_input)
                self.assertEqual(
                    points, n * i, msg=f"case:{ch.get_name()} test input:{test_input}"
                )

    def test_n_of_a_kind(self):
        non_valid_input = [1, 2, 3, 4, 5]
        for i in range(2, 6):
            ch = challenges.ch_n_of_a_kind(i)
            points = ch.set_result(non_valid_input)
            self.assertEqual(
                points, 0, msg=f"case:{ch.get_name()} test input:{non_valid_input}"
            )
        ch = challenges.ch_n_of_a_kind(2)
        self.assertEqual(ch.set_result([1, 2, 3, 4, 4]), 4 * 2)  # Zweierpasch
        ch = challenges.ch_n_of_a_kind(3)
        self.assertEqual(ch.set_result([1, 2, 3, 3, 3]), 3 * 3)  # Dreierpasch
        ch = challenges.ch_n_of_a_kind(4)
        self.assertEqual(ch.set_result([1, 2, 2, 2, 2]), 2 * 4)  # Viererpasch
        ch = challenges.ch_n_of_a_kind(5)
        self.assertEqual(ch.set_result([1, 1, 1, 1, 1]), 50)  # Kniffel

    def test_full_house(self):
        non_valid_inputs = (
            [1, 1, 2, 2, 3],
            [1, 1, 1, 1, 2],
            [1, 1, 1, 2, 3],
            [1, 2, 3, 4, 5],
            [6, 5, 4, 3, 2],
        )
        valid_inputs = (
            [1, 1, 1, 2, 2],
            [1, 1, 2, 2, 2],
            [2, 3, 2, 3, 2],
            [6, 5, 5, 5, 6],
        )
        ch = challenges.ch_full_house()
        for i in non_valid_inputs:  # test non valid
            points = ch.set_result(i)
            self.assertEqual(points, 0, msg=f"case:{ch.get_name()} test input:{i}")
        for i in valid_inputs:  # test valid
            points = ch.set_result(i)
            self.assertEqual(points, 25, msg=f"case:{ch.get_name()} test input:{i}")

    def test_small_street(self):
        non_valid_inputs = (
            [1, 1, 2, 2, 3],
            [1, 1, 1, 1, 2],
            [1, 2, 3, 5, 6],
            [2, 2, 4, 5, 1],
            [6, 5, 5, 5, 6],
        )
        valid_inputs = (
            [1, 2, 3, 4, 6],
            [2, 3, 4, 5, 5],
            [3, 4, 5, 6, 1],
            [1, 2, 3, 4, 5],
        )
        ch = challenges.ch_small_street()
        for i in non_valid_inputs:  # test non valid
            points = ch.set_result(i)
            self.assertEqual(points, 0, msg=f"case:{ch.get_name()} test input:{i}")
        for i in valid_inputs:  # test valid
            points = ch.set_result(i)
            self.assertEqual(points, 30, msg=f"case:{ch.get_name()} test input:{i}")

    def test_big_street(self):
        non_valid_inputs = (
            [1, 1, 2, 2, 3],
            [1, 1, 1, 1, 2],
            [1, 2, 3, 5, 6],
            [2, 2, 4, 5, 1],
            [6, 5, 5, 5, 6],
            [1, 2, 3, 4, 6],
            [2, 3, 4, 5, 5],
            [3, 4, 5, 6, 1],
        )
        valid_inputs = (
            [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6],
            [1, 5, 4, 3, 2],
            [6, 5, 4, 3, 2],
        )
        ch = challenges.ch_big_street()
        for i in non_valid_inputs:  # test non valid
            points = ch.set_result(i)
            self.assertEqual(points, 0, msg=f"case:{ch.get_name()} test input:{i}")
        for i in valid_inputs:  # test valid
            points = ch.set_result(i)
            self.assertEqual(points, 40, msg=f"case:{ch.get_name()} test input:{i}")

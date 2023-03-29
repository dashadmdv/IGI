import unittest

from ..src.functions import count_sentences, count_non_declarative, \
    calc_average_sentence_length, calc_average_word_length


class TestCountSentences(unittest.TestCase):

    def test_1(self):
        expected_value = 1
        returned_value = count_sentences('Hello, World!')
        self.assertEqual(returned_value, expected_value)

    def test_2(self):
        expected_value = 1
        returned_value = count_sentences('Hello, World.')
        self.assertEqual(returned_value, expected_value)

    def test_3(self):
        expected_value = 1
        returned_value = count_sentences('Are you okay?')
        self.assertEqual(returned_value, expected_value)

    def test_4(self):
        expected_value = 1
        returned_value = count_sentences('Hello, Mrs.Marple...')
        self.assertEqual(returned_value, expected_value)

    def test_5(self):
        expected_value = 3
        returned_value = count_sentences('There is some great news when it comes to job interviews. It’s not all '
                                         'doom and gloom (bad). Most recruiters these days ask the interviewees ('
                                         'you) the same basic questions.')
        self.assertEqual(returned_value, expected_value)

    def test_7(self):
        expected_value = 2
        returned_value = count_sentences('Hello v.i.p. client. Nice to meet you mr. Perez.')
        self.assertEqual(returned_value, expected_value)

    def test_6(self):
        expected_value = 2
        returned_value = count_sentences('Wtf?! I don\'t want know what u feeling.')
        self.assertEqual(returned_value, expected_value)

    def test_8(self):
        expected_value = 1
        returned_value = count_sentences('He said: "Hello. How are you?"')
        self.assertEqual(returned_value, expected_value)

    def test_9(self):
        expected_value = 1
        returned_value = count_sentences('Mr.Garcia is here !?')
        self.assertEqual(returned_value, expected_value)

    def test_10(self):
        expected_value = 1
        returned_value = count_sentences('He said: "Hello, what\'s up?"')
        self.assertEqual(returned_value, expected_value)

class TestAverageLengthOfWords(unittest.TestCase):
    def test_1(self):
        expected_value = 7.5
        returned_value = calc_average_word_length('Another sentence.')
        self.assertEqual(returned_value, expected_value)

    def test_2(self):
        expected_value = 17 / 3
        returned_value = calc_average_word_length('Mt strange sentence.')
        self.assertEqual(returned_value, expected_value)

    def test_3(self):
        expected_value = 0
        returned_value = calc_average_word_length('')
        self.assertEqual(returned_value, expected_value)

    def test_4(self):
        expected_value = 5
        returned_value = calc_average_word_length('Hello!!')
        self.assertEqual(returned_value, expected_value)

    def test_5(self):
        expected_value = 1
        returned_value = calc_average_word_length('M')
        self.assertEqual(returned_value, expected_value)


class TestAmountOfNonDeclarative(unittest.TestCase):
    def test_1(self):
        expected_value = 1
        returned_value = count_non_declarative('Hello Mr. Maks! Im a driver.')
        self.assertEqual(returned_value, expected_value)

    def test_2(self):
        expected_value = 1
        returned_value = count_non_declarative('Hi!')
        self.assertEqual(returned_value, expected_value)

    def test_3(self):
        expected_value = 0
        returned_value = count_non_declarative('')
        self.assertEqual(returned_value, expected_value)

    def test_4(self):
        expected_value = 0
        returned_value = count_non_declarative('I.')
        self.assertEqual(returned_value, expected_value)

    def test_5(self):
        expected_value = 1
        returned_value = count_non_declarative('Hello!!!!!')
        self.assertEqual(expected_value, returned_value)


class TestAverageLengthOfSentence(unittest.TestCase):
    def test_1(self):
        expected_value = 10
        returned_value = calc_average_sentence_length('Hello Mr. Maks! Im a driver.')
        self.assertEqual(expected_value, returned_value)

    def test_2(self):
        expected_value = 5
        returned_value = calc_average_sentence_length('Hello!')
        self.assertEqual(expected_value, returned_value)

    def test_3(self):
        expected_value = 0
        returned_value = calc_average_sentence_length('')
        self.assertEqual(expected_value, returned_value)

    def test_4(self):
        expected_value = 0
        returned_value = calc_average_sentence_length('1.')
        self.assertEqual(expected_value, returned_value)

    def test_5(self):
        expected_value = 0
        returned_value = calc_average_sentence_length(' ')
        self.assertEqual(expected_value, returned_value)


if __name__ == "__main__":
    unittest.main()

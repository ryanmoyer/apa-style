#!/usr/bin/env python

import unittest

from apa import format_apa_style


class TestApa(unittest.TestCase):
    def test_teaching_python_ryan(self):
        citation = format_apa_style(
            'Sean Fisk', 2012, 'Teaching Python to Ryan', 'Jenison',
            'MI', 'Kreiner Koders')
        self.assertEqual(
            citation,
            'Fisk, S. (2012). Teaching Python to Ryan. '
            'Jenison, MI: Kreiner Koders.')

    def test_k_and_r_c_programming(self):
        citation = format_apa_style(
            'Brian Kernighan', 1988, 'C Programming Language Ansi',
            'Englewood Cliffs', 'NJ', 'Prentice Hall')
        self.assertEqual(
            citation,
            'Kernighan, B. (1988). C Programming Language Ansi. '
            'Englewood Cliffs, NJ: Prentice Hall.')

    def test_handles_only_first_name(self):
        with self.assertRaises(ValueError) as context_manager:
            format_apa_style(
                'Sean', 2012, 'Teaching Python to Ryan', 'Jenison',
                'MI', 'Kreiner Koders')
        self.assertEqual(str(context_manager.exception), 'Invalid name')

    def test_handles_too_many_names(self):
        with self.assertRaises(ValueError) as context_manager:
            format_apa_style(
                'Sean Richard Fisk', 2012,
                'Teaching Python to Ryan', 'Jenison',
                'MI', 'Kreiner Koders')
        self.assertEqual(str(context_manager.exception), 'Invalid name')

    def test_handles_missing_data(self):
        citation = format_apa_style(
            'Sean Fisk', 2012, '', '',
            '', '')
        self.assertEqual(citation, 'Fisk, S. (2012). . , : .')


if __name__ == '__main__':
    unittest.main()

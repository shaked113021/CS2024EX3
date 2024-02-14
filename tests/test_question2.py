import unittest
from unittest.mock import patch
import io
import question2


class MyTestCase(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_GivenExample(self, fake_out: io.StringIO):
        expected_output = '\n'.join([
            'move disk 1 from A to C',
            'move disk 2 from A to B',
            'move disk 1 from C to B',
            'move disk 3 from A to C',
            'move disk 1 from B to A',
            'move disk 2 from B to C',
            'move disk 1 from A to C\n'
        ])

        question2.hanoi(3, "A", "C", "B")
        self.assertEqual(expected_output, fake_out.getvalue())


if __name__ == '__main__':
    unittest.main()

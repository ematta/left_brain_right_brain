import unittest
from src.args import parse_args  # replace 'your_module' with the actual module name

class TestParseArgs(unittest.TestCase):
    def test_no_args(self):
        with self.assertRaises(SystemExit):
            parse_args()

    def test_pdf_path_arg(self):
        args = parse_args(['--pdf-path', 'path/to/pdf'])
        self.assertEqual(args.pdf_path, 'path/to/pdf')
        self.assertFalse(args.server)
        self.assertFalse(args.new)

    def test_server_arg(self):
        args = parse_args(['--server', 'True'])
        self.assertIsNone(args.pdf_path)
        self.assertTrue(args.server)
        self.assertFalse(args.new)

    def test_new_arg(self):
        args = parse_args(['--new', 'True'])
        self.assertIsNone(args.pdf_path)
        self.assertFalse(args.server)
        self.assertTrue(args.new)

    def test_all_args(self):
        args = parse_args(['--pdf-path', 'path/to/pdf', '--server', 'True', '--new', 'True'])
        self.assertEqual(args.pdf_path, 'path/to/pdf')
        self.assertTrue(args.server)
        self.assertTrue(args.new)

    def test_invalid_arg(self):
        with self.assertRaises(SystemExit):
            parse_args(['--invalid-arg'])

if __name__ == '__main__':
    unittest.main()
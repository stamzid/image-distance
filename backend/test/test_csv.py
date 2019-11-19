import os
import unittest
from backend.app.file_processor import CSVProcessor


class TestCSVProcessor(unittest.TestCase):
    def test_read_csv(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, 'data/example_one.csv')

        csv_processor = CSVProcessor()
        file_data = csv_processor.read_csv(file_path)
        self.assertEqual(len(file_data), 2)
        self.assertEqual(file_data[0].get('image1'), 'hey.png')

    def test_read_csv_data(self):
        form_data = b'image1,image2\nimg1.png, img2.png\n'
        csv_processor = CSVProcessor()
        file_data = csv_processor.read_csv_data(form_data)

        self.assertEqual(len(file_data), 1)

    def test_write_csv(self):
        dict_row = {
            'image1': 'digi1.png',
            'image2': 'digi2.png',
            'similar': 0.23,
            'elapsed': 1.23
        }

        csv_processor = CSVProcessor()
        file_path = csv_processor.write_csv('testing.csv', [dict_row])

        file_data = csv_processor.read_csv(file_path)
        self.assertEqual(len(file_data), 1)
        self.assertEqual(file_data[0].get('image1'), 'digi1.png')
        os.remove(file_path)


if __name__=='__main__':
    unittest.main(verbosity=4)

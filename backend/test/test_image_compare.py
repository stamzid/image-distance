import os
import unittest
from backend.app.img_compare import ImageCompare


class TestImageCompare(unittest.TestCase):
    def test_same_ssim(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(dir_path, 'data/image_one.png')
        img_comp = ImageCompare()

        (score, diff) = img_comp.compare_ssim(image_path, image_path)
        self.assertEqual(score, 1.0)

    def test_same_mse(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(dir_path, 'data/image_one.png')
        img_comp = ImageCompare()

        err = img_comp.calculate_mse(image_path, image_path)
        self.assertEqual(err, 0.0)

if __name__=='__main__':
    unittest.main(verbosity=4)

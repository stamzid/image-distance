from skimage.metrics import structural_similarity as ssim
from PIL import Image
import numpy as np
import cv2


class ImageCompare:
    def compare_ssim(self, image_one, image_two):
        imageA = self.get_proper_image(image_one)
        imageB = self.get_proper_image(image_two)

        h, w = imageA.shape[:2]
        imageB = cv2.resize(imageB, (h,w))

        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        (score, diff) = ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")

        return (score, diff)

    def calculate_mse(self, image_one, image_two):
        imageA = self.get_proper_image(image_one)
        imageB = self.get_proper_image(image_two)

        h, w = imageA.shape[:2]
        imageB = cv2.resize(imageB, (h,w))

        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])

        return err

    def get_proper_image(self, image):
        if image.endswith('.gif'):
            converted = Image.open(image).convert('RGB')
            image_path = image.replace('.gif', '.jpg')
            converted.save(image_path)

            return cv2.imread(image_path)
        else:
            return cv2.imread(image)

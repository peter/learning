import numpy as np
import matplotlib.pyplot as plt

def plot(digit):
    if type(digit[1]) == np.ndarray:
        correct_digit = [i for i, n in enumerate(list(digit[1])) if n[0] == 1.0][0]
    else:
        correct_digit = digit[1]
    # The pixel intensity values are integers from 0 to 255
    def pixel_intensity(n):
        return round(n*255)
    pixels = np.array(list(map(pixel_intensity, digit[0][:,0])), dtype='uint8').reshape((28, 28))
    plt.title(f'Digit {correct_digit}')
    plt.imshow(pixels, cmap='gray')
    plt.show()

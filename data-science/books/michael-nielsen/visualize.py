import numpy as np
import matplotlib.pyplot as plt

def scale_range (input, min, max):
    input += -(np.min(input))
    input /= np.max(input) / (max - min)
    input += min
    return input

def plot_digit(digit):
    if type(digit[1]) == np.ndarray:
        correct_digit = [i for i, n in enumerate(list(digit[1])) if n[0] == 1.0][0]
    else:
        correct_digit = digit[1]
    plot_pixels(digit[0][:,0], title=f'Digit {correct_digit}')

def plot_pixels(values, title=''):
    def pixel_intensity(n):
        return round(n*255)
    pixels = np.array(list(map(pixel_intensity, scale_range(values, 0, 1))), dtype='uint8').reshape((28, 28))
    plt.title(title)
    plt.imshow(pixels, cmap='gray')
    plt.show()

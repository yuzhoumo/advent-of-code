import sys

""" Day 8: Space Image Format (Part 1)

Images are sent as a series of digits that each represent the color of a single pixel. The digits fill each row of the
image left-to-right, then move downward to the next row, filling rows top-to-bottom until every pixel of the image is
filled. Each image actually consists of a series of identically-sized layers that are filled in this way. So, the first
digit corresponds to the top-left pixel of the first layer, the second digit corresponds to the pixel to the right of
that on the same layer, and so on until the last digit, which corresponds to the bottom-right pixel of the last layer.

The image you received is 25 pixels wide and 6 pixels tall. To make sure the image wasn't corrupted during transmission,
the Elves would like you to find the layer that contains the fewest 0 digits. On that layer, what is the number of 1
digits multiplied by the number of 2 digits? """


class Image:  # Stores x, y dimensions, list of raw digits, and list of layer objects
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.raw_data, self.layers = [], []

    def add_layer(self, layer):
        assert layer.x == self.x and layer.y == self.y, 'Layer size does not match image size'
        self.layers.append(layer)

    def set_data(self, data):
        assert len(data) % (self.x * self.y) == 0, 'Data length does not match img size'
        self.raw_data = [int(n) for n in data]
        data = list(self.raw_data)

        while data:
            layer = Layer(self.x, self.y)
            layer.set_data(data[:self.x * self.y])  # Slices 1 layer worth of raw data and sets data to layer
            data = data[self.x * self.y:]  # Sets data to remaining data after slice
            self.add_layer(layer)


class Layer:  # Stores x, y dimensions, list of raw digits, and 2d list of layer data
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.raw_data, self.rows = [], []

    def add_row(self, row):
        assert len(row) == self.x, 'Row length does not match x dimension'
        self.rows.append(row)

    def set_data(self, data):
        assert len(data) == self.x * self.y, 'Data length does not match layer size'
        self.raw_data = [int(n) for n in data]
        data = list(self.raw_data)

        for _ in range(self.y):  # Slices raw data into rows and sets each row
            row, data = data[:self.x], data[self.x:]
            self.add_row(row)

    def count_digit(self, d):  # Counts how many times digit d appears in self.raw_data
        cnt = 0
        for n in self.raw_data:
            if n == d:
                cnt += 1
        return cnt


def corruption_check(image):
    # Gets layer in image with fewest zeros using count_digits function
    fewest_zeros_layer = min(image.layers, key=lambda x: Layer.count_digit(x, 0))
    # Returns number of 1 digits * number of 2 digits on layer with fewest zeros
    return fewest_zeros_layer.count_digit(1) * fewest_zeros_layer.count_digit(2)


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) > 2, 'Missing argument: x dimension of image'
    assert len(sys.argv) > 3, 'Missing argument: y dimension of image'
    assert len(sys.argv) < 5, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        x_dim, y_dim = int(sys.argv[2]), int(sys.argv[3])
        raw_data = f.read().strip()

    image = Image(x_dim, y_dim)
    image.set_data(raw_data)

    print(corruption_check(image))


if __name__ == '__main__':
    main()

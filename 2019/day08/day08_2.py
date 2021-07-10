import sys

""" Day 8: Space Image Format (Part 2)

Now you're ready to decode the image. The image is rendered by stacking
the layers and aligning the pixels with the same positions in each
layer. The digits indicate the color of the corresponding pixel: 0 is
black, 1 is white, and 2 is transparent. The layers are rendered with
the first layer in front and the last layer in back. So, if a given
position has a transparent pixel in the first and second layers, a black
pixel in the third layer, and a white pixel in the fourth layer, the
final image would have a black pixel at that position. What message is
produced after decoding your image? """


class Image:
    # Stores x, y dimensions, list of raw digits, and list of layer objects
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.raw_data, self.layers = [], []

    def add_layer(self, layer):
        assert layer.x == self.x and layer.y == self.y, \
            'Layer size does not match image size'
        self.layers.append(layer)

    def set_data(self, data):
        assert len(data) % (self.x * self.y) == 0, \
            'Data length does not match img size'
        self.raw_data = [int(n) for n in data]
        data = list(self.raw_data)

        while data:
            layer = Layer(self.x, self.y)
            # Slices 1 layer worth of raw data and sets data to layer
            layer.set_data(data[:self.x * self.y])
            # Sets data to remaining data after slice
            data = data[self.x * self.y:]
            self.add_layer(layer)

    def decode(self):  # Combines all layers into one layer object
        decoded, layers = Layer(self.x, self.y), list(self.layers)
        decoded.set_data(layers.pop().raw_data)

        while layers:
            # Overwrites decoded layer with next layer in image
            current = layers.pop()
            for y in range(self.y):
                for x in range(self.x):
                    # Does nothing if pixel is transparent (if value is 2)
                    # Overwrite if black or white pixel
                    if current.rows[y][x] == 0 or current.rows[y][x] == 1:
                        decoded.rows[y][x] = current.rows[y][x]

        return decoded


class Layer:
    # Stores x, y dimensions, list of raw digits, and 2d list of layer data
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.raw_data, self.rows = [], []

    def add_row(self, row):
        assert len(row) == self.x, 'Row length does not match x dimension'
        self.rows.append(row)

    def set_data(self, data):
        assert len(data) == self.x * self.y, \
            'Data length does not match layer size'
        self.raw_data = [int(n) for n in data]
        data = list(self.raw_data)

        for _ in range(self.y):
            # Slices raw data into rows and sets each row
            row, data = data[:self.x], data[self.x:]
            self.add_row(row)

    def __str__(self):
        result = ''
        for row in self.rows:
            for pixel in row:
                if pixel == 0:  # Black pixel
                    result += '░'
                elif pixel == 1:  # White pixel
                    result += '█'
                elif pixel == 2:  # Transparent pixel
                    result += ' '
            result += '\n'
        return result.strip('\n')


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

    print(image.decode())


if __name__ == '__main__':
    main()

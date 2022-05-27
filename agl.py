class Shape:
    """A shape with dimensions and a fill character"""

    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        """Create a shape"""

        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char

    def change_fill(self, fill_char):
        """Change the fill character"""

        self.fill_char = fill_char

    def translate(self, axis, num):
        """translate the shape"""

        if axis == "y":
            self.start_y += num
            self.end_y += num
        else:
            self.start_x += num
            self.end_x += num


class Canvas: 
    """A canvas to hold rectangles"""

    def __init__(self, width, height):
        """Create a canvas"""

        self.width = width
        self.height = height
        self.shapes = []

    def make_and_add_shape(self, start_x, start_y, end_x, end_y, fill_char):
        """Make a shape and add it to the canvas"""

        self.shapes.append(Shape(start_x, start_y, end_x, end_y, fill_char))

    def clear(self):
        """clears the canvas"""

        self.shapes = []

    def print_canvas(self):
        """Print the canvas and shapes to standard output"""

        coords = {}

        i = self.height

        #add all the coordinates to the dictionary as empty spaces
        while i > 0:
            j = self.width
            coords[i] = {}
            while j > 0:
                coords[i][j] = " "
                j -= 1
            i -= 1

        #for each shape add the character to the dictionary at the correct coordinate
        for shape in self.shapes:
            y = shape.end_y
            while y > shape.start_y:
                x = shape.end_x
                while x > shape.start_x:
                    coords[y][x] = shape.fill_char
                    x -= 1
                y -= 1

        print(coords)
        
        #print each line of the canvas
        for line in coords:
            line_to_print = ''
            for val in coords[line].values():
                line_to_print += val
            print(line_to_print)
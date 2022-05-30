from turtle import clear


class TriangularArray:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.array_size = int((self.rows**2 + self.rows)/2)
        self.array = [None] * self.array_size

    def insert_element(self, element, row, column):
        array_index = int(((row-1**2 + (row-1))/2))
        self.array[array_index] = element

    def get_element(self, row, column):
        array_index = int(((row-1**2 + (row-1))/2))
        return self.array[array_index]





if __name__ == '__main__':
    ta = TriangularArray(5, 5)
    ta.insert_element(88, 3, 2)
    print(ta.get_element(3, 2))

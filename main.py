class Field:
    def __init__(self, size, ships):
        self.size = size
        self.grid = []
        for i in range(size):
            self.grid.append([None] * size)
        self.ships_alive = ships

    def display(self, show_ships=False):
        letters = 'ABCDEFGHIJ'
        space = '    '

        for letter in letters:
            space += letter + ' '
        print(space)
        for i, row in enumerate(self.grid):
            display_row = ""
            for cell in row:
                if cell is None or (cell is not None and not show_ships):
                    display_row += "O "
                else:
                    display_row += "■ "
            if i + 1 != 10:  # вывод ноликов и квадратиков
                print(i + 1, " ", display_row)
            else:
                print(i + 1, "", display_row)
from case import Case


class Field:
    def __init__(self, field_string):
        self.matrix = []
        lines = str.split(field_string, '\n')
        for line in lines:
            newline = []
            for cell in line:
                if cell == ".":
                    newline.append(Case(0))
                elif cell == "*":
                    newline.append(Case(1))
            self.matrix.append(newline)
            self.cols_dim = len(newline)

    def resolve(self):
        self.update_proximities()
        resolve_str = self.result_string()
        return resolve_str

    def update_proximities(self):
        row = 0
        for line in self.matrix:
            column = 0
            for cell in line:
                if cell.is_mine() == 1:
                    self.update_proximity(column, row - 1)
                    self.update_proximity(column, row)
                    self.update_proximity(column, row + 1)
                column += 1
            row += 1
    
    def update_proximity(self, column, row):
            if 0 <= row < len(self.matrix):
                self.matrix[row][column].add_mine_proximity()
                if column - 1 >= 0:
                    self.matrix[row][column - 1].add_mine_proximity()
                if column + 1 < self.cols_dim:
                    self.matrix[row][column + 1].add_mine_proximity()

    def result_string(self):
        solution = ""
        row_index = 0
        for line in self.matrix:
            for cell in line:
                solution += cell.mine_proximity()
            row_index += 1
            if row_index < len(self.matrix):
                solution += '\n'
        return solution

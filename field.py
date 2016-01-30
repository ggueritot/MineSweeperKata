from case import Case


class Field:
    def __init__(self, field_string):
        self.matrix = []
        for cell in field_string:
            if cell == ".":
                self.matrix.append(Case(0))
            else:
                self.matrix.append(Case(1))

    def resolve(self):
        resolve_str = ""
        self.update_proximities()
        for cell in self.matrix:
            resolve_str += cell.mine_proximity()
        return resolve_str

    def update_proximities(self):
        column = 0
        for cell in self.matrix:
            if cell.is_mine() == 1:
                self.update_proximity(column)
            column += 1
    
    def update_proximity(self, column):
            if column - 1 >= 0:
                self.matrix[column - 1].add_mine_proximity()
            if column + 1 < len(self.matrix):
                self.matrix[column + 1].add_mine_proximity()

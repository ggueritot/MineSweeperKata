class Case:
    def __init__(self, is_mine):
            if is_mine == 0 or is_mine == 1:
                self.isMine = is_mine
            else:
                Exception("Wrong initialization")
            self.mineProximity = 0

    def is_mine(self):
        return self.isMine

    def mine_proximity(self):
        if self.isMine == 1:
            return "*"
        else:
            return str(self.mineProximity)

    def add_mine_proximity(self):
        self.mineProximity += 1



class Village:

    def __init__(self, village):
        self.village = village

    def owner(self, house):
        return self.village[house]

    def _neighbours(self, house):
        neighbours = []
        
        for r in range(house[0] - 1, house[0] + 2):
            for c in range(house[1] - 1, house[1] + 2):
                if r >= 0 and r < 5 and c >= 0 and c < 5 and (r, c) != house:
                    neighbours += (r, c)
                    
        return neighbours

    def show(self):
        for r in range(0, 5):
            print("{0}{1}{2}{3}{4}".format(
                self.village[r][0], self.village[r][1],
                self.village[r][2], self.village[r][3],
                self.village[r][4]
            ))
    
    def get_house(self, owner):
        for r in range(0, 5):
            for c in range(0, 5):
                if self.village[r][c] == owner:
                    return (r, c)
        return None
    
    def get_neighbours(self, owner):
        house = self.get_house(owner)
        if house == None:
            return None
        else:
            return self._neighbours(house)
        
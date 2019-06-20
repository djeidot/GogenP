class Village:

    def __init__(self, village):
        self.village = [list(word) for word in village]

    def get_owner(self, house):
        return self.village[house[0]][house[1]]

    def _set_owner(self, house, owner):
        self.village[house[0]][house[1]] = owner

    def _neighbours(self, house):
        neighbours = []

        for r in range(house[0] - 1, house[0] + 2):
            for c in range(house[1] - 1, house[1] + 2):
                if 0 <= r < 5 and 0 <= c < 5 and (r, c) != house:
                    neighbours.append((r, c))

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
        if house is None:
            return self.get_all_empty_houses()
        else:
            return self._neighbours(house)

    def get_empty_neighbours(self, owner):
        neighbours = self.get_neighbours(owner)
        empty_neighbours = []
        for house in neighbours:
            if self.get_owner(house) == '.':
                empty_neighbours.append(house)

        return empty_neighbours

    def get_all_empty_houses(self):
        empty_houses = []
        for r in range(0, 5):
            for c in range(0, 5):
                if self.village[r][c] == '.':
                    empty_houses.append((r, c))
        return empty_houses

    def buy_house(self, house, owner):
        if self.get_owner(house) == '.':
            self._set_owner(house, owner)
        pass
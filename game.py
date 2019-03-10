class Game(object):
    def __init__(self):
        self._rolls = [0] * 21
        self._current_roll = 0

    def roll(self, pins):
        self._rolls[self._current_roll] = pins
        self._current_roll += 1

    @property
    def score(self):
        score = 0
        index = 0
        for frame in range(0, 10):
            if self.isStrike(index):
                score += 10 + self.strikeAdd(index)
                index += 1
            elif self.isSpare(index):
                score += 10 + self.spareAdd(index)
                index += 2
            else:
                score += self._rolls[index] + self._rolls[index + 1]
                index += 2
        return score

        
    def spareAdd(self, index):
        return self._rolls[index + 2]

    def strikeAdd(self, index):
        return self._rolls[index + 1] + self._rolls[index + 2]

    def isSpare(self, index):
        return self._rolls[index] + self._rolls[index + 1] == 10

    def isStrike(self, index):
		return self._rolls[index] == 10
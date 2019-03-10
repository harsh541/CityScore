from game import Game
import unittest


class TestBowlingGame(unittest.TestCase):
 	def setUp(self):
 		self.game = Game()

 	def test_gutter_game(self):
 		self.multipleRolls(pins=0, num=20)

 		self.assertEqual(self.game.score, 0)

 	def testSingles(self):
 		self.multipleRolls(pins=1, num=20)

 		self.assertEqual(self.game.score, 20)

 	def multipleRolls(self, pins, num):
 		for i in range(num):
 			self.game.roll(pins)

 	def spare(self):
 		self.game.roll(5)
 		self.game.roll(5)

 	def testSpare(self):
 		self.spare()
 		self.game.roll(3)
 		self.multipleRolls(pins=0, num=17)

 		self.assertEqual(self.game.score, 16)

	def strike(self):
 		self.game.roll(10)

 	def testStrike(self):
 		self.strike()
 		self.game.roll(3)
 		self.game.roll(4)
 		self.multipleRolls(pins=0, num=16)

 		self.assertEqual(self.game.score, 24)

 	def test_perfect_game(self):
 		self.multipleRolls(pins=10, num=12)

 		self.assertEqual(self.game.score, 300)


if __name__ == '__main__':
    unittest.main()
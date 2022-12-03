import unittest
import main



class TestDay2(unittest.TestCase):

    def test_translate(self):
        input = ['A', 'X']
        self.assertEqual(main.translate(input), [0,0])
        input = ['B', 'Y']
        self.assertEqual(main.translate(input), [1,1])
        input = ['C', 'Z']
        self.assertEqual(main.translate(input), [2,2])

    def test_choice_points(self):
        self.assertEqual(main.choice_point('X'), 1)
        self.assertEqual(main.choice_point('Y'), 2)
        self.assertEqual(main.choice_point('Z'), 3)

    def test_play_points(self):
        self.assertEqual(main.play_points(['A', 'X']), 3)
        self.assertEqual(main.play_points(['B', 'Y']), 3)
        self.assertEqual(main.play_points(['C', 'Z']), 3)

        self.assertEqual(main.play_points(['A', 'Y']), 6)
        self.assertEqual(main.play_points(['A', 'Z']), 0)

        self.assertEqual(main.play_points(['B', 'X']), 0)
        self.assertEqual(main.play_points(['B', 'Z']), 6)

        self.assertEqual(main.play_points(['C', 'X']), 6)
        self.assertEqual(main.play_points(['C', 'Y']), 0)

    def test_play_points2_lose(self):
        self.assertEqual(main.play_points_2(['A', 'X']), 3)
        self.assertEqual(main.play_points_2(['B', 'X']), 1)
        self.assertEqual(main.play_points_2(['C', 'X']), 2)

    def test_play_points2_draw(self):
        self.assertEqual(main.play_points_2(['A', 'Y']), 4)
        self.assertEqual(main.play_points_2(['B', 'Y']), 5)
        self.assertEqual(main.play_points_2(['C', 'Y']), 6)
    
    def test_play_points2_win(self):
        self.assertEqual(main.play_points_2(['A', 'Z']), 8)
        self.assertEqual(main.play_points_2(['B', 'Z']), 9)
        self.assertEqual(main.play_points_2(['C', 'Z']), 7)


if __name__ == '__main__':
    unittest.main()

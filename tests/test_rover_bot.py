import unittest
from rover_bot import __version__
from rover_bot.rover import Rover


class RoverTest(unittest.TestCase):
    def test_set_coordinates_and_direction_of_rover(self):
        rover = Rover([1, 2, "N"])
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 2)
        self.assertEqual(rover.nose, "N")

    def test_change_nose_left(self):
        rover = Rover([1, 1, "N"])
        rover.move(["L"])
        self.assertEqual(rover.nose, "W")

    def test_change_nose_right(self):
        rover = Rover([1, 1, "N"])
        rover.move(["R"])
        self.assertEqual(rover.nose, "E")

    def test_change_nose_left_twice(self):
        rover = Rover([1, 1, "N"])
        rover.move(list("LL"))
        self.assertEqual(rover.nose, "S")

    def test_change_nose_right_three_times(self):
        rover = Rover([1, 1, "N"])
        rover.move(list("RRR"))
        self.assertEqual(rover.nose, "W")

    def test_move_forward_to_north(self):
        rover = Rover([1, 1, "N"])
        rover.move(list("M"))
        self.assertEqual(rover.nose, "N")
        self.assertEqual(rover.y, 2)

    def test_change_nose_to_east_and_move_forward_three_times(self):
        rover = Rover([1, 1, "N"])
        rover.move(list("RMMM"))
        self.assertEqual(rover.nose, "E")
        self.assertEqual(rover.x, 4)

    def test_complex_moves_and_changes_nose(self):
        rover = Rover([1, 2, "N"])
        rover.move(list("LMLMLMLMM"))
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 3)
        self.assertEqual(rover.nose, "N")

    def test_complex_moves_and_changes_nose_again(self):
        rover = Rover([3, 3, "E"])
        rover.move(list("MMRMMRMRRM"))
        self.assertEqual(rover.x, 5)
        self.assertEqual(rover.y, 1)
        self.assertEqual(rover.nose, "E")

    def test_trying_to_set_unknown_direction_and_receiving_north(self):
        rover = Rover([1, 1, "P"])
        self.assertEqual(rover.nose, "N")
        self.assertNotEqual(rover.nose, "P")

    def test_trying_to_apply_unknown_movement(self):
        rover = Rover([1, 2, "W"])
        rover.move(list("LJ"))
        self.assertEqual(rover.nose, "S")
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 2)

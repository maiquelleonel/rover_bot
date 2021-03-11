from rover_bot.rover import Rover
import time

rovers = []
movements = []

INPUT = """5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM"""


def get_instructions():
    for k, val in enumerate(INPUT.splitlines()):
        if k == 0:
            max_x, max_y = val.split(" ")
        else:
            if k % 2 == 0:
                movements.append(list(val))
            else:
                position = val.split(" ")
                rovers.append(Rover(position))


def apply_movements():
    for k, rover in enumerate(rovers):
        print(f"initial state of rover {k}: {rover}")
        time.sleep(1)
        print("apply movements")
        rover.move(movements[k])
        time.sleep(1)
        print(f"final state of rover {k}: {rover}")
        time.sleep(1)


def main():
    get_instructions()
    apply_movements()

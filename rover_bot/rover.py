MOVEMENTS = {
    "N": {"L": "W", "R": "E"},
    "S": {"L": "E", "R": "W"},
    "E": {"L": "N", "R": "S"},
    "W": {"L": "S", "R": "N"},
}


class Rover:
    x = 0
    y = 0
    nose = "N"

    def __init__(self, positions):
        self.x = int(positions[0])
        self.y = int(positions[1])
        self.nose = "N"
        if positions[2] in list("NSWE"):
            self.nose = positions[2]

    def __repr__(self):
        return f"{self.x} | {self.y} | {self.nose}"

    def move(self, moves):
        for movement in moves:
            if movement == "M":
                if self.nose == "N":
                    self.y += 1
                elif self.nose == "S":
                    self.y -= 1
                elif self.nose == "E":
                    self.x += 1
                elif self.nose == "W":
                    self.x -= 1
            else:
                if movement in list("LR"):
                    self.nose = MOVEMENTS[self.nose][movement]

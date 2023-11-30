import copy
import random

class Hat:
    def __init__(self, **balls) -> None:
        self.contents = [color for color, count in balls.items() for _ in range(count)]

    def draw(self, num_balls_drawn):
        if num_balls_drawn >= len(self.contents):
            return self.contents
        else:
            drawed_balls = []
            for _ in range(num_balls_drawn):
                rnd_idx = random.randrange(0, len(self.contents))
                drawed_balls.append(self.contents.pop(rnd_idx))
            return drawed_balls


    def debug(self):
        print(self.contents)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)

        drawn_balls = hat_copy.draw(num_balls_drawn)

        if all(drawn_balls.count(color) >= expected_balls.get(color, 0) for color in expected_balls):
            success_count += 1

    probability = success_count / num_experiments
    return probability


hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **args):
        self.contents = []
        for key, value in args.items():
            for i in range(value):
                self.contents.append(key)
        print(self.contents)

    def draw(self, number):
        try:
            balls = random.sample(self.contents, number)
        except:
            balls = copy.deepcopy(self.contents)

        for ball in balls:
            self.contents.remove(ball)

        return balls

    def get_contents(self):
        return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)
        expected_copy = copy.deepcopy(expected_balls)
        for color in balls:
            if color in expected_copy:
                expected_copy[color] -= 1

        if all(x <= 0 for x in expected_copy.values()):
            count += 1

    return count / num_experiments

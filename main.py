import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)  # Add each ball to contents

    def draw(self, number):
        chosen_balls = []

        # If we don't have enough balls, draw all of them
        if len(self.contents) < number:
            number = len(self.contents)  # Adjust number to draw only available balls
        
        for _ in range(number):
            random_ball = random.choice(self.contents)
            chosen_balls.append(random_ball)
            self.contents.remove(random_ball)  # Remove drawn ball from contents
        
        return chosen_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0  # Number of successful experiments

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)  # Make a copy of the hat to simulate one experiment
        drawn = hat_copy.draw(num_balls_drawn)  # Draw the balls

        # Count the occurrences of each color in the drawn balls
        drawn_counts = {ball: drawn.count(ball) for ball in drawn}

        # Check if the expected balls are met
        match = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                match = False
                break

        if match:
            M += 1  # If the condition is met, increase the success count

    return M / num_experiments  # Return the probability


# Example call
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={'red': 2, 'green': 1},
                         num_balls_drawn=5,
                         num_experiments=2000)

print(f"Probability: {probability}")

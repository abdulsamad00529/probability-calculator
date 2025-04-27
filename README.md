# Probability-Based Hat Drawing Simulation

This Python project simulates the process of drawing balls from a hat with a specified probability distribution. The goal is to estimate the probability of drawing a particular combination of balls over a number of experiments.

## Features:
- Define a hat with various colored balls and their respective quantities.
- Simulate drawing balls from the hat.
- Estimate the probability of drawing a specified combination of balls through multiple experiments.

## Classes:
1. **Hat**:
   - Allows the creation of a hat with different colored balls.
   - Supports the `draw()` method to randomly pick balls from the hat.

2. **experiment**:
   - Runs multiple experiments to calculate the probability of drawing the expected combination of balls.
     
##License:
This project is licensed under the MIT License.

## Example Usage:

```python
# Create a hat with 6 black balls, 4 red balls, and 3 green balls.
hat = Hat(black=6, red=4, green=3)

# Run an experiment to estimate the probability of drawing 2 red balls and 1 green ball, with 5 balls drawn, over 2000 trials.
probability = experiment(hat=hat,
                         expected_balls={'red': 2, 'green': 1},
                         num_balls_drawn=5,
                         num_experiments=2000)

print(f"Estimated Probability: {probability}")


Requirements:
Python 3.x 



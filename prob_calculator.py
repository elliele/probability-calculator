import copy
import random
# Consider using the modules imported above.
from copy import deepcopy
from collections import Counter

class Hat:

    # take a variable number of arguments
    def __init__(self, **kwargs):
        self.contents = [] # create empty list that act as Hat contents


        for k, v in kwargs.items(): # list of strings containing one item for each ball in the hat
            for i in range(v): # loop through the amount(v) of each color ball(k).
                self.contents.append(k) # append the ball color(k) to the list

    # draw method that draw balls from hat
    def draw(self, num):
        ball_removed = []

        # number of balls to draw exceeds the available quantity, return all the balls.
        if num >= len(self.contents):
            return self.contents

        # remove balls at random from contents and return those balls as list of strings
        for i in range(num):
            ball_drawn = self.contents.pop(random.randrange(len(self.contents)))
            ball_removed.append(ball_drawn)
        return ball_removed


# determine the probability
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    expected_balls_list = []
    for k,v in expected_balls.items():
        for _ in range(v):
            expected_balls_list.append(k)



    for i in range(num_experiments):
        copyhat = copy.deepcopy(hat)
        draw_list = copyhat.draw(num_balls_drawn)
        expected_balls_list = Counter(expected_balls_list)
        draw_list = Counter(draw_list)

        if expected_balls_list&draw_list == expected_balls:
            count += 1
 


    probability = count/num_experiments
    return probability





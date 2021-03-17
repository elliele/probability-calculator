# Created by Ellie Le at 3/5/2021

import copy
import random
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

    # loop through the number of experiments
    for i in range(num_experiments):
        copyhat = copy.deepcopy(hat) # copy the hat contents
        draw_list = copyhat.draw(num_balls_drawn) # draw ball from hat

        expected_balls_list = Counter(expected_balls_list) # count the number of color ball in expected list
        #print(expected_balls_list)
        draw_list = Counter(draw_list) # count the number of color ball during experiment
        #print(draw_list)

        if expected_balls_list&draw_list == expected_balls: # check if the number of expected balls is the same
            count += 1

    probability = count/num_experiments
    return probability


'''Test

hat = Hat(black=6, red=4, green=3)
hat.draw(2)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=10)
'''








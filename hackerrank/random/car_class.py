class Car(object):
    def __init__(self, color, year, make, model, current_speed, max_speed, current_direction, gas_level, mileage):
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.current_speed = current_speed
        self.max_speed = max_speed
        # would be North South East or West
        self.current_direction = current_direction
        # as a decimal from 0-1
        self.gas_level = gas_level
        self.mileage = mileage


    def accelerate(self):
        """Accelerates car 10MPH"""

        # take self.current_  speed and increment it by 10
        # would also have a check in this method to make sure that the car couldn't go past the max speed
        pass

    def get_speed(self):
        """prints the current speed of the car"""

        # print self.current_speed
        pass

    def brake(self):
        """Decelerates the car to 0"""

        # set current speed equal to zero and print "car stopped"
        pass

    def turn(self, direction):
        """Turns the car in whichever you specify: L or R"""

        # take the current direction which is in N,S,E,W and capture current direction in a variable
        # change the current direction to NSEW depending on which direction is specified, left or right
        # print a statment to the console that the car was heading __ (old direction) and now is heading __ new direction
        pass

    def change_direction(self, new_direction):
        """Changes direction of car using NSEW"""

        # capture the current direction in a variable
        # change self.current direction to the new_direction
        # print a statment to the console that the car was heading old direction and now is heading new direction
        pass

    def check_gas_level(self):
        """Prints gas tank level"""

        # print (10 * gas level) %
        pass

    def fill_tank(self):
        """Fills gas tank to full"""

        # find the difference between 1 and gas_level
        # if gas level is already 1, print tank is full
        # if the gas level is less than 1, fill up tank & print tank was filled with difference of old level and 1 as a percent
        pass

    def check_mileage(self):
        """Prints car mileage"""

        # print self.mileage
        pass

    def drive(self):
        """Drives the car and increments mileage & decrements gas"""

        # to make it simple, each time you call drive on an instance of a car, lets drive 10 miles
        # print "driving car 10 miles"
        # increment mileage by 10
        # decrement gas level by .1
        pass

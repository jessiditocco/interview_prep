class Person(object):
    def __init__(self, initial_age):
        if initial_age > 0:
            self.age = initial_age
        else:
            self.age = 0
            print "Age is not valid, setting age to 0."

    def year_passes(self):
        self.age += 1

    def am_i_old(self):
        if age < 13:
            print "You are young."
        elif age >= 13 and age < 18:
            print "You are a teenager."
        else:
            print "You are old."
class Person(object):
    def __init__(self, firstName, lastName, idNum):
        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum

    def print_person(self):
        print "Name: {}, {}".format(self.lastName, self.firstName)
        print "ID: {}".format(self.idNum)


class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        super(Student, self).__init__(firstName, lastName, idNum)
        self.scores = scores

    def calculate(self):
        sum_of_grades = 0
        num_grades = len(self.scores)

        for grade in self.scores:
            sum_of_grades += grade

        average = float(sum_of_grades / num_grades)

        if 90 <= average <= 100:
            return "O"
        elif 80 <= average <= 90:
            return "E"
        elif 70 <= average <= 80:
            return "A"
        elif 55 <= average <= 70:
            return "P"
        elif 40 <= average < 55:
            return "D"
        elif average < 40:
            return "T"







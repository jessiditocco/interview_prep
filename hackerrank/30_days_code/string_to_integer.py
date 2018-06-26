def parse_int_from_string(s):

    try:
        worked = int(S)
        print type(worked)

    except ValueError:
        print "That is not a valid number. Try again"


if __name__ == "__main__":

    S = raw_input("Please enter a number: ").strip()
    parse_int_from_string(S)
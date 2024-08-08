import random

def powerball () :
    number_1 = random.randrange(1, 60, 1)
    number_2 = random.randrange(1, 60, 1)
    number_3 = random.randrange(1, 60, 1)
    number_4 = random.randrange(1, 60, 1)
    number_5 = random.randrange(1, 60, 1)
    powerball_number = random.randrange(1, 36, 1)
    print("Today's numbers are " + str(number_1) + ", " + str(number_2) + ", " + str(number_3) + ", " + str(number_4) + ", and " + str(number_5) + ". The Powerball number is " + str(powerball_number) + ".")

powerball()
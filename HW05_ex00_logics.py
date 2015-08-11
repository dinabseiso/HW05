#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    fromUser = raw_input("Please enter an integer. \n")
    try:
        check = int(fromUser)
        pass
    except:
        print ("Please enter it in numeric format.\n")
    if check % 2.0 == 0 : 
        print ("Even")
    else : 
        print ("Odd")
    return None


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""

    for n in range(1,101) :
        if n < 10 :
                stringN = str(n)
                stringN = " "+ stringN
                print stringN,                 
        elif n % 10.0 != 0 : 
            print n,
            n += 1
        else : 
            if n != 100 : 
                rowEnd = str(n)
                rowEnd = " " + rowEnd
                print rowEnd 
            else :
                print n 
            n += 1

            
    
    pass


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    giveNumbers = None
    datapoints = []
    print ("Let's compute an average.")

    while giveNumbers != "done":
        giveNumbers = raw_input("Please enter a number: \n > ")
        try : 
            check = int(giveNumbers)
        except ValueError : 
            if giveNumbers == "done" :
                pass
            else : 
                print "That's not a numeric value. If you are done, type 'done'."
        else : 
            datapoints.append(check)
    average = sum(datapoints) / float(len(datapoints))
    return average



##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    print find_average()

if __name__ == '__main__':
    main()

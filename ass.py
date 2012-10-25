import sys

class ItWas5(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

while True:
    try:
        x = int(raw_input("Please enter a number: "))
        if x == 5:
            raise ItWas5('You can not use 5.')
    except ValueError:
        print("Oops! That was no valid number. Try again... ")
    except KeyboardInterrupt:
        print('\n')
        print("Nice try! Hahaha.")
        print('\n')
    except ItWas5 as e:
        print("Oh, and not 5.")
        print("Error: ", e.value)
    except:
        print("Oh shit! There was an error: ", sys.exc_info()[0])
        raise
    else:
        print("Yay, you did it!")
        break
    finally:
        print("Well, wheather you did it or not, it was a good run... ")

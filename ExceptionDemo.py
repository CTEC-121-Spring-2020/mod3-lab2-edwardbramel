"""
CTEC 121
Edward LaManna
Mod3 and lab 2
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""


def main():
    try:
        print(4/0)
    except ZeroDivisionError:
        print("\nthere was a divide by zero error. exiting\n")
        exit
    except:
        print("\nUnkown exception")
        exit()


main()

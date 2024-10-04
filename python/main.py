"""
https://open.kattis.com/problems/attendance2
"""

import sys

def get_input(this_input):
    if this_input+1 < len(sys.argv):
        return sys.argv[this_input+1]
    else:
        return input()

def main():
    num_students = int(get_input(0))
    absent_students = []
    inputs = []
    for i in range(num_students):
        inputs.append(get_input(i+1))


    for i in inputs:
        if i != "Present!":
            if inputs.index(i)+1 <= len(inputs):
                try:
                    if inputs[inputs.index(i)+1] != "Present!":
                        absent_students.append(i)
                except:
                    if i != "Present!":
                        absent_students.append(i)


    if len(absent_students) == 0:
        print("No Absences")
    else:
        for i in absent_students:
            print(i)


if __name__ == "__main__":
    main()
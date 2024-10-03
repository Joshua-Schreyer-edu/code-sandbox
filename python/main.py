"""
https://open.kattis.com/problems/attendance2
"""

def main():
    num_students = int(input())
    absent_students = []
    inputs = []
    for i in range(num_students):
        inputs.append(input())


    for i in inputs:
        if i != "Present!":
            if inputs.index(i)+1 < len(inputs):
                if inputs[inputs.index(i)+1] != "Present!":
                    absent_students.append(i)
            # this block of code does not run :(        
            if inputs.index(i) == len(inputs):
                absent_students.append(i)

    if len(absent_students) == 0:
        print("No Absences")
    else:
        for i in absent_students:
            print(i)


if __name__ == "__main__":
    main()

"""
6
Buckley
Burnadette
Present!
Chad
Present!
Erin
"""
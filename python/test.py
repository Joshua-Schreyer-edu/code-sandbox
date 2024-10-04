
import subprocess

def test(inputs):

    arguments = []
    arguments.append("python3")
    arguments.append("main.py")
    for i in inputs:
        arguments.append(i)

    subprocess.run(arguments)
    print("--- END OF TEST ---")

test(["8", "4"])
test(["10", "5"])
test(["321", "123"])
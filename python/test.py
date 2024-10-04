
import subprocess

inputs = ["3", "Joshua", "Present!", "Connor"]

arguments = []
arguments.append("python3")
arguments.append("main.py")
for i in inputs:
    arguments.append(i)

subprocess.run(arguments)
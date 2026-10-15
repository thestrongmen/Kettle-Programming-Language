from random import randint
from time import sleep

variables = {}
def translate(code_var):
    global line, var_line
    lines = code_var.splitlines()
    outputs = []
    for line in lines:
        if line.startswith("operation"):
            code_var = line.split()
            if code_var[3] == "+":
                print(int(code_var[3]) + int(code_var[4]))
            elif code_var[2] == "-":
                print(int(code_var[3]) - int(code_var[4]))
            elif code_var[2] == "*":
                print(int(code_var[3]) * int(code_var[4]))
            elif code_var[2] == "/":
                print(int(code_var[3]) / int(code_var[4]))
            elif code_var[2] == "^":
                print(int(code_var[3]) ** int(code_var[4]))
        elif line.startswith("say"):
            code_var = line[4:].strip()
            if code_var in variables:
                print(variables[code_var])
            else:
                print(code_var)
        elif line.startswith("random"):
            code_var = line[7:]
            print(randint(0, int(code_var)))
        elif line.startswith("wait"):
            code_var = line[5:]
            sleep(float(code_var))
        elif line.startswith("set"):
            var_line = line.split()
            variables[var_line[1]] = var_line[2]
            if var_line[2].casefold() == "true":
                variables[var_line[1]] = True
            elif var_line[2].casefold() == "false":
                variables[var_line[1]] = False
            else:
                try:
                    variables[var_line[1]] = int(var_line[2])
                except ValueError:
                    try:
                        variables[var_line[1]] = float(var_line[2])
                    except ValueError:
                        variables[var_line[1]] = str(var_line[2])
        elif line.startswith("type of"):
            code_var = line[8:]
            if code_var in variables:
                print(type(variables[code_var]).__name__)
    return "\n".join(outputs)


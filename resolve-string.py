from collections import defaultdict
import re

variablesdict = {}

def createDict(dictionaries=[]) -> None:
    for var in dictionaries:
        variablesdict[var[0]] = var[1]


def resolveString(input: str) -> str:
    pattern = re.compile(r"%[a-zA-Z]")

    def replace(match):
        var_name = match.group()[1]  
        return resolveString(
            variablesdict.get(var_name, match.group())
        )  

    return pattern.sub(replace, input)


def updateVariable(var: str, value: str) -> None:
    variablesdict[var] = value


createDict([("x", "new"), ("y", "%xworld"), ("z", "hello")])
print(resolveString("%z_%x_%y_world"))  # Output: hello_new_newworld_world
updateVariable("x", "old")
print(resolveString("z_%x_%y_world"))  # Output: hello_old_oldworld_world

def nfa_1(i, state):
    ns = state + 1
    return f"{state} --> {i} --> {ns}"

def occurrence(state):
    ns = state + 1
    return f"{ns} --> e --> {state}"


def check(re):
    state = 0
    regex=re.split()
    if "(" in re:
        regex = re.replace("(", " ( ").replace(")", " ) ").split()
        regex.remove("(")
        regex.remove(")")
    for i in regex:
        if "*" not in i and "|" not in i:
            print(nfa_1(i, state))
            state += 1
        elif "*" in i:
            char=i[:-1]
            startingnode = state
            ns = state + 1
            print(f"{state} --> e --> {ns}")
            state += 1
            print(nfa_1(char, state))
            print(occurrence(state))
            state += 1
            ns = state + 1
            print(f"{state} --> e --> {ns}")
            print(f"{startingnode} --> e --> {ns}")
            state += 1
        elif "|" in i:
            startingnode = state
            char = i.split('|')
            if '' in char:char.remove('')
            endingnode = (len(char) * 2 + 1)+state
            for j in char:
                ns = state + 1
                print(f"{startingnode} --> e --> {ns}")
                state += 1
                print(nfa_1(j, state))
                state += 1
                print(f"{state} --> e --> {endingnode}")
            state+=1

re_input = input("Enter regular expression: ")
check(re_input)
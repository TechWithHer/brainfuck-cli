def run_brainfuck(code: str):
    tape = [0] * 30000
    ptr = 0
    i = 0
    loop_stack = []
    output = ""

    while i < len(code):
        cmd = code[i]
        if cmd == '>':
            ptr += 1
        elif cmd == '<':
            ptr -= 1
        elif cmd == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif cmd == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif cmd == '.':
            output += chr(tape[ptr])
        elif cmd == ',':
            tape[ptr] = ord(input("Input a character: ")[0])
        elif cmd == '[':
            if tape[ptr] == 0:
                loop = 1
                while loop:
                    i += 1
                    if code[i] == '[': loop += 1
                    elif code[i] == ']': loop -= 1
            else:
                loop_stack.append(i)
        elif cmd == ']':
            if tape[ptr] != 0:
                i = loop_stack[-1]
            else:
                loop_stack.pop()
        i += 1
    return output


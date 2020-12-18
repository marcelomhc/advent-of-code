def evaluate(expr):
    v1 = expr.pop(0)
    subtotal = evaluate(expr) if v1 == '(' else int(v1)

    while len(expr) > 0:
        op = expr.pop(0)
        if op == ')':
            return subtotal

        v2 = expr.pop(0)
        v2 = evaluate(expr) if v2 == '(' else int(v2)

        subtotal = subtotal + v2 if op == '+' else subtotal * v2
    return subtotal


def precedence(expr):
    v1 = expr.pop(0)
    subtotal = precedence(expr) if v1 == '(' else int(v1)

    while len(expr) > 0:
        op = expr.pop(0)
        if op == ')':
            return subtotal
        elif op == '*':
            v2 = precedence(expr)
            return subtotal * v2
        else:
            v2 = expr.pop(0)
            v2 = precedence(expr) if v2 == '(' else int(v2)

        subtotal += v2
    return subtotal


def part1(expressions):
    total = 0
    stack = []
    for expr in expressions:
        for c in expr.strip():
            if c != ' ':
                stack.append(c)
        total += evaluate(stack)
    print(total)


def part2(expressions):
    total = 0
    stack = []
    for expr in expressions:
        for c in expr.strip():
            if c != ' ':
                stack.append(c)
        total += precedence(stack)
    print(total)


if __name__ == "__main__":
    with open("input/day18.data", 'r') as f:
        homework = f.readlines()
    part1(homework)
    part2(homework)

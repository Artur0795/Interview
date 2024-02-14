from interview import Stack


balanced_code1 = '(((([{}]))))'
balanced_code2 = '[([])((([[[]]])))]{()}'
balanced_code3 = '{{[()]}}'

unbalanced_code1 = '}{}'
unbalanced_code2 = '{{[(])]}}'
unbalanced_code3 = '[[{())}]'


def is_valid(lines):
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    open_par = Stack()

    if len(lines) % 2 > 0:
        return 'Несбалансированно'

    for i, char in enumerate(lines):
        if char in opening:
            open_par.push(char)
        elif char in closing:
            if open_par.is_empty():
                return 'Несбалансированно'
            elif opening.index(open_par.peek()) != closing.index(char):
                return 'Несбалансированно'
            else:
                open_par.pop()
                if open_par.is_empty() and i == len(lines)-1:
                    return 'Сбалансированно'


if __name__ == '__main__':
    print(f'Последовательность скобок 1: {is_valid(balanced_code1)}')
    print(f'Последовательность скобок 2: {is_valid(balanced_code2)}')
    print(f'Последовательность скобок 3: {is_valid(balanced_code3)}')
    print(f'Последовательность скобок 4: {is_valid(unbalanced_code1)}')
    print(f'Последовательность скобок 5: {is_valid(unbalanced_code2)}')
    print(f'Последовательность скобок 6: {is_valid(unbalanced_code3)}')

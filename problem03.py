def is_balance(inputs):
    bal = 0
    for inputs in inputs:
        if inputs == '(':
            bal += 1
        else: bal -= 1
    return not(bool(bal))

def is_correct(inputs):
    bal = 0
    if is_balance(inputs) == False:
        return False
    for inputs in inputs:
        if inputs == '(':
            bal += 1
        else: bal -= 1
        if bal < 0: return False
    return True


def solution(inputs):
    if is_correct(inputs) == True:
        return inputs
    for i in range(2, len(inputs)+1, 2):
        if is_balance(inputs[:i]) == True:
            x, z = inputs[:i], inputs[i:]
            break
    if is_correct(x) == True:
        return x + solution(z)
    else:
        result = '(' + solution(z) + ')'
        for i in x[1:-1]:
            if i == '(':
                result += ')'
            else:
                result += '('
        return result

def main():

    brackets = input()
    answer = solution(brackets)
    
    print(answer)


if __name__ == '__main__':

    main()

    

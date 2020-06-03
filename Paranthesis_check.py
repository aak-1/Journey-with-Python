def valid_parentheses(string):
    stack = []
    str = list(string)
    for x in str:
        if x == ')' and len(stack) == 0:
            return False
        if x == '(':
            stack.append(x)
        if x == ')':
            stack.pop()
        
    if len(stack) == 0:
        return True
    else:
        return False
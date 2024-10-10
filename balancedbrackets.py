def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in phrase:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return False
            else:
                continue
        return not stack
    
    print(has_balanced_brackets("([]{})"))  # True
print(has_balanced_brackets("([)]"))  # False
print(has_balanced_brackets("{{[()]}}"))  # True
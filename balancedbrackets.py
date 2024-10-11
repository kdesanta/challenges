# defining the function
def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """
    #keeps track of opening and closing brackets
    stack = []
    #Dictionary to corresponding brackets
    brackets = {
    ')': '(', 
    '}': '{', 
    ']': '['
    }

#begin loop through the charaters in phrase
    for char in phrase:
#adding character to the stack list (opening brackets)
        if char in brackets.values():
            stack.append(char)

#checking for closing brackets
        elif char in brackets.keys():
#if no characters in stack or unclosed openeing bracket return false
            if not stack or stack.pop() != brackets[char]:
                return False
# return not stack was inside the loop
    return not stack
    
print(has_balanced_brackets("([]{})"))  # True
print(has_balanced_brackets("([)]"))  # False
print(has_balanced_brackets("{{[()]}}"))  # True
print(has_balanced_brackets("((hello world)")) #False
print(has_balanced_brackets("({[this is not balanced})"))

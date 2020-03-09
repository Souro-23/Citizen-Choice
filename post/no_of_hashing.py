def split(string, delimiters = (' ','#')):
    """Behaves str.split but supports multiple delimiters."""

    delimiters = tuple(delimiters)
    stack = [string]

    for delimiter in delimiters:
        for i, substring in enumerate(stack):
            substack = substring.split(delimiter)
            stack.pop(i)
            for j, _substring in enumerate(substack):
                stack.insert(i+j, _substring)

    i=0
    while i in range(len(stack)):
        if stack[i] == '':
            stack.pop(i)
            i = i-1
        i = i+1
    return stack

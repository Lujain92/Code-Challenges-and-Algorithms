def isValid( s) :
        stack = []
        lpara = {')':'(', '}':'{', ']':'['}

        for ss in s:
            if ss in lpara.values():
                stack.append(ss)
            elif stack and lpara[ss] == stack[-1]:
                stack.pop()
            else:
                return False

        return stack == []

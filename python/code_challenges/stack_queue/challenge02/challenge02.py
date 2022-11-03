def isValid( s) :
        '''
        function that used to check it the string s has a valid parentheses
        if yes rturn true else false
        input s:string
        output : boolean
        '''

        stack = []
        lpara = {')':'(', '}':'{', ']':'['}
        for q in s:
            if q not in lpara.values() and q not in lpara.keys():
                s=s.replace(q,'')

        for ss in s:
            if ss in lpara.values():
                stack.append(ss)
            elif stack and lpara[ss] == stack[-1]:
                stack.pop()
            else:
                return False

        return stack == []

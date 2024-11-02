

'''


Min add to make valid here

'''
def minAddToMakeValid(self, s: str) -> int:
    open_brackets = 0
    min_adds_required = 0

    for c in s:
        if c == "(":
            open_brackets += 1

            '''
            When encounter a close bracket, we decrement open bracket
        
            '''
        else:
            if open_brackets > 0:
                open_brackets -= 1
                '''
                If no unmatched open brackets are available,
                
                add minAddsRequired
                '''

            else:
                min_adds_required += 1

    # Add the remaining open brackets as closing brackets would be required.
    return min_adds_required + open_brackets
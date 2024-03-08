


s = "hello world"


# the chlalnenge do this without using the split word
def lengthOfLastWord( s: str) -> int:
    p, length = len(s), 0


    # what is p here
    while p > 0:
        p -= 1
        print("p is", p);

        # we still don't see the last word yet here
        if s[p] != ' ':
            length += 1

        # here is the end of last word
        elif length > 0:
            return length

    return length

lengthOfLastWord("hello world")

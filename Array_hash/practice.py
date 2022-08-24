
# Use a set probably better
def findFirstNonRepeatingChar(s1):

    sets = set()

    for i in range(s1):
        if s1[i] not in sets:
            sets.add(s1[i])
            # we return the position that's found here

        else:
            return i

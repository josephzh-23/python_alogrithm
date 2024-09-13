'''
# of distinct subtrign in a string here

'''
from Playground.Trie import TrieNode


'''
Can use a special trie node here 
'''
class TrieNode:
    def __init__(s, character):
        s.ch = character
        # this here would be the type Map<Character, TrieNode>
        s.map = {}


def numDistinctSubstringInString(s):
    r = TrieNode('*')
    count = 0
    for i in range(len(s)):

        # each word will act as a trie here
        cur = r


        for j in range(i, len(s)):

            ch = s[j]
            if ch not in cur.map:

                '''
                a -> a 
                '''
                node = TrieNode(ch)
                cur.map[ch] = node
                count +=1


            # need to move the child node to the corresponding character at index i here
            # makes a lot of senses
            cur = cur.map.get(ch)
    print('count is', count)
    return count
numDistinctSubstringInString("aabbaba")
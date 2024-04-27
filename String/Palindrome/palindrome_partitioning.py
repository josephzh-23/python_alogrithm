'''
Traverse over the string in the dfs fashion here

for each recursive call, beginnign of the index of the string
: the start

1. Iterate and generate all possilbe substrtings beginnign at index start
2. For each of subtring check if a palindrome

3. If a substring palindrome
 the substring is a potential candidate.
 Add the substring to the currentList and perform a depth-first search on the remaining substring.
  If the current substring ends at index end end + 1 becomes start index of the next recurisve call here .

  4. If start index > = len(string), add current list to the result here, and then here we have the code


'''

'''
The stirng here 
'''


def partition(self, s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            partitions.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                path.append(s[start:end])
                backtrack(end, path)
                path.pop()

    partitions = []
    backtrack(0, [])
    return partitions

# using backtracking in python is much easier here



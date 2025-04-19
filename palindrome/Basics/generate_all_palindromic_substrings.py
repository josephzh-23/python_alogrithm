def find_palindromic_substrings(s):
    palindromes = set()

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1

    for i in range(len(s)):
        # Odd-length palindromes
        expand(i, i)
        # Even-length palindromes
        expand(i, i + 1)

    return sorted(palindromes)

# Example usage
input_str = "ababa"
print(find_palindromic_substrings(input_str))
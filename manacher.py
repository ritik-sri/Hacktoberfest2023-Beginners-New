'''

Manacher's Algorithm is used to find the longest palindromic substring in a given string in linear time complexity, O(n). It is more efficient than the naive approach of checking all possible substrings for being palindromic. Manacher's Algorithm takes advantage of the symmetry properties of palindromic strings to achieve linear time complexity.

'''
def longest_palindromic_substring(s):
    # Preprocess the input string
    processed_str = '#'.join('^{}$'.format(s))
    n = len(processed_str)
    P = [0] * n
    C, R = 0, 0  # Center and right boundary of the rightmost palindrome

    for i in range(1, n - 1):
        # Calculate the mirror position of i
        mirror = 2 * C - i

        # Update P[i] based on whether i is within R
        if i < R:
            P[i] = min(R - i, P[mirror])

        # Attempt to expand palindrome centered at i
        a, b = i + (1 + P[i]), i - (1 + P[i])
        while processed_str[a] == processed_str[b]:
            P[i] += 1
            a += 1
            b -= 1

        # If palindrome centered at i expands past R,
        # adjust center and right boundary
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Find the maximum element in P
    max_len, center_index = max((n, i) for i, n in enumerate(P))

    # Extract and return the longest palindrome
    start = (center_index - max_len) // 2
    end = start + max_len
    return s[start:end]

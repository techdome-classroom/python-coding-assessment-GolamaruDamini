def decode_message(s: str, p: str) -> bool:
    # Memoization dictionary
    memo = {}

    def helper(i, j):
        # Base case: both string and pattern are exhausted
        if i == len(s) and j == len(p):
            return True
        
        # If only the pattern is exhausted, check if there's remaining '*' in the pattern
        if j == len(p):
            return False

        # If only the string is exhausted, check if the remaining pattern is '*' symbols
        if i == len(s):
            return all(c == '*' for c in p[j:])
        
        # Check memoization first
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Case 1: If characters match or the pattern has a '?', continue
        if p[j] == s[i] or p[j] == '?':
            result = helper(i + 1, j + 1)
        # Case 2: If pattern has a '*' symbol
        elif p[j] == '*':
            result = helper(i + 1, j) or helper(i, j + 1)
        else:
            result = False
        
        # Memoize the result
        memo[(i, j)] = result
        return result
    
    return helper(0, 0)


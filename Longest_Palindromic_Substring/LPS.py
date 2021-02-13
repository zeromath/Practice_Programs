# This is an implemention of Manacher’s algorithm:

def preProcess(s):
    if s == "":
        return "^$"
    t = "^"
    for c in s:
        t += "#" + c
    t += "#$"
    return t

def longestPalindrome(s):
    t = preProcess(s)
    n = len(t)
    p = [0 for _ in range(n)]
    C = 0
    R = 0

    max_length = -1
    center = -1

    for i in range(1, n-1):
        i_mirror = 2 * C - i
        p[i] = min(R - i, p[i_mirror]) if R > i else 0
        # expand the palindrome centered at i
        while (t[i + p[i] + 1] == t[i - p[i] - 1]): p[i] += 1

        if i + p[i] > R:
            C = i
            R = i + p[i]

        if p[i] > max_length:
            max_length = p[i]
            center = i

    return s[(center - 1 - max_length) // 2: (center + max_length - 1) // 2]

if __name__ == "__main__":
    s = "abababababac"
    print(longestPalindrome(s))

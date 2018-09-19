# Practice Programs

- [Number](#number)
- [AVL Tree](#avltree)
- [KMP](#kmp)
- [Longest Palindromic Substring](#kps)

## <a name="number"></a> [Number](Number/Number.py)
#### Description
This is a class realizing unlimited length integers and their arithmetic operations `+ - * // %`.

#### Example
```python
a = Number(321)
b = Number(-1234)
print(a)      # 321
print(b)      # -1234
print(a == b) # False
print(a <= b) # False
print(a >= b) # True
print(a > b)  # True
print(a < b)  # False
print(a - b)  # 1555
print(a + b)  # -913
print(a * b)  # -396114
q, r = a.quotientWithRemainder(b)
print(q)      # -1
print(r)      # -913
c = Number('-inf')
print(c > a)  # False
print(c < a)  # True
print(c - a)  # -Infinity
print(c + a)  # -Infinity
print(c * a)  # -Infinity
d = Number('inf')
print(d > c)  # True
print(d * c)  # -Infinity
print(d - c)  # Infinity
c.flipSign()
print(c > d)  # False
```

## <a name="avltree"></a> [AVL Tree](AVL_Tree/AVLTree.py)
AVL tree is a balanced binary tree.
[To be updated]

## <a name="kmp"></a> [KMP](KMP/KMP.py)
#### Description
This is a realization of the KMP (Knuth-Morris-Pratt) algorithm, which takes `O(n)` time to determine whether a string `pattern` is a substring of a given string.

#### Example
```python
kmp = KMP("ababa")
s = "abababababcbabababd"
result = kmp.findMatch(s)
for i in result:
   print(str(i) + ": " + s[i: i+5])
```
The output is

```python
0: ababa
2: ababa
4: ababa
12: ababa
```

#### Reference

1. [KMP算法详解](http://www.matrix67.com/blog/archives/115)

## <a name="kps"></a> [Longest Palindromic Substring](Longest_Palindromic_Substring/LPS.py)
This is a realization of the Manacher’s algorithm, which takes `O(n)` time to find the longest palindromic substring in a string `s` where `n` is the length of `s`.

#### Example
```python
s = "abababababac"    
print(longestPalindrome(s))
```
The output is

```python
abababababa
```

#### Reference

1. [Longest Palindromic Substring Part II](https://articles.leetcode.com/longest-palindromic-substring-part-ii/)
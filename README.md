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
#### Description
AVL tree is a balanced searching binary tree.

#### Example
First we create a tree using following code:

```python
a = [6, 4, 7, 3, 5, 1, 2]
t = AVLTree()

for i in a:
    t.put(i)
    t.printSelf(t.root)
    print()
```
The output is

```python
6 None None # 6

6 4 None    #  ___6
4 None None # |
            # 4

6 4 7       #  ___6___
4 None None # |       |
7 None None # 4       7

6 4 7       #      ___6___
4 3 None    #     |       |
3 None None #  ___4       7
7 None None # |
            # 3

6 4 7       #      ___6___
4 3 5       #     |       |
3 None None #  ___4__     7
5 None None # |      |
7 None None # 3      5

4 3 6       #      ___4___
3 1 None    #     |       |
1 None None #  ___3     __6___
6 5 7       # |        |      |
5 None None # 1        5      7
7 None None #

4 2 6       #      ___4___
2 1 3       #     |       |
1 None None #  ___2__   __6___
3 None None # |      | |      |
6 5 7       # 1      3 5      7
5 None None #
7 None None #
```

Now we try to delete some elements from the tree:

```python
t.delete(6)
t.printSelf(t.root)
print()
t.delete(4)
t.printSelf(t.root)

```
The output is

```python
4 2 7       #      ___4___
2 1 3       #     |       |
1 None None #  ___2__   __7
3 None None # |      | |
7 5 None    # 1      3 5
5 None None #

5 2 7       #      ___5___
2 1 3       #     |       |
1 None None #  ___2__     7
3 None None # |      |
7 None None # 1      3
```

#### Reference

1. [Python与数据结构[3] -> 树/Tree[2] -> AVL 平衡树和树旋转的 Python 实现](https://www.imuo.com/a/b7397a6344a573df676260358fdbca9cc0ae60ec0a9df33318e028cd5902c991)
2. [AVL树的python实现](https://www.cnblogs.com/linxiyue/p/3659448.html)
3. [[Python算法实现]AVL Tree](https://zhuanlan.zhihu.com/p/32336678)

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
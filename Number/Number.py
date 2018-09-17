class Number(object):
    """This is a class for arbitrary long size integers

    Attributes:
        data: [int] A list of ints storing the value of this number
        sign: {-1, 0, 1} The sign of this number
        is_infinity: {True/False} A True/False value indicating whether this is infinity
        block_size = The size of an item in data 
        decimal =  The maximum value of an item in data

    """
    def readString(self, s):
        """Initialize the number with a string s. s is either a string of number, 'inf' or '-inf'"""
        # if the string is inf or -inf, then we create an Infinity
        if s == 'inf':
            self.__data = []
            self.__is_infinity = True
            self.__sign = 1
            return
        elif s == '-inf':
            self.__data = []
            self.__is_infinity = True
            self.__sign = -1
            return
        
        self.__is_infinity = False
        # if the string is a zero
        if s == '0':
            self.__sign = 0
            self.__data = [0]
            return
            
        # get rid of the sign
        if s[0] == '-':
            self.__sign = -1
            new_s = s[1:]
        else:
            self.__sign = 1
            new_s = s
            
        ld = len(new_s) // self.__block_size
        self.__data = [0 for _ in range(ld)]
        
        # the number is stored in reverse order
        ls = len(new_s) 
        for i in range(ld):
            self[i] = int(new_s[(ls - (i + 1) * self.__block_size): (ls - i * self.__block_size)])

        # there may be one more block, depending on the length of new_s
        if ls - ld * self.__block_size != 0:
            self.append(int(new_s[:ls - ld * self.__block_size]))

    def readInt(self, s):
        """Initialize the number with an int"""
        # an int is never Infinity
        self.__is_infinity = False
        
        if s == 0:
            self.__data = [0]
            self.__sign = 0
        else:
            self.__sign = 1 if s > 0 else -1
            new_s = abs(s)
            while new_s > 0:
                self.__data.append(new_s % self.__decimal)
                new_s //= self.__decimal
    
    def __init__(self, data, sign=1, is_infinity=False):
        """ Initial the number with given data type
            
        Args:
            data: it's either a list of the number, or an int, or a string
            sign: (default positive) the sign of the number. +1 for positive number, -1 for negative number and 0 for zero
            is_infinity: (default False) whether this is an infinity. If this is True, the data argument will be ignored
        """
        self.__block_size = 4
        self.__decimal = 10 ** self.__block_size
        
        if is_infinity:
            self.__data = []
            self.__sign = sign
            self.__is_infinity = is_infinity
        elif isinstance(data, list):
            self.__data = data
            self.__sign = sign
            self.__is_infinity = is_infinity
        elif isinstance(data, str):
            self.__data = []
            self.readString(data)
        elif isinstance(data, int):
            self.__data = []
            self.readInt(data)

    def __setSign(self, sign):
        """set the sign of this number"""
        self.__sign = sign

    def flipSign(self):
        """flip the sign of the number"""
        self.__sign = -self.__sign

# Implementing list operation
    def __getitem__(self, index):
        return self.__data[index]

    def __setitem__(self, index, item):
        self.__data[index] = item

    def append(self, item):
        self.__data.append(item)
        
    def __len__(self):
        return len(self.__data)

# Implementing string related operation
    def __str__(self):
        if self.__is_infinity:
            return 'Infinity' if self.__sign == 1 else '-Infinity'
        
        # the data is stored in reverse order, so we start at -1
        result_string = str(self[-1])
        for i in range(len(self) - 1, 0, -1):
            result_string += str(self[i - 1]).zfill(self.__block_size)

        # if it's negative, we have to put negative sign in the front
        if (self.__sign == -1):
            result_string = '-' + result_string
            
        return result_string
        
# Implementing order related properties
    def __isAbsolutelyGreaterThan(self, other):
        # assuming both numbers are finite
        if len(self) == len(other):
            index = len(self.__data) - 1
            while index > 0 and self[index] == other[index]: index -= 1
            return self[index] > other[index]
        else:
            return len(self) > len(other)
        
    def __eq__(self, other):
        if self.__is_infinity and other.__is_infinity:
            return self.__sign == other.__sign
        elif not (self.__is_infinity or other.__is_infinity):
            if self.__sign == other.__sign:
                return self.__data == other.__data
        return False

    def __isAbsolutelyGreaterEqual(self, other):
        return self.__data == other.__data or self.__isAbsolutelyGreaterThan(other)
    
    def __ne__(self, other):
        return not (self == other)

    def __gt__(self, other):
        if self.__is_infinity:
            if other.__is_infinity:
                return (self.__sign > other.__sign)
            else:
                return (self.__sign == 1)
        # now self is not infinity
        elif other.__is_infinity:
            return False
        # now both are not infinity
        elif self.__sign != other.__sign:
            return self.__sign > other.__sign
        # now both have the same sign
        elif self.isPositive():
            return self.__isAbsolutelyGreaterThan(other)
        else:
            return not self.__isAbsolutelyGreaterThan(other)

    def __ge__(self, other):
        return (self > other) or (self == other)
    
    def __lt__(self, other):
        return not self >= other

    def __le__(self, other):
        return not self > other

    def isZero(self):
        return self.__sign == 0

    def isPositive(self):
        return self.__sign > 0

    def isNegative(self):
        return self.__sign < 0

# Implementing + - * // % operations
    def __addition(self, other, sign):
        # assuming both are finite numbers
        length = max(len(self), len(other))
        result = [0 for _ in range(length)]
        
        for i in range(len(self)):
            result[i] += self[i]

        for i in range(len(other)):
            result[i] += other[i]

        for i in range(length - 1):
            if result[i] > self.__decimal:
                result[i + 1] += 1
                result[i] -= self.__decimal
                
        if result[-1] > self.__decimal:
            result[-1] -= self.__decimal
            result.append(1)
            
        return Number(0) if result == [0] else Number(result, sign)

    def __subtraction(self, other, sign):
    # assuming that self >= other
        result = self[:]
        for i in range(len(other), 0, -1):
            result[i - 1] -= other[i - 1]
            
        for i in range(len(result) - 1):
            if result[i] < 0:
                result[i + 1] -= 1
                result[i] += self.__decimal
                
        # delete redundant zeros
        i = len(result)
        while (i > 1) and (result[i-1] == 0): i -= 1
        return Number(0) if result[:i] == [0] else Number(result[:i], sign)

    def __multiplication(self, other):
        """Assume both are finite, return the product of self and other"""
        result = [0 for _ in range(len(self) + len(other))]
        for i in range(len(other)):
            for j in range(len(self)):
                result[i+j] += other[i] * self[j]
        for i in range(len(result)):
            if result[i] > self.__decimal:
                result[i + 1] += int(result[i] / self.__decimal)
                result[i] %= self.__decimal

        return Number(result[:-1], self.__sign * other.__sign) if result[-1] == 0 else Number(result, self.__sign * other.__sign)

    def __add__(self, other):
        if self.__is_infinity:
            if other.__is_infinity:
                if self.__sign != other.__sign:
                    raise(ArithmeticError("Infinity - Infinity is not defined"))
            else:
                return Number([], self.__sign, True)
        # now self is not infinity
        elif other.__is_infinity:
            return Number([], other.__sign, True)
        # now both are not infinity
        elif self.isZero():
            return other
        elif other.isZero():
            return self
        # now both are not zero
        elif self.__sign == other.__sign:
            return self.__addition(other, self.__sign)
        elif self.__sign == 1 and other.__sign == -1:
            if self.__isAbsolutelyGreaterThan(other):
                return self.__subtraction(other, 1)
            else:
                return other.__subtraction(self, -1)
        else:
            if self.__isAbsolutelyGreaterThan(other):
                return self.__subtraction(other, -1)
            else:
                return other.__subtraction(self, 1)

    def __iadd__(self, other):
        return self + other
        
    def __sub__(self, other):
        if self.__is_infinity:
            if other.__is_infinity and self.__sign == other.__sign:
                raise(ArithmeticError("Infinity - Infinity is not defined"))
            else:
                return Number([], self.__sign, True)
        elif other.__is_infinity:
            return Number([], -other.__sign, True)
        # now both are not infinity
        elif self.isZero():
            return other.__setSign(-other.__sign)
        elif other.isZero():
            return self
        # now both are not zero
        elif self.__sign == other.__sign:
            if self.__isAbsolutelyGreaterThan(other):
                return self.__subtraction(other, self.__sign)
            else:
                return other.__subtraction(self, -self.__sign)
        elif self.__sign == 1 and other.__sign == -1:
            return self.__addition(other, self.__sign)
        elif self.__sign == -1 and other.__sign == 1:
            return self.__addition(other, self.__sign)

    def __isub__(self, other):
        return self - other
        
    def __mul__(self, other):
        if self.__is_infinity:
            if other.__sign != 0:
                return Number([], self.__sign * other.__sign, True)
            else:
                raise(ArithmeticError("Infinity * Zero is not defined"))
        # now both are finite
        else:
            return self.__multiplication(other)
        
    def __imul__(self, other):
        return self * other

    def __quotientWithRemainder(self, other): 
        """Assume that self and other are positive, return the quotient q = self // other and the remainder r = self % other"""
        q = []
        r = Number(self[:])

        # if self < other, then the answer is immediate
        if not self.__isAbsolutelyGreaterEqual(other):
            return Number(0), r
        
        # now self > other
        while (r >= other):
            if Number(r[-len(other):]) >= other:
                a = Number(r[-len(other):])
                exponent = len(r) - len(other)
                i = int((r[-1] + 1)/ other[-1])
            else:
                a = Number(r[-len(other) - 1:])
                exponent = len(r) - len(other) - 1
                i = int((r[-1] + 1) * self.__decimal / other[-1])

            while not a.__isAbsolutelyGreaterEqual(other.__multiplication(Number(i))): i -= 1
            q.append(i)
            r = r.__subtraction(other.__multiplication(Number([0 for _ in range(exponent)] + [i])))
        return Number(q[::-1]), r

    def quotientWithRemainder(self, other):
        if other.isZero():
            raise(ArithmeticError("Division by Zero is not defined"))
        elif self.__is_infinity:
            if other.__is_infinity:
                raise(ArithmeticError("Infinity / Infinity is not defined"))
            else:
                return Number([], self.__sign, True), Number(0)
        elif self.isZero() or other.__is_infinity:
            return Number(0), Number(0)
        
        q, r = self.__quotientWithRemainder(other)
        
        if self.__sign != other.__sign:
            q += Number(1)
            q.__setSign(-1)
            
        if self.__sign == -1:
            if other.__sign == 1:
                r = other.__subtraction(r)
            else:
                r.__setSign(-1)
        else:
            if other.__sign == -1:
                r += other
        return q, r

    def __floordiv__(self, other):
        q, r = self.quotientWithRemainder(other)
        return q

    def __mod__(self, other):
        q, r = self.quotientWithRemainder(other)
        return r

    def __imod__(self, other):
        return self % other
        
# END_OF_CLASS

if __name__ == "__main__":
    a = Number(321)
    b = Number(-1234)
    #a.readString(input("a= "))
    #b.readString(input("b= "))
    print(a)
    print(b)
    print(a==b)
    print(a<=b)
    print(a>=b)
    print(a>b)
    print(a<b)
    print(a-b)
    print(a+b)
    print(a*b)
    q, r = a.quotientWithRemainder(b)
    print(q)
    print(r)
    c = Number('-inf')
    print(c>a)
    print(c<a)
    print(c-a)
    print(c+a)
    print(c*a)
    d = Number('inf')
    print(d>c)
    print(d*c)
    print(d-c)
    c.flipSign()
    print(c>d)
    

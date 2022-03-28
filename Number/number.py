class Number(object):
    """This is a class for arbitrary long size integers

    Attributes:
        data:        [int] A list of ints storing the value of this number
        sign:        {-1, 0, 1} The sign of this number
        is_infinite: {True/False} A True/False value indicating whether this is infinity
        block_size:  The size of an item in data 
        decimal:     The maximum value of an item in data

    """
    def read_string(self, data):
        """Initialize the number with a string `data`.
        `data` is either a string representation of a number, `inf`, or `-inf`.
        """
        # if the string is inf or -inf, then we create an Infinity
        if data in {'inf', 'Inf', 'Infinity'}:
            self.__data = []
            self.__is_infinite = True
            self.__sign = 1
            return
        elif data in {'-inf', '-Inf', '-Infinity'}:
            self.__data = []
            self.__is_infinite = True
            self.__sign = -1
            return
        
        self.__is_infinite = False
        # if the string is a zero
        if data == '0':
            self.__sign = 0
            self.__data = [0]
            return
            
        # get rid of the sign
        if data[0] == '-':
            self.__sign = -1
            data = data[1:]
        else:
            self.__sign = 1

        num_of_blocks = len(data) // self.__block_size
        
        # the number is stored in reverse order
        self.__data = [0 for _ in range(num_of_blocks)]
        for i in range(num_of_blocks):
            self[i] = int(data[(len(data) - (i + 1) * self.__block_size): (len(data) - i * self.__block_size)])

        # there may be one more block, depending on the length of `data`
        if len(data) - num_of_blocks * self.__block_size != 0:
            self.append(int(data[:len(data) - num_of_blocks * self.__block_size]))

    def read_int(self, value):
        """Initialize the number with an int"""
        # an int is never Infinity
        self.__is_infinite = False
        
        if value == 0:
            self.__data = [0]
            self.__sign = 0
            return 
        
        
        self.__sign = 1 if value > 0 else -1
        value = abs(value)
        while value > 0:
            self.__data.append(value % self.__decimal)
            value //= self.__decimal
    
    def __init__(self, data, sign=1, is_infinite=False):
        """ Initial the number with given data type
            
        Args:
            data: it's either a list of the number, or an int, or a string
            sign: (default positive) the sign of the number. +1 for positive number, -1 for negative number and 0 for zero
            is_infinite: (default False) whether this is an infinity. If this is True, the data argument will be ignored
        """
        self.__block_size = 4
        self.__decimal = 10 ** self.__block_size
        
        if is_infinite:
            self.__data = []
            self.__sign = sign
            self.__is_infinite = is_infinite
        elif isinstance(data, list):
            self.__data = data
            self.__sign = sign
            self.__is_infinite = is_infinite
        elif isinstance(data, str):
            self.__data = []
            self.read_string(data)
        elif isinstance(data, int):
            self.__data = []
            self.read_int(data)

    def __set_sign(self, sign):
        """set the sign of this number"""
        self.__sign = sign

    def flip_sign(self):
        """flip the sign of the number"""
        self.__sign = -self.__sign

    def get_sign(self):
        return self.__sign

# List operations.
    def __getitem__(self, index):
        return self.__data[index]

    def __setitem__(self, index, item):
        self.__data[index] = item

    def append(self, item):
        self.__data.append(item)
        
    def __len__(self):
        return len(self.__data)

# String related operations.
    def __str__(self):
        if self.is_infinite():
            return 'Infinity' if self.__sign == 1 else '-Infinity'
        
        # The data is stored in reverse order, so start at -1.
        result_string = str(self[-1])
        for i in range(len(self) - 1, 0, -1):
            result_string += str(self[i - 1]).zfill(self.__block_size)

        # If negative, need to put negative sign in the front.
        if (self.get_sign() == -1):
            result_string = '-' + result_string
            
        return result_string
        
# Order related properties.
    def __is_absolutely_greater_than(self, other):
        # assuming both numbers are finite
        if len(self) == len(other):
            index = len(self.__data) - 1
            while index > 0 and self[index] == other[index]: index -= 1
            return self[index] > other[index]
        else:
            return len(self) > len(other)
        
    def __eq__(self, other):
        if self.is_infinite() and other.is_infinite():
            return self.get_sign() == other.get_sign()
        elif not (self.is_infinite() or other.is_infinite()):
            if self.get_sign() == other.get_sign():
                return self.__data == other.__data
        return False

    def __is_absolutely_greater_than_or_equal_to(self, other):
        return self.__data == other.__data or self.__is_absolutely_greater_than(other)
    
    def __ne__(self, other):
        return not (self == other)

    def __gt__(self, other):
        if self.is_infinite():
            if other.is_infinite():
                return (self.get_sign() > other.get_sign())
            else:
                return (self.get_sign() == 1)
        # now self is not infinity
        elif other.is_infinite():
            return False
        # now both are not infinity
        elif self.get_sign() != other.get_sign():
            return self.get_sign() > other.get_sign()
        # now both have the same sign
        elif self.is_positive():
            return self.__is_absolutely_greater_than(other)
        else:
            return not self.__is_absolutely_greater_than(other)

    def __ge__(self, other):
        return (self > other) or (self == other)
    
    def __lt__(self, other):
        return not self >= other

    def __le__(self, other):
        return not self > other

    def is_zero(self):
        return self.get_sign() == 0

    def is_positive(self):
        return self.get_sign() > 0

    def is_negative(self):
        return self.get_sign() < 0

    def is_infinite(self):
        return self.__is_infinite

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
                result[i + j] += other[i] * self[j]
        for i in range(len(result)):
            if result[i] > self.__decimal:
                result[i + 1] += int(result[i] / self.__decimal)
                result[i] %= self.__decimal

        return Number(result[:-1], self.get_sign() * other.get_sign()) if result[-1] == 0 else Number(result, self.get_sign() * other.get_sign())

    def __add__(self, other):
        if self.is_infinite() or other.is_infinite():
            if self.is_infinite() and other.is_infinite() and self.get_sign() != other.get_sign():
                raise(ArithmeticError("Infinity - Infinity is not defined"))
            if self.is_infinite():
                return self
            return other
        
        # From here, both are not infinite
        if self.is_zero():
            return other
       
        if other.is_zero():
            return self

        # From here, both are not zero
        if self.get_sign() == other.get_sign():
            return self.__addition(other, self.get_sign())
        
        if self.get_sign() == 1 and other.get_sign() == -1:
            if self.__is_absolutely_greater_than(other):
                return self.__subtraction(other, sign=1)
            return other.__subtraction(self, sign=-1)
        
        if self.__is_absolutely_greater_than(other):
            return self.__subtraction(other, sign=-1)
            
        return other.__subtraction(self, sign=1)

    def __iadd__(self, other):
        return self + other
        
    def __sub__(self, other):
        if self.is_infinite() or other.is_infinite():
            if self.is_infinite() and other.is_infinite() and self.get_sign() == other.get_sign():
                raise(ArithmeticError("Infinity - Infinity is not defined"))
            if self.is_infinite():
                return self
            return Number(data=[], sign=-other.get_sign(), is_infinite=True)

        # now both are not infinity
        if self.is_zero():
            return other.flip_sign()

        if other.is_zero():
            return self

        # now both are not zero
        if self.get_sign() == other.get_sign():
            if self.__is_absolutely_greater_than(other):
                return self.__subtraction(other, self.get_sign())
            return other.__subtraction(self, -self.get_sign())

        if self.get_sign() == 1 and other.get_sign() == -1:
            return self.__addition(other, self.get_sign())
        
        return self.__addition(other, self.get_sign())

    def __isub__(self, other):
        return self - other
        
    def __mul__(self, other):
        if self.is_infinite() or other.is_infinite():
            if self.is_zero() or other.is_zero():
                raise(ArithmeticError("Infinity * Zero is not defined"))
      
            return Number(data=[], sign=self.get_sign() * other.get_sign(), is_infinite=True)

        return self.__multiplication(other)
        
    def __imul__(self, other):
        return self * other

    def __quotient_with_remainder(self, other): 
        """Assume that self and other are positive, return the quotient q = self // other and the remainder r = self % other"""
        q = []
        r = Number(self[:])

        # if self < other, then the answer is immediate
        if not self.__is_absolutely_greater_than_or_equal_to(other):
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

            while not a.__is_absolutely_greater_than_or_equal_to(other.__multiplication(Number(i))): i -= 1
            q.append(i)
            r = r.__subtraction(other.__multiplication(Number([0 for _ in range(exponent)] + [i])), sign=1)
        return Number(q[::-1]), r

    def quotient_with_remainder(self, other):
        if other.is_zero():
            raise(ArithmeticError("Division by Zero is not defined"))
        
        if self.is_infinite():
            if other.is_infinite():
                raise(ArithmeticError("Infinity / Infinity is not defined"))
            return self, Number(0)
        
        if self.is_zero() or other.is_infinite():
            return Number(0), Number(0)
        
        q, r = self.__quotient_with_remainder(other)
        
        if self.get_sign() != other.get_sign():
            q += Number(1)
            q.__set_sign(-1)
            
        if self.get_sign() == -1:
            if other.get_sign() == 1:
                r = other.__subtraction(r)
            else:
                r.__set_sign(-1)
        else:
            if other.get_sign() == -1:
                r += other
        return q, r

    def __floordiv__(self, other):
        q, r = self.quotient_with_remainder(other)
        return q

    def __mod__(self, other):
        q, r = self.quotient_with_remainder(other)
        return r

    def __imod__(self, other):
        return self % other
        
# END_OF_CLASS

if __name__ == "__main__":
    print(Number(123) % Number("inf"))
    

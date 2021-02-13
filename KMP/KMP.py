class KMP(object):
    def __init__(self, pattern):
        self.__previousattern = pattern
        self.__length = len(pattern)
        self.__previous = [0 for _ in range(len(pattern))]
        self.__findPreviousPosition()

    def __findPreviousPosition(self):
        self.__previous[0] = -1
        j = -1
        for i in range(1, self.__length):
            # keep going back until we find a match or we hit the begining
            while j > -1  and self.__previousattern[j + 1] != self.__previousattern[i]: j = self.__previous[j]
            # if it's a match, extend j by 1
            if self.__previousattern[j + 1] == self.__previousattern[i]: j+= 1
            # assgin j to p[i]
            self.__previous[i] = j

    def findMatch(self, string):
        match_position = []
        j = -1
        for i in range(len(string)):
            while j > -1 and self.__previousattern[j + 1] != string[i]: j = self.__previous[j]
            if self.__previousattern[j + 1] == string[i]: j += 1
            if j == self.__length - 1:
                match_position.append(i - self.__length + 1)
                j = self.__previous[j]
        return match_position

    def printSelf(self):
        print(self.__previous)

if __name__ == "__main__":
    kmp = KMP("ababa")
    s = "abababababcbabababd"
    l = kmp.findMatch(s)
    for i in l:
        print(str(i) + ": " + s[i: i+5])

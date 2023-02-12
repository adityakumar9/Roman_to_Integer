# Roman to Integer
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
import time

Rom = list(input("Enter a Roman value: ").upper())
value = []
Val = []
Sort = 0

class Roman_Integer:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def romIntRule(self):
        for i in range(len(self.a)):
            if self.a[i] == 'I':
                value.append(1)
                print(self.a[i], end="")
            elif self.a[i] == 'V':
                value.append(5)
                print(self.a[i], end="")
            elif self.a[i] == 'X':
                value.append(10)
                print(self.a[i], end="")
            elif self.a[i] == 'L':
                value.append(50)
                print(self.a[i], end="")
            elif self.a[i] == 'C':
                value.append(100)
                print(self.a[i], end="")
            elif self.a[i] == 'D':
                value.append(500)
                print(self.a[i], end="")
            elif self.a[i] == 'M':
                value.append(1000)
                print(self.a[i], end="")

# The numeral for four is not (IIII). Instead, the number four is written as (IV).
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
# IV=4, IX=9, XL=40, XC=90, CD=400, CM=900

    def romIntSortAdd(self, c):
        self.c = c
        for j in range(len(value)):
            #print(value[j])
            if j > 0 and value[j] > value[j - 1]:
                Val.append(value[j] - 2* value[j - 1])
            else:
                Val.append(value[j])
        print("\n",Val)
        for k in range(len(Val)):
            self.c += Val[k]
        if self.c >= 4000:
            print("Out of range")
        else:
            print("\n",self.c)

Rom_Int = Roman_Integer(Rom, value)
Rom_Int.romIntRule()
Rom_Int.romIntSortAdd(Sort)

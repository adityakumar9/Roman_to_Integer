Rom = list(input("Enter a Roman value: ").upper())
Val = []
Result = 0
roman= {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,}

class romanInteger:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def romToInt(self):

        for i in range(len(Rom)):
            if i > 0 and roman[Rom[i]] > roman[Rom[i-1]]:
                Val.append(roman[Rom[i]] - 2 * roman[Rom[i-1]])
            else:
                Val.append(roman[Rom[i]])
        #print(Val)
        for j in range(len(Val)):
            self.b += Val[j]
        if self.b >= 4000:
            print("Out of range")
        else:
            print(self.b)

Romint = romanInteger(Rom, Result)
Romint.romToInt()

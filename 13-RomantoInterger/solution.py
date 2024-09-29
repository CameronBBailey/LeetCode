class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        for i in range(1,len(s)+1):
            if s[-i] == 'I':
                value += 1
            elif s[-i] == 'V':
                if (i+1) < len(s) + 1:
                    if s[-(i+1)] == "I":
                        value += 3 
                    else:
                        value += 5
                else:
                    value += 5
            elif s[-i] == 'X':
                if (i+1) < len(s) + 1:
                    if s[-(i+1)] == "I":
                        value += 8 
                    else:
                        value += 10
                else:
                     value += 10
            elif s[-i] == 'L':
                if (i+1) < len(s) + 1:
                    if s[-(i+1)] == "X":
                        value += 30 
                    else:
                        value += 50
                else:
                     value += 50
            elif s[-i] == 'C':
                if (i+1) < len(s) + 1:
                    if s[-(i+1)] == "X":
                        value += 80 
                    else:
                        value += 100
                else:
                     value += 100
            elif s[-i] == 'D':
                if (i+1) < len(s) + 1:
                    if s[-(i+1)] == "C":
                        value += 300 
                    else:
                        value += 500
                else:
                     value += 500
            elif s[-i] == 'M':
                if (i+1) < len(s) + 1:
                    if s[-(i+1)] == "C":
                        value += 800 
                    else:
                        value += 1000
                else:
                     value += 1000
        return value
  
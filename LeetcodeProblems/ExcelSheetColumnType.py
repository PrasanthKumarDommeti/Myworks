def convertToTitle(self, columnNumber: int) -> str:
        res =""
        while columnNumber>0:
            # To get th current value of the character you need subtract 1 from present and perform % div with 26
            res=chr(ord('A')+(columnNumber-1)%26)+res
            # You can change it into character by perform floor division
            columnNumber = (columnNumber-1)//26
        return res
input : 701
output : "ZY"
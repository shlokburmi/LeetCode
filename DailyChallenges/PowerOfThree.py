#1780. Check if Number is a Sum of Powers of Three
def checkPowersOfThree(self, n):
        while n>1:
            n,r=divmod(n,3)      # r=nmod3  (divmod divides and then takes it as power of 3)
            if r==2:
                return False
        return True   
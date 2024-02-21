class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        #convert to binary and then strings with leading zeros
        lb = str(bin(left)[2:].zfill(31))
        rb = str(bin(right)[2:].zfill(31))

        #match the pattern in left and right and add trailing zeros
        res = ""

        for i in range(len(lb)):
            if lb[i]!=rb[i]:
                break
            else:
                res += lb[i]
                
        if len(res)<len(lb):
            for i in range(len(lb)-len(res)):
                res+="0"
        
        return int(res, 2)
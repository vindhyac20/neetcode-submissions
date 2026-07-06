class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        x_str=str(abs(x))
        rev_num=int(x_str[::-1])
        rev_num=sign*rev_num
        if rev_num < -2**31 or rev_num > 2**31:
            return 0
        else:
            return rev_num


        
        
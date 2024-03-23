//The problem is to find the rightmost bit of a non-negative number 'N' that is currently unset (i.e., has a value of 0) in its binary representation and set it to 1.

//Return the number after setting the rightmost unset bit of 'N'. If there are no unset bits in N's binary representation, then the number should remain unchanged.

def setBits(N : int) -> int:
    # Write your code here.
    # if N|(N+1) == N+N+1:
    #     return  N
    # else:
    #     return N | (N+1)
    ans= N
    while N&1!=0:
        N=N>>1
    if(N==0):
        return ans
    else:
        return ans|(ans+1)


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=str(n)
        s=list(s)
        r=len(s)-2

        while r>=0:
            if s[r]<s[r+1]:
                break
            r-=1
        if r==-1:
            return -1
        i=len(s)-1
        while True:
            if s[i]>s[r]:
                break
            i-=1
        t=s[r]
        s[r]=s[i]
        s[i]=t
        s[r+1:]=reversed(s[r+1:])
        ret=int(''.join(s))
        return ret if ret < 1<<31 else -1            
        
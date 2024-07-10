class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.num = []

        for i, n in enumerate(nums):
            if n:
                self.num.append((i,n))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        dotProd = 0
        i = j = 0

        while i < len(self.num) and j < len(vec.num):
            i_dx, i_num = self.num[i]
            j_dx, j_num = vec.num[j]

            if i_dx == j_dx:
                dotProd += i_num * j_num
                i += 1
                j += 1
            elif i_dx > j_dx:
                j += 1
            else:
                i += 1
        return dotProd        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
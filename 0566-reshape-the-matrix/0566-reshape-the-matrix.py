class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        #예외처리
        if m * n != r * c:
            return mat
        
        #mat to list
        elements = []
        for i in mat:
            for element in i:
                elements.append(element)

        result = []
        idx = 0
        for _ in range(r):
            temp = []
            for _ in range(c):
                temp.append(elements[idx])
                idx += 1
            result.append(temp[:]) 

        return result

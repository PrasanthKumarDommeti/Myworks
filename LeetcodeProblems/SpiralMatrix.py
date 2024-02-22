def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l=[]
        while matrix:
            l.extend(matrix.pop(0))
            matrix = [*zip(*matrix)][::-1]
        return l

input : [[1,2,3],[4,5,6],[7,8,9]]
output : [1,2,3,6,9,8,7,4,5]
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # remove matrix[0] list and add its values to the result
        # remove matrix[i][-1] values from the and add them to the result
        # remove matrix[-1][i] (in reverse) values and add them to the result
        # repeat until matrix is not empty
        result = []

        while matrix and matrix[0]:
            for num in matrix[0]:
                result.append(num)
            matrix.pop(0)

            if not matrix or not matrix[0]:
                break

            for row in range(len(matrix)):
                result.append(matrix[row][-1])
                matrix[row].pop()

            if not matrix or not matrix[0]:
                break

            for col in range(len(matrix[0]) - 1, -1, -1):
                result.append(matrix[-1][col])
            matrix.pop()

            if not matrix or not matrix[0]:
                break

            for row in range(len(matrix) - 1, -1, -1):
                result.append(matrix[row][0])
                matrix[row].pop(0)

        return result
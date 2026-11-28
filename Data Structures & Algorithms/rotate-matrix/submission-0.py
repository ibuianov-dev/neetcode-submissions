class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top = left
                bottom = right

                # save left top
                temp_1 = matrix[top][left + i]

                # Bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # Bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # Top right to left top
                matrix[top + i][right] = temp_1

            left += 1
            right -= 1

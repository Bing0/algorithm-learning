class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        result = 0

        m = len(matrix)
        n = len(matrix[0])

        calc_list = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                calc_list[i][j] = calc_list[i - 1][j] + calc_list[i][j - 1] - calc_list[i - 1][j - 1] + matrix[i - 1][
                    j - 1]

        for r1 in range(1, m + 1):
            for r2 in range(r1, m + 1):
                sum_dict = {0: 1}

                for col in range(1, n + 1):
                    total = calc_list[r2][col] - calc_list[r1 - 1][col]

                    to_find = total - target
                    result += sum_dict.get(to_find, 0)

                    sum_dict[total] = sum_dict.get(total, 0) + 1

        return result

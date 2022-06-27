from bisect import bisect_left

def neighborhood(nums: list[int]) -> list[list[int]]:
    result = []
    ordered = [(nums[0], 0)]

    def find_from_left(index):
        if index == 0:
            return None, None
        index -= 1
        value, ind = ordered[index]
        index -= 1
        while index >= 0:
            tmp_val, tmp_ind = ordered[index]
            if tmp_val != value:
                break
            if tmp_ind < ind:
                ind = tmp_ind
            index -= 1
        return value, ind

    def find_from_right(index):
        if index == len(ordered):
            return None, None

        value, ind = ordered[index]
        index += 1
        while index < len(ordered):
            tmp_val, tmp_ind = ordered[index]
            if tmp_val != value:
                break
            if tmp_ind < ind:
                ind = tmp_ind
            index += 1
        return value, ind

    for index, num in enumerate(nums[1:]):
        index += 1
        print(index, num)
        new_item = (num, index)
        index = bisect_left(ordered, new_item)

        value_left, index_left = find_from_left(index)
        value_right, index_right = find_from_right(index)

        if value_left is None or value_right is None:
            if value_left is None:
                close = [abs(value_right - num), index_right + 1]
            else:
                close = [abs(value_left - num), index_left + 1]
            result.append(close)
        else:
            left_dis = abs(value_left - num)
            right_dis = abs(value_right - num)
            if left_dis < right_dis:
                result.append([left_dis, index_left + 1])
            elif left_dis > right_dis:
                result.append([right_dis, index_right + 1])
            else:
                if index_left < index_right:
                    result.append([right_dis, index_left + 1])
                else:
                    result.append([right_dis, index_right + 1])

        ordered.insert(index, new_item)

    return result

# if __name__ == '__main__':
#     k = [5, 1, 7, 4, 2, 7, 10]
#     print(neighborhood(k))

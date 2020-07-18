def has_negatives(a):
    """
    YOUR CODE HERE
    """
    num_cache = {}
    pos_num_list = []

    for num in a:
        num_cache[num] = 1
        if num is not 0 and num * -1 in num_cache:
            pos_num_list.append(abs(num))

    return pos_num_list


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

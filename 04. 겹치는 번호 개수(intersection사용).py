def count_matching_numbers(list_1, list_2):
    same_numbers = list(set(list_1).intersection(list_2))
                                    #이거는 리스트에서 교집합intersection 함수 사용..
    return len(same_numbers)

print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40],[14]))


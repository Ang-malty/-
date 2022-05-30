from random import randint


def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        new_number = randint(1, 45)
        if new_number not in numbers:
            numbers.append(new_number)

    return numbers


def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

def count_matching_numbers(numbers, winning_numbers):
                #numbers라는 리스트와 winnin_numbers라는 리스트를 변수로
    count = 0  #겹치는 숫자개수 0으로 시작
    for num in numbers: #numbers의 리스트값을 num으로 지정
        if num in winning_numbers:  #지정된 num이 winning_numbers 리스트에 있으면
            count = count + 1   #카운트 +1
    return count

def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])
    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return  50000000
    elif count == 5:
        return 100000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

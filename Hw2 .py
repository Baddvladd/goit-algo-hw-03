import random

def get_numbers_ticket(min_value, max_value, quantity):
    if not (1 <= min_value <= max_value <= 1000) or not (0 < quantity <= (max_value - min_value + 1)):
        return []
    return sorted(random.sample(range(min_value, max_value + 1), quantity))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Вашi лотерейнi числа:", lottery_numbers)

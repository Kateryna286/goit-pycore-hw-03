import random

def get_numbers_ticket(min, max, quantity):

    if min >=1 and max <= 1000 and min < max and quantity > 0 and quantity <= (max - min + 1):
        numbers_set = list(range(min, max + 1))

        vinner_set = random.sample(numbers_set, quantity)
        vinner_set.sort()
        return vinner_set
    else:
        return []

# print(get_numbers_ticket(1, 49, 6))
# print(get_numbers_ticket(-1, 1001, 100))
# print(get_numbers_ticket(1, 49, 0))
# print(get_numbers_ticket(50, 49, 6))
# print(get_numbers_ticket(1, 49, 50))
# print(get_numbers_ticket(1, 2, 2))
print(get_numbers_ticket(10, 11, 6))
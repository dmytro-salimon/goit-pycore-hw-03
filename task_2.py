import random

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000 and min < max and 1 <= quantity <= (max - min + 1):
        return sorted(random.sample(range(min, max + 1), quantity))
    return []

if __name__ == "__main__":
    print(get_numbers_ticket(1, 49, 6))
    print(get_numbers_ticket(1, 36, 5))
    print(get_numbers_ticket(1, 1000, 1005))
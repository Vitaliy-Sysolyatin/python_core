import random


def generate_login():
    users = ["tim", "vitaliy", "sasha", "maria"]
    name = random.choice(users)
    number = random.randint(1, 999)

    return f"{name}_{number}"


def generate_age():
    return random.randint(18, 60)


def generate_status():
    statuses = ["ACTIVE", "BLOCKED", "INACTIVE"]

    return random.choice(statuses)


def generate_user():
    user = {"login": generate_login(), "age": generate_age(), "status": generate_status()}

    return user
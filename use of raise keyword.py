def withdraw(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    print("Withdrawal:", amount)

withdraw(-500)

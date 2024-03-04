def add_to_receipt(receipt):
    return receipt * 1.15


print("Введіть кіл-сть друзів: ")
friends = int(input())
print("Введіть суму рахунку: ")
receipt = float(input())
new_receipt = add_to_receipt(receipt)
print("Кожен друг повинен сплатити: ",round(new_receipt/friends,2))

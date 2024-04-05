def input_tickets_sold():
    # Функция для ввода количества проданных билетов на каждый класс мест
    tickets_sold_A = int(input("Введите количество проданных билетов класса A: "))
    tickets_sold_B = int(input("Введите количество проданных билетов класса B: "))
    tickets_sold_C = int(input("Введите количество проданных билетов класса C: "))
    return tickets_sold_A, tickets_sold_B, tickets_sold_C

def calculate_revenue(tickets_sold_A, tickets_sold_B, tickets_sold_C, price_A, price_B, price_C):
    # Функция для расчета дохода от продажи билетов на каждый класс и в целом
    revenue_A = tickets_sold_A * price_A
    revenue_B = tickets_sold_B * price_B
    revenue_C = tickets_sold_C * price_C
    total_revenue = revenue_A + revenue_B + revenue_C
    return revenue_A, revenue_B, revenue_C, total_revenue

# Ввод цен на билеты для каждого класса
price_A = float(input("Введите цену билета класса A: "))
price_B = float(input("Введите цену билета класса B: "))
price_C = float(input("Введите цену билета класса C: "))

# Ввод количества проданных билетов для каждого класса
tickets_sold_A, tickets_sold_B, tickets_sold_C = input_tickets_sold()

# Расчет дохода от продажи билетов для каждого класса и в целом
revenue_A, revenue_B, revenue_C, total_revenue = calculate_revenue(tickets_sold_A, tickets_sold_B, tickets_sold_C, price_A, price_B, price_C)

# Вывод результатов
print(f"Доход от продажи билетов класса A: {revenue_A} грн")
print(f"Доход от продажи билетов класса B: {revenue_B} грн")
print(f"Доход от продажи билетов класса C: {revenue_C} грн")
print(f"Общий доход: {total_revenue} грн")

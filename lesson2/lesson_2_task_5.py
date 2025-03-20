n = int(input("Введите номер месяца: "))
def month_to_season(month):
    if month in [12, 1, 2]:
        return "зима"
    elif 3 <= month <= 5:
        return "весна"
    elif 6 <= month <= 8:
        return "лето"
    elif 9 <= month <= 11:
        return "осень"
    else:
        return "Некорректный номер месяца"
print(month_to_season(n))
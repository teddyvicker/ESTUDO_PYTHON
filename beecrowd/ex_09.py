nome = input()
sal_fixo = float(input())
qt_devendas = float(input())
bonus = float(qt_devendas * (15/100))
total = sal_fixo + bonus
print("TOTAL = R$ %0.2f" %total)
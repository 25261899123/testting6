"""Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...). Программа
должна быть эффективной и не выполнять лишних действий!
"""
Spisoks = ["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"]

print(Spisoks)

for index, spisok in enumerate(Spisoks,0):
     if index % 2 == 0 :
        print ([index],spisok)
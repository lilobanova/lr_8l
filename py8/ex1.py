#!/usr/bin/env python3
# -*- coding: utf-8 -*-

A = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
# Запрос к вводу названия дня недели
day = str(input("Enter day: "))
# Корректно вычислить индекс
if day in A:
    # проверка, есть ли строка day в кортеже A
    num = A.index(day)
    print("Number of day = ", num + 1)
else:
    num = -1
    print("Wrong day.")

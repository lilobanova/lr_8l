#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    a = tuple(int(i) for i in input().split())
    k = a.count(a[0])
    a_rev = tuple(reversed(a))
    idx = a_rev.index(a[0])
    a_sliced = a_rev[0:idx]
    print(f"Количество равных элементов: {k}")
    print("Оставшиеся элементы после последнего из них: "
          f"{tuple(reversed(a_sliced))}"
    )

def is_score(lst) -> bool:
    lst.sort(reverse=True)
    while lst and lst[-1] > 0:
        k = lst.pop()
        if k > len(lst):
            return False
        else:
            for i in range(k):
                lst[i] -= 1
            lst.sort(reverse=True)
    return True


# vstup = input("Vlozte vstup oddeleny ciarkami: ")
# vstup = vstup.split(",")
# vstup = [int(x) for x in vstup]

vstup = [2, 2, 2, 3, 3, 4]

print(is_score(vstup))

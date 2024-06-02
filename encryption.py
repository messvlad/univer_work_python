def bin_counter():
    def first_exercise():
        print("1)", int("1100111", 2))
        return

    def from_second_to_third_exercise():
        first_number = int("124", 8)
        second_number = int("31", 8)

        print("2)", f"{first_number},{second_number}")
        first_number = int("-1A120 ", 16)
        second_number = int("34", 16)

        print("3)", f"{first_number},{second_number}")
        first_number = int("74", 9)
        second_number = int("213", 4)
        third_number = int("1A", 16)
        fourth_number = int("45", 6)

        print("Вычисления 4 задания")
        mas = []
        mas.append(first_number)
        mas.append(second_number)
        mas.append(third_number)
        mas.append(fourth_number)

        print(mas)
        mas.sort()
        print(mas)

        print("4)", "1A^16, 45^6, 213^4, 74^9")
        print("5)", bin(41)[2:])
        print("6)", hex(122)[2:])

        #Сегодня 02.09.23 <ГГ>,<ММ>=23,09
        first_number = hex(23)[2:]
        second_number = hex(9)[2:]
        print("7)", f"{first_number},{second_number}")
        return

    first_exercise()
    from_second_to_third_exercise()
    return


bin_counter()

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    j = 0
    index = 0
    while(1):
        try:
            list_length = my_list_1[i] / my_list_2[j]
            print(f"{list_length}")
        except (ValueError, TypeError):
            print("wrong type")
            list_length = 0
            pass
        except ZeroDivisionError:
            print("division by 0")
            list_length = 0
            pass
        except IndexError:
            if (i < len(my_list_1)):
                if (j < len(my_list_2)):
                    print("out of range")
                    list_length = 0
            break
        i += 1
        j += 1
        index += 1

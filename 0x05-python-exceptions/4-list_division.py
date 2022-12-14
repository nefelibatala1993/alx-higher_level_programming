#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i, aux = 0, 0
    new_list = []
    while i < list_length:
        try:
            aux = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(aux)
            aux = 0
            i += 1
    return new_list

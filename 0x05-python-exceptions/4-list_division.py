#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        result = 0
        try:
            if type(my_list_1[i]) not in (int, float) or type(my_list_2[i]) not in (int, float):
                raise TypeError("wrong type")
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError as e:
            print(e)
        finally:
            result_list.append(result)

    return (result_list)

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:

            # Raise an IndexError if the index is out of range
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            # Try to divide corresponding elements, if they exist
            num1 = my_list_1[i] if i < len(my_list_1) else 0
            num2 = my_list_2[i] if i < len(my_list_2) else 0

            # Check for division by 0 and wrong type
            if not all(isinstance(num, (int, float)) for num in (num1, num2)):
                raise TypeError("wrong type")
            if num2 == 0:
                raise ZeroDivisionError("division by 0")

            # Perform division and append the result to the result list
            division_result = num1 / num2
            result.append(division_result)

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass

    return result

def function_tuple(a, b, c, *number_tuple):
    print(str(a) + ", " + str(b) + ", " + str(c) + ", " + str(number_tuple))
    print("Tuple:")
    for n in number_tuple:
        print(n)


def function_dic(a, b, c, *number_list, **value_dic):
    print(str(a) + ", " + str(b) + ", " + str(c) + ", " + str(number_list) + ", " + str(value_dic))
    print("Tuple:")
    for n in number_list:
        print(n)

    print("Dic:")
    for n in value_dic:
        print(n, value_dic[n])


function_tuple(1, 2, 3, 4, 5, 6)
function_dic(1, 2, 3, 4, 5, 6, val1="Hello", val2="world", val3="from python")

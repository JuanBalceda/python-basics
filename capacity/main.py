def main():
    a, b, c = 3, 2, 1
    if a < b:
        print("{} es menor que {}".format(a, b))
    elif c < b:
        print("{} es menor que {}".format(c, b))
    else:
        print("{} es mayor que {}".format(a, b))


if __name__ == '__main__':
    main()

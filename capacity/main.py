def main():
    a, b, c = 3, 2, 1
    if a < b:
        print("{} is less than {}".format(a, b))
    elif c < b:
        print("{} is less than {}".format(c, b))
    else:
        print("{} is grater than {}".format(a, b))

    days = dict(day1="monday", day2="tuesday", day3="wednesday", day4="thursday", day5="friday", day6="saturday",
                day7="sunday")

    today = "day5"
    print(days[today])


if __name__ == '__main__':
    main()

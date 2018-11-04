def main():

        # Conditions
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

        # Loops
        x = 1

        while x < 200:
            if x % 3 == 0:
                print(x)
            x += 1

        for i in range(1, 200):
            if x % 3 == 0:
                print(x)
            x += 1

        x = "This is a text chain"
        for i, c in enumerate(x):
            print(i, c)

        for r in x:
            if r == 'a':
                print(r, end=' ')
            else:
                print("Not found.")



if __name__ == '__main__':
    main()

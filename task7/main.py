def get_max_candies(pinatas):
    n = len(pinatas)
    pinatas = [1] + pinatas + [1]
    ind_l = 0
    ind_r = 0
    max_candies = 0
    sum_candies = 0
    while n > 0:
        for i in range(1, n + 1):
            candies = pinatas[i - 1] * pinatas[i] * pinatas[i + 1]
            if candies > max_candies:
                max_candies=candies
                ind_l = i - 1
                ind_r = i + 1
        del pinatas[ind_l : ind_r + 1]
        n -= 3
        print(max_candies)
        sum_candies += max_candies
        max_candies=0

    return sum_candies


def main():
    input_str = input("Input array of pinatas with candies separate with space: ")
    pinatas = list(map(int, input_str.split(" ")))
    res=get_max_candies(pinatas)
    print(f"Max candies: {res}")
    input("Exit")

if __name__ == "__main__":
    main()

import csv


def read_csv(filename):
    data = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            data[(row[0], row[1])] = True
    return data


if __name__ == "__main__":
    csv_file1 = 'data/day1.csv'
    csv_file2 = 'data/day2.csv'
    day1_data = read_csv(csv_file1)
    day2_data = read_csv(csv_file2)

    in_both_day = {}
    in_second_day = {}

    for key in day2_data:
        if key in day1_data:
            in_both_day[key] = True
        else:
            in_second_day[key] = True

    print("In both days:", in_both_day.keys())
    print("In second day:", in_second_day.keys())
    input("Exit")

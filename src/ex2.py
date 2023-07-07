import csv
from pprint import pprint

file_path = ["../files/week-1.csv", "../files/week-2.csv", "../files/week-3.csv"]

def find_total_visits():
    count = 0
    for file in file_path:
        # print(file)
        with open(file, "r") as csv_file:
            rows = csv.reader(csv_file, delimiter=',')
            next(csv_file)
            for line in csv_file:
                x = line.split(',')
                nums = x[1:]
                for num in nums:
                    real_num = int(num)
                    if real_num == 1:
                        count += 1
    return count


def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()
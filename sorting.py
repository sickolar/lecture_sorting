import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    data = {}
    i = 0
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode = "r") as file_name:
        reader = csv.DictReader(file_name)

        for row in reader:
            for key, value in row.items():
                if i == 0:
                    data[key] = [int(value)]
                else:
                    data[key].append(int(value))
            i = i + 1
        return data


def selection_sort(seznam, direction):
    middle_man = 0
    delka = len(seznam)
    for i in range(delka - 1):
        min = i
        for j in range(i + 1, delka):
            if direction == "vzestupne":
                if seznam[j] < seznam[min]:
                    min = j
            elif direction == "sestupne":
                if seznam[j] > seznam[min]:
                    min = j
            else:
                return print("Spatna direction")
        middle_man = seznam[i]
        seznam[i] = seznam[min]
        seznam[min] = middle_man

    return seznam



def main():
    cus = read_data("numbers.csv")
    seznam = cus["series_1"]
    selection_sort(seznam,"sestupne")
    print(seznam)


if __name__ == '__main__':
    main()

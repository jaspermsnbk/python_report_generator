import csv


class transaction():
    def __init__(self, date, description, amount, trans_type, category, account_name, labels="", notes=""):
        self.date = date
        self.description = description
        self.amount = amount
        self.trans_type = trans_type
        self.category = category
        self.account_name = account_name
        self.labels = labels
        self.notes = notes

    pass


def handle_file():
    filename = input("transactions file to use: ")
    data = []
    skip = True
    with open(filename, "r") as trans:
        reader = csv.reader(trans)
        for l in reader:
            if skip:
                skip = False
                continue
            data.append(
                transaction(l[0], l[1], l[2], float(l[3]), l[4], l[5], l[6], l[7]))
    print(f"${len(data)} transactions were read")
    return data


def main():
    data = handle_file()
    build_report(data)
    return


def build_report(data):
    print(len(data))

    pass


main()

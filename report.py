import csv
from typing import List, Dict


class Transaction():
    positive = ["Income", "Paycheck", "Investments",
                "Transfer", "Returned Purchase", "Reimbursement"]

    def __init__(self, s: str, date: str, description: str, o_description: str, amount: float, trans_type: str, category: str, account_name: str, labels="", notes=""):
        self.date = date
        self.description = description
        self.o_description = o_description
        self.amount = amount
        self.trans_type = trans_type
        self.category = category
        self.account_name = account_name
        self.labels = labels
        self.notes = notes
        self.s = s
        if self.category not in self.positive:
            self.amount *= -1

    def __str__(self) -> str:
        return self.s
    pass


def main():
    data = read_file()
    build_report(data)
    return


def read_file():
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
                Transaction(", ".join([l[0], l[3], l[5]]), l[0], l[1], l[2], float(l[3]), l[4], l[5], l[6], l[7]))
    print(f"{len(data)} transactions were read")
    return data


def build_report(data: list):
    print(len(data))

    months = [[], [], [], [], [], [], [], [], [], [], [], []]
    report = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
    # loop through transactions
    # if month is in the map then append transaction to list
    for t in data:
        month = int(t.date.split("/")[0]) - 1  # get month
        months[month].append(t)  # append transaction to month
    j = 0
    for m in months:
        cur = report[j]
        for t in m:
            if t.category in cur:
                cur[t.category] += t.amount
            else:
                cur[t.category] = t.amount
        j += 1
        pass
    # print report
    z = 1
    for m in report:
        print(z)
        for k, v in m.items():
            print(f"{k}: {v:.2f}")
        z += 1
    return [report, months]


def get_categories(trans: List[Transaction]) -> list:
    res = []
    for t in trans:
        if t.category not in res:
            res.append(t.category)
    d = {}
    i = 0
    for n in res:
        d[n] = i
        i += 1
    return d


main()

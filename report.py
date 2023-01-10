import csv
from typing import List, Dict

MONTHS = ["January", "Feburary", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


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
    [report, months] = build_report(data)
    l = get_categories(months)
    build_csv(l, report, months)
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
            if "total" in cur:
                cur["total"] += t.amount
            else:
                cur["total"] = t.amount
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


def get_categories(trans: List[List[Transaction]]) -> list:
    res = ["total"]
    for m in trans:
        for t in m:
            if t.category not in res:
                res.append(t.category)
    d = {}
    i = 0
    for n in res:
        d[n] = i
        i += 1
    return d


def build_csv(cat_d: Dict[str, int], report: List[Dict[str, float]], months: List[List[Transaction]]):
    final = [[months[0][0].date.split("/")[2]]]
    final[0].extend(MONTHS)
    cat_by_month = []
    for cat, v in cat_d.items():
        l = [cat, "", "", "", "", "", "", "", "", "", "", "", ""]
        cat_by_month.append(l)

    # add numbers
    offset = 1
    for m in report:
        for k, v in m.items():
            cat_by_month[cat_d[k]][offset] = v
        offset += 1

    final.extend(cat_by_month)
    out = open("output.csv", "w")
    wr = csv.writer(out)
    wr.writerows(final)
    out.close()


main()

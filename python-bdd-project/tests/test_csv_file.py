import csv

path = r"tests\loanstatus.csv"

with open(path) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # print(reader)
    name = []
    status = []
    # for row in reader:
    #     name.append(row[0])
    #     status.append(row[1])
    # print(name)
    # print(status)

# Index = name.index('tim')
# LoanStatus = status[Index]
# print(f"Loan status for 'tim': {LoanStatus}")

# To write to a CSV file
with open(path,'a') as wfile:
    write = csv.writer(wfile)
    write.writerow(['Abs', 'rejected'])


'''OPERATORS AND CODES'''
data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []

for i in data:
    if i.isnumeric():
        codes.append(i)
    else:
        designations.append(i)

operators = dict(zip(designations, [{code} for code in codes]))

del operators["Katel"]
del operators["Fonex"]

operators['O!'].update({'0700', '0500'})
operators['Megacom'].update({'0999', '0555'})
operators['Beeline'].update({'0777', '0222'})

for operator, code in operators.items():
    print(f'"operator" - {operator} | "code" - {code}')

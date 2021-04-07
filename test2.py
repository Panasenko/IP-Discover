#!/usr/bin/python3


from prettytable import PrettyTable  # Импортируем установленный модуль.

x = PrettyTable()

x.field_names = ["City name", "Area"]
x.add_rows(
[
    ['ip', '92.222.129.112'],
    ['country', 'France'],
    ['score', 1]
]
)

print(x)

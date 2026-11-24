menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below
for day in range(1, number_of_days + 1):
    row = []
    for menu in menus:
        portion = int(input("Day " + str(day) + ", " + menu + ": "))
        row.append(portion)
    sales.append(row)

# Traversal per baris: total per hari
print("Total per day:")
for i in range(len(sales)):
    day_total = 0
    for j in range(len(sales[i])):
        day_total = day_total + sales[i][j]
    print("Day " + str(i + 1) + ":", day_total)

# Traversal per kolom: total per menu
menu_totals = []
for j in range(len(menus)):
    menu_total = 0
    for i in range(len(sales)):
        menu_total = menu_total + sales[i][j]
    menu_totals.append((menus[j], menu_total))
print("Total per menu:", menu_totals)

# Menu terlaris
best_name = ""
best_total = -1
for name, total in menu_totals:
    if total > best_total:   # pakai ">" agar menu yang muncul lebih dulu dipilih jika sama
        best_name = name
        best_total = total
print("Best seller: " + best_name + " (" + str(best_total) + ")")
menu_data = [
    ('Bruschetta', 'Appetizer', 2.50, 8.50, 150),  # Profit: 900
    ('Steak Frites', 'Main Course', 9.00, 24.00, 200), # Profit: 3000
    ('Caesar Salad', 'Appetizer', 3.00, 10.00, 250), # Profit: 1750
    ('Pasta Carbonara', 'Main Course', 5.50, 18.50, 300),# Profit: 3900
    ('Tiramisu', 'Dessert', 4.00, 9.00, 400)      # Profit: 2000
]


def calculate_total_profit(dish_tuple):
    profit_tabe = []
    for i in dish_tuple:
        name = i[0]
        cat = i[1]
        cost = i[2]
        price = i[3]
        ordered = i[4]
        profit = ((price - cost) * ordered)
        profit_tabe.append((i, profit))
    return profit_tabe

profit = calculate_total_profit(menu_data)

def find_most_profitable_dish(menu_data):
    menu_data.sort()
    profit = 0
    famous_dish = menu_data[0]
    for i in range(len(menu_data)):
        pre_profit = (menu_data[i][3] - menu_data[i][2]) * menu_data[i][4]
        if profit < pre_profit:
            profit = pre_profit
            famous_dish = menu_data[i][0]
    return famous_dish # ,profit

famous_dish = find_most_profitable_dish(menu_data)



def get_dishes_in_category(menu_data, category_name):
    
    same_names = []
    
    for i in range(len(menu_data)):
        if menu_data[i][1] == category_name:
    
            same_names.append(menu_data[i][0])
    
    return same_names
same_category = get_dishes_in_category(menu_data, 'Main Course')



def get_category_popularity(menu_data):
    category_totals = []
    
    for item in menu_data:
        category = item[1]
        order = item[4]
        found = False
        for i in range(len(category_totals)):
            if category_totals[i][0] == category:
                category_totals[i][1] += order
                found = True
                break
        if not found:
            category_totals.append([category, order])

    return category_totals
     

category_tot = get_category_popularity(menu_data)
category_tot.sort()
print((famous_dish, same_category, category_tot  ))
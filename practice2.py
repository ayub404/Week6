votes = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple', 'grape']
# votes = ['apple', 'apple', 'apple', 'banana', 'grape', 'orange', 'orange']
words = ['code', 'sleep', 'eat', 'code', 'repeat', 'eat', 'code', 'sleep']
def get_top_n_frequent(items, n):
    items.sort()
    counts = []
    count = 1
    for i in range(1,len(items)):
        if items[i] == items[i-1]:
            count += 1
        else:
            counts.append((items[i-1], count))
            count = 1
    counts.append((items[-1], count))
    return counts



print('\n\n\n\n\n')


def top_tier(data, n):
    list_num = []
    data = data[:]
    top_tie = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[j][1] > data[i][1]:
                data[i], data[j] = data[j], data[i]
    for i in range(n):
        top_tie.append(data[i][0])
    
    for fruit, count in data:
        list_num.append(f'{fruit} = {count}')
    return list_num, top_tie

result = get_top_n_frequent(votes, 3)
list_result, top_tie = top_tier(result, 2)

     

print(f"Frequencies: {list_result}")
print(f"Top tier: {top_tie}")
print(f"Expected output: {top_tie}")




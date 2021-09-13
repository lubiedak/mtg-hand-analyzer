def count_cost(cost_text):
    cost_list = [cost_text[i:i+3] for i in range(0, len(cost_text), 3)]
    total = 0
    for cost in cost_list:
        cost = cost.replace("{", "").replace("}", "")
        if cost.isnumeric():
            total = total + int(cost)
        else:
            total = total + 1
    return total


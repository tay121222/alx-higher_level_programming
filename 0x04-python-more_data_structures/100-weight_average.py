#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == None:
        return 0

    weight_total_sum = 0
    weight_total = 0

    for score, weight in my_list:
        weight_total_sum += score * weight
        weight_total += weight

    return(weight_total_sum / weight_total)

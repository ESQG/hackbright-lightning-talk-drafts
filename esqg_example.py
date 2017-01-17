def ca_tax(subtotal):
    exact_total = 0.085 * subtotal
    return round(exact_total, 2)

def verify_receipt(number_list, total, tax):
    subtotal = 0
    for num in number_list:
        subtotal += num
    if tax:
        real_total = subtotal + ca_tax(subtotal)
    else:
        real_total = subtotal

    print "Submitted total:", total
    print "Calculated total:", real_total
    print real_total == total

receipts = [
([23.99], 26.03, True),
([5.25, 1.70], 7.56, True)

]
for receipt in receipts:
    print receipt[0]
    verify_receipt(*receipt)
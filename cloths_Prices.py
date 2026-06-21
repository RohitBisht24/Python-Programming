price_shirt  = 400
price_jeans =  700

quantity_shirt = 2
quantity_jeans = 1 

total_shirt = price_shirt * quantity_shirt
total_jeans = price_jeans * quantity_jeans
subtotal = total_shirt + total_jeans
print("Subtotal : ", subtotal)
discount = subtotal * 0.10
final_price = subtotal - discount
print("Final Price with 10% discount : ",final_price)
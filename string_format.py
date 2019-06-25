price = 49
txt = "The price is {} dollars"

print(txt.format(price))

# index numbers

quantity = 3
item_no = 567
pri = 30

myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."

print(myorder.format(quantity, item_no, pri))

#name index

buy = "I have a {dress}, it is of {colour} colour."

print(buy.format(dress = "frock", colour = "pink"))


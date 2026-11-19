prices=[50,20,30,10,40,60,70,80,90,100]
average_price = sum(prices)/len(prices)
result=sorted([p for p in prices if p > average_price],reverse=True)
print(result)
print("Product Prices:", prices)
print("Average Price:", average_price)
print("Prices Above Average:", result)
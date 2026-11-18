price_per_notebook = 45

print("Cost of 7 notebooks:", 7 * price_per_notebook, "rupees")

budget = 500
notebooks = budget // price_per_notebook
print("Notebooks you can buy:", notebooks)

leftover = budget % price_per_notebook
print("Money left over:", leftover, "rupees")
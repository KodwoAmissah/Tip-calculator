Food_charge=float(input("Please enter the charge for food: $"))
amount_on_tip=Food_charge * 18/100
amount_on_sales_tax=Food_charge*7/100
grand_total=Food_charge+amount_on_sales_tax+amount_on_tip
print(f"${Food_charge:.2f}")
print(f"${amount_on_tip:.2f}")
print(f"$ slaes tax={amount_on_sales_tax:2f}")
print(f"$ grand total={grand_total:.2f}")
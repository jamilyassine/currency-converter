exchange_rates={"JPY":140 , "USD":1 , "MAD" :10 , "GBP":0.78 , "EUR":0.91 }
origin_currency=input("Insert the origin currency  :  ")
while(origin_currency.upper().strip() not in exchange_rates.keys()):
    print(f"The currency {origin_currency} is not a valid currency ")
    origin_currency=input(f'Please enter one of the following valid currencies : {", ".join(exchange_rates.keys())}\n')

target_currency=input("Insert the target currency  :  ")
while(target_currency.upper().strip() not in exchange_rates.keys()):
    print(f"The currency {target_currency} is not a valid currency ")
    target_currency=input(f'Please enter one of the following valid currencies : {", ".join(exchange_rates.keys())}\n')


amount=float(input(f"Insert the amount that you want to convert from {origin_currency} to {target_currency}\n"))
converted_amount=amount*(exchange_rates[target_currency.upper().strip()]/exchange_rates[origin_currency.upper().strip()])
print(f"{amount} {origin_currency.upper()}  =  {converted_amount} {target_currency.upper()}")


convert = {
    'USD': 1.00,
    'EUR': 0.84,
    'GBP': 0.72,
    'JPY': 109.98,
    'AUD': 1.33, 
    'CAD' : 1.26,
    'CHF' : 0.92,
    'CNY': 6.46,
    'HKD': 7.76,
    'NZD': 1.43
}

amt = int(input("Enter the amount: "))
src = input("Enter the source currency code(USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, HKD, NZD): ").upper()
trgt = input("Enter the source currency code(USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, HKD, NZD): ").upper()

if (src and trgt) in convert:
    trgt_amt = amt / convert[src] * convert[trgt]
    print(f" {amt} {src} = {trgt_amt} {trgt}")
else:
    print("Invalid source/target curency code. ")
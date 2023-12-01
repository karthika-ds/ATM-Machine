
def credit(amt):
    print("rupees",amt,"is credited")

def debit(amt):
    print("rupees",amt,"is debited")

def credit(amt,total):
    print("Total balance", total)
    print("Amount Credited",amount)
    total = total + amount
    return total

def debit(amt,total):
    print("Total balance", total)
    print("Withdrawal amount",amount)
    print("Amount Debited",amount)
    total = total - amount
    return total

def validate(card,pin):
    if card == "1234" and pin =="5678":
        return "valid"
    elif card !="1234":
        return "card is invalid"
    elif pin !="4321":
        return "pin is invalid"

def bank_details(bank_atm,card,pin):
    print("Welcome to ",bank_atm, "ATM")
    print("INSERT YOUR ATM CARD AND ENTER PIN NUMBER")
    return validate(card,pin)

amount = 10000
limit = 3
total = 40000
bank_atm = "SBI"
card = "1234"
pin = "5678"
Money = 1000

for x in range(3):
    value = bank_details(bank_atm, card, pin)
    if value == "valid":
        total = debit(amount,total)
        print("Balance amount", amount)
        print(value)
    else:
        print(value)
        break
    print("Thanks for using this ATM.")

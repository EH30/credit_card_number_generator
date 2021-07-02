import gen
import random
import datetime

def exp_date():
    out = None
    year = int(datetime.datetime.now().strftime("%Y")) + random.randint(1, 2)
    month = random.randint(1, 12)
    day = random.randint(1, 31)

    while not out:
        try:
            out = datetime.datetime(year, month, day)
        except Exception as err:
            out = None
            day -= 1
    
    return str(out)

def main():
    output = {"Number": None, "type": None, "cvv": None, "pin": None, "IIN": None, "PAN": None, "exp-date": None}
    types = {"1":"v", "2":"m"}
    types_full = {"1":"Visa", "2":"MasterCard"}
    optlist = "1) Visa\n2) MasterCard"
    
    print(optlist)
    user_input = input("Enter: ")
    if user_input.strip() not in ['1','2']:
        print("Invalid Input")
        exit(1)
    
    output["Number"] = gen.GenerateCardNumber().gen_val(types[user_input])
    output["IIN"] = ""
    output["PAN"] = ""

    # The first 6 digits are Issuer Identification Number
    # The last digit is the check digit
    # The numbers that are between the first 6 digits and the last digit
    # is the Personal Account Number  
    for i in range(len(output["Number"])-1):
        if i > 5:
            output["PAN"] += output["Number"][i]
        else:
            output["IIN"] += output["Number"][i]

    output["type"] = types_full[user_input]
    output["cvv"] = "".join([str(random.randint(0, 9)) for i in range(0, 3)])
    output["pin"] = "".join(str(random.randint(0, 4)) for i in range(0, 4))
    output["exp-date"] = exp_date().split(" ")[0]
    print("\n")

    for item in output:
        print(item,":", output[item])

if __name__ == "__main__":
    main()

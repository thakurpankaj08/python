def billCalc():
    print("Welcome to tip calculator")
    totalBill = float(input("what was the total bill? "))
    numberOfPpl = float(input("How many people to split the bill? "))
    tipPercent = float(input("What percentage tip would you like to give? "))

    totalBill = totalBill + totalBill*tipPercent/100.0
    eachPersonShare = totalBill/numberOfPpl

    print("Each person should pay "+ str(round(eachPersonShare,1)))

billCalc()




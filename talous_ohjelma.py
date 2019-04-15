#!/usr/bin/env python3

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Used to prompt user for input.
prompt = "> "
cont = "(Hit RETURN to continue...)"

# Main program runs in a while loop
while True:
    print("\nWhat do you want to do?\n\t(A) Calculate how much your savings cumulate "
        "over time\n\t(B) Calculate your passive income\n\t(C) Calculate ROE for your "
        "investments\n\t(D) Calculate the future value of money\n\t(E) Calculate the "
        "present value of money\n\t(F) Use Gordon equation to calculate the right price"
        " for a stock\n\t(Q) Quit\n\nEnter corresponding letter and press "
        "RETURN.")
    answer = input(prompt).lower()
    if answer == "a":
        print("\nHow much will you save in a year?")
        amount = int(input(prompt))
        print("For how many years will you continue to save?")
        years = int(input(prompt))
        voitto = amount*1.07**5
        for x in range(1, years):
            voitto = voitto+amount*1.07**x
        print(bcolors.OKGREEN + "\nAfter %s years you will have %s €\n" 
            % (years, round(voitto)) + bcolors.ENDC)
        input(cont)
    elif answer == "b":
        print("\nHow much have you invested?")
        vastaus = int(input(prompt))
        v_tulot = vastaus*0.07*0.98
        kk_tulot = v_tulot/12
        tulot = round(kk_tulot*0.7)
        print(bcolors.OKGREEN + "\nYour monthly passive income after taxes is "
            "%s €\n" % tulot + bcolors.ENDC)
        input(cont)
    elif answer == "c":
        print("\nHow much debt?")
        velka = int(input(prompt))
        print("What is the the interest (%) for the debt?")
        velan_korko = float(input(prompt))
        print("How much capital you have invested?")
        oma_paaoma = int(input(prompt))
        print("What is the return (%) for the investment?")
        tuotto = float(input(prompt))
        roe = (((velka + oma_paaoma) * tuotto - (velka * velan_korko)) / 
            oma_paaoma)
        print(bcolors.OKGREEN + "\nYour ROE is %s %%\n" % roe + bcolors.ENDC)
        input(cont)
    elif answer == "d":
        print("\nWhat is the amount of money you have now?")
        pv = int(input(prompt))
        print("Amount of years to wait?")
        yrs = int(input(prompt))
        a = round(pv*(1.02**yrs))
        print(bcolors.OKGREEN + "\nThat will grow to %s € in %s years\n" 
            % (a, yrs) + bcolors.ENDC)
        input(cont)
    elif answer == "e":
        print("\nHow much money do you want to have?")
        fv = int(input(prompt))
        print("In how many years?")
        yrs = int(input(prompt))
        a = round(fv / (1.0175 ** yrs))
        print(bcolors.OKGREEN + "\nThat equals to %s € in todays money\n" 
            % a + bcolors.ENDC)
        input(cont)
    elif answer == "f": # Gordon equation
        print("\nWhat is the dividend for next year?")
        dividend = float(input(prompt))
        print("What is the average dividend growth rate (%) for the last 5"
        " years?")
        dgrowth = float(input(prompt))
        price = round(dividend / (0.1 - dgrowth*0.01))
        print(bcolors.OKGREEN + "\nThe right stock price for that company "
            "is {0} € when calculated using the expected rate of return "
            "of 10 %.\n".format(price) + bcolors.ENDC)
        input(cont)
    elif answer == "q":
        break
    else:
        print(bcolors.WARNING + "\nYou pressed a wrong button, please try "
            "again.\n" + bcolors.ENDC)
        input(cont)
#!/usr/bin/env python3

# NOTE! Replace time delay with a promt to press 'enter' when ready to 
# continue.
import time

# Used to promt user for input.
promt = "> "

# Main program runs in a while loop
while True:
    print("\nWhat do you want to do?\n\t(A) Calculate how much your savings cumulate "
        "over time\n\t(B) Calculate your passive income\n\t(C) Calculate ROE\n"
        "\t(D) Estimate how cheap/expensive a company share is\n\t(E) Future value "
        "of money\n\t(F) Present value of money\n\t(X) Exit\n")
    answer = input("Enter corresponding letter and press enter : ").lower()
    if answer == "a":
        print("\nHow much will you save in a year?")
        amount = int(input(promt))
        print("For how many years will you continue to save?")
        years = int(input(promt))
        voitto = amount*1.07**5
        for x in range(1, years):
            voitto = voitto+amount*1.07**x
        print("\n**********\n")
        print("After "+str(years)+" years you will have "+str(round(voitto))+" €.")
        print("\n**********")
        time.sleep(5)
    elif answer == "b":
        print("\nHow much have you invested?")
        vastaus = int(input(promt))
        v_tulot = vastaus*0.07*0.98
        kk_tulot = v_tulot/12
        tulot = round(kk_tulot*0.7)
        print("\n**********\n")
        print("Your monthly passive income:		    "+str(tulot)+" €")
        print("Monthly passive income before taxes:        "+str(round(kk_tulot))+" €")
        print("\n**********")
        time.sleep(5)
    elif answer == "c":
        print("\nHow much debt?")
        velka = int(input(promt))
        print("What is the the interest (%) for the debt?")
        velan_korko = float(input(promt))
        print("How much capital you have invested?")
        oma_paaoma = int(input(promt))
        print("What is the return (%) for the investment?")
        tuotto = float(input(promt))
        print("\n**********\n")
        print("ROE is: "+str(((velka + oma_paaoma) * tuotto - (velka * velan_korko))
         / oma_paaoma)+" %")
        print("\n**********")
        time.sleep(5)
    elif answer == "d":
        print("\nWhat is the P/E?")
        pe = int(input(promt))
        print("What is the P/Bv?")
        pbv = float(input(promt))
        print("What is the ROE(%)")
        roe = int(input(promt))
        print("\n**********\n")
        if pe * pbv <= 15 and roe >= 15:
            print("Halpaa ku saippua")
        else:
            print("Kallis, älä perkele osta")
        print("\n**********")
        time.sleep(5)
    elif answer == "e":
        print("\nWhat is the amount of money you have now?")
        pv = int(input(promt))
        print("Amount of years to wait?")
        yrs = int(input(promt))
        a = pv*(1.02**yrs)
        print("\n**********\n")
        print("That wil grow to %.2f" % a+" € in "+str(yrs)+" years.")
        print("\n**********")
        time.sleep(5)
    elif answer == "f":
        print("\nHow much money do you want to have?")
        fv = int(input(promt))
        print("In how many years?")
        yrs = int(input(promt))
        a =fv/(1.0175**yrs)
        print("\n**********\n")
        print("That equals to %.2f" % a+" € in todays money")
        print("\n**********")
        time.sleep(5)
    elif answer == "x":
        break
    else:
        print("\n**********\nYou pressed a wrong button, try again.\n**********")
        time.sleep(4)
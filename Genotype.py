print("Welcome to our Marriage compatibility checker written by DharaDavvy")
def ask():
    #this checks if the use wants to check another Genotype
    ac= input("Do you want to check another Genotype? (Y/N): ")
    if (ac.upper()== "Y"):
        checks()
    elif (ac.upper()== "N"):
        print("Thanks for using our program")
    else:
        print("Invalid Character")
        ask()

def checks():
    g1= input("Genotype: ")
    g2= input("Spouse's Genotype: ")

    if g1.upper()== "AA" and g2.upper()== "AA":
        print("Fit for marriage")
        ask()
    elif g1.upper()== "AA" and g2.upper()== "AS":
        print("Fit for Marriage")
        ask()
    elif g1.upper()== "AA" and g2.upper()=="SS":
        print("Fit for Marriage")
        ask()
    elif g1.upper()== "AS" and g2.upper()=="AS":
        print("Not fit for Marriage")
        ask()
    elif g1.upper()=="AS" and g2.upper()== "AA":
        print("Fit for Marriage")
        ask()
    elif g1.upper() == "AS" and g2.upper()== "SS":
        print("Not fit for Marriage")
        ask()
    elif g1.upper()== "SS" and g2.upper()== "SS":
        print("Not fit for Marriage")
        ask()
    elif g1.upper()=="SS" and g2.upper()== "AS":
        print("Not fit for Marriage")
        ask()
    elif g1.upper() == "SS" and g2.upper() == "AA":
        print("Fit for Marriage")
        ask()
    else:
        print("Please input Valid Genotype Character")
        ask()
        checks()
checks()



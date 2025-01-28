# weight = int(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
# if unit.upper() == "L":
#      converted = weight * 0.45
#      print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")

# genotype_self= (input("Genotype: "))
# genotype_spouse= input("Spouse's Genotype: ")
# if genotype_self.upper() and genotype_spouse.upper() == "AS":
#     print("Unfit for marriage")
# elif genotype_self.upper() == "AA" and genotype_spouse.upper == "AS":
#     print("Fit for marriage")

Genotype1= ["AS","SS"]
Genotype2= ["AA"]
Genotype_A= input("Genotype: ")
Genotype_B= input("Spouse's Genotype: ")
if (Genotype_A.upper() and Genotype_B.upper() in Genotype1):
    print("Unfit for marriage!")
else:
    print("Fit for marriage!")
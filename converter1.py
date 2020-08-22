# --------------------- This is a converter from Celcius to  Fehrenheit or from Fehrenheit to Celcius---------------
# ----------------------------------This program build by Akram Belfakih----------------------------------
print("This is a converter from Celcius to  Fehrenheit or from Fehrenheit to Celcius ")
print("""Usage instructions:
      [1]: when you choses "c" The program does the conversion from celsuis to Fehrenheit
      [2]: when you choses "f" The program does the conversion from Fehrenheit to celsuis""")

x = input(" enter ""c"" or ""f"" :  ")

if x == "f":
    y = int(input("Insert a Fehrenheit value: "))

    y = ((y-32)*(5/9))
    print(str(y)+' C')

if x == "c":
    z = int(input("Insert a value in Celcius: "))

    z = round(z*(9/5) + 32)
    print(str(z) + ' F')

print("Thanks for using our programme")

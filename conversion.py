#conversion
class Conversion:
    def __init__(self, temp):
        self.temp = int(temp)

    def CtoF(self):
        return self.temp * (9/5) + 32

    def FtoC(self):
        return (self.temp - 32) * (5 / 9)

def menu():
    print ("Temperature Converter")
    print ("1. Celcius to Fahrenheit")
    print ("2. Fahrenheit to Celcius")
  
def main():
    menu()
    while True:
        inputStr = input("\nSelect your option (Press <Enter> to quit): ")
        if inputStr == "":
            break

        elif int(inputStr) == 1:
            temp = float(input("\nEnter the temperature: "))
            ans = Conversion(temp)
            print (temp, "degree Celcius is {0:.1f} degree Fahrenheit.".format(ans.CtoF()))
              
        elif int(inputStr) == 2:
            temp = float(input("\nEnter the temperature: "))
            ans = Conversion(temp)
            print (temp, "degree Fahrenheit is {0:.1f} degree Celcius.".format(ans.FtoC()))
          
        else:
            print ("Your option is not valid. Please try again.")

if __name__ == "__main__":
    main()

    

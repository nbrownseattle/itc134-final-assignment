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
    print ("Select your option\n")
    print ("1. Celcius to Fahrenheit")
    print ("2. Fahrenheit to Celcius")
    print ("3. Quit\n")
    user_input = '0'

def main():
    menu()
    user_input = int(input("Choose your option: "))

    while user_input != 3:
        if user_input == 1:
            temp = eval(input("Enter your temperature:"))
            ans = Conversion(temp)
            print (ans.CtoF())
        elif user_input == 2:
            temp = eval(input("Enter your temperature:"))
            ans = Conversion(temp)
            print (ans.FtoC())
        elif user_input == 3:
            exit()
        else:
            print ("Your option is not valid. Please try again.")
            menu()

if __name__ == "__main__":
    main()

    

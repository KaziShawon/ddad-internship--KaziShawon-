class FactorialCalculator:
    def __init__(self, number):
        self.number = int(number)
    
    def show(self):
        n = self.number
        
        if n < 0: #...... If number is less than zero then demands correction
            print("Sorry, factorial does not exist for negative numbers")
        elif n == 0:
            print("The factorial of 0 is 1")
        elif n > 10:
            print("Please choose a number between 0 and 10.")
        else:
            fact = 1
            while(n > 1): 
                fact *= n
                n -= 1
            return print(f"The factorial of {self.number} is {fact}.")


message = ""
while message != 'q':
    if message != 'q':
        n = input("\nEnter number to calculate factorial: ")
        call = FactorialCalculator(n)
        call.show()
    message = input("\nEnter 'q' to exit and any key to continue: ")



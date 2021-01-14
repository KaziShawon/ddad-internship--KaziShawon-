class FibonacciCalculator:
    def __init__(self, number):
        self.number = int(number)
    
    def showNumbers(self):
        a = self.number
        f=0 #first element of series
        s=1 #second element of series
        if a<=0:
            print("The requested series is",f)
        else:
            print(f,s,end=" ")
            for x in range(2,a):
                next=f+s                           
                print(next,end=" ")
                f=s
                s=next


message = ""
while message != 'q':
    if message != 'q':
        n = input("\nEnter number to show fibonacci: ")
        call = FibonacciCalculator(n)
        call.showNumbers()
    message = input("\nEnter 'q' to exit and any key to continue: ")

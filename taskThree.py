def isPalindrome(s):
    # Function to check palindrome
    length = len(s)
    if length <= 1:
        return True
    if s[0] != s[length-1]:
        return False
    return isPalindrome(s[1:length-1])

def makeOddString(Str): 
    # Function to make odd string
    odd = "" 
    for i in range(1, len(Str), 2): 
        odd += Str[i] 
  
    return odd

def makeevenString(Str): 
    # Function to make even string
    even = "" 
    for i in range(0, len(Str), 2): 
        even += Str[i] 
  
    return even

def check(Str):

    # Check if it's a palindrome
    Str = Str.lower()
    if isPalindrome(Str):
        odd = makeOddString(Str) # Generate odd indexed string
        even = makeevenString(Str) # Generate even indexed string

        # Check if its a odd-even palindrome.
        if (isPalindrome(odd) and isPalindrome(even)):
            print("It is odd-even palindrome.")
        else:
            print("It is just a palindrome.")
    else:
        print("It is not a palindrome.\n")

n = input("\nEnter a string to check Even Palindrome or Odd Palindrome or Not a Palindrome: ")
check(n)

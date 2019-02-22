def reverse(number):
    rev=0
    while number > 0:
        rev = (10*rev)+number%10
        number//=10
    return rev

#print(reverse (number))

def isPalindrome(number):
    if number == reverse(number):
        return ("The number is a Palindrome")
    else:
        return ("The number is not a Palindrome")
        
#print (isPalindrome(number))

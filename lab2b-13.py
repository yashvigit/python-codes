#convert number to words
def numtoword():
    number = int(input("Enter a number between 0 and 19: "))
    words = ["zero", "one", "two", "three", "four", "five", 
             "six", "seven", "eight", "nine", "ten", 
             "eleven", "twelve", "thirteen", "fourteen", 
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    if (0 <= number <= 19):
        print("The number {number} in words is: ",words[number])

    else:
        print("The number {number} is not in range")
numtoword()        
# WAP that inputs dividend and divisor. It then calulates and displays the quotient and remainder.
div=int(input("Enter dividend: "))
dis = int(input("Enter divisor: "))
q= div // dis
r= div % dis
print("Quotient = ", q)
print("Remainder = ", r)
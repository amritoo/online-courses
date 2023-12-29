from cs50 import get_string

number = get_string("Number: ")

ar = [int(i) for i in number]
ar.reverse()

# checking for length
if len(number) in range(13, 17):
    osum, esum = 0, 0
    # iterating over each digit and calculating result
    for i in range(0, len(number)):
        if i % 2 == 0:
            osum += ar[i]
        else:
            x = ar[i] * 2
            esum += sum([int(i) for i in str(x)])
    # end for
    if (osum + esum) % 10 != 0:
        print("INVALID")
    elif len(ar) == 15 and ar[-1] == 3 and ar[-2] in [4, 7]:
        print("AMEX")
    elif len(ar) == 16 and ar[-1] == 5 and ar[-2] in range(1, 6):
        print("MASTERCARD")
    elif ar[len(ar) - 1] == 4:
        print("VISA")
    else:
        print("INVALID")
# end if
else:
    print("INVALID")
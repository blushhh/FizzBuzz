i = int(raw_input("Vnesi stevilo med 1 in 100: "))
if i > 100:
    print("Vnesli ste preveliko stevilo!")
else:
    for x in range(1,i+1):
        if (x % 3 != 0) and (x % 5 != 0):
            print x
        if (x % 3 == 0) and (x % 5 == 0):
            print "fizzbuzz"
        elif (x % 3 == 0):
            print "fizz"
        elif (x % 5 == 0):
            print "buzz"


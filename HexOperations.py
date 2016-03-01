#!/usr/bin/python

# Usage: enter your hex values with leading "0x" so that python knows the base

def format(hex):
    # remove prefix
    hex = hex[2:]
    # upper case
    hex = hex.upper() 
    # create leading zeros
    zeros = ""
    if (len(hex) < 8):
        for i in range(0, 8-len(hex)):
            zeros += "0"
    # put it back together
    hex = "0x" + zeros + hex
    return hex

print "Please choose an operation:"
print "1) complement\n2) sll\n3) srl\n4) and\n5) or\n6) xor"
choice = input("Choice: ")

hex1 = raw_input("hex value 1: ")
if (choice == 1):
    # bitwise complement
    print "Complement: " + format(hex(~ int(hex1, 0)))
elif (choice > 1 and choice <= 3):
    shift = input("shift by: ")
    if (choice == 2):
        # shift bits to left by shift places
        print "sll: " + format(hex(int(hex1, 0) << shift))
    elif (choice == 3):
        # shift bits to right by shift places
        print "srl: " + format(hex(int(hex1, 0) >> shift))
elif (choice >= 4 and choice < 7):
    hex2 = raw_input("hex value 2: ")
    if (choice == 4):
        # logical and
        print "AND: " + format(hex(int(hex1, 0) & int(hex2, 0)))
    elif (choice == 5):
        # logical or
        print "OR: " + format(hex(int(hex1, 0) | int(hex2, 0)))
    elif (choice == 6):
        # logical xor
        print "XOR: " + format(hex(int(hex1, 0) ^ int(hex2, 0)))
else:
    print "invalid choice"

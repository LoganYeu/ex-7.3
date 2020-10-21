# Group: Kaleb Hyde, Logan Yeubanks
print('Exercise 7.3')
fname = input('What file should we open? ')

try:
    fh = open(fname)
 
except:
    if fname == "na na boo boo":
        print ("NA NA BOO BOO TO YOU - You have been punk'd!")   
        quit()
    else:
        print(fname, 'is not found. Please enter a valid file.')
        quit()

for line in fh:
    line = line.rstrip()
    print(line.upper())
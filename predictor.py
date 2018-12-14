import pandas as pd
import binascii

#read csv
df = pd.read_csv('small.txt', sep=' ', header=None)

#key-value pair dictionary to store address as key and 2bit sat counter and prediction next to it.
pair = {}

#list to store predictions
predictions = []


#accepting the bits to be extracted.
while(True):
    i1 = input("Starting Bit?\n")
    i2 = input("Ending Bit?\n")
    if i2-i1!=14 or i2<i1 or i2>23 or i1<0:
        print "Invalid Input. Enter Again."
    else:
        break 

#traversing through the csv
for addr, outcome in zip(df[0], df[1]):
    
    #converting address to binary
    addr = bin(int(addr, 16))[2:]
    #extracting 14 bits from the middle of the binary addresss
    addr = addr[i1:i2]

    #if address is not already in dictionary, add prediction as not taken, initialize sat counter to 0
    if addr not in pair:
        pair[addr] = ['N', 0]
    else:
        #if sat counter has value greater than 2, predict taken
        if pair[addr][1]>=2:
            pair[addr][0] = 'T'
        
        #else predict not taken
        else:
            pair[addr][0] = 'N'
    
    #append predictions to list
    predictions.append(pair[addr][0])

    #since it is a saturating counter, it increments and stays at 3 even if actual outcome was taken
    if outcome=='T' and pair[addr][1]!=3:
        pair[addr][1]+=1
    
    #similarly, it decrements and stays at 0 if actual outcome was not taken
    elif outcome=='N' and pair[addr][1]!=0:
        pair[addr][1]-=1

#counting correct predictions
correct = 0
c = 0

#comparing outcomes and predictions
for outcome in df[1]:
    if predictions[c] == outcome:
        correct += 1
    c+=1
print 'Accuracy: ' + str((float(correct)/df.shape[0])*100) + '%' 
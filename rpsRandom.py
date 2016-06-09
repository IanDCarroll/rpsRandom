import numpy as np
import os

def rps(item1, item2):
    def choose():
	#uses cryptographically secure random by swacad @ github 
	np.random.seed(int(os.urandom(4).encode('hex'),16))
	choose = (int((np.random.random()) * 3))+1
	if choose == 1:
	    return 'Rock!'
	elif choose == 2:
	    return 'Paper!'
	else: #choose == 3:
	    return 'Scissors!'

    item1choice = choose()
    item2choice = choose()
    #print '%s: %s vs. %s: %s' %(item1, item1choice, item2, item2choice)

    if item1choice == item2choice:
	return rps(item1,item2)
    elif item1choice == 'Rock!' and item2choice == 'Scissors!':
	#print 'Rock breaks Scissors!'
	return item1
    elif item1choice == 'Scissors!' and item2choice == 'Paper!':
	#print 'Scissors cut Paper!'
	return item1
    elif item1choice == 'Paper!' and item2choice == 'Rock!':
	#print 'Paper covers Rock!'
	return item1
    elif item1choice == 'Rock!' and item2choice == 'Paper!':
	#print 'Rock is covered by Paper!'
	return item2
    elif item1choice == 'Paper!' and item2choice == 'Scissors!':
	#print 'Paper is cut by Scissors!'
	return item2
    else: #item1choice == 'Scissors!' and item2choice == 'Rock!':
	#print 'Scissors are broken by Rock!'
	return item2

#only a 2-item list ATM...
def rpsSelect(theList):
    if len(theList) == 2:
	return rps(theList[0],theList[1])
    else:
	return 'Only 2 items ATM...'

#def rpsShuffl():

def main():
    #if statements to determine data type to be shuffled.

    #if statements to determine shuffl or select
    #just a test with batman and superman. Which is really better?:
    print rps('Batman', 'Superman')
    print rpsSelect(['Ketchup','Mustard'])

if __name__ == '__main__':
    main()

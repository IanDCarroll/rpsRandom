import numpy as np
import os

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


def rps(item1, item2):

    i1Thro = choose()
    i2Thro = choose()
    #print '%s: %s v. %s: %s' %(item1, i1Thro, item2, i2Thro)

    if i1Thro == i2Thro:
	return rps(item1,item2)
    elif i1Thro == 'Rock!' and i2Thro == 'Scissors!':
	#print 'Rock breaks Scissors!'
	return item1
    elif i1Thro == 'Scissors!' and i2Thro == 'Paper!':
	#print 'Scissors cut Paper!'
	return item1
    elif i1Thro == 'Paper!' and i2Thro == 'Rock!':
	#print 'Paper covers Rock!'
	return item1
    elif i1Thro == 'Rock!' and i2Thro == 'Paper!':
	#print 'Rock is covered by Paper!'
	return item2
    elif i1Thro == 'Paper!' and i2Thro == 'Scissors!':
	#print 'Paper is cut by Scissors!'
	return item2
    else: #i1Thro == 'Scissors!' and i2Thro == 'Rock!':
	#print 'Scissors are broken by Rock!'
	return item2

def rps3(item1,item2,item3):

    i1Thro = choose()
    i2Thro = choose()
    i3Thro = choose()
    #print '%s: %s v. %s: %s v. %s: %s' % (item1,i1Thro,item2,i2Thro,item3,i3Thro)

    if i1Thro == i2Thro == i3Thro:
	return rps3(item1,item2,item3)
    elif i1Thro != i2Thro != i3Thro != i1Thro:
	return rps3(item1,item2,item3)
    elif i1Thro == 'Rock!' and i2Thro == 'Scissors!' and i3Thro == i2Thro:
	return item1
    elif i1Thro == 'Scissors!' and i2Thro == 'Paper!' and i3Thro == i2Thro:
	return item1
    elif i1Thro == 'Paper!' and i2Thro == 'Rock!' and i3Thro == i2Thro:
	return item1
    elif i2Thro == 'Rock!' and i3Thro == 'Scissors!' and i1Thro == i3Thro:
	return item2
    elif i2Thro == 'Scissors!' and i3Thro == 'Paper!' and i1Thro == i3Thro:
	return item2
    elif i2Thro == 'Paper!' and i3Thro == 'Rock!' and i1Thro == i3Thro:
	return item2
    elif i3Thro == 'Rock!' and i1Thro == 'Scissors!' and i2Thro == i1Thro:
	return item3
    elif i3Thro == 'Scissors!' and i1Thro == 'Paper!' and i2Thro == i1Thro:
	return item3
    elif i3Thro == 'Paper!' and i1Thro == 'Rock!' and i2Thro == i1Thro:
	return item3
    elif i1Thro == 'Rock!' and i2Thro == 'Scissors!' and i3Thro == i1Thro:
	return rps(item1,item3)
    elif i1Thro == 'Scissors!' and i2Thro == 'Paper!' and i3Thro == i1Thro:
	return rps(item1,item3)
    elif i1Thro == 'Paper!' and i2Thro == 'Rock!' and i3Thro == i1Thro:
	return rps(item1,item3)
    elif i2Thro == 'Rock!' and i3Thro == 'Scissors!' and i1Thro == i2Thro:
	return rps(item2,item1)
    elif i2Thro == 'Scissors!' and i3Thro == 'Paper!' and i1Thro == i2Thro:
	return rps(item2,item1)
    elif i2Thro == 'Paper!' and i3Thro == 'Rock!' and i1Thro == i2Thro:
	return rps(item2,item1)
    elif i3Thro == 'Rock!' and i1Thro == 'Scissors!' and i2Thro == i3Thro:
	return rps(item3,item2)
    elif i3Thro == 'Scissors!' and i1Thro == 'Paper!' and i2Thro == i3Thro:
	return rps(item3,item2)
    else: #if i3Thro == 'Paper!' and i1Thro == 'Rock!' and i2Thro == i3Thro:
	return rps(item3,item2)

def main():
    #if statements to determine data type to be shuffled.

    #if statements to determine shuffl or select

	#test cases
    #print rps('Batman', 'Superman')
    #print rpsSelect(['Ketchup','Mustard'])
    print rps3('Yani','John Tesh','Kenny G')
    #print rpsSelect(['Rene Descarte','John Stewart Mill','Aristotle'])

if __name__ == '__main__':
    main()

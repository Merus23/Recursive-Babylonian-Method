#Computing Square Roots - Recursive Implementation of the Babylonian method
#http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method
import sys
listOfNumbers=[]

def usuage():
	print "Usage:"
	print "sqrt.py numberToSqrt numberOfSigFigs\n"
	print "For example:"
	print "sqrt.py 12345 6\n"
	sys.exit(1)

def babSqrt(number, sigDig, counter=0):
	inflatedSigDig = sigDig*100

	half = 0.50

	if counter==0:
		global firstNumber
		firstNumber=number
		calculatedNumber = (half*(inflatedSigDig+(firstNumber/inflatedSigDig)))
		listOfNumbers.append(number)
		return babSqrt(calculatedNumber, sigDig, counter+1)
	else:	
		listOfNumbers.append(number)
		print counter
		if listOfNumbers[counter-1] == listOfNumbers[counter]:
			return listOfNumbers[counter]
		else:
			calculatedNumber = (half*(number+(firstNumber/number)))
			#print calculatedNumber
			return babSqrt(calculatedNumber, sigDig, counter+1)

 
if len(sys.argv)!=3:
	print usuage()

print babSqrt(int(sys.argv[1]),int(sys.argv[2]))

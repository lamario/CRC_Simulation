######################################################
#
#   CRC simulation
#   by Lamario
#   v1.0    2018-02-12
#
######################################################
# DEFINING FUNCTIONS
def remLeadZero (inputStr) :
    number = len(inputStr)

    counter = 1
    while counter != number+1 :
        if inputStr[0] == '0' :
            inputStr = inputStr[1:]
        counter += 1
    return inputStr

def doCRC (sequence, polynomial, errorPattern) :
    sequence = remLeadZero(sequence)
    #print sequence
    polynomial = remLeadZero(polynomial)
    errorPattern = remLeadZero(errorPattern)

    CRCloop = len(sequence)
    #print CRCloop

    run = True
    positionTemp = 5
    sequenceStart = ""

    for loop in range( 0, len(polynomial) ) :
        sequenceStart += sequence[loop]
    test1Str = sequenceStart

    while run :
        position = 0
        midtest = ""        
        for loop in range( 0, len(polynomial) ) :
            test1 = test1Str[loop]
            test2 = polynomial[loop]
            testResult = int(test1) ^ int(test2)
            midtest = midtest + str(testResult)               

        if positionTemp != (CRCloop) :

            #print 'original midtest: ', midtest

            newMidtest = remLeadZero(midtest)
            #print 'midtest without 0: ', newMidtest
            #print 'original positionTemp: ', positionTemp

            bitsToAdd = 5 - len(remLeadZero(midtest))
            #print 'how many bits to add: ', bitsToAdd

            for loop2 in range ( bitsToAdd ) :
                positionTemp += 1
                newMidtest += sequence[positionTemp - 1]
            
                #print 'newMidtest: ', newMidtest
                #print 'positionTemp: ', positionTemp

            #print 'new positionTemp: ', positionTemp

            test1Str = newMidtest

            #if CRCloop == positionTemp :
        else : 
            run = False
        
        #print ""
    return midtest[1:]

# defining the main () function
def main () :
    print "CRC calculation simulator\n\n"

    #defaults
    sequence = "0001101111000101"
    polynomial = "10011"
    errorPattern = "101"

    userAnswer = str ( input ('Use defaults? "1"=Yes, "0"=No: '))
    if userAnswer == "0" :
        print 'Default code sequence is: \t ' + sequence
        newSequence = str ( input ('Enter code or \"2\" for default:   '))
        if newSequence != "2" :
            sequence = newSequence
        print ""

        print 'Default polynomial is: \t\t ' + polynomial
        newPolynomial = str ( input ('Enter code or \"2\" for default:   '))
        if newPolynomial != "2" :
            polynomial = newPolynomial
        print ""

        print 'Default error pattern is: \t ' + errorPattern
        newErrorPattern = str ( input ('Enter code or \"2\" for default:   '))
        if newErrorPattern != "2" :
            errorPattern = newErrorPattern
    elif userAnswer == "1" :
        print "Using defaults..."

    firstCRC = doCRC (sequence + "0000", polynomial, errorPattern)
    print ""
    print "CRC: " + firstCRC

    secondCRC = doCRC (sequence + firstCRC, polynomial, errorPattern)    
    print "Verifying CRC... " + secondCRC

    if secondCRC == "0000" :
        print "CRC was successfull"
    
    print "\nIntroducing Error randomly into the sequence...NOT IMPLEMENTED\n"


# THIS IS THE MAIN BODY / START OF THE PROGRAM
main ()
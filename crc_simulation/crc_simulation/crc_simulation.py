######################################################
#
#   Name Search
#   Exercise no. 7, Assignment 7
#   Richard Beno (rich1034@edu.eal.dk)
#   v1.0    2016-01-10
#
######################################################
# LIST OF FUNCTIONS: readFiles (), getNameInput (), main ()

# DEFINING FUNCTIONS
def remLeadZero (inputStr) :
    number = len(inputStr)
    #print number

    counter = 1
    while counter != number+1 :
        if inputStr[0] == '0' :
            inputStr = inputStr[1:]

        counter += 1
    return inputStr

def doCRC (sequence, polynomial, errorPattern) :
    sequence = remLeadZero(sequence)
    print sequence
    polynomial = remLeadZero(polynomial)
    errorPattern = remLeadZero(errorPattern)

    CRCloop = len(sequence)
    print CRCloop

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

            print 'original midtest: ', midtest

            newMidtest = remLeadZero(midtest)
            print 'midtest without 0: ', newMidtest
            print 'original positionTemp: ', positionTemp

            bitsToAdd = 5 - len(remLeadZero(midtest))
            print 'how many bits to add: ', bitsToAdd

            for loop2 in range ( bitsToAdd ) :
                positionTemp += 1
                newMidtest += sequence[positionTemp - 1]
            
                print 'newMidtest: ', newMidtest
                print 'positionTemp: ', positionTemp

            #positionTemp = positionTemp + bitsToAdd
            print 'new positionTemp: ', positionTemp

            test1Str = newMidtest

            #if CRCloop == positionTemp :
        else : 
            run = False
        
        print ""
    return midtest



# defining the main () function
def main () :
    #sequence = [0,0,0,1,1,0,1,1,1,1,0,0,0,1,0,1]
    #polynomial = [1,0,0,1,1]
    #errorPattern = [1,0,1]
    sequence = "0001101111000101"
    polynomial = "10011"
    errorPattern = "101"
    midtest = ""
    sequence = sequence + "0000"
    
    print doCRC (sequence, polynomial, errorPattern)

    #print remLeadZero("000011")
# THIS IS THE MAIN BODY / START OF THE PROGRAM
main ()
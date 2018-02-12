######################################################
#
#   CRC simulation
#   by Lamario
#   v1.2    2018-02-12
#
######################################################
# DEFINING FUNCTIONS
import random

def remLeadZero ( s ) :
    return s[s.find('1'):]

def doCRC ( sequence, polynomial ) :
    sequence = remLeadZero(sequence)
    polynomial = remLeadZero(polynomial)
    run = True
    position = len(polynomial)
    sequenceStart = ""
    partialSequence = sequence[:len(polynomial)]

    while run :
        partialCRC = ""   
        
        # XOR with polynomial     
        for loop in range( 0, len(polynomial) ) :
            sequenceBit = partialSequence[loop]
            polynomialBit = polynomial[loop]
            xorResult = int(sequenceBit) ^ int(polynomialBit)
            partialCRC = partialCRC + str(xorResult)               

        if position != len(sequence) :            
            partialCRC = remLeadZero(partialCRC)
            bitsToAdd = 5 - len(partialCRC)

            # Adding bits to partialCRC from sequence
            if bitsToAdd <= len(sequence) - position :
                for loop in range(bitsToAdd) :
                    position += 1
                    partialCRC += sequence[position - 1]
            else :
                partialCRC = partialCRC + sequence[position:]
                run = False

            partialSequence = partialCRC
        else : 
            run = False
        
    return partialCRC[1:]

def implementError( sequence, error ) :
    errorPosition = random.randint( 1, len(sequence) - 1 - len(error) ) 
    prefix =  sequence[:errorPosition]
    errorSequence = ""
    suffix = sequence[errorPosition+len(error):]

    for loop in range ( 0, len(error) ) :
        if error[loop] == "1" : 
            if sequence[errorPosition + loop] == "1" :
                errorSequence += "0"
            elif sequence[errorPosition + loop] == "0" :
                errorSequence += " 1"
        elif error[loop] == "0" :
            errorSequence += sequence[errorPosition + loop]

    return ( prefix + errorSequence + suffix )

# defining the main () function
def main () :
    print "CRC calculation simulator\n\n"

    #defaults
    sequence = "0001101111000101"
    polynomial = "10011"
    errorPattern = "101"

    # Get user input on using default values
    userAnswer = str ( raw_input ('Use defaults? "no"=No: '))
    if userAnswer == "no" :
        print 'Default code sequence is: \t ' + sequence
        newSequence = str ( raw_input ('Enter code or leave empty for default:   '))
        if newSequence != "" :
            sequence = newSequence

        print '\nDefault polynomial is: \t\t ' + polynomial
        newPolynomial = str ( raw_input ('Enter code or leave empty for default:   '))
        if newPolynomial != "" :
            polynomial = newPolynomial

        print '\nDefault error pattern is: \t ' + errorPattern
        newErrorPattern = str ( raw_input ('Enter code or leave empty for default:   '))
        if newErrorPattern != "" :
            errorPattern = newErrorPattern
    elif userAnswer == "1" :
        print "Using defaults..."

    # Calculate CRC
    print "\nCalculating CRC number..."
    firstRound = doCRC ( sequence + "0000", polynomial ) 
    print "CRC = " + firstRound

    # Verify CRC
    secondRound = doCRC ( sequence + firstRound, polynomial )    
    print "Verifying CRC... " + secondRound
    if secondRound == "0000" :
        print "CRC was successfull" 
              
    # Implement Error to sequence
    print "\nIntroducing Error randomly into the sequence...\n"
    print "Error = " + errorPattern
    errorSequence = implementError ( sequence + firstRound, errorPattern )
    print 'Original: ' + sequence + firstRound
    print 'W/ error: ' + errorSequence    
    print len(errorSequence)

    # Check for errors
    thirdRound = doCRC ( errorSequence, polynomial )
    print "\nChecking for Errors...\nCRC = " + thirdRound
    if thirdRound != "0000" :
        print "Error was found!  " + firstRound + '=/=' + thirdRound
    else :
        print "No error was found.\n"

# THIS IS THE MAIN BODY / START OF THE PROGRAM
main ()
PROGRAM fizzbuzz
    IMPLICIT NONE
    CHARACTER*100 :: nAsCharacter   !takes user input as a char
    INTEGER :: n  
    INTEGER :: currentNumber
    CALL get_command_argument(1, nAsCharacter)
    READ(nAsCharacter,*) n !converts user input to integer
    
    DO currentNumber=1,n    !loops up to n for FizzBuzz
        IF (MOD(currentNumber,15) == 0) THEN
            WRITE (*,*) "FizzBuzz"
        ELSE IF (MOD(currentNumber,5) == 0) THEN
            WRITE (*,*) "Buzz"
        ELSE IF (MOD(currentNumber,3) == 0) THEN
            WRITE (*,*) "Fizz"
        ELSE
            WRITE (*,*) currentNumber
        END IF
    END DO

END PROGRAM fizzbuzz
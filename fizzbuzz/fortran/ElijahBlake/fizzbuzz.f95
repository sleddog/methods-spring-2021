PROGRAM fizzbuzz
    IMPLICIT NONE
    CHARACTER*100 :: nAsCharacter   !takes user input as a char
    INTEGER :: n  
    INTEGER :: currentNumber
    CALL get_command_argument(1, nAsCharacter)
    READ(nAsCharacter,*) n !converts user input to integer
    
    DO currentNumber=1,n    !loops up to n for FizzBuzz
        IF (MOD(currentNumber,1155) == 0) THEN
            WRITE (*,*) "FizzBuzzPingPong"
        ELSE IF (MOD(currentNumber,385) == 0) THEN
            WRITE (*,*) "BuzzPingPong"
        ELSE IF (MOD(currentNumber,231) == 0) THEN
            WRITE (*,*) "FizzPingPong"
        ELSE IF (MOD(currentNumber,77) == 0) THEN
            WRITE (*,*) "PingPong"
        ELSE IF (MOD(currentNumber,55) == 0) THEN
            WRITE (*,*) "BuzzPong"
        ELSE IF (MOD(currentNumber,35) == 0) THEN
            WRITE (*,*) "BuzzPing"
        ELSE IF (MOD(currentNumber,33) == 0) THEN
            WRITE (*,*) "FizzPong"
        ELSE IF (MOD(currentNumber,15) == 0) THEN
            WRITE (*,*) "FizzBuzz"
        ELSE IF (MOD(currentNumber,11) == 0) THEN
            WRITE (*,*) "Pong"
        ELSE IF (MOD(currentNumber,7) == 0) THEN
            WRITE (*,*) "Ping"
        ELSE IF (MOD(currentNumber,5) == 0) THEN
            WRITE (*,*) "Buzz"
        ELSE IF (MOD(currentNumber,3) == 0) THEN
            WRITE (*,*) "Fizz"
        ELSE
            WRITE (*,*) currentNumber
        END IF
    END DO

END PROGRAM fizzbuzz
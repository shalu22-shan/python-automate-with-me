Start
Input n   (the limit number)

For number = 2 to n
    Set isPrime = true
    For i = 2 to number - 1
        If number % i == 0 then
            isPrime = false
            Break
    End For
    If isPrime == true then
        Print number
End For

Stop
def fizzbuzz (x):
    numero = int(x)
    if numero%3==0 and numero%5!=0:
        return  'Fizz';
    if numero%3==0 and numero%5==0:
        return 'FizzBuzz';
    if numero%3!=0 and numero%5==0:
                 return 'Buzz';
    else:
        return numero;

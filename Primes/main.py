def sieve(s):
  """Implements Sieve of Eratosthenes
    Args:
        s (list): List of possible primes less than an including prime   
          candidate
        
    Returns:
        list: list of remaing possible primes not div by fist element.
    """
  m=s[0]
  filtered = filter(lambda i:  i % m , s)
  return list(filtered)
  
def prime_checker(number) :
  """Check for a prime number
    Args:
      number (int): prime candidate

    Returns
      nothing
  """
  prime = False
  testing = True

  my_sieve = list(range(2,number+1))

  while testing :
    print(my_sieve)
    if number == my_sieve[0]:
      prime = True
      break
    elif number % my_sieve[0] == 0:
      prime = False
      break
    else :
      my_sieve =sieve(my_sieve)
     
    
  if(prime):
    print(f"{number} is a prime number.")
  else :
    print(f"{number} is NOT a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)




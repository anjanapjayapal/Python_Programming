
num=int(input("Enter a number: "))

def is_prime(num):
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    else:
        return False
    
                
    
print(f"{num} is prime: {is_prime(num)}")            

                
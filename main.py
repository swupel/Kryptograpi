from mpmath import mp
import requests

loop_o_death=0,33,25,90,248,480,105,50,32,16,41,3,7,2,14,1,4,5,10,15

with open("C:\\Users\\anton\\Downloads\\Pi\\Pi - Dec.txt", mode="r") as f:
    pi=f.read()  
    
def generate_pi_until_sequence(sequence):
    # Set initial precision
    precision = 50  # Start with a precision of 50 digits
    found_sequence = False
    pi_digits = ""

    while not found_sequence:
        # Set the precision for mpmath
        mp.dps = precision + 10  # Add some extra digits for accuracy
        
        # Calculate Pi
        pi_value = str(mp.pi)[2:]  # Get digits after the decimal point
        pi_digits = pi_value  # Store the current digits
        
        # Check if the sequence is found in the generated digits
        if sequence in pi_digits:
            found_sequence = True
        else:
            precision += 10  # Increase the precision for more digits
            
        print(len(pi_digits))

    return len(pi_digits)

def fetch_until_squence(sequence):
    
    found=False
    start=0
    number=1000
    while not found:
        url=f"https://api.pi.delivery/v1/pi?start={start}&numberOfDigits={number}&radix=10"
        segment=requests.get(url).json()["content"]
        found=segment.find(sequence) != -1
        start+=number
        print(start)
    start-=number
    return start+segment.find(sequence)

def encrypt(message):
    found=message
    c=0  
    tips={}
    o_found=0
    while True:
    # The sequence to look for
        found=str(pi.find(found))
        if str(pi.find(found[:-1])) == str(pi.find(found)) and pi.find(found) != -1:
            found=found
            tips[c]=found[-1]
        if found == "-1" or found==o_found:
            break
        c+=1
        o_found=found
    return [o_found,c,tips]

def decrypt(data):
    count=0
    o_found,c,tips=data[0],data[1],data[2]
    o_found=int(o_found)
    
    while count != c:   
        
        o_ende=o_found+1
        while pi.find(str(pi[o_found:o_ende])) != o_found:
            o_ende+=1

        
        try:
            suffix=tips[c-count-2]
            o_found=pi[o_found:o_ende]
            o_found+=suffix
        except KeyError:
            o_found=pi[o_found:o_ende]
            pass
        o_found=int(o_found)

        count+=1
        
    return o_found
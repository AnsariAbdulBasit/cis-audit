# Python Program to calculate the square root

# Note: change this value for a different result
import sys
import os
orign_stdout = sys.stdout
hostname = os.popen("hostname -f").read()
sys.stdout = open("/tmp/cis_audit_report.txt","w")

num = 8 

# To take the input from the user
#num = float(input('Enter a number: '))

num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

sys.stdout.close()

sys.stdout = orign_stdout

print('Script completed on server '),
print(hostname)

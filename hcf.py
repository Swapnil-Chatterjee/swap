x=int(input("Enter the 1st no.:"))
y=int(input("Enter the 2nd no.:"))
if x<y :
      small=y
else :
      small=x
for i in range(1,(small+1)):
      if((x%i)==0 and (y%i)==0):
            hcf=i
lcm=(x*y)/hcf
print("HCF=",hcf)
print("LCM=",lcm)      
      

# with list

a=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
b=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
n=int(input('enter no.'))
print('roman no.:-',end=' ')
for j in range(len(a)):
	i=n//b[j]
	n-=(b[j]*i)
	print(a[j]*i,end='')
print()


# with dictonory

r_n={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
n=int(input('enter no.'))
for j in r_n:
	i=n//j
	n%=j
	print(r_n[j]*i,end='')
print()

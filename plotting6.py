from plotting import plot
n1=complex(input("Enter 1st Complex number: "))
n2=complex(input("Enter 2nd Complex number: "))
n3=complex(input("Enter 3rd Complex number: "))
n4=complex(input("Enter 4th Complex number: "))
n5=complex(input("Enter 5th Complex number: "))
s={n1,n2,n3,n4,n5}
s1={(-1)*z for z in s}
plot(s1,100)

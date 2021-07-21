i=2
try:
    i = 2/0  
except ZeroDivisionError:
    print("error")
print(1)


try:
    i = 2/0  
except:
    print("error inesperado")

print(i)


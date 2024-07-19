
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1
       
       
    for i in [2,1,5]:
         print(i)
         
         
         
         
#
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

for n in "banana":
    print(n)
    

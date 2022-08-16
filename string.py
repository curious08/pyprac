name ="Sumesh"
#understanding index position string positon start with 0 to n-1
#  -6 -5 -4 -3 -2 -1  => -(length of string),-n+1 to 1
#   S  u  m  e  s  h
#   0  1  2  3  4  5  => 0 to n-1
print("index 0",name[0],"index 1",name[1],"index 2",name[2],"index 3",name[3],"index 4",name[4],"index 5",name[5])

print(name[1:10])
print(name[1:])
print(name[:4])
print(name[:])
print(name*3)

c='a'
print(type(c))#str
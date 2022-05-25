
a=int(input("entre el primer lado "))
b=int(input("entre el segundo lado "))
c=int(input("entre el tercer lado "))
if a<(b+c) and b<(a+c) and c<(a+b):
  print('Si a =',a,', b =',b,'y c =',c,' entonces si se puede hacer un triangulo')
  if a==b==c:
    print('Equilatero')
  elif a==b or b==c or a==c:
    print('Isósceles')
  else:
    print('Escaleno')
else:
  print('Si a =',a,', b =',b,'y c =',c,' entonces no se puede hacer un triangulo')
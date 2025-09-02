num = input()
num1 = [int(x) for x in str(num)]
num1.reverse
par = []
impar = []
par = num1[::2]
impar = num1[1::2]
imparf = sum(impar)
parf = []
for i in range (len(par)):
  g = par[i]*2
  if g > 9:
    g -= 9
  par[i]=parf
valido=parf + imparf
if valido % 10 == 0:
  print("Cartão válido")
else:
  print("Cartão inválido")

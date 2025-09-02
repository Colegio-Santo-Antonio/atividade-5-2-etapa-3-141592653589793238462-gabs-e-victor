num = input()
num1 = [int(x) for x in str(num)]
num1.reverse
par = []
impar = []
par = num1[::2]
impar = num1[1::2]
parf = sum(par)
imparf = []
for i in range (len(impar)):
  g = par[i]*2
  if g > 9:
    g -= 9
    impar[i]=g
  par[i]=parf
valido=sum(parf) + imparf
if valido % 10 == 0:
  print("Cartão válido")
else:
  print("Cartão inválido")

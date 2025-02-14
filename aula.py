codigo=[4,4.5,5,2,1.5]


pedido=int(input('Digite o codigo do produto :'))
pedido1=int(input('Digite a quantidade desse produto:'))

if pedido==1:
    total=codigo[0]*pedido1
    print('Tota:R$',total)
elif pedido==2:
    total=codigo[1]*pedido1
    print('Tota:R$',total)
elif pedido==3:
    total=codigo[2]*pedido1
    print('Tota:R$',total)
elif pedido==4:
    total=codigo[3]*pedido1
    print('Tota:R$',total)
elif pedido==5:
    total=codigo[4]*pedido1
    print('Tota:R$',total)
else:
    print('Verifique os dados ')





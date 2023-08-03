import matplotlib.pyplot as plt

def menu(x,a,b,c):
    y=a*x + b*x - c
    return y

x1 =5
x2 =7
x3 =8
x4 =10
x5 =13
x6 =14
x7 =16
x8 =19
x9 =20
x10 =21

a=3
b=7
c=6

plt.title('Gráfico Exercicio 02 ')

plt.grid()

plt.plot(x1,menu(x1,a,b,c), marker='o',markersize=10,markerfacecolor='red')
plt.plot(x2,menu(x2,a,b,c), marker='o',markersize=10,markerfacecolor='blue')
plt.plot(x3,menu(x3,a,b,c), marker='o',markersize=10,markerfacecolor='green')
plt.plot(x4,menu(x4,a,b,c), marker='o',markersize=10,markerfacecolor='red')
plt.plot(x5,menu(x5,a,b,c), marker='o',markersize=10,markerfacecolor='blue')
plt.plot(x6,menu(x6,a,b,c), marker='o',markersize=10,markerfacecolor='green')
plt.plot(x7,menu(x7,a,b,c), marker='o',markersize=10,markerfacecolor='red')
plt.plot(x8,menu(x8,a,b,c), marker='o',markersize=10,markerfacecolor='blue')
plt.plot(x9,menu(x9,a,b,c), marker='o',markersize=10,markerfacecolor='green')
plt.plot(x10,menu(x10,a,b,c), marker='o',markersize=10,markerfacecolor='red')
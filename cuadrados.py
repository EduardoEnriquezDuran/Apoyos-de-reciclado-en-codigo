import openpyxl
import matplotlib.pyplot as plt

doc = openpyxl.load_workbook("ordinarios.xlsx")
hoja = doc["Hoja1"]
x=[]
y=[]
for row in hoja.iter_rows():
    d=row[0].value
    e=row[1].value
    x.append(d)
    y.append(e)

n=len(x)
xy=[]
cuadrado=[]
sumatoria_x=0
sumatoria_y=0
print("x: ",x)
print("y: ",y)
for a in range(n):
    multiplicacion=0
    sumatoria_x+=x[a]
    sumatoria_y+=y[a]
    multiplicacion=x[a]*y[a]
    xy.append(multiplicacion)
    cuadrado1=0
    cuadrado1=x[a]*x[a]
    cuadrado.append(cuadrado1)
print("xy: ",xy)
print("x^2: ",cuadrado)

exy=0
ex2=0

for b in range(n):
    exy+=xy[b]
    ex2+=cuadrado[b]
m=((exy-((sumatoria_x)*(sumatoria_y))/n)/(ex2-((sumatoria_x*sumatoria_x)/n)))
print("m= ",m)

media_y=sumatoria_y/n
media_x=sumatoria_x/n

b=(media_y-(m*media_x))
print("b=",b)


plt.scatter(x, y, label='Datos')  
plt.plot(x, [m * xi + b for xi in x], color='red', label='Línea de regresión')  
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend() 

plt.show()

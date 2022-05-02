import math


print ("EMPEZAREMOS POR CREAR NUESTRO POLIGONO ");
n = int(input("Num. de vertices (debe ser mayor que 3): "));
poligono=[];
perimetro = 0.0;
while n < 3:
    n = int(input("Num. de vertices (debe ser mayor que 3): "));
i = 1;
pos = 0;
neg = 0;
print("Coordenadas vertice:", i);
x1 = int(input("\tx: "));
y1 = int(input("\ty: "));
poligono.append([x1,y1]);
i = 2;
print("Coordenadas vertice:", i);
xant = int(input ("\tx: "));
yant = int(input ("\ty: "));
poligono.append([xant,yant]);
e1x = xant - x1;
e1y = yant - y1;
perimetro = math.sqrt(e1x*e1x+e1y*e1y);
eantx = e1x;
eanty = e1y;
i = 3;
while i <= n :
    print ("Coordenadas vertice:\n", i);
    x = int(input("\tx: "));
    y = int(input("\ty: "));
    poligono.append([x,y]);
    ex = x - xant;
    ey = y - yant;
    perimetro= perimetro + (ex*ex + ey*ey);
    z = eantx * ey - eanty * ex;
    if (z > 0):
        pos = pos +1;
    else:
        if z < 0:
            neg = neg +1;
    xant = x;
    yant = y;
    eantx = ex;
    eanty = ey;
    i = i+1;
print("Bienvenido a nuestra aplicacion de poligonos\n")
print("Pulsa 1 para calcular la concavidad y la convexidad" )
print("Pulsa 2 para calcular el perimetro")
print("Pulsa 3 para saber si esta dentro \n")
mathop = input("Elija una opcion: \n") # Ask for the choice and make sure it is an interger.
if mathop == "1":
    print ("CONCAVIDAD/CONVEXIDAD POLIGONO\n");
    print ("==============================\n\n");
    ex = x1 - xant;
    ey = y1 - yant;
    z = eantx * ey - eanty * ex;
    if z > 0:
        pos = pos +1;
    else:
        if z < 0:
            neg = neg +1;
        z = ex * e1y - ey * e1x;
        if z > 0:
            pos = pos +1;
        else:
            if z < 0:
                neg = neg +1;
        if (pos):
            if (neg):
                print ("\nPoligono concavo");
            else:
                print("\nPoligono convexo");
        else:
            if (neg):
                print("\nPoligono convexo");
            else:
                print("\nPoligono degenerado en una linea");
elif mathop == "2":
    print ("Perimetro del poligono\n");
    print ("==============================\n\n");
    print("El perimetro del poligono es \n");
    print(perimetro);
elif mathop == "3":
    print ("INTRUDUZCA LAS COORDENADAS DEL PUNTO");
    print ("Coordenadas vertice:\n", i);
    x = int(input("\tx: "));
    y = int(input("\ty: "));
    i = 0
    j = len(poligono) - 1
    salida = False
    for i in enumerate(len(poligono)):
        if (poligono[i][1] < y and poligono[j][1] >= y) or (poligono[j][1] < y and poligono[i][1] >= y):
            if poligono[i][0] + (y - poligono[i][1]) / (poligono[j][1] - poligono[i][1]) * (poligono[j][0] - poligono[i][0]) < x:
                 salida = not salida
        j = i
    if salida:
        print("EL PUNTO SE ENCUENTRA DENTRO DEL POLIGONO \n");
    else:
        print("ESTA FUERA \n");
else:
    print("Please enter a valid option. Exiting")

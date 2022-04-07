
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

int main()
{
	char c;
	float e1x, e1y, ex, ey, eantx, eanty;
	float x1, y1, x, y, xant, yant;
	float z;
	int pos, neg;
	int n, i;
	do
	{
		system("cls||clear");
		printf("CONCAVIDAD/CONVEXIDAD POLIGONO\n");
		printf("==============================\n\n");
		do
		{
			printf("Num. de vertices: ");
			scanf(" %d", &n);
		} while (n < 3);
		i = 1;
		pos = 0;
		neg = 0;
		printf("Coordenadas vertice %d:\n", i);
		printf("\tx: ");
		scanf(" %f", &x1);
		printf("\ty: ");
		scanf(" %f", &y1);
		i = 2;
		printf("Coordenadas vertice %d:\n", i);
		printf("\tx: ");
		scanf(" %f", &xant);
		printf("\ty: ");
		scanf(" %f", &yant);
		e1x = xant - x1;
		e1y = yant - y1;
		eantx = e1x;
		eanty = e1y;
		i = 3;
		while (i <= n)
		{
			printf("Coordenadas vertice %d:\n", i);
			printf("\tx: ");
			scanf(" %f", &x);
			printf("\ty: ");
			scanf(" %f", &y);
			ex = x - xant;
			ey = y - yant;
			z = eantx * ey - eanty * ex;
			if (z > 0)
			{
				pos++;
			}
			else
			{
				if (z < 0)
				{
					neg++;
				}
			}
			xant = x;
			yant = y;
			eantx = ex;
			eanty = ey;
			++i;
		}
		ex = x1 - xant;
		ey = y1 - yant;
		z = eantx * ey - eanty * ex;
		if (z > 0)
		{
			pos++;
		}
		else
		{
			if (z < 0)
			{
				neg++;
			}
		}
		z = ex * e1y - ey * e1x;
		if (z > 0)
		{
			pos++;
		}
		else
		{
			if (z < 0)
			{
				neg++;
			}
		}
		if (pos)
		{
			if (neg)
			{
				printf("\nPoligono concavo");
			}
			else
			{
				printf("\nPoligono convexo");
			}
		}
		else
		{
			if (neg)
			{
				printf("\nPoligono convexo");
			}
			else
			{
				printf("\nPoligono degenerado en una linea");
			}
		}
		printf("\n\nDesea efectuar una nueva operacion (s/n)? ");
		scanf(" %c", &c);
	} while ((c != 'N') && (c != 'n'));
	return 0;
}
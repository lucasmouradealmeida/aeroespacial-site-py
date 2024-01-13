import numpy as np
from matplotlib import pyplot as plt

# Sistema Dinamico Sol-Jupiter-Particula

# Massa do Sol
m1 = 1.989*10**30

# Massa de Jupiter
m2 = 1.898*10**27

# Distancia entre a Sol e Jupiter
r12 = 748.41*10**9

mi = (m2)/(m1+m2)

# Localização dos Pontos Lagrangianos

Lx, L4, L5 = points()

# Curvas de velocidade zero

# Constante Gravitacional
G = 1
# Sol
mi1 = G*(1-mi)
# Jupiter
mi2 = G*mi

# % Cj (Possiveis valores iniciais)
CL1 = (3) + (3**(3/4))*((mi2)**(2/3))-((10*(mi2))/3)
CL2 = (3) + (3**(3/4))*(mi2**(2/3))-((14*mi2)/3)
CL3 = 3 + mi2
CL4 = 3 - mi2
CL5 = CL4

# Cj (Valores corrigidos - especifico para o Sistema Sol-Jupiter-particula)
CLj = [CL1+0.1, CL2+0.01821, CL3, CL4+0.001, CL5]


# Plot dos graficos

# j = 0.01;
# k = 2;

# x = -k:j:k;
# y = -k:j:k;

# [X,Y] = meshgrid(x,y);
        
# for i=1:5
#     Cj = CLj(1,i);
    
#     Z = X.^2 + Y.^2 + 2.*(((1-mi)./(sqrt((X+mi).^2+Y.^2))) + ((mi)./(sqrt((X-1+mi).^2+Y.^2)))) - Cj;
    
#     L = [L4; L5; Lx(1,1) 0; Lx(2,1) 0; Lx(3,1) 0];
    
#     figure(i)
#     clf;
#     contour(X,Y,Z,[0 0],'k')
#     hold on
#     scatter(L(:,1),L(:,2),'filled')
#     grid on
#     title(sprintf('C_J = %.4f',CLj(1,i)))
# end

# Plot dos gráficos
j = 0.01
k = 2

x = np.arange(-k, k + j, j)
y = np.arange(-k, k + j, j)

X, Y = np.meshgrid(x, y)

for i in range(5):
    Cj = CLj[i]

    Z = X**2 + Y**2 + 2 * (((1 - mi) / (np.sqrt((X + mi)**2 + Y**2))) + ((mi) / (np.sqrt((X - 1 + mi)**2 + Y**2)))) - Cj

    L = np.array([L4, L5, [Lx[0, 0], 0], [Lx[1, 0], 0], [Lx[2, 0], 0]])

    plt.figure(i + 1)
    plt.clf()
    plt.contour(X, Y, Z, [0], colors='k')
    plt.scatter(L[:, 0], L[:, 1], c='black', marker='o')
    plt.grid(True)
    plt.title(f'C_J = {CLj[i]:.4f}')
    plt.show()


def points() -> list:

    # Localizacao dos Pontos Lagrangianos
    # Pontos L4 e L5
    mi = 0.2
    L4 = [-mi + 0.5, np.sqrt(3)/2]
    L5 = [L4[0], -L4[1]]

    # Pontos L1, L2 & L3
    rt = np.zeros((5, 1))
    x = -10
    k = 0
    c = 5

    # Teorema de Bolzano
    while k < c:
        f0 = x - (((1 - mi) / ((abs(x + mi))**3)) * (x + mi)) - ((mi / ((abs(x - 1 + mi))**3)) * (x - 1 + mi))
        x = x + 0.005
        f1 = x - (((1 - mi) / ((abs(x + mi))**3)) * (x + mi)) - ((mi / ((abs(x - 1 + mi))**3)) * (x - 1 + mi))

        if f0 > 0 and f1 < 0:
            rt[k, 0] = x - 0.005
            k = k + 1
        elif f1 > 0 and f0 < 0:
            rt[k, 0] = x - 0.005
            k = k + 1

    Er = 1e-8
    z = 0
    Lx = np.ones((3, 1))
    j = 0

    # Metodo de Newton-Raphson
    for i in range(0, 5, 2):
        x0 = rt[i, 0]
        Erx = 1
        while Erx > Er:
            fx = x0 - (((1 - mi) / ((abs(x0 + mi))**3)) * (x0 + mi)) - ((mi / ((abs(x0 - 1 + mi))**3)) * (x0 - 1 + mi))

            fx_d = ((3 * mi * ((mi + x0 - 1)**2)) / ((abs(mi + x0 - 1))**5)) - ((mi) / ((abs(mi + x0 - 1))**3)) - \
                ((1 - mi) / ((abs(mi + x0))**3)) + ((3 * (1 - mi) * ((mi + x0)**2)) / ((abs(mi + x0))**5)) + (1)

            x = x0 - (fx / fx_d)
            Erx = (abs(x0 - x)) / (abs(x))
            x0 = x
        Lx[z, 0] = x
        z = z + 1

    return Lx, L4, L5



# %Localizacao dos Pontos Lagrangianos
# %Pontos L4 e L5
# L4 = [-mi+0.5 sqrt(3)/2];
# L5 = [L4(1,1) -L4(1,2)];

# %Pontos L1, L2 & L3
# rt = zeros(5,1);
# x = -10;
# k = 1;
# c = 6;

# %Teorema de Bolzano

# while k < c
#     f0 =  x - (((1-mi)/((abs(x+mi))^3))*(x+mi)) - ((mi/((abs(x-1+mi))^3))*(x-1+mi));
#     x = x + 0.005;
#     f1 =  x - (((1-mi)/((abs(x+mi))^3))*(x+mi)) - ((mi/((abs(x-1+mi))^3))*(x-1+mi));
    
#     if f0>0 && f1<0
#         rt(k,1) = x - 0.005;
#         k = k + 1;
#     elseif f1>0 && f0<0
#         rt(k,1) = x - 0.005;
#         k = k + 1;
#     end
# end


# Er = 10^-8;
# z = 1;
# Lx = ones(3,1);
# j = 0;

# %Metodo de Newton-Raphson
# for i=1:2:5
#     x0 = rt(i,1);
#     Erx = 1;
#     while Erx > Er
#         fx =  x0 - (((1-mi)/((abs(x0+mi))^3))*(x0+mi)) - ((mi/((abs(x0-1+mi))^3))*(x0-1+mi));
        
#         fx_d = ((3*mi*((mi+x0-1)^2))/((abs(mi+x0-1))^5))-((mi)/((abs(mi+x0-1))^3))-((1-mi)/((abs(mi+x0))^3))+((3*(1-mi)*((mi+x0)^2))/((abs(mi+x0))^5))+(1);      
       
#         x = x0 - (fx/fx_d);
#         Erx = (abs(x0-x))/(abs(x));
#         x0 = x;
#     end
#     Lx(z,1) = x;
#     z = z + 1;
# end



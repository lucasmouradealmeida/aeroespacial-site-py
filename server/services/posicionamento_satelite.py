# Importação de bibliotecas

import math as m
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Módulos

from converter_anomalia_media_verdadeira import converter_anomalia_media_verdadeira
from semieixo_maior import semieixo_maior
from dir_orbital import dir_orbital
from matrix_transposta_rotacao import matrix_transposta_rotacao
from vel_orbital import vel_orbital


def posicionamento_satelites() -> list:
    """Obter o posicionamento do satélite na órbita

    
    """
    # Constantes 
    mi_terra = 3.986*(10**5) # km3/s2

    # Two lines
    # First line = [satelliteNumber(1) intDesignator(2) epochNumb(3).julianDate(4)
    # 1st(5) 2nd(6) drag(7) epochy(8) elementNumb(9)]

    # Second Line = [satelliteNumber(1) inclination(2) rightAscendingNode(3) eccentricity(4)
    # argumentPerigeu(5) anomaliaMedia(6) meanMotion(7) revNumb(8)]

    # first_line = [0.7276, 74026, 22158.20205273, 0.00000124, 00000, 00000, 0, 9995]
    second_line = [0.7276, 64.2707, 228.5762, 0.6489050, 281.4937, 16.8767, 2.45097347248963]

    # Variáveis

    anomalia_media = second_line[5]
    excentricidade = second_line[3]
    mean_motion = second_line[6]
    inclination = second_line[1]
    argumento_perigeu = second_line[4]
    nodo_ascendente = second_line[2]

    # Conversão da anomalia média para verdadeira (graus)
    theta = converter_anomalia_media_verdadeira(anomalia_media, excentricidade)

    # Semieixo maior
    semieixo, n = semieixo_maior(mi_terra, mean_motion)

    # Coordenada Orbital
    xo, yo, zo = dir_orbital(m.radians(theta), excentricidade, semieixo)

    # Coordenada Inercial
    matrix1 = matrix_transposta_rotacao(m.radians(inclination), m.radians(argumento_perigeu), m.radians(nodo_ascendente))
    coord_inercial = np.dot(matrix1, np.array([xo, yo, zo]))

    # Velocidade Orbital
    vx, vy, vz = vel_orbital(n, excentricidade, m.radians(theta), semieixo)

    # Velocidade Inercial
    matrix2 = matrix_transposta_rotacao(m.radians(inclination), m.radians(argumento_perigeu), m.radians(nodo_ascendente))
    velocidade_inercial = np.dot(matrix2, np.array([vx, vy, vz]))

    # Aplicação do processo de integração

    # Dados do Item a
    T = 2*m.pi/n
    r = np.transpose(coord_inercial)
    v = np.transpose(velocidade_inercial)

    # Plot do Elipsoide de Referência
    r_pol = 6356.752 # Raio polar
    r_eq = 6378.137 # Raio equatorial





    # Plot do Elipsoide de Referência


    # Flatten or concatenate the position and velocity arrays
    # init_cond = np.concatenate([r, v]).ravel()

    # # Use a longer integration range to cover multiple orbits
    # sol = odeint(edos, init_cond, np.linspace(0, 5 * 50 * T, 1000))

    # sol_reshaped = np.reshape(sol, (len(sol), 18))

    # # Extract position and velocity from the reshaped array
    # sol_position = sol_reshaped[:, :9]
    # sol_velocity = sol_reshaped[:, 9:]

    # # Plot the graph
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.plot(sol_position[:, 0], sol_position[:, 1], sol_position[:, 2])
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # ax.set_zlabel('z')
    # plt.show()



    # Inicializando a figura e os eixos 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Listas para armazenar os pontos na órbita
    x_points = []
    y_points = []
    z_points = []


    # Plot - Solução Analítica
    for theta in np.arange(0, 2*m.pi, 0.07):
        p = semieixo*(1 - excentricidade**2)
        r = p/(1+excentricidade*m.cos(theta))
        xo = r*m.cos(theta)
        yo = r*m.sin(theta)
        zo = 0
        matrix = matrix_transposta_rotacao(m.radians(inclination), m.radians(argumento_perigeu), m.radians(nodo_ascendente))
        coord_inercial = np.dot(matrix, np.array([xo, yo, zo]))

        # Adicionando pontos às listas
        x_points.append(coord_inercial[0, 0])
        y_points.append(coord_inercial[0, 1])
        z_points.append(coord_inercial[0, 2])

    # # Adicionando uma linha à órbita
    # ax.plot(x_points, y_points, z_points, color='red', label='Órbita')

    # # Adicionando rótulos aos eixos
    # ax.set_xlabel('Eixo X')
    # ax.set_ylabel('Eixo Y')
    # ax.set_zlabel('Eixo Z')

    # # Ajustando a relação de aspecto e mostrando o gráfico
    # plt.axis('equal')
    # plt.legend()
    # plt.show()


    # Adicionando uma linha à órbita
    ax.plot(x_points, y_points, z_points, color='red', label='Órbita')

    # Criando uma malha para o elipsoide de referência
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x_elipsoide = r_eq * np.outer(np.cos(u), np.sin(v))
    y_elipsoide = r_eq * np.outer(np.sin(u), np.sin(v))
    z_elipsoide = r_pol * np.outer(np.ones(np.size(u)), np.cos(v))

    # Plotando o elipsoide de referência
    ax.plot_surface(x_elipsoide, y_elipsoide, z_elipsoide, color='blue', alpha=0.3, label='Elipsoide de Referência')

    # Adicionando rótulos aos eixos
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')

    # Ajustando a relação de aspecto e mostrando o gráfico
    plt.axis('equal')
    plt.legend()
    plt.show()

    

def edos(x, t):
    mi = 3.986e5
    
    dx = np.zeros(18)
    
    dx[0] = x[3]
    dx[1] = x[4]
    dx[2] = x[5]
    dx[3] = -mi * (x[0] / ((x[0]**2 + x[1]**2 + x[2]**2)**(3/2)))
    dx[4] = -mi * (x[1] / ((x[0]**2 + x[1]**2 + x[2]**2)**(3/2)))
    dx[5] = -mi * (x[2] / ((x[0]**2 + x[1]**2 + x[2]**2)**(3/2)))
    
    return dx


   

posicionamento_satelites()


# %Condicao inicial
# InitCond = [r v];

# %Solucoes ODE45 (Possivel modificar e multiplicar T (quantidade de periodos))
# options = odeset('RelTol',1e-12); %minimizacao do erro 

# [Times,Out] = ode45(@edos, [0 50*T], InitCond, options);

# %Plot do grafico - Numérica
# p = plot3(Out(:,1),Out(:,2),Out(:,3));

# axis equal
# grid on

# %Textura da terra no elipsoide (Necessaria uma conexao com a internet)
# texture_url = 'http://www.shadedrelief.com/natural3/images/earth_clouds.jpg';
# cdata = flip(imread(texture_url));
# set(body, 'FaceColor', 'texturemap', 'CData', cdata, 'EdgeColor', 'none');

# %Plot - Solucao Analitica 
# for theta=0:0.07:deg2rad(360)
#     p = semieixo*(1 - excentricidade^2);
#     r = p/(1+excentricidade*cos(theta));
#     xo = r*cos(theta);
#     yo = r*sin(theta);
#     zo = 0;
#     coordInercial = matrizTranspostaRotacao(deg2rad(64.2707), deg2rad(281.4937), deg2rad(228.5762)) * [xo; yo; zo];
#     scatter3(coordInercial(1,1), coordInercial(2,1), coordInercial(3,1), '.','red')
# end

# hold off






import math as m


def dir_orbital(theta, ex, semieixo) -> list:
    """Obter as coordenadas orbitais

    Args:
        theta (float): Anomalia verdadeira
        ex (float): Excentricidade
        semieixo (float): Semieixo maior

    Returns:
        list: Coordenadas orbitais
    """
    p = semieixo*(1 - ex**2)
    r = p/(1+ex*m.cos(theta))
    xo = r*m.cos(theta)
    yo = r*m.sin(theta)
    zo = 0
    return xo, yo, zo




# %Função coordenadas orbitais
# function [xo, yo, zo] = dirOrbital(theta, ex, semieixo)
#     p = semieixo*(1 - ex^2);
#     r = p/(1+ex*cos(theta));
#     xo = r*cos(theta);
#     yo = r*sin(theta);
#     zo = 0;
# end







import math as m

def converter_anomalia_media_verdadeira(M, e) -> float:
    # Determinacao do valor inicial - anomalia excentrica
    if M < m.pi:
        u0 = M + (e/2)
    else:
        u0 = M - (e/2)

    #declaracao de variaveis
    Erx = 100
    u = 0
    j = 1

    #Segmentacao das conicas
    if e < 1: # equacao para elipse
        
        #Newton-Raphson
        while Erx >= 1e-8:
            u = u0 - ((u0 - e*m.sin(u0) - M)/(1 - e*m.cos(u0)))
            Erx = abs((u0-u)/(u))
            u0 = u

        #Anomalia Verdadeira
        theta_0 = 2*m.atan((m.sqrt( ((1+e)/(1-e)))*m.tan(u0/2)))
                    
        # Conversão de valores
        u = m.degrees(u0)
        theta = m.degrees(theta_0)
        
        if(theta_0 < 0):
            theta = 360 + theta
        
                 
        #Caso as anomalias ultrapassem 360graus
        #Anomalia Excentrica (u)
        if u > 360 or u < -360:
            u = u - (360*m.trunc(u/360))
        
        #Anomalia Verdadeira (Theta)
        if theta > 360 or theta < -360:
            theta = theta - (360*m.trunc(theta/360))


    else: # equacao para a hiperbole 
        while Erx >= 1e-8:
            u = u0 - ((-u0 + e*m.sinh(u0) - M)/(e*m.cosh(u0) -1))
            Erx = abs((u0-u)/(u))
            u0 = u
            j = j +1
                    
        #Anomalia Verdadeira
        teta0 = 2*m.atan((m.sqrt(((e+1)/(e-1))) * m.tanh(u/2)))
            
            
        # Conversao de valores
        u = m.degrees(u0)
        theta = m.degrees(teta0)
                
                
        #Caso as anomalias ultrapassem 360graus
        #Anomalia Excentrica (u)
        if u > 360 or u < -360:
            u = u - (360*m.trunc(u/360))

        #Anomalia Verdadeira (Theta)
        if theta > 360 or theta < -360:
            theta = theta - (360*m.trunc(theta/360))
        

    return theta


from math import *
import numpy as np

def matrix_transposta_rotacao(i , w, o) -> list:
    """Obter a matriz transposta de rotação

    Args:
        i (float): Inclinação
        w (float): Argumento do perigeu
        o (float): Nodo ascendente

    Returns:
        list: Matriz transposta de rotação
    """
    # Matriz de rotação
    r_x = np.matrix([[1, 0, 0], [0, cos(i), sin(i)], [0, -sin(i), cos(i)]])
    r_z0 = np.matrix([[cos(w), sin(w), 0], [-sin(w), cos(w), 0], [0, 0, 1]])
    r_zi = np.matrix([[cos(o), sin(o), 0], [-sin(o), cos(o), 0], [0, 0, 1]])

    # Matriz transposta (Orbital para Inercial)
    m = np.dot(r_z0, r_x)
    m2 = np.dot(m, r_zi)
    mt = np.transpose(m2)

    return mt



import math as m

def semieixo_maior(mi, n) -> list:
    """Obter o semieixo maior

    Args:
        mi (float): Constante gravitacional
        n (float): Movimento médio

    Returns:
        list: Semieixo maior e movimento médio
    """
    n_segundo = (2*m.pi*n/86400)
    semieixo = (mi/(n_segundo**2))**(1/3)
    return semieixo, n_segundo



#     %Função semieixo maior
# function [semieixo, n_segundo] = semieixoMaior (mi, n)
#     n_segundo = (2*pi*n/86400);
#     semieixo = (mi/(n_segundo^2))^(1/3);
# end







import math as m


def vel_orbital(n, ex, theta, semieixo) -> list:
    """Obter a velocidade orbital

    Args:
        n (float): Mean motion
        ex (float): Eccentricity
        theta (float): True anomaly
        semieixo (float): Semieixo maior

    Returns:
        list: Velocidade orbital
    """
    vx = -(n*semieixo/m.sqrt(1-ex**2))*m.sin(theta)
    vy = (n*semieixo/m.sqrt(1-ex**2))*(ex+m.cos(theta))
    vz = 0

    return vx, vy, vz



# %Função velocidade orbital

# function [vx, vy, vz] = velOrbital(n, ex, theta, semieixo)
#     vx = -(n*semieixo/sqrt(1-ex^2))*sin(theta);
#     vy = (n*semieixo/sqrt(1-ex^2))*(ex+cos(theta));
#     vz = 0;
# end


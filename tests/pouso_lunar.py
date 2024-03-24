def edos30(t, x):
    dx = np.zeros(4)
    M = 1.1  # kg
    g_lunar = 1.8  # m/s2
    E = 3.6  # N - empuxo jato
    theta = 30
    # Condicoes de contorno
    dx[0] = x[2]
    dx[1] = x[3]
    dx[2] = (E * np.sin(np.deg2rad(theta))) / M
    dx[3] = (E * np.cos(np.deg2rad(theta)) / M) - g_lunar

    return dx


def edos0(t, x):
    dx = np.zeros(4)
    M = 1.1  # kg
    g_lunar = 1.8  # m/s2
    E = 3.6  # N - empuxo jato
    theta = 0
    # Condicoes de contorno
    dx[0] = x[2]
    dx[1] = x[3]
    dx[2] = (E * np.sin(np.deg2rad(theta))) / M
    dx[3] = (E * np.cos(np.deg2rad(theta)) / M) - g_lunar

    return dx


def edosN30(t, x):
    dx = np.zeros(4)
    M = 1.1  # kg
    g_lunar = 1.8  # m/s2
    E = 3.6  # N - empuxo jato
    theta = -30
    # Condicoes de contorno
    dx[0] = x[2]
    dx[1] = x[3]
    dx[2] = (E * np.sin(np.deg2rad(theta))) / M
    dx[3] = (E * np.cos(np.deg2rad(theta)) / M) - g_lunar

    return dx


def pouso_lunar():
    # Constantes
    M = 1.1  # kg
    g_lunar = 1.8  # m/s2
    E = 3.6  # N - empuxo jato
    theta = 0
    theta1 = 30
    theta2 = -30

    # Condicoes de contorno
    # Movimento vertical
    Fx = E * np.sin(theta)
    Fy = E * np.cos(theta)
    Fy1 = E * np.cos(np.deg2rad(theta1))
    Fy2 = E * np.cos(np.deg2rad(theta2))
    P = M * g_lunar

    # Eixo x
    ax = Fx / M

    # Eixo y
    ay = (Fy - P) / M

    # Pouso Suave
    # Final: y = 0; vx e vy = 0

    # Condições Iniciais
    y0 = 18
    vy = -7

    # Utilizando a equação de Torricelli
    y = np.linspace(0, 40, 100)

    # Curvas de velocidade inicial
    V0 = -np.sqrt(((Fy - P) / M) * (2 * y))
    V01 = -np.sqrt(((Fy1 - P) / M) * (2 * y))
    V02 = -np.sqrt(((Fy2 - P) / M) * (2 * y))

    # Curvas de velocidade Final
    vf1 = -np.sqrt((vy) ** 2 + 2 * (((Fy - P) / M)) * (y - y0))
    vf2 = -np.sqrt((vy) ** 2 + 2 * (((Fy1 - P) / M)) * (y - y0))

    # Minimização do y para 0 -> Condição 1
    fun = lambda y: -((Fy - P) / M) * (2 * y) + (vy) ** 2 + 2 * (((Fy1 - P) / M)) * (y - y0)
    x = fsolve(fun, 2)  # Altura de encontro entre as curvas

    vo_value = -np.sqrt(((Fy - P) / M) * (2 * x))  # Velocidade no encontro entre as curvas
    t_transf = (vo_value - vy) / (((Fy1 - P) / M))  # Tempo para transferencia
    t_red = (0 - vo_value) / ((Fy - P) / M)  # Tempo da curva para pouso
    tempo_total = t_transf + t_red  # Tempo total

    # Minimização para y para 0 -> Condição 2
    fun2 = lambda y: ((-7) ** 2 + 2 * (((Fy - P) / M)) * (y - 18)) - (((Fy2 - P) / M) * (2 * y))
    x2 = fsolve(fun2, 2)
    vo_value2 = -np.sqrt(((Fy2 - P) / M) * (2 * x2))
    t_transf2 = (vo_value2 + 7) / ((Fy - P) / M)
    t_red2 = (0 - vo_value2) / ((Fy2 - P) / M)
    tempo_total2 = t_transf2 + t_red2

    # Primeira Condição -> Ocorre o ajuste para zerar a velocidade em X
    # Sx Sy Vx Vy
    InitCond = [0, 18, 0, -7]
    # Defina as opções de tolerância
    options = {"rtol": 1e-12}

    # Resolva as EDOs usando solve_ivp
    sol = solve_ivp(edos30, [0, t_transf - 0.34486], InitCond, method="LSODA", rtol=options["rtol"])

    # Os resultados serão acessíveis em sol.t e sol.y
    Times = sol.t
    Out = sol.y

    len1 = len(Out) - 1

    InitCond2 = [Out[len1, 0], Out[len1, 1], Out[len1, 2], Out[len1, 3]]
    solX = solve_ivp(edosN30, [t_transf - 0.34486, t_transf], InitCond2, method="LSODA", rtol=options["rtol"])
    TimesX = solX.t
    OutX = solX.y

    lenX = len(OutX) - 1

    InitCond3 = [OutX[len1, 0], OutX[len1, 1], OutX[len1, 2], OutX[len1, 3]]
    sol2 = solve_ivp(edos0, [t_transf, tempo_total], InitCond3, method="LSODA", rtol=options["rtol"])
    Times2 = sol2.t
    Out2 = sol2.y

    # Segunda Condição -> Ocorre o ajuste para zerar a velocidade em X
    # Sx Sy Vx Vy

    InitCond = [0, 18, 0, -7]
    sol3 = solve_ivp(edos0, [0, t_transf2], InitCond, method="LSODA", rtol=options["rtol"])
    Times3 = sol3.t
    Out3 = sol3.y

    len2 = len(Out3) - 1
    InitCond2 = [Out3[len2, 0], Out3[len2, 1], Out3[len2, 2], Out3[len2, 3]]
    sol4 = solve_ivp(edos30, [t_transf2, tempo_total2 - 1.48835], InitCond2, method="LSODA", rtol=options["rtol"])
    Times4 = sol4.t
    Out4 = sol4.y

    len3 = len(Out4) - 1
    InitCond3 = [Out4[len3, 0], Out4[len3, 1], Out4[len3, 2], Out4[len3, 3]]
    sol5 = solve_ivp(edos0, [tempo_total2 - 1.48835, tempo_total2], InitCond3, method="LSODA", rtol=options["rtol"])
    Times5 = sol5.t
    Out5 = sol5.y

    # Plot dos pontos iniciais e finais
    plt.figure(1)
    p1 = plt.plot(V0, y, "red", label="Pouso suave 0")
    p2 = plt.plot(V01, y, "blue", label="Pouso suave 30")
    p3 = plt.plot(V02, y, "black", label="Pouso suave -30")
    # p4 = plt.scatter(-7, 18, color="black", label="Ponto inicial")
    p5 = plt.plot(vf1, y, "green", label="Final 0")
    p6 = plt.plot(vf2, y, "magenta", label="Final 30 ou -30")
    plt.xlabel("Velocidade em y")
    plt.ylabel("Altitude")
    plt.legend()
    plt.show()

    # Plots dos vetores finais -> Condição 2
    # x = np.concatenate((Out3[:, 0], Out5[:, 0]))
    # y = np.concatenate((Out3[:, 1], Out5[:, 1]))
    # Vx = np.concatenate((Out3[:, 2], Out5[:, 2]))
    # Vy = np.concatenate((Out3[:, 3], Out5[:, 3]))

    # plt.figure(2)
    # plt.plot(x, y)
    # plt.xlabel("Coordenadas em X")
    # plt.ylabel("Coordenadas em y")
    # plt.xlim(0, 1)
    # plt.ylim(0, 1)
    # plt.show()

    # plt.figure(3)
    # plt.plot(Vx, y)
    # plt.xlabel("Velocidade em X")
    # plt.ylabel("Coordenadas em y")
    # plt.xlim(0, 1)
    # plt.ylim(0, 1)
    # plt.show()

    # plt.figure(4)
    # plt.plot(Vx, Vy)
    # plt.xlabel("Velocidade em X")
    # plt.ylabel("Velocidade em y")
    # plt.xlim(0, 1)
    # plt.ylim(0, 1)
    # plt.show()

    # plt.figure(5)
    # plt.plot(Vy, x)
    # plt.xlabel("Velocidade em y")
    # plt.ylabel("Coordenadas em x")
    # plt.xlim(0, 1)
    # plt.ylim(0, 1)
    # plt.show()

    # plt.figure(6)
    # plt.plot(Vy, y)
    # plt.xlabel("Velocidade em y")
    # plt.ylabel("Coordenadas em y")
    # plt.xlim(0, 1)
    # plt.ylim(0, 1)
    # plt.show()

    return "Pouso lunar realizado com sucesso!"

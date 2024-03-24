from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

# Resources
from server.resources.pouso_lunar_resource import VelocidadesResource


def curvas_de_pouso_suave(data: VelocidadesResource) -> tuple:
    """Dados das curvas de pouso suave

    Args:
        massa (float): Massa da nave em kg
        gravidade (float): gravidade local em m/s2
        intensidade (float): Intensidade do empuxo do jato em N
        angulacao (int): Angulação do jato em graus

    Returns:
        list: Lista de dados de velocidade para geração dos gráficos
    """
    # Movimento vertical
    Fy = data.intensidade * np.cos(np.deg2rad(data.angulacao))
    P = data.massa * data.gravidade

    # Geração de pontos em y
    y = np.linspace(0, 40, 100)

    # Curva de velocidade inicial - Velocidade Final = 0
    v0 = -(np.sqrt(((Fy - P) / data.massa) * (2 * y)))

    return {
        "velocidade": v0,
        "altura": y,
    }


def curvas_velocidade(data: VelocidadesResource) -> dict[list]:
    """Dados das curvas de velocidade inicial e final

    Args:
        massa (float): Massa da nave em kg
        gravidade (float): gravidade local em m/s2
        intensidade (float): Intensidade do empuxo do jato em N
        angulacao (int): Angulação do jato em graus

    Returns:
        list: Lista de dados de velocidade para geração dos gráficos
    """
    # Movimento vertical
    Fy = data.intensidade * np.cos(np.deg2rad(data.angulacao))
    P = data.massa * data.gravidade

    # Condições Iniciais
    y0 = data.altura
    vy = data.velocidade_inicial

    # Geração de pontos em y
    y = np.linspace(0, 40, 100)

    # Curvas baseadas na velocidade inicial do veículo
    vf = -(np.sqrt((vy) ** 2 + 2 * (((Fy - P) / data.massa)) * (y - y0)))

    return {
        "velocidade": vf,
        "altura": y,
    }

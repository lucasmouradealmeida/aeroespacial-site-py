from server.core.base_model import BaseModel


class VelocidadesResource(BaseModel):
    massa: float
    gravidade: float
    intensidade: float
    angulacao: int
    altura: float
    velocidade_inicial: float

from server.core.base_model import BaseModel


class VelocidadesResource(BaseModel):
    massa: float | None = None
    gravidade: float | None = None
    intensidade: float | None = None
    angulacao: int | None = None
    altura: float | None = None
    velocidade_inicial: float | None = None

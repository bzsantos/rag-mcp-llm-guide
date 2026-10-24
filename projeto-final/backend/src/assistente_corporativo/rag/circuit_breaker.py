import time


class CircuitBreaker:
    def __init__(self, max_falhas: int = 3, tempo_reset_segundos: int = 30):
        self.max_falhas = max_falhas
        self.tempo_reset_segundos = tempo_reset_segundos
        self.falhas_consecutivas = 0
        self.aberto_desde: float | None = None

    def circuito_aberto(self) -> bool:
        if self.aberto_desde is None:
            return False
        if time.monotonic() - self.aberto_desde > self.tempo_reset_segundos:
            self.aberto_desde = None  # tempo de espera passou — tenta de novo
            self.falhas_consecutivas = 0
            return False
        return True

    def registrar_sucesso(self) -> None:
        self.falhas_consecutivas = 0
        self.aberto_desde = None

    def registrar_falha(self) -> None:
        self.falhas_consecutivas += 1
        if self.falhas_consecutivas >= self.max_falhas:
            self.aberto_desde = time.monotonic()

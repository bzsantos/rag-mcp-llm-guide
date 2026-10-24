from assistente_corporativo.core.exceptions import ServicoIndisponivelError
from assistente_corporativo.rag.circuit_breaker import CircuitBreaker

_circuit_breaker = CircuitBreaker(max_falhas=3, tempo_reset_segundos=30)


class RagService:
    ...
    def _chamar_llm_protegido(self, prompt: str) -> str:
        if _circuit_breaker.circuito_aberto():
            raise ServicoIndisponivelError("O assistente de IA está temporariamente desativado após falhas consecutivas.")
        try:
            resultado = self._chamar_llm(prompt)
            _circuit_breaker.registrar_sucesso()
            return resultado
        except (httpx.ConnectError, httpx.TimeoutException):
            _circuit_breaker.registrar_falha()
            raise ServicoIndisponivelError("O assistente de IA está indisponível no momento.")

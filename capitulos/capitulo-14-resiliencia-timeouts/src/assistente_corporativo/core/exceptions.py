class ServicoIndisponivelError(Exception):
    """Levantado quando um serviço externo (LLM, banco vetorial) está fora do ar ou muito lento."""
    pass

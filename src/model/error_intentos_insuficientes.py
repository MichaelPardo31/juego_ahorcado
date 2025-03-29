class ErrorIntentosInsuficientes(Exception):
    """
        Error personalizado que se lanza cuando el jugador ha agotado todas sus oportunidades
        para adivinar la palabra.
    """

    def __init__(self):
        super().__init__(f"se han agotado las oportunidades para adivinar la palabra")

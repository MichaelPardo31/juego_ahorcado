from src.model.diccionario import Diccionario
from src.model.adivinanza import Adivinanza
from src.model.error_intentos_insuficientes import ErrorIntentosInsuficientes

class Juego:
    """
    Representa:
        El juego el juego del ahorcadito.
        esta clase permite almacenar datos de la dificultad, intentos, palabras,
        y dar mas intentos segun la difcultad.
    class attributes:
        DIFICULTAD_BAJA: selecciona la dificultad baja
        DIFICULTAD_MEDIA: selecciona la dificultad media
        DIFICULTAD_ALTA: selecciona la dificultad alta
    """
    DIFICULTAD_BAJA = "DIFICULTAD_BAJA"
    DIFICULTAD_MEDIA = "DIFICULTAD_MEDIA"
    DIFICULTAD_ALTA = "DIFICULTAD_ALTA"

    def __init__(self):
        """
            Inicializa el juego con dificultad baja por defecto.
        """
        self.__dificultad = Juego.DIFICULTAD_BAJA
        self.__intentos_realizados: int = 0
        self.__diccionario = Diccionario()
        self.__adivinanza: Adivinanza = None

    def obtener_intentos_realizados(self):
        return self.__intentos_realizados

    def obtener_adivinanza(self) -> Adivinanza:
        return self.__adivinanza

    def __generar_palabra(self) -> str:
        return self.__diccionario.obtener_palabra()

    def calcular_intentos_permitidos(self) -> int:
        '''
        define los intentos  dependiendo de la dificultad escogida.
        '''
        if self.__dificultad == self.DIFICULTAD_BAJA:
            return 20
        if self.__dificultad == self.DIFICULTAD_MEDIA:
            return 10
        if self.__dificultad == self.DIFICULTAD_ALTA:
            return 5
        return 0

    def modificar_dificultad(self, dificultad: str) -> None:
        self.__dificultad = dificultad

    def iniciar_partida(self) -> int:
        '''
        comienza el juego generando la palabra y mostrando los intentos permitidos.
        returns: cantidad de posiciones de la palabra generada.
        '''
        palabra = self.__generar_palabra()
        self.__adivinanza: Adivinanza = Adivinanza(palabra)
        self.__intentos_realizados = self.calcular_intentos_permitidos()
        return self.__adivinanza.obtener_cantidad_posiciones()

    def adivinar(self, letra: str) -> [int]:
        """
            Letra ingresada por el usuario para adivinar si es correcta o no.
            Args:
                letra (str): Letra que el jugador ingresa.
            Returns:
                int: posicion de la letra ingresada si es correcta, si no pierdes un intento.
            Raises:
                ErrorIntentosInsuficientes: Si no quedan intentos disponibles.
        """
        if self.__intentos_realizados < 0:
            raise ErrorIntentosInsuficientes()
        self.__intentos_realizados -= 1
        return self.__adivinanza.adivinar(letra)

    def verificar_si_hay_intentos(self) -> bool:
        return self.__intentos_realizados >= 0

    def verificar_triunfo(self) -> bool:
        return self.__adivinanza.verificar_si_hay_triunfo()
    """
    verifica si hay un triunfo o una derrota.
    Returns:
        bool: True si ganaste, False si no.
    """
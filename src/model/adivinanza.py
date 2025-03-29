class Adivinanza:
    """
        Representa una palabra a adivinar en el juego.

        Attributes:
            __letras (list[str]): Lista de caracteres que conforman la palabra a adivinar.
            __posiciones (list[bool]): Lista de booleanos que indican si cada letra ha sido adivinada.
    """

    def __init__(self, palabra: str):
        self.__letras: list[str] = list(palabra)
        self.__posiciones: list[bool] = [False] * len(self.__letras)
        """ 
        inicializa una instancia de Adivinanza.

        Args:
            palabra (str): palabra a adivinar
        """

    def adivinar(self, letra: str) -> [int]:
        """
        Devuelve la posicion correcta de la letra ingresada. 
        Args:
            letra: letra ingresada en la palabra a adivinar
        Returns:
            Int: posicion(es) de si acertaste la letra, una lista vacia si no.
        """
        if letra not in self.__letras:
            return []
        posiciones_donde_esta_la_letra = []
        for i in range(len(self.__letras)):
            if self.__letras[i] == letra:
                posiciones_donde_esta_la_letra.append(i)
                self.__posiciones[i] = True
        return posiciones_donde_esta_la_letra

    def obtener_letras(self) -> [str]:
        return self.__letras

    def obtener_posiciones(self) -> [bool]:
        return self.__posiciones
    
    def obtener_cantidad_posiciones(self) -> int:
        return len(self.__letras)

    def verificar_si_hay_triunfo(self) -> bool:
        return all(self.__posiciones)
    """
    Verifica si ganaste o perdiste
    Returns:
        bool: True si lograste adivinar todas las palabras, False si no.
    """


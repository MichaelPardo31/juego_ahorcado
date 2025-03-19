class Adivinanza:
    """
        Representa una palabra a adivinar en el juego del ahorcado.

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

        Atributos de instancia:
            __posiciones (list[bool]): Lista de booleanos que indican si cada letra ha sido adivinada.

        """

    def adivinar(self, letra: str) -> [int]:
        """
        Devuelve la posicion correcta de la letra ingresada. 

        Returns:
            list: Vacia.
            posicion lista: posiciones_donde_esta_la_letra.

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
    """
    Devuelve: la letra ingresada

    Returns:
        list[str]: = list(palabra) (letra ingresada en palabra)
    """

    def obtener_posiciones(self) -> [bool]:
        return self.__posiciones
    """
    Devuelve: las posiciones

    Returns:
        list[bool]: (posicion)
    """

    def obtener_cantidad_posiciones(self) -> int:
        return len(self.__letras)
    """
    Devuelve: un entero de cantidad de posiciones

    Returns:
        int: la cantidad de posiciones
    """


    def verificar_si_hay_triunfo(self) -> bool:
        return all(self.__posiciones)
    """
    Devuelve: bool: Si ganaste o perdiste.

    Returns:
        bool: True si todos los elementos son verdaderos
            False: si algun elemento es falso
    """


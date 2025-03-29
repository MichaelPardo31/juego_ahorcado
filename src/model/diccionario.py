import random
class Diccionario:
    """
    Utliza las palabras desde el archivo palabras.txt
    Attributes: 
        palabras: trae las palabras del archivo
    """
    def __init__(self):
        """
            Inicializa una instancia de la clase Diccionario.
        """
        self.palabras: list[str] = self.__cargar_palabras()

    def __cargar_palabras(self) -> list[str]:
        """
        carga las palabras desde el archivo
        Returns:
            list[str]: de palabras 
        """
        palabras = []
        with open("assets/palabras.txt", "r", encoding="utf8") as archivo:
            for line in archivo:
                palabras.append(line.strip())
        return palabras

    def obtener_palabra(self) -> str:
        indice_aleatorio = random.randint(0, len(self.palabras) - 1)
        return self.palabras[indice_aleatorio]

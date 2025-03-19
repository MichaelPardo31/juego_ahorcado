import random


class Diccionario:
    """
    Representa: una estructura de datos que almacena palabras desde un archivo

    Attributes: 
        Inicializa una instancia de la clase Diccionario, cargando las palabras desde un archivo

    """


    def __init__(self):
        """
            Inicializa una instancia de la clase Diccionario, cargando las palabras desde un archivo.
        """
        self.palabras: list[str] = self.__cargar_palabras()

    def __cargar_palabras(self) -> list[str]:
        """
        Devuelve:

        Returns:
            list[str]: palabras 
        """
       
        palabras = []
        with open("assets/palabras.txt", "r", encoding="utf8") as archivo:
            for line in archivo:
                palabras.append(line.strip())

        return palabras

    def obtener_palabra(self) -> str:
        """
        Devuelve: posicion de la letra(correcta que ingreso el ususario)


        Returns:
            str: posicion o indice_aleatorio

        """
        indice_aleatorio = random.randint(0, len(self.palabras) - 1)
        return self.palabras[indice_aleatorio]

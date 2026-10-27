"""implementá una función contar_paginas(lista_libros) que reciba la lista
y devuelva la suma de las páginas de todos los libros."""


class Libro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas

    def obtener_paginas(self):
        return self.paginas


l1 = Libro("Python", 150)
l2 = Libro("Java", 200)
l3 = Libro("SQL", 100)

libros = [l1, l2, l3]

def contar_paginas(lista_libros):
    acum=0
    for l in lista_libros:
        acum += l.obtener_paginas()
    return acum

print(contar_paginas(libros))

from funciones_trans import comenzar_transicion, the_estado_transicion, sustantivo_estado_transicion, verbo_estado_transicion, not_estado_transicion, estruct_bidimensional,estruct_bidimensional_completa, reset_estruct

from maquina_estado import MaquinaEstado

m = MaquinaEstado()
m.anadir_estado("Comenzar", comenzar_transicion)
m.anadir_estado("estado_the", the_estado_transicion)
m.anadir_estado("estado_sustantivo", sustantivo_estado_transicion)
m.anadir_estado("estado_verbo", verbo_estado_transicion)
m.anadir_estado("estado_not", not_estado_transicion)
m.anadir_estado("estado_negativo", None, estado_final=1)
m.anadir_estado("estado_positivo", None, estado_final=1)
m.anadir_estado("estado_error", None, estado_final=1)
m.fijar_empiezo("Comenzar")

m.ejecutar("Pablo are optimistic")
print(estruct_bidimensional)
reset_estruct()

m.ejecutar("The ball is not round")
print(estruct_bidimensional)
reset_estruct()

m.ejecutar("Edgar is")
print(estruct_bidimensional)
reset_estruct()

m.ejecutar("The bees are not Pablo")
print(estruct_bidimensional)
reset_estruct()

""""
m.ejecutar("Crows are lazy")
print(estruct_bidimensional)
reset_estruct()

m.ejecutar("Raul is not entertaining")
print(estruct_bidimensional)
reset_estruct()

m.ejecutar("The pirates are rude")
print(estruct_bidimensional)
reset_estruct()

m.ejecutar("The man is not polite")
print(estruct_bidimensional)
reset_estruct()
"""

""""
m.ejecutar("Kiko is good")
print(estruct_bidimensional)
reset_estruct()

m.ejecutar("Boys are not boring")
print(estruct_bidimensional)
reset_estruct()

m.ejecutar("The girl is great")
print(estruct_bidimensional)
reset_estruct()

m.ejecutar("The cows are not ugly")
print(estruct_bidimensional)
reset_estruct()
"""

"""
m.ejecutar("Cesar is ugly")
print(estruct_bidimensional)
reset_estruct()

m.ejecutar("Parrots are not fun")
print(estruct_bidimensional)
reset_estruct()

m.ejecutar("Parrots are not fun")
print(estruct_bidimensional)
reset_estruct()

m.ejecutar("Paco is not ddas")
print(estruct_bidimensional)
reset_estruct()

m.ejecutar("The bees is boring")
print(estruct_bidimensional)
reset_estruct()

m.ejecutar("The boy are not bad")
print(estruct_bidimensional)
reset_estruct()
"""
estruct_bidimensional_completa()

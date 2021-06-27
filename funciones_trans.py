import inflect
inflect = inflect.engine()

adjetivos_positivos = ["good", "great","super", "fun", "entertaining", "easy", "polite", "optimistic"]
adjetivos_negativos = ["boring", "difficult", "ugly", "bad", "fat", "cruel", "lazy", "rude"]

sustantivos_plurales = []

estruct_bidimensional = []

def funcion_transicion(estado, entrada, matriz):
  #entrada the
  if estado == 0 and entrada == 0:
    celda = [[estado, entrada], 1]
    matriz.append(celda)
  #entrada sustantivo
  elif estado == 0 and entrada == 1:
    celda = [[estado, entrada], 2]
    matriz.append(celda)    

  elif estado == 1 and entrada == 1:
    celda = [[estado, entrada], 2]
    matriz.append(celda)    
  #entrada are,is
  elif estado == 2 and entrada == 2:
    celda = [[estado, entrada], 3]
    matriz.append(celda)    
  #entrada not  
  elif estado == 3 and entrada == 3:
    celda = [[estado, entrada], 4]
    matriz.append(celda)   
  #entrada adj. pos
  elif estado == 3 and entrada == 6:
    celda = [[estado, entrada], 6]
    matriz.append(celda)

  elif estado == 4 and entrada == 6:
    celda = [[estado, entrada], 7]
    matriz.append(celda)                
  #entrada adj. neg
  elif estado == 3 and entrada == 7:
    celda = [[estado, entrada], 7]
    matriz.append(celda)

  elif estado == 4 and entrada == 7:
    celda = [[estado, entrada], 6]
    matriz.append(celda)      
  else:
    celda = [[estado, entrada], 5]
    matriz.append(celda)        

def estruct_bidimensional_completa():
  matriz = []

  for i in range(8):
    for j in range(5):
      funcion_transicion(j, i, matriz)
  print("Estructura bidimensional completa de la tabla de transiciones:")
  print(matriz)

def comenzar_transicion(txt):
    estado = 0

    texto_cortado = txt.split(None,1)
    palabra, txt = texto_cortado if len(texto_cortado) > 1 else (txt,"")

    if inflect.singular_noun(palabra):
      sustantivos_plurales.append(palabra)

    if palabra == "The":
        nuevoEstado = "estado_the"
        entrada = 0
    elif palabra:
        nuevoEstado = "estado_sustantivo"
        entrada = 1        
    else:
        nuevoEstado = "estado_error"
        entrada = 5
    
    funcion_transicion(estado, entrada, estruct_bidimensional)
    return (nuevoEstado, txt)

def the_estado_transicion(txt):
    estado = 1
    
    texto_cortado = txt.split(None,1)
    palabra, txt = texto_cortado if len(texto_cortado) > 1 else (txt,"")

    if inflect.singular_noun(palabra):
      sustantivos_plurales.append(palabra)

    if palabra:
        nuevoEstado = "estado_sustantivo"
        entrada = 1                
    else:
        nuevoEstado = "estado_error"
        entrada = 5        

    funcion_transicion(estado, entrada, estruct_bidimensional)        
    return (nuevoEstado, txt)

def sustantivo_estado_transicion(txt):
    estado = 2

    texto_cortado = txt.split(None,1)

    palabra, txt = texto_cortado if len(texto_cortado) > 1 else (txt,"")

    if palabra == "is" and len(sustantivos_plurales) > 0:
        nuevoEstado = "estado_error"
        entrada = 5
    elif palabra == "are" and len(sustantivos_plurales) > 0:
        nuevoEstado = "estado_verbo"
        entrada = 2
    elif palabra == "is" and len(sustantivos_plurales) == 0:
        nuevoEstado = "estado_verbo"
        entrada = 2
    else:
        nuevoEstado = "estado_error"
        entrada = 5

    if len(sustantivos_plurales) > 0:
      sustantivos_plurales.pop()

    funcion_transicion(estado, entrada, estruct_bidimensional)    
    return (nuevoEstado, txt)

def verbo_estado_transicion(txt):
    estado = 3

    texto_cortado = txt.split(None,1)
    palabra, txt = texto_cortado if len(texto_cortado) > 1 else (txt,"")

    if palabra == "not":
        nuevoEstado = "estado_not"
        entrada = 3
    elif palabra in adjetivos_positivos:
        nuevoEstado = "estado_positivo"
        entrada = 6
    elif palabra in adjetivos_negativos:
        nuevoEstado = "estado_negativo"
        entrada = 7
    else:
        nuevoEstado = "estado_error"
        entrada = 5

    funcion_transicion(estado, entrada, estruct_bidimensional)            
    return (nuevoEstado, txt)

def not_estado_transicion(txt):
    estado = 4

    texto_cortado = txt.split(None,1)
    palabra, txt = texto_cortado if len(texto_cortado) > 1 else (txt,"")
    
    if palabra in adjetivos_positivos:
        nuevoEstado = "estado_negativo"
        entrada = 6
    elif palabra in adjetivos_negativos:
        nuevoEstado = "estado_positivo"
        entrada = 7
    else:
        nuevoEstado = "estado_error"
        entrada = 5

    funcion_transicion(estado, entrada, estruct_bidimensional)    

    return (nuevoEstado, txt)

def reset_estruct():
  del estruct_bidimensional[:]
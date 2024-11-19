
def leer_archivo():
    array = []
    with open("log.txt", "r") as archivo:
        contenido = archivo.readlines()
        for contra in contenido:
            if "\n" in contra:
                var = contra.replace("\n", "")
                array.append(var)
            else:
                array.append(contra)
    return array

def calcular_si_es_contrasena(array):
    contador_si = 0
    contador_no = 0

    for contra in array:
        es_numero = False
        es_letra = False
        es_contra = True

        numero_act = 0
        letra_act = ""

        for digito in contra:
            if digito.isdigit():
                digito_int = int(digito)
                if not es_letra and not es_numero:
                    numero_act = digito_int
                    es_numero = True
                elif es_numero and not es_letra:
                    if numero_act <= digito_int:
                        numero_act = digito_int
                    else:
                        contador_no += 1
                        es_contra = False
                        break
                else:
                    contador_no += 1
                    es_contra = False
                    break
            elif digito.isalpha():
                if not es_letra and not es_numero:
                    letra_act = digito
                    es_letra = True
                elif es_letra or not es_letra:
                    if letra_act <= digito:
                        letra_act = digito
                        es_letra = True
                    else:
                        contador_no += 1
                        es_contra = False
                        break
                else:
                    contador_no += 1
                    es_contra = False
                    break
        
        if es_contra:
            contador_si += 1
    
    print("Si", contador_si, "No", contador_no)
calcular_si_es_contrasena(leer_archivo())
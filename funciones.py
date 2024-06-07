import json

def print_menu(bandera): #alt+z
    if bandera == False:
        print(f"\n1. Leer archivo JSON.\n")
    elif bandera == True:
        print(f"\n2. Tabla con datos\n"
            "3. Guardar el listado ordenado en un CSV. Pedir el nombre del archivo al usuario.\n"
            "4. Mostrar servicios seleccionados\n"
            "5. Mostrar Servicios ordenados de manera ascendente\n"
            "6. Guardar en archivo json los servicios del punto anterior\n"
            "7. Salir\n")

def validar_datos():
    opciones = input("Elija alguna de las opciones: ")
    if opciones.isdigit():
        retorno = opciones
    else:
        retorno = print("\nIngrese un dato valido\n")
    return retorno

#1
def funcion_leer_json_array(ubicacion_archivo:str):
    retorno = False
    try:
        with open(ubicacion_archivo, 'r') as archivo:
            datos = json.load(archivo)
            lista = datos
            retorno = lista
        return retorno
    except FileNotFoundError:
        return retorno
    except json.JSONDecodeError:
        return retorno
    

#2
def imprimir_diccionarios_en_listas(lista:list):
    """por parametro paso una lista y los diccionarios que estan en ella los imprimo

    Args:
        lista (list): en la lista hay diccionarios
    """
    print(f"id_servicio\t\tdescripcion\t\ttipo\t\tprecio Unitario\t\tcantidad\ttotalServicio")
    for dic in lista:
        print(f"{dic['id_servicio']:20}{dic['descripcion']:30}{dic['tipo']:14}\t{dic['precioUnitario']}\t\t{dic['cantidad']}\t\t{dic['totalServicio']}")


#3
#3) Asignar totales: Se deberá hacer uso de una función lambda que asignará a cada servicio el
#total calculado (totalServicio) de la siguiente forma: cantidad x precioUnitario.

def normalizar_datos(lista:list): #revisar
    """los datos de los diccionarios los pasa su respectivo type

    Args:
        lista (list): lista en donde estan los diccionarios con los datos

    Returns:
        _type_: la misma lista con los datos ya cambiado
    """
    if lista == []:
            normalizar_datos = False
    else:
        for personajes in lista:
            if type(personajes["cantidad"]) != int:
                personajes["cantidad"] = int(personajes["cantidad"])
                normalizar_datos = True
                #print(type(personajes["peso"]))
            if type(personajes["precioUnitario"]) != float:
                personajes["precioUnitario"] = float(personajes["precioUnitario"])
                normalizar_datos = True
            else:
                normalizar_datos = False
    if normalizar_datos == True:
        return lista #("Datos normalizados")
    elif normalizar_datos == False:
        return False


total = lambda cantidad, precio_unitario: cantidad*precio_unitario

def agregar_nueva_clave(lista,clave:str,clave_2:str,nueva_clave:str):
    """realiza un calculo a base de dos valores que estan en la clave pasada por parametro

    Args:
        lista (_type_): donde estan los diccionario
        clave (str): tiene que ser numerico
        clave_2 (str): tiene que ser numerico
    """
    for dic in lista:
        total_servicio = total(dic[clave],dic[clave_2])
        dic[nueva_clave] = total_servicio

#4
def si_(lista):
    if type(lista) == list:
        return True
    else:
        return False

def buscar_segun_una_condicion(lista:list,clave:str, valor:str):
    """busca dentro de la lista los diccionarios que tengan lo que buscamos, 
    de donde 'CLAVE' y que cosa 'VALOR'
    Args:
        lista (list): donde estan los valores
        clave (_type_): lo que quiero del diccionario
        valor (str): lo que quiero de la clave 

    Returns:
        _type_: una lista con los diccionarios que cumplan con el criterio
    """
    lista_nueva = []
    if si_(lista) == True:
        for diccionario in lista:
            if diccionario[clave] == valor:
                lista_nueva.append(diccionario)
        return lista_nueva
    
def crear_json(nombre_archivo:str,data:list):
    """creo un archivo json 

    Args:
        nombre_archivo (str): el nombre que quiero que tenga el archivo
        data (list): lo que quiero que tenga
    """
    nombre_archivo += ".json"
    with open(nombre_archivo,"w") as file:
        json.dump(data,file,indent=4)

#5
def ordenamiento_ascendente_descendente(lista:list, clave:str,ordenamiento:bool):
    """recorre la lista y oredena segun parametro ingesado,
    puede ser de forma ascendente o descendente 

    Args:
        lista (list): lista de los personajes
        clave (str): puede ser cualquier key de los diccionarios    
        ordenamiento (bool): se ingresa TRUE si es ascendete y FALSE si es descendente

    Returns:
        _type_: una nueva lista con las condiciones
    """
    if si_(lista) == True:
        return sorted(lista, key = lambda x: x[clave],reverse= ordenamiento) 
    else:
        return False
    
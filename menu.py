from funciones import *

def menu_opciones():
    bandera_menu_opciones = True
    bandera_print_menu_opciones = False
    lista_creada = False
    while bandera_menu_opciones:
        print_menu(bandera_print_menu_opciones)
        dato = validar_datos()
        if dato == "1":
            lista_servicios = funcion_leer_json_array("data.json")
            bandera_print_menu_opciones = True
        else:
            if bandera_menu_opciones == False:
                print("primero valide los datos")
            else:
                if dato == "2":
                    imprimir_diccionarios_en_listas(lista_servicios)
                elif dato == "3": #problema (deep?)
                    normalizar_datos(lista_servicios)
                    agregar_nueva_clave(lista_servicios,'cantidad','precioUnitario','totalServicio')
                elif dato == "4":
                    lista_con_condicion = buscar_segun_una_condicion(lista_servicios,'descripcion','cierre pantalon')
                    crear_json("nueva_json",lista_con_condicion)
                elif dato == "5":
                    lista_ordenada = ordenamiento_ascendente_descendente(lista_servicios,'descripcion',True)
                    lista_creada = True
                    imprimir_diccionarios_en_listas(lista_ordenada)
                elif dato == "6":
                    if lista_creada == True:
                        crear_json("lista_ordenada",lista_ordenada)
                    else:
                        print("Crear lista ordenada primero")
                elif dato == "7":
                    bandera_menu_opciones = False
                else:
                    print("No coincide con ninguna opción\n")

menu_opciones()
from prettytable import PrettyTable
from datetime import datetime
from openpyxl import load_workbook
from logo import logo
from matplotlib import pyplot as plt
from os.path import abspath

class Tarea:
    def __init__(self, titulo, fecha_creacion, fecha_limite):
        self.id = 1
        self.titulo = titulo
        self.fecha_creacion = fecha_creacion
        self.fecha_limite = fecha_limite
        self.completado = "❌"

absoluta = abspath("proyecto\\tareas.xlsx")

wb = load_workbook(absoluta)
ws = wb.active
tarea = Tarea(1,'', '')

columnas = ['Id. de Tarea', 'Título', 'Fecha de creación', 'Fecha límite', 'Completada']
tabla_tarea = PrettyTable(columnas)
    
def actualizar_tabla():
     
    actualizar_identificadores()
      
    tabla_tarea.clear_rows()
    for fila in ws.iter_rows():
        valores = []
        for celda in fila:
            valores.append(celda.value)
        tabla_tarea.add_row(valores)
    print(tabla_tarea)

def actualizar_identificadores():
     identificador = 1
     for fila in ws.iter_rows(min_row=1, max_col=1):
        for celda in fila:
            celda.value = identificador
            identificador+=1
            wb.save(absoluta)

def ingrese_fecha_limite():
    dia_limite = int(input("Ingrese el día de la fecha límite: "))
    mes_limite = int(input("Ingrese el mes de la fecha límite: "))
    anio_limite =  int(input("Ingrese el año de la fecha límite: "))
    return datetime(anio_limite, mes_limite, dia_limite)

def diferencia_dias(fecha_limite, fecha_creacion):

    dia_creacion = fecha_creacion.date()
    dia_limite = fecha_limite.date()
    diferencia_dias = dia_limite - dia_creacion
    print(f"Tienes {diferencia_dias.days} días para completar la tarea")

def agregar_tarea():
    fecha_creacion = datetime.now()
    print("Proporcione la fecha límite para realizar esta tarea. ")

    fecha_limite = ingrese_fecha_limite()

    diferencia_dias(fecha_limite, fecha_creacion)

    tarea.titulo = input('Inserte el titulo de la tarea: ')
    tarea.fecha_creacion = fecha_creacion
    tarea.fecha_limite = fecha_limite
    ws.append((tarea.id, tarea.titulo, tarea.fecha_creacion.strftime("%d-%m-%Y"), tarea.fecha_limite.strftime("%d-%m-%Y"), tarea.completado))
    wb.save(absoluta)

#✅
#❌

def eliminar_fila(id):
    for fila in ws.iter_rows(min_row=1, max_col=1):
        for celda in fila:
            if celda.value == id:
                ws.delete_rows(celda.row)
                wb.save(absoluta)
                return True

def editar_fila(id, editar_titulo, editar_fecha, completada):
    if id <= ws.max_row:
        
        fila = ws[id]
        if editar_titulo == 's':
            fila[1].value = input("Ingrese el titulo de la tarea: ")
        if editar_fecha == 's':
            fila[3].value = ingrese_fecha_limite().strftime("%d-%m-%Y")
        if completada == 's':
            fila[4].value = '✅'
        else:
            fila[4].value = '❌'

        wb.save(absoluta)
    else:
        print("Ingrese un identificador valido.")

def mostrar_estadistica():
    
    etiquetas = ["Tareas completadas", "Tareas No completadas"]
    tareas_totales = ws.max_row
    tareas_completadas = 0

    for fila in ws.iter_rows(min_row=1, min_col=5, max_col=5):
        for celda in fila:
            if celda.value == '✅':
                tareas_completadas+=1

    tareas_faltantes = tareas_totales-tareas_completadas

    tareas_completadas/=tareas_totales*100
    tareas_faltantes/=tareas_totales*100
    valores = [tareas_completadas, tareas_faltantes]
    exp = (0.1,0.1)
    ax1 = plt.subplots()
    ax1.pie(valores, explode=exp, labels=etiquetas, autopct='%1.1f%%', shadow=True, startangle=90)

    ax1.axis('equal')
    plt.title("Estadísticas de tareas")
    plt.legend()
    plt.show()

print(logo)
actualizar_tabla()
print('')

seguir_ejecutando = True

while seguir_ejecutando:

    respuesta_usuario = input('¿Qué desea hacer? a: Agregar tarea | b: Eliminar | c: Editar | e: Mostrar estadística | s: Salir: ')

    if respuesta_usuario == 'a':
        agregar_tarea()

    elif respuesta_usuario == 'b':

        dato_eliminar = int(input("Ingrese el Id. de la tarea a eliminar: "))
        if eliminar_fila(dato_eliminar):
            print("Tarea eliminada exitosamente :)")
        else:
            print("No se ha podido eliminar la fila :(")

    elif respuesta_usuario == 'c':

        dato_editar = int(input("Ingrese el Id. del dato que desea modificar: "))

        editar_titulo = input('¿Desea editar el titulo? s/n: ')
        editar_fecha = input('¿Desea editar la fecha limite? s/n: ')
        completada = input('¿Ya completaste la tarea? s/n: ')

        editar_fila(dato_editar, editar_titulo, editar_fecha, completada)
    
    elif respuesta_usuario=='e':
        mostrar_estadistica()
    elif respuesta_usuario == 's':
        seguir_ejecutando = False
    else:
        print("Seleccione una opción válida.")
    actualizar_tabla()

wb.close()

print('\x1b[6;30;42m' + 'Gracias por usar el programa!' + '\x1b[0m')

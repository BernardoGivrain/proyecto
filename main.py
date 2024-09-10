from prettytable import PrettyTable
from tarea import Tarea
from datetime import datetime
from openpyxl import Workbook, load_workbook
from logo import logo

wb = load_workbook('C:/Users/Givrain/OneDrive/Escritorio/Primer Semestre - tec/Pensamiento/proyecto/tareas.xlsx')
ws = wb.active
tarea = Tarea(1,'', '')
tabla_tarea = PrettyTable(['Id. de Tarea', 'Título', 'Fecha de creación', 'Fecha límite', 'Completada'])
    
def actualizar_tabla():

    tabla_tarea.clear_rows()
    for data in ws.iter_rows():
        
        tabla_tarea.add_row([data[0].value, data[1].value, data[2].value, data[3].value, data[4].value])

    print(tabla_tarea)

def diferencia_dias(fecha_limite, fecha_creacion):

    dia_creacion = fecha_creacion.date()
    dia_limite = fecha_limite.date()
    diferencia_dias = dia_limite - dia_creacion
    print(f"Tienes {diferencia_dias.days} días para completar la tarea")

def agregar_tarea():
    fecha_creacion = datetime.now()

    print("Proporcione la fecha límite para realizar esta tarea. ")

    dia_limite = int(input("Ingrese el día de la fecha límite: "))
    mes_limite = int(input("Ingrese el mes de la fecha límite: "))
    anio_limite =  int(input("Ingrese el año de la fecha límite: "))
    fecha_limite = datetime(anio_limite, mes_limite, dia_limite)

    diferencia_dias(fecha_limite, fecha_creacion)

    tarea.titulo = input('Inserte el titulo de la tarea: ')
    tarea.fecha_creacion = fecha_creacion
    tarea.fecha_limite = fecha_limite
    ws.append((tarea.id, tarea.titulo, tarea.fecha_creacion, tarea.fecha_limite, tarea.completado))
    wb.save('C:/Users/Givrain/OneDrive/Escritorio/Primer Semestre - tec/Pensamiento/proyecto/tareas.xlsx')

def eliminar_fila(id):
    for fila in ws.iter_rows(min_row=1, max_col=1):
        for celda in fila:
            if celda.value == id:
                ws.delete_rows(celda.row)
                return True
    
    

def editar_fila():
    pass

print(logo)
actualizar_tabla()
print('')


seguir_ejecutando = True

while seguir_ejecutando:

    respuesta_usuario = input('¿Qué desea hacer? a: agregar tarea b: eliminar c: editar s: salir: ')

    if respuesta_usuario == 'a':
        agregar_tarea()
    elif respuesta_usuario == 'b':
        dato_eliminar = int(input("Ingrese el Id. de la tarea a eliminar: "))

        if eliminar_fila(dato_eliminar):
            print("Celda eliminada exitosamente.")
 

    elif respuesta_usuario == 'c':
        editar_fila()
    elif respuesta_usuario == 's':
        seguir_ejecutando = False
    else:
        print("Seleccione una opción válida.")

    actualizar_tabla()

wb.close()

print('Gracias por usar el programa!')







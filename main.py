from prettytable import PrettyTable
from tarea import Tarea
from datetime import datetime
from openpyxl import load_workbook
from logo import logo

wb = load_workbook('C:/Users/Givrain/OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey/Desktop/Primer Semestre - tec/Pensamiento/proyecto/tareas.xlsx')
ws = wb.active
tarea = Tarea(1,'', '')
tabla_tarea = PrettyTable(['Id. de Tarea', 'Título', 'Fecha de creación', 'Fecha límite', 'Completada'])
    
def actualizar_tabla():
     
     actualizar_identificadores()
     
     tabla_tarea.clear_rows()
     for data in ws.iter_rows():
        tabla_tarea.add_row([data[0].value, data[1].value, data[2].value, data[3].value, data[4].value])


     print(tabla_tarea)

def actualizar_identificadores():
     identificador = 1
     for fila in ws.iter_rows(min_row=1, max_col=1):
        for celda in fila:
            celda.value = identificador
            identificador+=1
            wb.save('C:/Users/Givrain/OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey/Desktop/Primer Semestre - tec/Pensamiento/proyecto/tareas.xlsx')

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
    wb.save('C:/Users/Givrain/OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey/Desktop/Primer Semestre - tec/Pensamiento/proyecto/tareas.xlsx')

#✅
#❌

def eliminar_fila(id):
    for fila in ws.iter_rows(min_row=1, max_col=1):
        for celda in fila:
            if celda.value == id:
                ws.delete_rows(celda.row)
                wb.save('C:/Users/Givrain/OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey/Desktop/Primer Semestre - tec/Pensamiento/proyecto/tareas.xlsx')
                return True

def editar_fila(id, editar_titulo, editar_fecha, completada):
    if id <= ws.max_row:
        fila = ws[id]

        if editar_titulo == 's':
            fila[1].value = input("Ingrese el titulo de la tarea: ")
        if editar_fecha == 's':
            fila[3].value = ingrese_fecha_limite()
        if completada == 's':
            fila[4].value = '✅'
        else:
            fila[4].value = '❌'

        wb.save('C:/Users/Givrain/OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey/Desktop/Primer Semestre - tec/Pensamiento/proyecto/tareas.xlsx')
    else:
        print("Ingrese un identificador valido.")
    

print(logo)
actualizar_tabla()
print('')

seguir_ejecutando = True

while seguir_ejecutando:

    respuesta_usuario = input('¿Qué desea hacer? a: agregar tarea | b: eliminar | c: editar | s: salir: ')

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

    elif respuesta_usuario == 's':
        seguir_ejecutando = False
    else:
        print("Seleccione una opción válida.")
    actualizar_tabla()

wb.close()

print('\x1b[6;30;42m' + 'Gracias por usar el programa!' + '\x1b[0m')






lista_estudiantes=["ernesto","juan","andres","mafe","nicolas"]

lista_calificaciones=[45,10,30,35,44]

lista_asignaturas=["AL","PC","CD","PC","CD"]

# dic_est={"Ernesto":4.5,
#                  "Juan":1.0,
#          "Juan":1.5
#                  }
dic_est={"ernesto":[4.5,"AL"]}
nombre=input("escriba nombre")
# print("el estudiante", nombre, "sacó", dic_est[nombre])
for i in dic_est.keys():
    print("estudiante",i,"sacó",dic_est[i])
    

# for  i,element in enumerate(lista_estudiantes):
#     print(i)
#     print(element)
# list(enumerate(lista_estudiantes))
# list(range(5,17))

# def  buscar(persona,lista_estudiantes):
#     for  pos,element in enumerate(lista_estudiantes):
#         if persona==element:
#             return (pos)
# est=input("buscar nombre")
# resultado=buscar(est,lista_estudiantes)
# 
# if resultado==None:
#     print("No existe")
# else:
#     nota=lista_calificaciones[resultado]
#     materia=lista_asignaturas[resultado]
#     print("El estudiante",est,"sacó",nota,"en",materia)

# perdio=[]
# # perdio=perdio+["juan"]
# perdio+=["juan"]
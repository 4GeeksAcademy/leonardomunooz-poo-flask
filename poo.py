class Human:
   def __init__(self,nombre,apellido,edad,color_piel):
      self.nombre = nombre
      self.apellido = apellido
      self.edad = edad
      self.color_piel = color_piel
      self.caminando = True  # con esta variable cambio el valor del metodo informacion 

   def __repr__(self) :
      return "esta es la representacion de Human"
   
   def saludar(self):
      print(f"Hola que tal {self.nombre} {self.apellido} ?")

   def despedirse(self):
      print(f"Hasta luego, {self.nombre} {self.apellido}")

   def informarcion(self):
      if self.caminando:
         print(f"El senior {self.nombre} se encuentra caminando")
      else:
        print(f"el senior {self.nombre} se ha detenido en stop")

      print(
         f"Nombre: {self.nombre}"
         f"\nApellido: {self.apellido}"
         f"\nEdad: {self.edad}"
         f"\nColor de piel: {self.color_piel}"
      
      )

   def serialize(selt):
      return {
         "nombre": selt.nombre,
         "apellido": selt.apellido
      }
      
    
   def caminar(self,data): # con este metodo puedo cambiar el valor de la clase de manera dinamica
      self.caminando = data


class Trabajador(Human):
   def __init__(self, salario, profesion,human_nombre,human_apellido,human_edad,human_color_piel):
         super().__init__(human_nombre,human_apellido,human_edad,human_color_piel)
         self.salario = salario
         self.profesion = profesion

   def informarcion(self):
      super().informarcion()
      print(
         f"salario: {self.salario}"
         f"\nprofesion: {self.profesion}"
      )
     
# instancia de la clase humano1 

arr = []
leonardo = Human("jose","alvarez",21,"claro")
# leonardo.saludar()
# leonardo.despedirme()
leonardo.informarcion()
print("********************************************")
leonardo.caminar(False)
leonardo.informarcion()


# instancia trabajador que hereda de humano 

print("*"*80)
trabajador_deimian = Trabajador(1500,"presidente","jose","trump",58, "blanco")
trabajador_raul  = Trabajador(150,"Operador de produccion","raul","manzanarez",36,"oscuro")
trabajador_deimian.informarcion()
print("*"*80)
trabajador_raul.caminar(False)
trabajador_raul.informarcion()

print("*"*80)

arr.append(trabajador_raul)
arr.append(trabajador_deimian)


for person in arr:
   print(person.serialize())
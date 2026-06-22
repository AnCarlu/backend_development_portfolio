from abc import ABC, abstractmethod

class Model():

    @property
    @abstractmethod 
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(cls, _id):
        print(f'buscando por id {_id} en la tabla {cls.tabla}')

class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print(f'Guardando {self.tabla} en BBDD')
        

usuario= Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)
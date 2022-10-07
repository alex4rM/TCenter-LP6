class Usuario:
    def __init__(self,name,dni,correo,telefono):
        self.name = name
        self.dni = dni
        self.correo = correo
        self.telefono = telefono
    
    def toDBCollection(self):
        return{
            'name':self.name,
            'dni':self.dni,
            'correo':self.correo,
            'telefono':self.telefono
        }
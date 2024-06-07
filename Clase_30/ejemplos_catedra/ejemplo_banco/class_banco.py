from class_cuenta import Cuenta

class Banco:
    def __init__(self, nom):
        self.nombre= nom
        self.clientes= [] # Acá que voy a almacenar los datos de mis cuentas

    def agregar_cliente(self, cue): # TO-DO: agregar cliente a la lista clientes
        self.clientes.append(cue)

    def __str__(self):
        # TO-DO: devolver todos los clientes
        texto = ''
        texto+= f'Banco: {self.nombre}' + '\n'
        if len(self.clientes)==0:
            texto+= 'El Banco no tiene clientes aún.'
        else:
            texto+= 'Listado de clientes:' + '\n'
            for cli in self.clientes:
                texto+= str(cli) + '\n'
        texto+= '\n'
        return texto

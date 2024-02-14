class Tienda:
    '''
    Clase de cada tienda de mi negocio de electrodomésticos

    Attributes:
        tipo (str): Tipo de productos en venta
        abierta (bool): Defina si está abierta al público
    '''

    tipo = "Electrodomésticos"
    abierta = True

    def __init__(self, nombre, direccion, n_empleados, ventas_3m):
        '''
        Args:
            nombre (str): Nombre de la tienda
            direccion (str): Dirección de la tienda
            n_empleados (int): Número de empleados trabajando en la tienda
            ventas_3m (list): Contiene el número de artículos vendidos en los últimos 3 meses
        '''
        self.nombre = nombre
        self.direccion = direccion
        self.n_empleados = n_empleados
        self.ventas_3m = ventas_3m

    def ventas_totales(self):
        '''
        Devuelve las ventas totales de los últimos 3 meses de la tienda
        '''
        return sum(self.ventas_3m)
    
    def media_ventas(self):
        '''
        Devuelve la media de las ventas totales de los últimos 3 meses por empleado
        '''
        return self.ventas_totales() / self.n_empleados
    
    def info_tienda(self):
        '''
        Devuelve la información de nombre y dirección de la tienda
        '''
        return self.nombre + " " + self.direccion
    
    def ult_ventas(self):
        '''
        Devuelve las ventas del último mes.
        '''
        return self.ventas_3m[-1]

    def inv_mark(self, inv:int):
        '''
        Calcula la proyección de las ventas en función a un presupuesto invertido en marketing.

        Args:
            inv (int): importe de inversión en marketing

        Returns:
            list con la proyección de las ventas de los últimos 3 meses.
        '''
        # Comprueba el importe de la inversión para actualizar ventas con mayor o menor procentaje
        if inv < 1000:
            # Es una list comprehension que recorre los valores originales y los actualiza * 1.2
            self.ventas_3m = [1.2 * x for x in self.ventas_3m]
        else:
            self.ventas_3m = [1.5 * x for x in self.ventas_3m]
        return self.ventas_3m
    
class Perro:

    '''
    Clase para modelar los perros de mi perrera

    Attributes:
        patas (int): númera de patas
        orejas (int): número de orejas
        ojos (int): número de ojos
        velocidad (float): velocidad en Km/h a la que va el perro
    '''
    
    patas = 4
    orejas = 2
    ojos = 2
    velocidad = 0

    def __init__(self, raza, pelo="Marrón", dueño=False):
        '''
        Args:
            raza (str): Raza del perro
            pelo (str): Color del pelo
            dueño (bool): Indicador de si tiene dueño
        '''
        self.raza = raza
        self.pelo = pelo
        self.dueño = dueño

    def andar(self, aumento_v:float):
        '''
        Hace andar al perro añadiendole una velocidad
        
        Args:
            aumento_v (float): aumento de la velocidad del perro
        Returns:
            str con la velocidad a la que va el perro
        '''
        self.velocidad = self.velocidad + aumento_v
        return "Perro andando con velocidad de " + str(self.velocidad)
    
    def parar(self):
        '''
        Hace para al perro con una velocidad por tanto de 0

        Returns:
            str con la velocidad a la que va el perro de 0
        '''
        self.velocidad = 0
        return "Perro parado con velocidad de " + str(self.velocidad)

    def ladrar(self, msg:str):
        '''
        El perro ladra, con un mensaje

        Args:
            msg (str): mensaje que ladra el perro
        Returns:
            str con un ladrido y el mensaje
        '''
        return "GUAU! " + msg

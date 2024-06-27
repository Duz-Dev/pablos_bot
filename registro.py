import logging

class Registro(logging.Logger):
    """
    Configura y maneja los registros
    
    Parámetros
    -
    - nombre: str -> nombre del archivo desde donde sucede el registro
    """
    
    # Indicador de instancia de esta clase
    _instancia = None
    
    # Formato global para los registros
    formato = logging.Formatter("""
Hora: %(asctime)s
Archivo: %(filename)s
Función: %(funcName)s
Registro: %(message)s                                
""")
    
    def __new__(cls, nombre: str):
        """Gestiona la creacion de instancias de esta clase"""
        
        # No hay una instancia creada
        if cls._instancia is None:
            # Nueva instancia
            cls._instancia = super().__new__(cls)
            
            # Pasa el nombre el metodo init de la instancia creada
            cls._instancia.__init__(nombre=nombre)
        
        # El atributo nombre es diferente al actual
        elif cls._instancia.nombre != nombre:
            # Establece el nuevo nombre a la instancia actual
            cls._instancia.nombre = nombre
        
        # Retorna la instancia actual
        return cls._instancia
    
    def __init__(self, nombre: str):
        super().__init__(name=nombre)
        # Nombre del resgistro
        self.nombre = nombre
        
        # Establece el nivel de los registros
        self.setLevel(logging.INFO)
        
        # Manejador de registros
        manejador = logging.StreamHandler()
        
        # Establece el formato al manejador de registros
        manejador.setFormatter(self.formato)
        
        # Añade el manejador al registro actual
        self.addHandler(manejador)
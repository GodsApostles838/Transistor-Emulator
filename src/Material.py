class Material:
    """
    A class representing a semiconductor material with its thermal and electrical properties.
    """
    
    def __init__(self, name: str, thermal_conductivity: float, resistivity: float, melting_point: float) -> None:
        """
        Initializes a material with its properties.

        :param name: Name of the material
        :param thermal_conductivity: Thermal conductivity in W/m·K
        :param resistivity: Electrical resistivity in Ω·m
        :param melting_point: Melting point in degrees Celsius
        """
        self.name = name
        self.thermal_conductivity = thermal_conductivity  # W/m·K
        self.resistivity = resistivity  # Ω·m
        self.melting_point = melting_point  # °C


SILICON = Material("Silicon", thermal_conductivity=150, resistivity=2.3e3, melting_point=1414)
GERMANIUM = Material("Germanium", thermal_conductivity=60, resistivity=4.6e-1, melting_point=938)
GALLIUM_ARSENIDE = Material("Gallium Arsenide", thermal_conductivity=55, resistivity=1e8, melting_point=1238)

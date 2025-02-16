class Transistor:
    """
    A class representing a transistor with thermal properties.

    Attributes:
        material: Object representing the transistor's material properties.
        max_junction_temp (float): Maximum allowable junction temperature before failure.
        ambient_temp (float): The ambient temperature in degrees Celsius (default is 25°C).
        junction_temp (float): Current junction temperature.
        power_dissipation (float): Power dissipated by the transistor.
        aging_factor (float): Factor affecting transistor degradation over time.
    """

    def __init__(self, material, max_junction_temp, ambient_temp=25):
        """
        Initializes the Transistor object.

        Args:
            material: Object containing material properties, including melting point.
            max_junction_temp (float): The maximum allowable junction temperature.
            ambient_temp (float, optional): The surrounding temperature (default is 25°C).
        """
        self.material = material
        self.max_junction_temp = max_junction_temp
        self.junction_temp = ambient_temp
        self.ambient_temp = ambient_temp
        self.power_dissipation = 0
        self.aging_factor = 1.0

    def calculate_junction_temp(self, power_dissipation, thermal_resistance):
        """
        Calculates and updates the junction temperature based on power dissipation
        and thermal resistance.

        Args:
            power_dissipation (float): The power dissipated by the transistor in watts.
            thermal_resistance (float): The thermal resistance in °C/W.

        Returns:
            float: The updated junction temperature.
        """
        self.junction_temp = self.ambient_temp + (power_dissipation * thermal_resistance)
        return self.junction_temp

    def check_failure(self):
        """
        Checks whether the transistor has exceeded its safe temperature limits.

        Returns:
            str: A status message indicating whether the transistor is operational, 
                 has exceeded its maximum temperature, or has melted.
        """
        if self.junction_temp >= self.material.melting_point:
            return "Catastrophic failure: Transistor melted!"

        elif self.junction_temp >= self.max_junction_temp:
            return "Warning: Junction temperature exceeded maximum limit!"

        return "Operational"

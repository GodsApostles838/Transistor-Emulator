class TemperatureSimulator:
    """
    A class that simulates the temperature behavior of a transistor based on power dissipation
    and thermal resistance.
    """

    def __init__(self, transistor, thermal_resistance: float = 0.5) -> None:
        """
        Initializes the temperature simulator.

        :param transistor: The transistor instance being simulated
        :param thermal_resistance: Thermal resistance in °C/W (default: 0.5)
        """
        self.transistor = transistor
        self.thermal_resistance = thermal_resistance

    def update_temperature(self, power_dissipation: float, airflow: float = 0) -> float:
        """
        Updates the junction temperature of the transistor based on power dissipation and airflow.

        :param power_dissipation: Power dissipation in watts
        :param airflow: Airflow coefficient (default: 0, meaning no additional cooling)
        :return: Updated junction temperature in degrees Celsius
        """
        effective_resistance = self.thermal_resistance / (1 + airflow)
        self.transistor.calculate_junction_temp(power_dissipation, effective_resistance)
        return self.transistor.junction_temp

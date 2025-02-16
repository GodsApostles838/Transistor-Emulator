from Temperature import TemperatureSimulator

class TransistorState:
    """
    A class representing the operational state of a transistor.

    Attributes:
        transistor: An instance of a transistor containing its physical properties.
        electrical: An object responsible for electrical calculations.
    """

    def __init__(self, transistor, electrical):
        """
        Initializes the TransistorState object.

        Args:
            transistor: An instance representing the transistor's physical properties.
            electrical: An object responsible for electrical calculations such as 
                        current gain and power dissipation.
        """
        self.transistor = transistor
        self.electrical = electrical

    def determine_state(self, v_be, v_ce):
        """
        Determines the operational state of the transistor based on input voltages.

        Args:
            v_be (float): Base-emitter voltage in volts.
            v_ce (float): Collector-emitter voltage in volts.

        Returns:
            tuple: A tuple containing:
                - str: The operational state ("Cutoff", "Saturation", or "Active").
                - float: The calculated collector current (i_c).
        """
        v_t = 0.02585  
        i_c = self.electrical.calculate_current_gain(v_be, v_ce)

        if v_be < 0.7:
            return "Cutoff", i_c  

        if v_ce < v_be:
            return "Saturation", i_c 

        return "Active", i_c  

    def operate(self, v_be, v_ce):
        """
        Simulates the transistor's operation, updating its state, power dissipation, 
        and temperature while checking for failures.

        Args:
            v_be (float): Base-emitter voltage in volts.
            v_ce (float): Collector-emitter voltage in volts.

        Returns:
            dict: A dictionary containing:
                - "state" (str): The transistor's operational state.
                - "i_c" (float): The collector current.
                - "power_dissipation" (float): The power dissipated by the transistor.
                - "temp" (float): The updated junction temperature.
                - "status" (str): The transistor's failure status.
        """
        state, i_c = self.determine_state(v_be, v_ce)
        power_dissipation = self.electrical.calculate_power_dissipation(v_ce, i_c)

        temp_simulator = TemperatureSimulator(self.transistor)
        temp = temp_simulator.update_temperature(power_dissipation)

        status = self.transistor.check_failure()

        return {
            "state": state,
            "i_c": i_c,
            "power_dissipation": power_dissipation,
            "temp": temp,
            "status": status,
        }

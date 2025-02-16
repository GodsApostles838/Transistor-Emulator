import math

class TransistorElectrical:
    """
    A class representing the electrical behavior of a transistor, specifically focusing on current gain
    and power dissipation calculations.
    """
    
    def __init__(self, beta: float = 100, v_early: float = 50) -> None:
        """
        Initializes the transistor with given parameters.
        
        :param beta: Current gain (h_FE) of the transistor (default: 100)
        :param v_early: Early voltage in volts (default: 50)
        """
        self.beta = beta  
        self.v_early = v_early  

    def calculate_current_gain(self, v_be: float, v_ce: float) -> float:
        """
        Calculates the collector current (I_C) based on the base-emitter voltage (V_BE) and
        collector-emitter voltage (V_CE), considering the Early effect.
        
        :param v_be: Base-emitter voltage in volts
        :param v_ce: Collector-emitter voltage in volts
        :return: Collector current (I_C) in amperes
        """
        v_t = 0.02585  
        i_c = self.beta * (math.exp(v_be / v_t)) * (1 + v_ce / self.v_early)
        return i_c

    def calculate_power_dissipation(self, v_ce: float, i_c: float) -> float:
        """
        Calculates the power dissipation of the transistor.
        
        :param v_ce: Collector-emitter voltage in volts
        :param i_c: Collector current in amperes
        :return: Power dissipation in watts
        """
        return v_ce * i_c

from rich.console import Console
from rich.table import Table
from rich.progress import track
from Material import SILICON
from Transistor import Transistor
from Electrical import TransistorElectrical
from TransistorState import TransistorState

console = Console()

def display_results(time_steps, results):
    """
    Displays the simulation results in a formatted table using Rich library.

    Args:
        time_steps (iterable): The time steps of the simulation.
        results (list): A list of dictionaries containing the simulation results for each time step.
    """
    # Create a table to display the results
    table = Table(title="Transistor Simulation Results", show_header=True, header_style="bold magenta")
    table.add_column("Time (s)", justify="right")
    table.add_column("State", justify="left")
    table.add_column("I_C (A)", justify="right")
    table.add_column("Power (W)", justify="right")
    table.add_column("Temp (°C)", justify="right")
    table.add_column("Status", justify="left")

    for t, result in zip(time_steps, results):
        table.add_row(
            f"{t}",
            result["state"],
            f"{result['i_c']:.6f}",
            f"{result['power_dissipation']:.4f}",
            f"{result['temp']:.2f}",
            result["status"],
        )

    console.print(table)

if __name__ == "__main__":
    """
    Main function to run the transistor simulation.

    Initializes the transistor, electrical, and state objects.
    Simulates the transistor's operation over time using different input voltages.
    Displays the results in a formatted table.
    """
    # Initialize the transistor with material (SILICON) and maximum junction temperature
    transistor = Transistor(material=SILICON, max_junction_temp=150)

    # Initialize the electrical properties of the transistor
    electrical = TransistorElectrical()

    # Create the transistor state object to manage transistor behavior
    transistor_state = TransistorState(transistor, electrical)

    # Define input voltages for base-emitter (v_be) and collector-emitter (v_ce)
    v_be_list = [0.7] * 50 + [0.6] * 50  # Base-emitter voltage profile
    v_ce_list = [t * 0.1 for t in range(100)]  # Collector-emitter voltage profile

    # Time steps for the simulation
    time_steps = range(0, 100)

    # Initialize an empty list to store simulation results
    results = []

    for t, v_be, v_ce in track(zip(time_steps, v_be_list, v_ce_list), description="Simulating..."):
        # Operate the transistor for the given v_be and v_ce values
        result = transistor_state.operate(v_be, v_ce)
        results.append(result)

    display_results(time_steps, results)
    input("Enter To Exit...")

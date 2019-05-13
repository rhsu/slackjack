from services.simulation_service import SimulationService
from services.roulette_service import RouletteService


def test_simulate():
    s = SimulationService(RouletteService())
    print("\n\n\nSimulation Starts...")
    print(s.simulate())


def test_flip():
    s = SimulationService(RouletteService())
    print("\n\n\nSimulaton Starts...")
    print(s.flip())

class SimulationController:
    def __init__(self, simulation_service):
        self.simulation_service = simulation_service

    def parse_command(self, command):
        command = command.lower()
        if command.startswith("simulate"):
            return self.simulation_service.simulate()
        elif command.startswith("flip"):
            return self.simulation_service.flip()

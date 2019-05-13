from controllers.simulation_controller import SimulationController
from test.mocks.mock_objects import MockSimulationService


def test_simulate():
    controller = SimulationController(MockSimulationService())
    response = controller.parse_command("simulate")
    assert "simulate" == response


def test_spin():
    controller = SimulationController(MockSimulationService())
    response = controller.parse_command("flip")
    assert "flip" == response

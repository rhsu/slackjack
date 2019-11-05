from services.red_snake_service import RedSnakeService
from test.mocks.mock_objects import MockRouletteService


def test_play(default_user_data):
    mock_roulette_service = MockRouletteService(1, "red")
    service = RedSnakeService(default_user_data, mock_roulette_service)
    

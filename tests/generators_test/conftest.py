import pytest
from src.generators.player import Player

@pytest.fixture
def get_player_generator():
    return Player()
import pytest

from catan_core.player.player import Player
from catan_core.player_hand import PlayerHand
from catan_core.resource_type.clay import Clay
from catan_core.resource_type.rock import Rock
from catan_core.resource_type.sheep import Sheep
from catan_core.resource_type.wheat import Wheat
from catan_core.resource_type.wood import Wood


class TestPlayerHand:
    def test_init_player(self):
        player = Player()
        player_hand = PlayerHand(player=player)
        assert player_hand.player == player

    def test_init_hand(self):
        player = Player()
        player_hand = PlayerHand(player=player)
        assert player_hand.hand[Clay] == 0
        assert player_hand.hand[Rock] == 0
        assert player_hand.hand[Sheep] == 0
        assert player_hand.hand[Wheat] == 0
        assert player_hand.hand[Wood] == 0

    def test_has_at_least_x_of_resource_type(self):
        player = Player()
        player_hand = PlayerHand(player=player)
        player_hand.hand[Clay] = 2
        assert player_hand.has(resource_type=Clay, count=2)

    def test_has_less_than_x_of_resource_type(self):
        player = Player()
        player_hand = PlayerHand(player=player)
        player_hand.hand[Clay] = 2
        assert not player_hand.has(resource_type=Clay, count=3)

    def test_add_raises_if_count_less_than_1(self):
        player = Player()
        player_hand = PlayerHand(player=player)
        with pytest.raises(
            RuntimeError, match="Cannot add 0 or less cards to the hand."
        ):
            player_hand.add(resource_type=Clay, count=0)

    def test_add_resources_to_hand(self):
        player = Player()
        player_hand = PlayerHand(player=player)
        player_hand.add(resource_type=Clay, count=10)
        assert player_hand.hand[Clay] == 10

    def test_remove_raises_if_count_less_than_1(self):
        player = Player()
        player_hand = PlayerHand(player=player)
        with pytest.raises(
            RuntimeError, match="Cannot remove 0 or less cards from the hand."
        ):
            player_hand.remove(resource_type=Clay, count=0)

    def test_remove_has_at_least_x_of_resource_type(self):
        player = Player()
        player_hand = PlayerHand(player=player)
        player_hand.hand[Clay] = 2
        removed_count = player_hand.remove(resource_type=Clay, count=1)
        assert removed_count == 1
        assert player_hand.hand[Clay] == 1

    def test_remove_has_less_than_x_of_resource_type(self):
        player = Player()
        player_hand = PlayerHand(player=player)
        player_hand.hand[Clay] = 2
        removed_count = player_hand.remove(resource_type=Clay, count=3)
        assert removed_count == 2
        assert player_hand.hand[Clay] == 0

    def test_can_buy_road(self):
        player = Player()
        player_hand = PlayerHand(player=player)

        assert not player_hand.can_buy_road()

        player_hand.hand[Clay] = 1
        player_hand.hand[Wood] = 1

        assert player_hand.can_buy_road()

    def test_can_buy_settlement(self):
        player = Player()
        player_hand = PlayerHand(player=player)

        assert not player_hand.can_buy_settlement()

        player_hand.hand[Wood] = 1
        player_hand.hand[Clay] = 1
        player_hand.hand[Wheat] = 1
        player_hand.hand[Sheep] = 1

        assert player_hand.can_buy_settlement()

    def test_can_buy_city(self):
        player = Player()
        player_hand = PlayerHand(player=player)

        assert not player_hand.can_buy_city()

        player_hand.hand[Rock] = 3
        player_hand.hand[Wheat] = 2

        assert player_hand.can_buy_city()

    def test_can_buy_development_card(self):
        player = Player()
        player_hand = PlayerHand(player=player)

        assert not player_hand.can_buy_development_card()

        player_hand.hand[Rock] = 1
        player_hand.hand[Sheep] = 1
        player_hand.hand[Wheat] = 1

        assert player_hand.can_buy_development_card()

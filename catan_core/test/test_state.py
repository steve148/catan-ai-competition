from catan_core.action import Action
from catan_core.board import Board
from catan_core.building.city import City
from catan_core.building.settlement import Settlement
from catan_core.development_card.deck import DevelopmentCardDeck
from catan_core.player.player import Player
from catan_core.player_hand import PlayerHand
from catan_core.resource_type.clay import Clay
from catan_core.resource_type.deck import ResourceCardDeck
from catan_core.resource_type.sheep import Sheep
from catan_core.resource_type.wheat import Wheat
from catan_core.resource_type.wood import Wood
from catan_core.road import Road
from catan_core.state import State


class TestState:
    """Tests for State class."""

    def test_init_resource_cards(self):
        """Check that initial state of game includes all resource cards."""
        state = State(players=["p1"])
        assert isinstance(state.resource_card_deck, ResourceCardDeck)

    def test_init_deck_of_development_cards(self):
        state = State(players=["p1"])
        assert isinstance(state.development_card_deck, DevelopmentCardDeck)

    def test_init_board(self):
        state = State(players=["p1"])
        assert isinstance(state.board, Board)

    def test_init_player_pieces(self):
        """Check that initial state of game includes pieces for each player."""
        state = State(players=["p1"])
        assert state.player_pieces == {
            "p1": {"cities": 4, "roads": 15, "settlements": 5}
        }

    def test_init_bonus_victory_points_tracker(self):
        state = State(players=["p1"])
        assert state.bonus_victory_points == {
            "p1": {
                "victory_point_development_cards": 0,
                "longest_road": False,
                "largest_army": False,
            }
        }

    def test_init_player_hands(self):
        state = State(players=["p1"])
        assert isinstance(state.player_hand["p1"], PlayerHand)

    def test_init_player_order_includes_all_players(self):
        players = ["p1", "p2", "p3", "p4"]
        state = State(players=players)
        for player in players:
            assert player in state.players

    def test_init_current_player_turn(self):
        players = ["p1", "p2", "p3", "p4"]
        state = State(players=players)
        assert state.current_player_turn == state.players[0]

    def test_init_dice_rolled(seslf):
        state = State(players=["p1"])
        assert not state.dice_rolled

    def test_is_game_over_no_player_won(self):
        state = State(players=["p1", "p2"])
        assert not state.is_game_over()

    def test_is_game_over_player_has_won(self):
        state = State(players=["p1", "p2"])

        state.board.vertices[0].building = City(player="p1")
        state.board.vertices[1].building = Settlement(player="p1")
        state.bonus_victory_points["p1"]["victory_point_development_cards"] = 3
        state.bonus_victory_points["p1"]["longest_road"] = True
        state.bonus_victory_points["p1"]["largest_army"] = True

        assert state.is_game_over() == "p1"

    def test_can_build_road_returns_nothing_if_player_missing_resources(self):
        player = Player()
        state = State(players=[player])
        assert state.can_build_road(player=player) == []

    def test_can_build_road_returns_possible_build_locations(self):
        player = Player()

        state = State(players=[player])
        state.player_hand[player].add(Wood, 1)
        state.player_hand[player].add(Clay, 1)

        state.board.edges[0].road = Road(player=player)

        assert state.can_build_road(player=player) == [
            Action(name="build_road", kwargs={"edge": state.board.edges[1]}),
            Action(name="build_road", kwargs={"edge": state.board.edges[6]}),
        ]

    def test_can_build_settlement_returns_nothing_if_player_missing_resources(self):
        player = Player()
        state = State(players=[player])
        assert state.can_build_settlement(player=player) == []

    def test_can_build_settlement_returns_nothing_if_no_vertices_available(self):
        player = Player()
        state = State(players=[player])

        for vertex in state.board.vertices:
            vertex.building = Settlement(player=player)

        assert state.can_build_settlement(player=player) == []

    def test_can_build_settlement_on_available_vertices(self):
        player = Player()
        state = State(players=[player])

        state.player_hand[player].add(resource_type=Sheep, count=1)
        state.player_hand[player].add(resource_type=Wheat, count=1)
        state.player_hand[player].add(resource_type=Wood, count=1)
        state.player_hand[player].add(resource_type=Clay, count=1)
        state.board.edges[0].assign_road(road=Road(player=player))

        assert state.can_build_settlement(player=player) == [
            Action(name="build_settlement", kwargs={"vertex": state.board.vertices[0]}),
            Action(name="build_settlement", kwargs={"vertex": state.board.vertices[1]}),
        ]

    def test_can_build_first_settlement_on_all_vertices_if_board_empty(self):
        player = Player()
        state = State(players=[player])

        assert len(state.can_build_first_settlement(player=player)) == 54

    def test_can_build_first_settlement_on_available_vertices(self):
        player = Player()
        other_player = Player()
        state = State(players=[player, other_player])

        state.board.vertices[-1].assign_building(
            building=Settlement(player=other_player)
        )

        assert len(state.can_build_first_settlement(player=player)) == 51
        assert state.can_build_first_settlement(player=player)[0] == Action(
            name="build_first_settlement", kwargs={"vertex": state.board.vertices[0]}
        )

    def test_can_build_starting_road(self):
        player = Player()
        state = State(players=[player])

        state.board.vertices[0].assign_building(building=Settlement(player=player))

        assert state.can_build_starting_road(player=player) == [
            Action(name="build_starting_road", kwargs={"edge": state.board.edges[0]}),
            Action(name="build_starting_road", kwargs={"edge": state.board.edges[6]}),
        ]

    def test_can_build_second_settlement(self):
        player = Player()
        other_player = Player()
        state = State(players=[player, other_player])

        state.board.vertices[-1].assign_building(
            building=Settlement(player=other_player)
        )

        assert len(state.can_build_second_settlement(player=player)) == 51
        assert state.can_build_second_settlement(player=player)[0] == Action(
            name="build_second_settlement", kwargs={"vertex": state.board.vertices[0]}
        )

    def test_player_actions_roll_dice_roll_if_not_done(self):
        state = State(players=["p1"])
        actions = state.player_actions(player=state.current_player_turn)
        assert Action(name="roll_dice") in actions

    def test_player_actions_no_roll_dice_if_already_done(self):
        state = State(players=["p1"])
        state.dice_rolled = True
        actions = state.player_actions(player=state.current_player_turn)
        assert Action(name="roll_dice") not in actions

    def test_player_actions_end_turn(self):
        state = State(players=["p1"])
        state.dice_rolled = True
        actions = state.player_actions(player=state.current_player_turn)
        assert Action(name="end_turn") in actions

    def test_build_first_settlement(self):
        player = Player()
        state = State(players=[player])
        state.build_first_settlement(player=player, vertex=state.board.vertices[0])

        assert state.board.vertices[0].building == Settlement(player=player)

    def test_build_second_settlement(self):
        player = Player()
        state = State(players=[player])
        vertex = state.board.vertices[0]
        resource_type = vertex.hexes[0].resource_type

        state.build_second_settlement(player=player, vertex=vertex)

        assert state.board.vertices[0].building == Settlement(player=player)

        actual_hand = state.player_hand[player]
        expected_hand = PlayerHand(player=player)
        expected_hand.add(resource_type=resource_type, count=1)

        assert actual_hand == expected_hand

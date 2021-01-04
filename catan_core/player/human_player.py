from typing import List

from catan_core.player.player import Player
from catan_core.state import Action


class HumanPlayer(Player):
    def __init__(self, name: str) -> None:
        self.name = name

    def choose_action(self, actions: List[Action]) -> Action:
        print(actions)
        i = int(input("Choose an action: "))
        return actions[i]

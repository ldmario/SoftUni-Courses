from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.player = []

    def assign_player(self, player: Player):
        if player in self.player:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.player.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.player:
            if player.name == player_name:
                self.player.remove(player)
                player.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        info = f"Guild: {self.name}"
        for player in self.player:
            info += f"\n{player.player_info()}"

        return info.strip()

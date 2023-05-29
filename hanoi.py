from tower_classes import Tower


class Game:
    def __init__(self):
        self.move_count = 0
        self.difficulty = 0

        # Game introduction, and difficulty prompting
        self.game_explanation()
        self.choose_difficulty()

        # Create and print the towers
        towers = self.start_towers()
        self.center_tower.add_disk(
            is_game_initialization=True, difficulty=self.difficulty
        )
        print(self.draw_towers(towers))

        # Make a move
        self.prompt_move(towers)

    def can_continue(self, answer):
        return answer == ""

    def game_explanation(self):
        objective = "Welcome to @lcsvoj's Towers of Hanoi!\nThe objective is to move all disks from the central rod to one of the other rods."
        rules = "Rules:\n1. Move only one disk at a time.\n2. Move a disk to the top of another stack or an empty rod.\n3. Never place a disk on top of a smaller disk."
        game_mechanism = "After each move, the remaining number of moves will be displayed. Use your moves wisely.\n\tGood luck, and don't f*ck it up!"
        introduction_content = [objective, rules, game_mechanism]

        for item in introduction_content:
            explanation = input(f"\n{item}\n\n[Press ENTER to continue] ")
            while not self.can_continue(explanation):
                explanation = input("[Press ENTER to continue] ")
        print()

    def choose_difficulty(self):
        min_level = 1
        max_level = 3
        while True:
            try:
                self.difficulty = int(
                    input(
                        f"Choose your difficulty level from {min_level} (easier) to {max_level} (harder). "
                    )
                )
                if min_level <= self.difficulty <= max_level:
                    break
                else:
                    print(f"Please enter a number between {min_level} and {max_level}.")
            except ValueError:
                print(f"Please enter a number between {min_level} and {max_level}.")
        self.difficulty += 2
        required_moves = 2**self.difficulty - 1

        print(f"\nIn this level, you'll have {required_moves} moves to reach the goal.")
        confirmation = input(
            "If you're ready for this challenge, [press ENTER to continue].\nIf you want to choose a different level, type anything else then press Enter. "
        )
        if not self.can_continue(confirmation):
            self.choose_difficulty()
        else:
            print("\nOk, let's begin! Here are the Towers of Hanoi: ")
            return

    def start_towers(self):
        self.left_tower = Tower(self.difficulty)
        self.center_tower = Tower(self.difficulty)
        self.right_tower = Tower(self.difficulty)
        towers = [self.left_tower, self.center_tower, self.right_tower]
        return towers

    def draw_towers(self, towers):
        recomposed_towers = "\n"
        for i in reversed(range(1, self.difficulty + 2)):
            for tower in towers:
                recomposed_towers += tower.tower_levels[i]["image"]
            recomposed_towers += "\n"
        recomposed_towers += towers[0].tower_levels[0]["image"] * 3 + "\n"
        recomposed_towers += "\n" + "        Tower 1        " + "        Tower 2        " + "        Tower 3        " + "\n"
        return recomposed_towers

    def prompt_move(self, towers):
        tower_options = {
            "1": self.left_tower,
            "Tower 1": self.left_tower,
            "2": self.center_tower,
            "Tower 2": self.left_tower,
            "3": self.right_tower,
            "Tower 3": self.left_tower,
        }
        
        from_tower = ""
        while from_tower.strip().capitalize() not in tower_options.keys():
            try:
                from_tower = input(
                    "Select the tower number to remove the top disk: "
                )
            except ValueError:
                pass

        to_tower = ""
        while to_tower.strip().capitalize() not in tower_options:
            try:
                to_tower = input(
                    "Now select the tower number to place the disk: "
                )
            except ValueError:
                pass

def main():
    new_game = Game()


if __name__ == "__main__":
    main()

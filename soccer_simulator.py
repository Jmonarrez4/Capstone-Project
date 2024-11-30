"""This is a Soccer Team Simulator that implements random scores, tactics, training methods,
and morale to help the user find success!
This program includes a promotion/relegation system as well."""

# Import the random library to use in the code.
# Nicknaming rn to make calling functions of the library easy.
import random as rn

# Define what Team is and what will be included in the final results.
# This will help keep track of wins, losses, ties.
# The overall points and goal difference will break up any ties in the final rankings.
class Team:
    """Determines what a team is and its attributes."""
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.goal_difference = 0
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.current_tactic = 'balanced' # Default tactic
        self.training_focus = None # Default training focus
        self.morale_boost = 'neutral' # Default morale boost

    def reset(self):
        """Resets the record, and team attributes after each season."""
        self.points = 0
        self.goal_difference = 0
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.current_tactic = 'balanced' # Reset tactic
        self.training_focus = None # Reset training focus
        self.morale_boost = 'neutral' # Reset morale boost

    # This is how the final standings will apper to the user.
    # The order is name: points, goal difference, wins, losses, ties.
    def __repr__(self):
        return (f"{self.name}: {self.points} pts, GD: {self.goal_difference}, "
                f"W: {self.wins}, L: {self.losses}, T: {self.ties}")

# Define PostGameOptions to add more variety to the user interface
class PostGameOptions:
    """These will be the options the user has to affect their team."""
    def __init__(self, user, team):
        self.user = user
        self.team = team

    def display_options(self):
        """Shows the user the options they have."""
        self.show_team_record()
        print(f"\n{self.user}, choose an option to influence {self.team.name}:")
        print("1. Change Tactics")
        print("2. Adjust Player Training")
        print("3. Boost Team Morale")
        print("4. Don't Change Anything")

    def execute_option(self, choice):
        """Implements the choice of the user."""
        if choice == 1:
            self.change_tactics()
        elif choice == 2:
            self.adjust_training()
        elif choice == 3:
            self.boost_morale()
        elif choice == 4:
            self.advance_schedule()
        else:
            print("Invalid choice. Please select again.")

    def show_team_record(self):
        """Shows the user their current record in order to help their decision."""
        print(f"Current record for {self.team.name}:")
        print(f"Wins: {self.team.wins}, Losses: {self.team.losses}, Ties: {self.team.ties}")
        print(f"Current tactic is {self.team.current_tactic}")
        print(f"Current training focus is {self.team.training_focus}")
        print(f"Current morale booster is {self.team.morale_boost}")

    def change_tactics(self):
        """Implements the tactic change option."""
        print("You have chosen to change tactics.")
        tactic_option = input("Which tactic will you use?: (offensive, balanced, defensive)")
        if tactic_option in ['offensive', 'balanced', 'defensive']:
            self.team.current_tactic = tactic_option
            print(f"Your team will play {tactic_option} next game!")
        else:
            print("You have not chosen a valid option, choose again")

    def adjust_training(self):
        """Implements the training focus adjustment."""
        print("You have chosen to adjust player training")
        practice_option = input("What would you like to change in practice?: (offense, defense)")
        if practice_option in ['offense', 'defense']:
            self.team.training_focus = practice_option
            print(f"Your team will focus on {practice_option} in training!")
        else:
            print("You have not chosen a valid option, choose again")

    def boost_morale(self):
        """Implements the morale booster."""
        print("You have chosen to boost team morale")
        morale_booster = input("How will you boost team morale?: (positive, negative)")
        if morale_booster in ['positive', 'negative']:
            self.team.morale_boost = morale_booster
            print(f"Your team morale has been {morale_booster}ly influenced!")
        else:
            print("You have not chosen a valid option, choose again")

    @staticmethod
    def advance_schedule():
        """Advances to the next game with no effect on the actual score."""
        print("You have chosen not to change anything! Moving on to next week")

# This is the function used to simulate the regular season.
# Every team will play every other team at least once.
# Top Range of goals in games tend to be 5
def play_match(team1, team2, game_number=1):
    """Regular season game."""

    if game_number % 4 == 0: # Resets tactics after 4 games
        team1.current_tactic = 'balanced'
        team2.current_tactic = 'balanced'

    if game_number % 2 == 0: # Resets training focus and morale booster after 2 games
        team1.training_focus = None
        team2.training_focus = None
        team1.morale_boost = 'neutral'
        team2.morale_boost = 'neutral'

    # Adjust goal range based on tactics
    if team1.current_tactic == 'offensive':
        team1_goal_range = (1, 6)
    elif team1.current_tactic == 'defensive':
        team1_goal_range = (0, 3)
    else: # balanced
        team1_goal_range = (0, 5)

    if team2.current_tactic == 'offensive':
        team2_goal_range = (1, 6)
    elif team2.current_tactic == 'defensive':
        team2_goal_range = (0, 3)
    else: # balanced
        team2_goal_range = (0, 5)

    # Adjust goals based on training focus
    if team1.training_focus == 'offense': # Increase upper limit
        team1_goals = rn.randint(team1_goal_range[0], team1_goal_range[1] + 1)
    else: # Default or defensive training focus
        team1_goals = rn.randint(*team1_goal_range)

    if team2.training_focus == 'offense':
        team2_goals = rn.randint(team2_goal_range[0], team2_goal_range[1] + 1)
    else:
        team2_goals = rn.randint(*team2_goal_range)

    # Adjust goals based on morale boost
    if team1.morale_boost == 'positive':
        team1_goals += 1 # Increase goals due to positive morale
    elif team1.morale_boost == 'negative':
        team1_goals -= 1 # Decrease goals due to negative morale

    if team2.morale_boost == 'positive':
        team2_goals += 1
    elif team2.morale_boost == 'negative':
        team2_goals -= 1

    # Ensure goals are within valid range
    team1_goals = max(0, team1_goals)
    team2_goals = max(0, team2_goals)

    # Simulate a match with adjusted scores
    if team1_goals > team2_goals:
        team1.points += 3
        team1.wins += 1
        team2.losses += 1
        winner = team1
    elif team1_goals < team2_goals:
        team2.points += 3
        team2.wins += 1
        team1.losses += 1
        winner = team2
    else:
        team1.points += 1
        team2.points += 1
        team1.ties += 1
        team2.ties += 1
        winner = None

    # Would like to add a way to determine who is the home team and who is the away team.
    # Increase user immersion and satisfaction with program.

    # Goal difference is calculated by taking the goals for and subtracting the goals against.
    team1.goal_difference += team1_goals - team2_goals
    team2.goal_difference += team2_goals - team1_goals

    game_number += 1

    return team1_goals, team2_goals, winner

# Penalty shootouts occur when both teams end extra time still tied.
# Regular season games do not end in penalties as teams can tie in the regular season.
def penalties(team1, team2):
    """Helps to find a winner after extra time has been completed."""
    # Simulate penalty shootout
    team1_goals = rn.randint(0, 11)
    team2_goals = rn.randint(0, 11)
    if team1_goals > team2_goals:
        team1.wins += 1
        team2.losses += 1
        return team1
    else:
        team2.wins += 1
        team1.losses += 1
        return team2

# Extra time occurs when both teams end regular time with the same amount of goals.
# Regular season games do not go into extra time as teams can tie in the regular season.
# Extra time consists of 2 shorter halves therefore the max range has been lowered from 3 ot 1.
def extra_time(team1, team2):
    """Helps to find a winner after regular time has been completed."""
    # Simulate extra time and determine if penalties are needed
    team1_goals = rn.randint(0, 1)
    team2_goals = rn.randint(0, 1)
    if team1_goals > team2_goals:
        team1.wins += 1
        team2.losses += 1
        return team1
    elif team2_goals > team1_goals:
        team2.wins += 1
        team1.losses += 1
        return team2
    else:
        return penalties(team1, team2)

# Playoff matches can not end in a tie, therefore this will determine if teams go into extra time.
# Playoff games tend to be more intense and skilled therefore we lower the max range from 5 to 3.
def playoff_match(team1, team2):
    """Simulates a game with playoff rules."""
    # Simulate a playoff match with extra time and penalties
    team1_goals = rn.randint(0, 3)
    team2_goals = rn.randint(0, 3)

    if team1_goals > team2_goals:
        team1.wins += 1
        team2.losses += 1
        print(f"The {team1.name} wins the match against the {team2.name} "
              f"with a score of {team1_goals} to {team2_goals}.")
        return team1
    elif team2_goals > team1_goals:
        team2.wins += 1
        team1.losses += 1
        print(f"The {team2.name} wins the match against the {team1.name} "
              f"with a score of {team2_goals} to {team1_goals}.")
        return team2
    else:
        winner = extra_time(team1, team2)
        print(f"The match between {team1.name} and {team2.name} ended in a tie after regular time. "
              f"Winner after extra time or penalties: {winner.name}")

    return winner

def simulate_season(teams, user, user_team_name):
    """Goes through list of teams and pairs them together to create a record for each team."""
    # Simulate the regular season
    for team in teams:
        team.reset()

    number_of_teams = len(teams)
    for i in range(number_of_teams):
        for j in range(i + 1, len(teams)):
            play_match(teams[i], teams[j])
            # Add post-game options for the user's team
            if user_team_name in (teams[i].name, teams[j].name):
                post_game = PostGameOptions(user,
                        teams[i] if teams[i].name == user_team_name else teams[j])
                post_game.display_options()
                choice = int(input("Enter your choice: "))
                post_game.execute_option(choice)

def main():
    """Main function part of code."""
    # Asks the user for their name.
    user = input("What is your name? ")
    user_team_name = input("What is your team name? ")

    # Creates a text that immerses the user into the program
    print("Welcome to Soccer Club Simulator!")
    print("\nMay your team find glory in the Super League!")

    # Names of teams in league.
    # Allows user to create a team and add them to the league in hopes of winning it all.
    teams = [Team("Kansas City Legends"), Team("Pittsburgh Iron-men"),
             Team("Atlanta Flames"), Team("Los Angeles Stars"),
             Team("Detroit Pride"), Team("Phoenix Coyotes"),
             Team("San Fransisco Miners"), Team("Miami Manatees"), Team("New England Liberty"),
             Team("Dallas Stampede"), Team("Oklahoma City Cyclones"), Team("New York Skyscrapers"),
             Team("St. Louis Steamboats"), Team("Minnesota Blizzard"), Team("Washington Storm"),
             Team("Milwaukee Wolves"), Team("Oregon Pines"), Team("Orlando Dolphins"),
             Team("Charlotte Mountaineers"), Team("Puerto Rico Beach Balls"), Team("D.C. Colonels"),
             Team("Philadelphia Freedom"), Team("Houston Hurricanes"), Team("Jacksonville Sharks"),
             Team("Alaska Glaciers"), Team("Las Vegas Gamblers"), Team("Salt Lake City Cougars"),
             Team("Albuquerque Indians"), Team("Hawaii Volcanoes"), Team("Vancouver Whalers"),
             Team("Toronto Lumberjacks"), Team(user_team_name)]

    division_two_teams = [Team("Austin Rough riders"),
                          Team("New York Metros"), Team("Tampa Bay Speedsters"),
                          Team("Montreal Underground"), Team("Connecticut Robins"),
                          Team("San Diego Surfers"), Team("Green Bay Lake Monsters"),
                          Team("San Antonio Cavalry"), Team("New Orleans Voodoo"),
                          Team("Memphis Jazz"), Team("Nashville Rockstars"),
                          Team("Cincinnati Gorillas"), Team("Indianapolis Rush"),
                          Team("Buffalo Waterfalls"), Team("Boston Fishermen"),
                          Team("Cleveland Community"), Team("Manhattan Prairie Dogs"),
                          Team("Des Moine Shockers"), Team("Denver Altitude"),
                          Team("Montana Stallions")]

    year = 2024

    continue_game = 'yes'
    while continue_game.lower() == 'yes':

        print(f"Welcome to the {year} Season!")

        print("\nSuper League Season Standings:")
        simulate_season(teams, user, user_team_name)
        position = 1
        for team in sorted(teams, key=lambda x: (x.points, x.goal_difference), reverse=True):
            print(position, team)
            position += 1

        print("The playoffs are about to begin!")

        playoff_teams = sorted(teams, key=lambda x: (x.points, x.goal_difference), reverse=True)

        # Simulate playoffs.
        print("\nPlayoffs:")
        quarter_finalists = [playoff_teams[0], playoff_teams[1], playoff_teams[2],
                             playoff_teams[3], playoff_teams[4],
                             playoff_teams[5], playoff_teams[6], playoff_teams[7]]

        # Quarter-finals.
        # The Quarter-Finalists are the 8 best teams in the league.
        # As is typical in sports the highest ranked team will play the lowest ranked team.
        # This is a way to reward them for being good during the regular season.
        print("\nQuarter-Finals:")
        quarter_finals_winner1 = playoff_match(quarter_finalists[0], quarter_finalists[7])
        quarter_finals_winner2 = playoff_match(quarter_finalists[1], quarter_finalists[6])
        quarter_finals_winner3 = playoff_match(quarter_finalists[2], quarter_finalists[5])
        quarter_finals_winner4 = playoff_match(quarter_finalists[3], quarter_finalists[4])

        # The semi-finalists are the winners of the 4 quarter-final games.
        semi_finalists = [quarter_finals_winner1, quarter_finals_winner2, quarter_finals_winner3,
                                 quarter_finals_winner4]

        # Semi-finals.
        # The teams are organized by the outcome of the quarter-final games.
        print("\nSemi-Finals:")
        semi_final_winner1 = playoff_match(semi_finalists[0], semi_finalists[3])
        semi_final_winner2 = playoff_match(semi_finalists[1], semi_finalists[2])

        # Final.
        # These are the last 2 teams left standing.
        print("\nThe Final:")
        champion = playoff_match(semi_final_winner1, semi_final_winner2)
        print(f"\nThe champion of the season is the: {champion.name}!")

        print("\nDivision Two season standings:")
        simulate_season(division_two_teams, user, user_team_name)
        position = 1
        for team in sorted(division_two_teams,
                           key=lambda x: (x.points, x.goal_difference), reverse=True):
            print(position, team)
            position += 1

        relegated_teams = sorted(teams,
                                 key=lambda x: (x.points, x.goal_difference), reverse=True)
        relegated = relegated_teams[-3:]
        promoted_teams = sorted(division_two_teams,
                                key=lambda x: (x.points, x.goal_difference), reverse=True)
        promoted = promoted_teams[:3]

        print(f"\nTeams relegated to Division Two: {relegated[0].name}, {relegated[1].name}, "
              f"{relegated[2].name}")
        print(f"Teams promoted to the Super League: {promoted[0].name}, {promoted[1].name}, "
              f"{promoted[2].name}")

        for team in relegated:
            division_two_teams.append(team)
            teams.remove(team)
        for team in promoted:
            teams.append(team)
            division_two_teams.remove(team)

        print("\nCongrats on your inaugural season!")
        print("Ready for next season?")

        continue_game =input("Do you want to play another season? (yes,no): ")

        if continue_game == 'no':
            print("Thank you for playing!")

        year += 1

if __name__ == "__main__":
    main()

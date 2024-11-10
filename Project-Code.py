# Import the random library to use in the code.
# Nicknaming rn to make calling functions of the library easy.
import random as rn

# Define what Team is and what will be included in the final results.
# This will help keep track of wins, losses, ties.
# The overall points and goal difference will break up any ties in the final rankings.
class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.goal_difference = 0
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def reset(self):
        self.points = 0
        self.goal_difference = 0
        self.wins = 0
        self.losses = 0
        self.ties = 0

    # This is how the final standings will apper to the user.
    # The order is name: points, goal difference, wins, losses, ties.
    def __repr__(self):
        return f"{self.name}: {self.points} pts, GD: {self.goal_difference}, W: {self.wins}, L: {self.losses}, T: {self.ties}"

# This is the function used to simulate the regular season.
# Every team will play every other team at least once for a total of 31 games per team.
# Using the average min/ max of real-life games (being 0, 5) to generate a random score for the games.
def play_match(team1, team2):
    # Simulate a match with random scores
    team1_goals = rn.randint(0, 5)
    team2_goals = rn.randint(0, 5)

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

    return team1_goals, team2_goals, winner

# Penalty shootouts occur when both teams end regular time and extra time with the same amount of goals.
# Regular season games do not end in penalties as teams can tie in the regular season.
def penalties(team1, team2):
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
# The likelihood of a goal being scored in extra time is lower due to the shorter time and team exhaustion.
def extra_time(team1, team2):
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

# Playoff matches can not end in a tie, therefore this will determine if teams need to go into extra time.
# Playoff games tend to be more intense and skilled therefore we lower the max range from 5 to 3.
def playoff_match(team1, team2):
    # Simulate a playoff match with extra time and penalties
    team1_goals = rn.randint(0, 3)
    team2_goals = rn.randint(0, 3)

    if team1_goals > team2_goals:
        team1.wins += 1
        team2.losses += 1
        print(f"The {team1.name} wins the match against the {team2.name} with a score of {team1_goals} to "
              f"{team2_goals}.")
        return team1
    elif team2_goals > team1_goals:
        team2.wins += 1
        team1.losses += 1
        print(f"The {team2.name} wins the match against the {team1.name} with a score of {team2_goals} to "
              f"{team1_goals}.")
        return team2
    else:
        winner = extra_time(team1, team2)
        print(f"The match between {team1.name} and {team2.name} ended in a tie after regular time. Winner after "
              f"extra time or penalties: {winner.name}")
        return winner

def simulate_season(teams):
    # Simulate the regular season
    for team in teams:
        team.reset()

    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            play_match(teams[i], teams[j])

def main():
    # Asks the user for their name.
    print("Hello,", input("What is your name?"))

    # Creates a text that immerses the user into the program
    print("Welcome to Soccer Club Simulator!")
    print("\nMay your team find glory in the Super League!")
    your_team = input("What is your team name?:")

    # Names of teams in league.
    # Allows user to create a team and add them to the league in hopes of winning it all.
    teams = [Team("Kansas City Legends"), Team("Pittsburgh Iron-men"),
             Team("Atlanta Flames"), Team("Los Angeles Stars"), Team("Detroit Pride"), Team("Phoenix Coyotes"),
             Team("San Fransisco Miners"), Team("Miami Manatees"), Team("New England Liberty"),
             Team("Dallas Stampede"), Team("Oklahoma City Cyclones"), Team("New York Skyscrapers"),
             Team("St. Louis Steamboats"), Team("Minnesota Blizzard"), Team("Washington Storm"),
             Team("Milwaukee Wolves"), Team("Oregon Pines"), Team("Orlando Dolphins"),
             Team("Charlotte Mountaineers"), Team("San Diego Speedboats"), Team("D.C. Colonels"),
             Team("Philadelphia Freedom"), Team("Houston Hurricanes"), Team("Jacksonville Sharks"),
             Team("Alaska Glaciers"), Team("Las Vegas Gamblers"), Team("Salt Lake City Cougars"),
             Team("Albuquerque Indians"), Team("Hawai'i Volcanoes"), Team("Vancouver Whalers"),
             Team("Toronto Lumberjacks"), Team(your_team)]

    division_two_teams = [Team("Austin Roughriders"), Team("New York Metros"), Team("Tampa Bay Speedsters"),
                          Team("Montreal Underground"), Team("Connecticut Robins"), Team("San Diego Surfers"),
                          Team("Green Bay Lake Monsters"), Team("San Antonio Cavalry"), Team("New Orleans Voodoo"),
                          Team("Memphis Jazz"), Team("Nashville Rockstars"), Team("Cincinnati Gorillas"),
                          Team("Indianapolis Rush"), Team("Buffalo Waterfalls"), Team("Boston Fishermen"),
                          Team("Cleveland Community"), Team("Manhattan Prarie Dogs"), Team("Des Moine Shockers"),
                          Team("Denver Altitude"), Team("Montana Stallions")]

    year = 2024

    continue_game = 'yes'
    while continue_game.lower() == 'yes':

        print(f"Welcome to the {year} Season!")

        print("\nSuper League Season Standings:")
        simulate_season(teams)
        position = 1
        for team in sorted(teams, key=lambda x: (x.points, x.goal_difference), reverse=True):
            print(position, team)
            position += 1

        print("The playoffs are about to begin!")

        playoff_teams = sorted(teams, key=lambda x: (x.points, x.goal_difference), reverse=True)

        # Simulate playoffs.
        print("\nPlayoffs:")
        quarter_finalists = [playoff_teams[0], playoff_teams[1], playoff_teams[2], playoff_teams[3], playoff_teams[4],
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

        # The semi-finalists are the winners of the 4 quarter final games.
        semi_finalists = [quarter_finals_winner1, quarter_finals_winner2, quarter_finals_winner3,
                                 quarter_finals_winner4]

        # Semi-finals.
        # The trend of highest ranked team playing the lower ranekd team does not apply here as the quarter-finals
        # determine a bracket that shapes the playoffs in its entirety.
        print("\nSemi-Finals:")
        semi_final_winner1 = playoff_match(semi_finalists[0], semi_finalists[3])
        semi_final_winner2 = playoff_match(semi_finalists[1], semi_finalists[2])

        # Final.
        # These are the last 2 teams left standing.
        print("\nThe Final:")
        champion = playoff_match(semi_final_winner1, semi_final_winner2)
        print(f"\nThe champion of the season is the: {champion.name}!")

        print("\nDivision Two season standings:")
        simulate_season(division_two_teams)
        position = 1
        for team in sorted(division_two_teams, key=lambda x: (x.points, x.goal_difference), reverse=True):
            print(position, team)
            position += 1

        relegated_teams = sorted(teams, key=lambda x: (x.points, x.goal_difference), reverse=True)
        relegated = relegated_teams[-3:]
        promoted_teams = sorted(division_two_teams, key=lambda x: (x.points, x.goal_difference), reverse=True)
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

    # Future additions can add home games for the highest seeds and the final location taking place at any random city
    # from the lists of teams that should not be repeated for at least 5 years to create variety.

        print("\nCongrats on your inaugral season!")
        print("Ready for next season?")

        continue_game =input("Do you want to play another season? (yes,no): ")

        if continue_game == 'no':
            print("Thank you for playing!")

        year += 1

if __name__ == "__main__":
    main()
# Welcome to my project!

## Here you will find a Soccer Team Simulator that allows you to create a team and begin your journey in the super league!

## Some features of this game include:
- Simulate matches with random scores
- Track team statistics like points, goal difference, wins, losses, and ties
- A detailed Promotion and Relegation system between two divisions
  - The Top 3 Teams in the second division will replace the bottom 3 teams of the first division based off total points and goal difference
- Allow re-playability for the user!

## How to run the game
1. Have Python installed on your system (Most recent is always preferred).
2. Save this code to a file with the name 'Soccer_Manager' (or whatever you would like to name it).
3. Open your terminal or command center prompt.
4. Locate the game file you saved in the directory you placed it in.
5. Run the game using the command:
    '''sh
    python soccer_manager.py
    (or whatever you named the file)

# Breakdown of the code:
- Class:
  - By giving Team a class it helps to simplify the definition of the attributes each team presents, such as:
    - Total points, Goal difference, and Overall record.
  - Along with Team being defined as a class I have included 2 functions to help with the user interface.
    - reset() and __repr__()
      - reset() clears the records and statistics of each team, should the user decided to simulate the next season.
      - __repr__() defines a doc string that the program will put out to make the appearance for the user cleaner and simplified.

- Functions:
  - play_match(team1, team2):
    - This function simulates a regular season match between the 2 teams presented to the program with the outcome of the game affecting the records of both teams, all statistics are updated automatically.
  - penalties(team1, team2):
    - This function simulates what a penalty shootout would be should both teams be even after regular time and overtime.
  - extra_time(team1, team2):
    - This function simulates what extra time would be should both teams be even after regular time occurs.
  - playoff_match(team1, team2):
    - This function simulates a playoff match, which a tougher regular season game, between a fixed set of teams that finished in the top 8 spots of the final standings.
  - simulate_season(teams):
    - This function is the base of the entire program, its sole function is to go through the list of teams and simulate the games between each team to create a final standings table once all teams have played each other at least once.
  - display_standings(teams):
    - This function prints out the final standings table for the user to see.

- Main():
  - The main() function is what runs the game. This function initializes the two divisions of the league and will then call upon the other functions in a specific order to make the game function properly.
  - This function also is what provides the user with the ability to have input and ensure that the input is responded to accordingly.

# License
 - This project is licensed under the MIT License. See License.md for more information

## This project was created with inspiration from various other soccer/sport manager games and Python programming tutorials and classes!
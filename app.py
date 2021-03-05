import teamtools as tt
import constants

player_list = constants.PLAYERS  # Import the player list
teams = constants.TEAMS  # Import the team list
team_rosters = {}
num_of_teams =[]

player_list = tt.clean_data(player_list)

rosters = tt.balanace_teams(player_list, teams)

while True:
    print('\n\nBASKETBALL TEAM STATS TOOL\n')
    print("-"*4 + "MENU " + "-"*4)

    print("""Here are you choices:
A) Display Team Stats
B) Quit""")
    choice = input('Enter an option: ')
    if choice.upper() == "A":
        for idx, team in enumerate(teams):
            num_of_teams.append(int(idx+1))
            print(f'{idx+1}. {team}')
        try:
            team_selected = input('\nSelect a team to display their stats: ')
            team_selected = (int(team_selected) - 1)
            if (team_selected + 1) not in num_of_teams:
                raise ValueError
        except ValueError:
            print('That is not a valid input.')
            continue
        

        tt.display_team_stats(teams[team_selected], rosters[teams[team_selected]])
        input('\n\nPress Enter to continue.....')
            
    else:
        break
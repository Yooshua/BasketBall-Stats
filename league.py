import applications as app
import constants

player_list = constants.PLAYERS  # Import the player list
teams = constants.TEAMS  # Import the team list
team_rosters = {}

#  Cleanup the player list to include onnly the relevant data of Name, Height
#  and Experience.
#  player_list = app.clean_data(player_list)


rosters = app.balanace_teams(player_list, teams)

while True:
    print('\n\nBASKETBALL TEAM STATS TOOL\n')
    print("-"*4 + "MENU " + "-"*4)

    print("""Here are you choices:
A) Display Team Stats
B) Quit""")
    choice = input('Enter an option: ')
    print('')
    if choice.upper() == "A":
        for idx, team in enumerate(teams):
            print(f'{idx+1}. {team}')
        team_selected = int(input('\nSelect a team to display their stats: ')) - 1
        app.display_team_stats(teams[team_selected], rosters[teams[team_selected]])
        app.display_parents(rosters[teams[team_selected]])
        input('\n\nPress Enter to continue.....')
    else:
        break
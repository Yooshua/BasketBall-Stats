def clean_data(list_players):
    """Create a new list of players with only the important info:
    Height
    Experiance
    Name
    """
    clean_player_list =[] # I don't really see the point of "cleaning" the player list
    for player in list_players:
        clean_player_list.append({
        'name': player['name'],
        'experience': player['experience'],
        'height': player['height']})
    return clean_player_list

def balanace_teams(player_list, team_list):
    """Balance the teams by Experience first then by height
    """
    experienced_players = []
    novice_players = []
    roster_size = len(player_list) / len(team_list)
    team_rosters = {}

    for team in team_list:
        team_rosters[team] = [] # Create a Dictonary with the team name as a key

    # Sort the players into two lists: one with experience, one without
    for player in player_list:
        if player['experience'] == 'YES':
            experienced_players.append(player)
        else:
            novice_players.append(player)
    
    # TODO: it would be wise to sort the players by height also?


    # Distribute the players among the rosters
    index = 0
    for player in experienced_players:
        team_rosters[team_list[index]].append(player)
        index +=1
        if index == len(team_list):
            index = 0

    for player in novice_players:
        team_rosters[team_list[index]].append(player)
        index +=1
        if index == len(team_list):
            index = 0
    
    return team_rosters

def display_team_stats(team_name, team_roster):
    """Display the team stats"""

    roster_names = []
    player_heights = []
    players_with_xp = []
    players_no_xp = []
    player_heights = []

    for player in team_roster:
        roster_names.append(player.get('name'))
        player_heights.append(int((player.get('height')).split(" ")[0])) # there has to be a better way :D
        if player['experience'] == 'YES':
            players_with_xp.append(player.get('name'))
        else:
            players_no_xp.append(player.get('name'))
    
    average_height = int(sum(player_heights) / len(player_heights))
    print(f"\n\n{team_name}'s Team stats:")
    print("-"*(len(f"{team_name}'s Team stats:"))) # Make the number of "-" match the string length
    print(f'Total players: {len(roster_names)}')
    print(f'Total experienced: {len(players_with_xp)}')
    print(f'Total inexperienced: {len(players_no_xp)}')
    print(f'Average heights: {average_height}\n')



    print("The Following Players are on the team:")
    print(", ".join(roster_names))
    


def display_parents(team_roster):
    """Create list of guardians seperated by a comma"""

    # create list of parents
    parents_list = []
    for player in team_roster:
        parents_list.append(player.get('guardians'))

    # clean_parents_list create a list of parents without and
    clean_parents_list = [] 
    for guardian in parents_list:
        if "and" in guardian:
            clean_parents_list.append(guardian.split(' and ')[0]) # add first guardian
            clean_parents_list.append(guardian.split(' and ')[1]) # add second guardian
        else:
            clean_parents_list.append(guardian)

    print('\nGuardians:')
    print(", ".join(clean_parents_list))




if __name__ == "__main__":
    pass

def clean_data(list_players):
    """Clean up the player data to the format we want"""
    clean_player_list = [] 
    clean_height = 1
    experience = True

    for player in list_players:
        guardian = player['guardians']

        #  Return only inches by splitting height into a list and only taking
        #  the first value
        clean_height = int(player.get('height').split(" ")[0])

        #  Check if they have two guardians and if they do split string up 
        #  and put them in a list
        if "and" in guardian:
            parent1 = (guardian.split(' and ')[0]) 
            parent2 = (guardian.split(' and ')[1])
            guardian = [parent1, parent2]

        #  Change the expereience vale to a boolean value
        if player['experience'] == "YES":
            experience = True
        else:
            experience = False

        #  Create new list entry with cleaned up values.
        clean_player_list.append({
        'name': player['name'],
        'guardians': guardian,
        'height': clean_height,
        'experience': experience})
        
    return clean_player_list
            



def balanace_teams(player_list, team_list):
    """Balance the teams by Experience first then by height
    """
    experienced_players = []
    novice_players = []
    team_rosters = {}

    # Create a Dictonary with the team name as a key
    for team in team_list:
        team_rosters[team] = [] 

    # Sort the players into two lists: one with experience, one without
    for player in player_list:
        if player['experience'] == True:
            experienced_players.append(player)
        else:
            novice_players.append(player)

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
    player_guardians =[]
    players_with_xp = []
    players_no_xp = []

    for player in team_roster:
        roster_names.append(player.get('name'))
        player_heights.append(player.get('height')) 
        if isinstance(player['guardians'], list):
            player_guardians.append(player.get('guardians')[0])
            player_guardians.append(player.get('guardians')[1])
        else:
            player_guardians.append(player.get('guardians'))
        if player['experience'] == True:
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
    print("  " + ", ".join(roster_names))
    print('\n')
    print('Guardians:')
    print("  " + ", ".join(player_guardians))

#Python Web Development Techdegree
#Project 2 - Basketball Team Stat Tool
#Going for Exceeds Expectations rejected if project 2 does not meet all Exceeds Expectations Requirements Thank You.
import constants
import copy
import os


player_data = copy.deepcopy(constants.PLAYERS)
team_names = copy.deepcopy(constants.TEAMS)
team_data = copy.deepcopy(constants.TEAMS)
guardian_list = []
experienced_player = []
non_experienced_player = []


def clean_data():
    for player in player_data:
        height = player["height"].split()
        player["height"] = int(height[0])
        guardian = player["guardians"].split(" and ")
        for parent in guardian:
            guardian_list.append(parent)
        if player["experience"] == "YES":
            player["experience"] = True
            experienced_player.append(player)
        else:
            player["experience"] = False
            non_experienced_player.append(player)
    return player_data


def draft_teams():
    if int(len(player_data)) % int(len(team_data)) == 0:
        team = 0
        team_length = int(len(team_data))
        draft_increment = int(len(experienced_player)/len(team_data))
        draft_number = 0
        player_per_round = 3
        while team != team_length:
            team_data[team] = experienced_player[draft_number:player_per_round] + non_experienced_player[draft_number:player_per_round]
            team += 1
            draft_number += draft_increment
            player_per_round += draft_increment
    return team_data


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_stats(stats):
    clear_screen()
    stats = stats - 1
    team_roster = []
    experienced_team_players = []
    inexperienced_team_players = []
    player_height = []
    team_guardians = []
    for player in team_data[stats]:
        team_roster.append(player["name"])
        guardians = player["guardians"].split(" and ")
        for parent in guardians:
            team_guardians.append(parent)
        if player["experience"]:
            experienced_team_players.append(player["name"])
        else:
            inexperienced_team_players.append(player["name"])
        player_height.append(player["height"])
    print("**********{}**********\n".format(team_names[stats]))
    print("Total number of players: {}\n".format(len(team_roster)))
    print("-----TEAM ROSTER-----\n{}\n".format(", ".join(team_roster)))
    print("-----TEAM EXPERIENCE-----\nTotal number of experienced players: {}\nTotal number of inexperienced players: {}\n".format(len(experienced_team_players), len(inexperienced_team_players)))
    print("Avrage height of players:{} inches\n".format(round(sum(player_height) / int(len(team_roster)), 2)))
    print("*****TEAM GUARDIANS*****\n{}".format(", ".join(team_guardians)))
    input("\n\nEnter any key to continue")
    clear_screen()


def team_menu():
    while True:
        clear_screen()
        team_number = 1
        print("-----Teams-----")
        for team in team_names:
            print("{}) ".format(team_number), team)
            team_number += 1
        team_input = input("Enter the number corosponding to the team you wish to view\n>")
        try:
            team_input = int(team_input)
            if team_input < 0 or team_input > len(team_names):
                raise ValueError
        except ValueError:
            clear_screen()
            input("OH NO!!! please Enter the number corosponding to the team you wish to view\nFor example ENTER 1 for {} stats\nEnter any key to continue\n>".format(team_names[0]))
            continue

        else:
            show_stats(team_input)
            break


def main_menu():
    print("BASKETBALL TEAM STATS TOOL\n")
    while True:
        print("-----------MENU-----------\n1) Display Team Stats\n2)QUIT\n")
        menu_input = input("Enter a corosponding menu number to continue  ")
        while menu_input != "1" and menu_input != "2":
            clear_screen()
            menu_input = input("OH NO invlad selection!!!\nPlease enter either 1 for TEAM STATS or 2 to QUIT the program\n\n-----------MENU-----------\n\n1) Display Team Stats\n2)QUIT\n>  ")

        if menu_input == "1":
            team_menu()
        else:
            clear_screen()
            print("Good Bye")
            break


if __name__ == "__main__":
    clean_data()
    draft_teams()
    main_menu()

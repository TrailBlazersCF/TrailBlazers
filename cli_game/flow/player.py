import os
from termcolor import colored, cprint

class Character:
    """An instance of a character in the game."""
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.clothed = True
        self.sick = []
        self.alive = True

    def return_health_status_report(self):
        status_string = f'  {self.name} is '
        if 95 <= self.health:
            status_string += (colored('in perfect health.', 'green'))
        if 80 <= self.health < 95:
            status_string += (colored("feeling great.", 'cyan'))
        if 65 <= self.health < 80:
            status_string += (colored("feeling good.", 'yellow'))
        if 35 <= self.health < 65:
             status_string += (colored("feeling poor.", "blue"))
        if self.health < 35:
            status_string += (colored("in critical condition.", "red"))
        if self.sick:
            status_string += (colored('(SICK)' , "red"))
        
        return status_string

###########################################################################################################
def character_creation():
    """
    Function to create the characters in the party
    creates instances of the Character class
    A leader and 4 members are created at the start of every game.
    Returns a list of the members for use by the game and the starting funds available for use.
    """
    acceptable_no = ['no', 'n', 'nah', 'naw', 'no way', 'nope', 'x', '']

    while True:
        wagon_party = []

        chosen_leader, starting_funds = prompt_player_to_pick_a_leader()

        wagon_party.append(chosen_leader)
        wagon_party.append(prompt_player_to_enter_name('2', wagon_party))
        wagon_party.append(prompt_player_to_enter_name('3', wagon_party))
        wagon_party.append(prompt_player_to_enter_name('4', wagon_party))
        wagon_party.append(prompt_player_to_enter_name('5', wagon_party))

        print_member_list(wagon_party)
        response = input('Is this your team? y/n?')
        if response.lower() not in acceptable_no:
            os.system('clear')
            return (wagon_party, starting_funds)
        else:
            input ('Please select "y" or "n" next time')
        os.system('clear')
    




###########################################################################################################



###########################################################################################################
def prompt_player_to_pick_a_leader():
    """
    Function to handle player choosing a starting leader
    Returns a tuple of (the name of the leader, and the starting_funds (based on leader's profession))
    """
    print('Every wagon train needs a leader...')
    print('1. Banker')
    print('2. Carpenter')
    print('3. Farmer')

    response = ''
    while response != '1' and response != '2' and response != '3':
        response = input('What occupation does your leader have?')

    if response == '1':
        starting_funds = 1600 # Easy game
    if response == '2':
        starting_funds = 800 # Medium
    if response == '3':
        starting_funds = 400 # Hard

    os.system('clear')
    response = input('What is your leader\'s first name? ')
    while response == '':
        response = input('What is your leader\'s first name? ')

    leader = Character(response)
    print(f'1. {response}')
    os.system('clear')
    return (leader, starting_funds)
###########################################################################################################



###########################################################################################################
def prompt_player_to_enter_name(member_seq_number, member_list):
    """
    Function that handles choosing names for the four other wagon party members.
    Returns a new instance of the Character class to be added to the wagon_party in the game.
    """
    print_member_list(member_list)

    response = input('What is the first name of your next member? ')
    while response == '':
        response = input('What is the first name of your next member? ')
    new_member = Character(response)
    os.system('clear')
    return new_member
###########################################################################################################



###########################################################################################################
def print_member_list(member_list):
    """prints members of the party"""
    counter = 1
    for member in member_list:
        print(f'{counter}. {member.name}')
        counter += 1
###########################################################################################################





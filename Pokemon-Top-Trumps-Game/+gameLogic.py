import random
# import the random library so that random code choice can be generated
from math import floor
# import floor from math library so that code can now round down
import sys, time
# import sys library so that the timing of code can be controlled
import requests
# imports the request library to respond to information requests
from pprint import pprint
# For the JSON response to be legible to user/coders

def delprint(text='Type a String in', delay_time=0.05):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        #clears internal buffer of the file
        time.sleep(delay_time)


# function to delay the printing of characters by 0.05
def getRandomPokemon():
    r1 = random.randint(1, 151)
    # generates random number between 1 and 151
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(r1)
    # api where the information about Pokemon are gathered
    response = requests.get(url)
    # requests to get the information from the api
    if response.status_code == 200:
        # if the request is successful this code runs
        pokemon = response.json()

        pokemon_id = pokemon['id']
        pokemon_name = pokemon['name']
        pokemon_height = pokemon['height']
        pokemon_weight = pokemon['weight']

        stats_json = pokemon['stats']
        # all the Pokemon stats are is stats_json

        base_stats = []
        for stat in stats_json:
            stat_name = stat['stat']['name'].title()
            base_stat = stat['base_stat']
            pokemon.__setitem__(stat_name, base_stat)
            # the name and stat figure are made into dictionaries and added into the Pokemon list
        # gets all info about the random Pokemon
        # the name,id,height,weight,hp(health),attack,defense,special-attack,special-defense,speed
    else:
        print("Unable to retrieve Pokemon information. Please check the Pokemon's ID and try again.")
    return pokemon
    # the return makes sure that the info retrieved is collected


# this function generates a random Pokemon
yourPokemonStats = []
# a list to contain the user's Pokemon
compPokemonStats = []
# a list to contain the opponents Pokemon
print('Your Pokemon')
yourPokemonStats.append(getRandomPokemon())
# adds a random Pokemon to your list for your Pokemon
print('{0:15}   {1}'.format("Pokemon ID:", yourPokemonStats[0]['id']))
print('{0:15}   {1}'.format("Name:", yourPokemonStats[0]['name']))
print('{0:15}   {1}'.format("Height:", (yourPokemonStats[0]['height'])))
print('{0:15}   {1}'.format("Weight:", (yourPokemonStats[0]['weight'])))
print('{0:15}   {1}'.format('Hp:', (yourPokemonStats[0]['Hp'])))
print('{0:15}   {1}'.format('Attack:', (yourPokemonStats[0]['Attack'])))
print('{0:15}   {1}'.format('Defense:', (yourPokemonStats[0]['Defense'])))
print('{0:15}   {1}'.format('Special-Attack:', (yourPokemonStats[0]['Special-Attack'])))
print('{0:15}   {1}'.format('Special-Defense:', (yourPokemonStats[0]['Special-Defense'])))
print('{0:15}   {1}'.format('Speed:', (yourPokemonStats[0]['Speed'])))
# prints out all the stats for your Pokemon to the screen
print('')
print('Your opponents Pokemon')
compPokemonStats.append(getRandomPokemon())
# add a random Pokemon to your opponents list for their Pokemon
print('{0:15}   {1}'.format("Pokemon ID:", compPokemonStats[0]['id']))
print('{0:15}   {1}'.format("Name:", compPokemonStats[0]['name']))
print('{0:15}   {1}'.format("Height:", (compPokemonStats[0]['height'])))
print('{0:15}   {1}'.format("Weight:", (compPokemonStats[0]['weight'])))
print('{0:15}   {1}'.format('Hp:', (compPokemonStats[0]['Hp'])))
print('')
# prints some but not all of your opponents stats to the screen so the user is aware of which Pokemon they are fighting

delprint('A battle has started!')
# slowly prints out that a battle has started
print('\n')

while (yourPokemonStats[0]['Hp'] > 0) and (compPokemonStats[0]['Hp'] > 0):
    # a while loop used to make sure the battle keeps running until one of the Pokemon have been defeated
    delprint('Its your turn!')
    print('\n')
    chosen_attack = input('What do you wish to battle with? \nAttack / Special-Attack / Special-Defense / Speed -> ')
    print('')
    # user inputs what stat they wish to use to attack
    print(yourPokemonStats[0]['name'], ' uses ', chosen_attack, ' its very effective!')
    print('')
    # the attack is announced
    if chosen_attack == 'Attack':
        chosen_attack = yourPokemonStats[0]['Attack']
    elif chosen_attack == 'Special-Attack':
        chosen_attack = yourPokemonStats[0]['Special-Attack']
    elif chosen_attack == 'Special-Defense':
        chosen_attack = yourPokemonStats[0]['Special-Defense']
    elif chosen_attack == 'Speed':
        chosen_attack = yourPokemonStats[0]['Speed']
    # this changes the chosen attack from the name of the attack to the power of the attack
    else:
        print('What you chose is not an option')
        continue
        # continue is used in case an attack is typed in wrong or an option that's not there is chosen
        # it will take the user back again to the beginning to chose their attack again
    damage = floor(
        0.5 * (yourPokemonStats[0]['Attack'] / yourPokemonStats[0]['Defense']) * (compPokemonStats[0]['Attack'] /
                                                                                  compPokemonStats[0][
                                                                                      'Defense']) * 1 * chosen_attack) + 1
    # formula used to calculate the exact amount of damage that is delt according to the attack chosen
    compPokemonStats[0]['Hp'] = compPokemonStats[0]['Hp'] - damage
    # this takes away the damage from your opponents health
    print(compPokemonStats[0]['name'], ' has suffered damage! Its health is now ', compPokemonStats[0]['Hp'])
    print('')
    # announces that damage has occurred and the new health of your opponent

    if compPokemonStats[0]['Hp'] <= 0:
        break
        # checks that your opponent is still alive
        # if the opponent was defeated the break makes sure that the loop stops and the battle ends

    delprint('Its your opponents turn!')
    print('\n')
    # prints slowly that it's the opponents turn
    attacks_available = ['Attack', 'Special-Attack', 'Special-Defense', 'Speed']
    # list of attacks that the opponent can chose
    chosen_attack = random.choice(attacks_available)
    # a random attack from the list is chosen
    print(compPokemonStats[0]['name'], ' uses ', chosen_attack, ' its very effective!')
    print('')
    # the chosen attack is announced to the user
    if chosen_attack == 'Attack':
        chosen_attack = compPokemonStats[0]['Attack']
    elif chosen_attack == 'Special-Attack':
        chosen_attack = compPokemonStats[0]['Special-Attack']
    elif chosen_attack == 'Special-Defense':
        chosen_attack = compPokemonStats[0]['Special-Defense']
    elif chosen_attack == 'Speed':
        chosen_attack = compPokemonStats[0]['Speed']
        # this changes the chosen attack from the name of the attack to the power of the attack
    else:
        print('What you chose is not an option')
        continue
        # continue is used in case an attack is typed in wrong or an option that's not there is chosen
        # it will take the user back again to the beginning to chose their attack again
    damage = floor(
        0.5 * (yourPokemonStats[0]['Attack'] / yourPokemonStats[0]['Defense']) * (compPokemonStats[0]['Attack'] /
                                                                                  compPokemonStats[0][
                                                                                      'Defense']) * 1 * chosen_attack) + 1
    # formula used to calculate the exact amount of damage that is delt according to the attack chosen
    yourPokemonStats[0]['Hp'] = yourPokemonStats[0]['Hp'] - damage
    # this takes away the damage from your Pokemon health
    print(yourPokemonStats[0]['name'], ' has suffered damage! Your Pokemons health is now ', yourPokemonStats[0]['Hp'])
    print('')
    # announces that damage has occurred and the new health of your Pokemon
    if yourPokemonStats[0]['Hp'] <= 0:
        break
        # checks that your Pokemon is still alive
        # if your Pokemon was defeated the break makes sure that the loop stops and the battle ends
# end of the while loop
delprint('The battle is over!')
# slowly prints the battle is over
if yourPokemonStats[0]['Hp'] <= 0:

    print('\n')
    print('Your Pokemon has been defeated')
    delprint('You lose!')
    print('\n')
    # checks if your Pokemon was defeated if true it announces that you lose
else:
    # if your Pokemon is still alive you win
    print('')
    print('You have defeated your opponents Pokemon')
    delprint('You win!')

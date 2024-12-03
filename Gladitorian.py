import random
import time

def play_game():
    moves = {
        1: 'Murmillo',     # Heavy armored gladiator with sword and shield
        2: 'Retiarius',    # Trident and net fighter
        3: 'Thraex',       # Curved sword fighter
        4: 'Hoplomachus',  # Spear and small shield fighter
        5: 'Dimachaerus'   # Dual sword wielder
    }

    rules = {
        'Murmillo': ['Thraex', 'Hoplomachus'],      # Heavy armor beats curved blade and spear
        'Retiarius': ['Murmillo', 'Dimachaerus'],   # Net and trident trap heavy and dual wielders
        'Thraex': ['Retiarius', 'Hoplomachus'],     # Curved blade cuts through nets and reaches past spears
        'Hoplomachus': ['Retiarius', 'Dimachaerus'], # Spear outreaches net and dual swords
        'Dimachaerus': ['Murmillo', 'Thraex']       # Dual swords overwhelm single weapon fighters
    }

    print('\n=== GLORY OF THE ARENA ===')
    print('Choose your Champion! (1-5):')
    print('1. Murmillo    - Heavily armored sword and shield warrior')
    print('2. Retiarius   - Trident and net fighter of the sea')
    print('3. Thraex      - Agile curved sword master')
    print('4. Hoplomachus - Elite spear warrior')
    print('5. Dimachaerus - Deadly dual sword fighter')
    
    try:
        cpu = random.randint(1, 5)
        player = int(input('\nSelect your gladiator: '))

        if player in moves:
            player_move = moves[player]
            cpu_move = moves[cpu]
            
            print('\n⚔️ The gates of the Colosseum open...')
            time.sleep(1)
            print(f'You enter the arena as: {player_move}')
            time.sleep(1)
            print(f'Your opponent stands as: {cpu_move}')
            time.sleep(1)
            
            print('\nThe crowd thirsts for blood...')
            time.sleep(1)
            
            if player_move == cpu_move:
                print("🤝 The match is declared a draw by the Emperor!")
            elif cpu_move in rules[player_move]:
                print("🏆 VICTORIA! The crowd erupts in cheers!")
            else:
                print("⚰️ You fall with honor in the arena!")
        else:
            print('Invalid choice! Choose a number between 1 and 5.')

    except ValueError:
        print('The Emperor demands valiant choices!')

    play_again = input("\nThe citizens desire more, what say ye? (yes/no): ").lower()
    return play_again in ['yes', 'y']

while True:
    if not play_game():
        print("\nMay your name be remembered in the annals of the arena!")
        break

        

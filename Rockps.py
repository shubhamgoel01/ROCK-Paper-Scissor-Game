import random

def play():
    user = input(" 'r' for Rock , \n 'p'for paper ,\n 's' for scissors \n whts Your Choice:")
    comp = random.choice(['r','p','s'])
    if(user == comp):
        return 'Tie'
 
    # r>s , p>r ,s>p
    if is_win(user,comp):
        return f'YOU WON , computer choice:{comp}'
    return f'YOU lost , Computer choose {comp}'
    

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r' ) \
        or (player == 's' and opponent == 'p'):
            return True

print(play())

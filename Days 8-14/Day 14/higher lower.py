import art, game_data, random
logo = art.logo
vs = art.vs
game_data = game_data.data

def game():
    def select_game_data():
        first = random.choice(game_data)
        second = random.choice(game_data)
        while first == second:
            second = random.choice(game_data)
        return(first,second)

    def get_result(choice,notchoice):
        if int(choice.get('follower_count')) > int(notchoice.get('follower_count')):
            return "win"
        else:
            return "loose"

    def get_winner(play_data):
        answer =input("Who has more followers A or B:")
        answer = answer.lower()
        if answer == "a":
            choice = play_data[0]
            notchoice = play_data[1]
            winorloose = get_result(choice,notchoice)
            return winorloose
        elif answer == "b":
            choice = play_data[1]
            notchoice = play_data[0]
            winorloose = get_result(choice,notchoice)
            return winorloose
        else:
            print("Not a valid answer, try again")
            get_winner(play_data)

    score = 0
    play_on = True
    while play_on:
        play_data = select_game_data()
        print(logo)
        print(f"Compare A: {play_data[0].get('name')}, a {play_data[0].get('description')}, from {play_data[0].get('country')}.")
        print(vs)
        print(f"AGainst B: {play_data[0].get('name')}, a {play_data[0].get('description')}, from {play_data[0].get('country')}.")
        winner = get_winner(play_data)
        print(f"You {winner}")
        if winner == "win":
            score += 1
            print(f"Your score is {score}")
        else:
            print(f"Your final score is {score}")
            again = input("Want to play again? Yes or No\n")
            again = again.lower()
            if again == "yes":
                game()
            else:
                play_on = False


game()
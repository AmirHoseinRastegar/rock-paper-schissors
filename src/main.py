import random 


class RockPaperScissorsGame:
    def __init__(self,name):
        self.name = name
        
        self.possible_choices=['rock','paper','scissors']
        
    def get_user_choice(self):
        
        user_choice= input(f"Enter Your Choice to play({self.possible_choices})")
        if user_choice.lower() in self.possible_choices:
            return user_choice.lower()
        
        print('Invalid choice please try again')
        return self.get_user_choice()
    
    def get_pc_choice(self):
        return random.choice(self.possible_choices)
    
    
    def winner(self,user_choice,pc_choice):
        if user_choice==pc_choice:
            return print('tie')
            
        win_combination=[('rock','scissors'),('scissors','paper'),('paper','rock')]
        for win_comb in win_combination:
            if (user_choice==win_comb[0]) & (pc_choice==win_comb[1]):
                return "You Won"
                
        return "You Lost"
    
    
    def play(self):
        user_input=self.get_user_choice()
        pc_input= self.get_pc_choice()
        print(f"Pc Choice: {pc_input}")
        print(self.winner(user_input,pc_input))
        

if __name__=='__main__':
    game= RockPaperScissorsGame("AmirHosein")
    
    while True:
        game.play()
        
        continue_choosing= input("press any key to play again or press q to finish the game...")
        if continue_choosing.lower() =='q':
            break  
           
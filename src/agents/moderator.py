from agent import Agent



class SimpleModeratorAgent(Agent):
    def __init__(self, name):
        super().__init__(name, 'Evaluate Moderator')
        self.turn_order = []
        self.current_turn_index = 0
        self.topics = []
        
    def get_topics(self):
        self.topics = ["The impact of technology on education", "Climate changes", "Risk of AI in future", "Finding friend for our life"]
        return self.topics

    def set_turn_order(self, debaters):
        self.turn_order = debaters
        self.current_turn_index = 0
        
    def moderate_turn(self):
        if not self.turn_order:
            raise ValueError("Turn order not set")
        current_debater = self.turn_order[self.current_turn_index]
        self.current_turn_index = (self.current_turn_index + 1) % len(self.turn_order)
        return current_debater
    
    def moderate_debate(self, debaters, topic):
        if not self.turn_order:
            self.set_turn_order(debaters)
            print(f"Moderating a debate on '{topic}'")
            for phase in ['Opening Statement', 'Main Argument', 'Rebuttal', 'Closing Statement']:
                print(f"\n{phase} Phase:")
                for debater in debaters:
                    debater.generate_argument(topic)
        
    def start_debate(self, topic):
        print(f"Starting the debate on: {topic}")
        for phase in ['Opening Statements', 'Main Arguments', 'Rebuttals', 'Closing Statements']:
            print(f"Phase: {phase}")
            
    def set_turn_order(self, debaters):
        self.turn_order = debaters



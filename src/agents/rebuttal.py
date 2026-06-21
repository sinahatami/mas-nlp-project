from .base import Agent
from utils.llm import shared_argument_generator


class RebuttalAgent(Agent):
    def __init__(self, name):
        super().__init__(name, 'Rebuttal Debater Agent')
        self.argument_generator = shared_argument_generator
    
    def generate_rebuttal(self, opponent_argument, topic):
        context = f"Rebutting the argument on {topic}: {opponent_argument}"
        rebuttal = self.argument_generator(context, max_length=80)[0]['generated_text']
        return rebuttal
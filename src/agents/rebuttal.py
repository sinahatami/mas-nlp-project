from agent import Agent
from transformers import pipeline


class RebuttalAgent(Agent):
    def __init__(self, name):
        super().__init__(name, 'Rebuttal Debater Agent')
        self.argument_generator = pipeline('text-generation', model='gpt2')
    
    def generate_rebuttal(self, opponent_argument, topic):
        context = f"Rebutting the argument on {topic}: {opponent_argument}"
        rebuttal = self.argument_generator(context, max_length=80)[0]['generated_text']
        return rebuttal
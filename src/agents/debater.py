import random
from transformers import pipeline
from agent import Agent




class DebaterAgent(Agent):
    def __init__(self, name, style):
        super().__init__(name, 'Debater')
        self.feedback_history = []
        self.style = style
        self.argument_generator = pipeline('text-generation', model='gpt2-medium')

    def generate_argument(self, topic, previous_arguments=None):
        if previous_arguments is None:
            previous_arguments = []
        context = " ".join(previous_arguments[-2:])
        if self.style == "Factual":
            return self.generate_factual_argument(topic, context)
        elif self.style == "Emotional":
            return self.generate_emotional_argument(topic, context)
        
    def generate_factual_argument(self, topic, context):
        factual_prompts = [
            f"Discuss the statistical impact of {topic}.",
            f"Explain a study about {topic} and its conclusions.",
            f"Describe the empirical evidence supporting {topic}."
        ]
        if context == '':
            prompt = random.choice(factual_prompts)
        else:
            prompt = random.choice(factual_prompts) + f" Considering previous points: {context}"
        return self.argument_generator(prompt, max_new_tokens=120)[0]['generated_text']
    
    def generate_emotional_argument(self, topic, context):
        emotional_prompts = [
            f"Share a personal story about how {topic} affects individuals.",
            f"Discuss the ethical implications of {topic}.",
            f"Make an emotional appeal about the importance of {topic}."
        ]
        if context == '':
            prompt = random.choice(emotional_prompts)
        else:
            prompt = random.choice(emotional_prompts) + f" Considering previous points: {context}"
        return self.argument_generator(prompt, max_new_tokens=120)[0]['generated_text']



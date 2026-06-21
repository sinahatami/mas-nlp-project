from .base import Agent

import spacy
nlp = spacy.load("en_core_web_md")

class EvaluateModeratorAgent(Agent):
    def __init__(self, name):
        super().__init__(name, 'Evaluate Moderator')
        

    def evaluate_relevance_spacy(self, current_debater, argument, topic):
        doc_argument = nlp(argument)
        doc_topic = nlp(topic)
        relevance_score = doc_argument.similarity(doc_topic) * 100
        return relevance_score
        
    def adapt_strategy(self, current_debater):
        if not current_debater.feedback_history:
            print(f"No feedback available for {current_debater.name}.")
            return 0, "No feedback available yet."
        average_score = sum(current_debater.feedback_history) / len(current_debater.feedback_history)
        print(f"Average feedback score for {current_debater.name}: {average_score:.2f}")
        result = ''

        if average_score < 50:
            result = f"{current_debater.name}'s average score is {average_score:.2f}. So, needs significant improvement in argument quality."
            print(result)
            return average_score, result 
        elif average_score < 70:
            result = f"{current_debater.name}'s average score is {average_score:.2f}. So, could benefit from moderate improvements."
            print(result)
            return average_score, result 
        else:
            result = f"{current_debater.name}'s average score is {average_score:.2f}. So, is performing well. Minor tweaks could be made."
            print(result)
            return average_score, result 
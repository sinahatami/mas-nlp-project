from evaluate_moderator_agent import EvaluateModeratorAgent
from output_debate import create_debate_pdf
from debater_agent import DebaterAgent
from rebuttal_agent import RebuttalAgent
from simple_moderate_agent import SimpleModeratorAgent


debater1 = DebaterAgent(name="Alice", style="Factual")
debater2 = DebaterAgent(name="Bob", style="Emotional")
rebuttal_agent = RebuttalAgent(name="Eve")
simple_moderator = SimpleModeratorAgent(name="Carol")
evaluate_moderator = EvaluateModeratorAgent(name="Alex")

simple_moderator.set_turn_order([debater1, debater2])

debater1.introduce()
debater2.introduce()
rebuttal_agent.introduce()
simple_moderator.introduce()
evaluate_moderator.introduce()

debate_content = []
topics = simple_moderator.get_topics()

for index1, topic in enumerate(topics):
    simple_moderator.start_debate(topic)
        
    previous_arguments_debater1 = []
    previous_arguments_debater2 = []

    for index2 in range(3):
        

        current_debater = simple_moderator.moderate_turn()
        print(f"\nRound {index2 + 1} {current_debater.name}'s turn to argue:")
        argument1 = current_debater.generate_argument(topic, previous_arguments_debater1)
        previous_arguments_debater1.append(argument1)
        print(f"{current_debater.name}'s argument: {argument1}")
        debate_content.append(f"Round {index2 + 1}")
        debate_content.append(f"topic {index1 + 1} : '{topic}':")
        debate_content.append(f"{current_debater.name}'s argument: {argument1}")
        

        relevance_score1 = evaluate_moderator.evaluate_relevance_spacy(current_debater, argument1, topic)
        print(f"Relevance Score for {current_debater.name}'s argument: {relevance_score1:.2f}")
        debate_content.append(f"Relevance Score for {current_debater.name}'s argument: {relevance_score1:.2f}")

        current_debater.feedback_history.append(relevance_score1)
        average_score, feedback = evaluate_moderator.adapt_strategy(current_debater)
        debate_content.append(f"Feedback: {feedback}")
        
        debate_content.append("____________________________")
        
        
        

        rebuttal1 = rebuttal_agent.generate_rebuttal(argument1, topic)
        previous_arguments_debater1.append(rebuttal1)
        print(f"{rebuttal_agent.name}'s rebuttal to {current_debater.name}: {rebuttal1}")
        debate_content.append(f"{rebuttal_agent.name}'s rebuttal to {current_debater.name}: {rebuttal1}")

        debate_content.append("____________________________")
        
        

        current_debater = simple_moderator.moderate_turn()
        print(f"\n{current_debater.name}'s turn to argue:")
        argument2 = current_debater.generate_argument(topic, previous_arguments_debater2)
        previous_arguments_debater2.append(argument2)
        print(f"{current_debater.name}'s argument: {argument2}")
        debate_content.append(f"{current_debater.name}'s argument: {argument2}")
        

        relevance_score2 = evaluate_moderator.evaluate_relevance_spacy(current_debater, argument2, topic)
        print(f"Relevance Score for {current_debater.name}'s argument: {relevance_score2:.2f}")
        debate_content.append(f"Relevance Score for {current_debater.name}'s argument: {relevance_score2:.2f}")

        current_debater.feedback_history.append(relevance_score2)
        average_score2, feedback2 = evaluate_moderator.adapt_strategy(current_debater)
        debate_content.append(f"Feedback: {feedback2}")
        
        debate_content.append("____________________________")
        

        rebuttal2 = rebuttal_agent.generate_rebuttal(argument2, topic)
        previous_arguments_debater2.append(rebuttal2)
        print(f"{rebuttal_agent.name}'s rebuttal to {current_debater.name}: {rebuttal2}")
        debate_content.append(f"{rebuttal_agent.name}'s rebuttal to {current_debater.name}: {rebuttal2}")
        
        
        debate_content.append("____________________________")
        
    

        if relevance_score1 > relevance_score2:
            winner = debater1.name
            debate_content.append(f"\nThe winner is {winner} with a score of {relevance_score1:.2f} in round {index2 + 1}")
            print(f"\nThe winner is {winner} with a score of {relevance_score1:.2f} in round {index2 + 1}")
        elif relevance_score1 < relevance_score1:
            winner = debater2.name
            debate_content.append(f"\nThe winner is {winner} with a score of {relevance_score2:.2f} in round {index2 + 1}")
            print(f"\nThe winner is {winner} with a score of {relevance_score2:.2f} in round {index2 + 1}")
        else:
            debate_content.append(f"\nThe debate ends in a tie in round {index2 + 1}")
            print("\nThe debate ends in a tie.")
        
        debate_content.append("_________________________________________________________________")
        

    if average_score > average_score2:
        winner = debater1.name
        debate_content.append(f"\nThe winner is {winner} with a score of {average_score:.2f} in topic of {topic}")
        print(f"\nThe winner is {winner} with a score of {average_score:.2f} in topic of {topic}")
    elif average_score < average_score2:
        winner = debater2.name
        debate_content.append(f"\nThe winner is {winner} with a score of {average_score2:.2f} in topic of {topic}")
        print(f"\nThe winner is {winner} with a score of {average_score2:.2f} in topic of {topic}")
    else:
        debate_content.append("\nThe debate ends in a tie  in topic of")
        print("\nThe debate ends in a tie.")


create_debate_pdf("debate_summary.pdf", debate_content)

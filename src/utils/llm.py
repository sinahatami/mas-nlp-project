from transformers import pipeline

# Share a single model instance across agents to save memory and initialization time
shared_argument_generator = pipeline('text-generation', model='gpt2-medium')

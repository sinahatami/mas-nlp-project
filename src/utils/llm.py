from transformers import pipeline
import torch

# Automatically use GPU for best performance if available
device = 0 if torch.cuda.is_available() else -1

# Share a single model instance across agents to save memory and initialization time
shared_argument_generator = pipeline(
    'text-generation', 
    model='gpt2-medium', 
    device=device,
    pad_token_id=50256
)

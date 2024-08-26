import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from utils.context_manager import ConversationContext
from model.emotion_handler import EmotionHandler

# Load pre-trained model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

context = ConversationContext()
emotion_handler = EmotionHandler()

def generate_response(prompt, max_length=500):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2)
    return tokenizer.decode(output[0], skip_special_tokens=True)

def main():
    print("Hey there! I'm so happy to talk to you. How are you doing today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye', 'exit']:
            print("Aww, I'll miss you! Take care and come back soon!")
            break

        context.add_user_message(user_input)
        full_context = context.get_context_string()
        
        emotion = emotion_handler.get_emotion(user_input)
        full_prompt = f"{full_context}\nAI Girlfriend ({emotion}):"
        response = generate_response(full_prompt)
        
        # Extract only the AI's response
        ai_response = response.split("AI Girlfriend:")[-1].strip()
        
        context.add_ai_message(ai_response)
        print(ai_response)

if __name__ == "__main__":
    main()
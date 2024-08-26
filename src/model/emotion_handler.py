import random

class EmotionHandler:
    def __init__(self):
        self.emotions = ['happy', 'excited', 'neutral', 'sad', 'angry', 'jealous']
        self.current_emotion = 'neutral'

    def get_emotion(self, user_input):
        # This is a very simple emotion detection. In a real scenario, you'd use
        # more sophisticated NLP techniques to determine the appropriate emotion.
        if any(word in user_input.lower() for word in ['love', 'like', 'happy']):
            self.current_emotion = random.choice(['happy', 'excited'])
        elif any(word in user_input.lower() for word in ['sad', 'upset', 'angry']):
            self.current_emotion = random.choice(['sad', 'angry'])
        elif any(word in user_input.lower() for word in ['other', 'girl', 'friend']):
            self.current_emotion = 'jealous'
        else:
            self.current_emotion = random.choice(self.emotions)
        
        return self.current_emotion
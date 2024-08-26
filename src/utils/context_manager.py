class ConversationContext:
    def __init__(self, max_turns=5):
        self.context = []
        self.max_turns = max_turns

    def add_user_message(self, message):
        self.context.append(f"User: {message}")
        self._trim_context()

    def add_ai_message(self, message):
        self.context.append(f"AI Girlfriend: {message}")
        self._trim_context()

    def get_context_string(self):
        return "\n".join(self.context)

    def _trim_context(self):
        if len(self.context) > self.max_turns * 2:
            self.context = self.context[-self.max_turns * 2:]
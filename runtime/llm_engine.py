class LLMEngine:
    def __init__(self, models):
        self.models = models  # {"default": model_obj, "react": model_obj, ...}

    def run(self, agent_role, skill, prompt):
        model = self.models.get(skill, self.models["default"])
        return model.generate(prompt)  # ou chamar API local
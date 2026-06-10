from llama_cpp import Llama
from threading import Lock

class LLM:

    def __init__(self, model_path: str):

        self.model = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_threads=8,
            verbose=False,
            low_vram=True
        )

        self.lock = Lock()

        print(f"[LLM] Modelo carregado: {model_path}")

    def generate(
        self,
        prompt: str,
        max_tokens=1024,
        temperature=0.7
    ) -> str:

        with self.lock:

            response = self.model(
                prompt,
                max_tokens=max_tokens,
                temperature=temperature
            )

        return response["choices"][0]["text"]

llm = LLM(
    "models/qwen2.5-coder-1.5b-instruct-q2_k.gguf"
)
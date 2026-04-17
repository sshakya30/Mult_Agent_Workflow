"""
Multi-Agent Workflow

Converted from the Jupyter notebook for easy viewing and download from GitHub.
"""

# Required dependencies:
# pip install transformers accelerate torch

# ==== Cell 1 ====
# ==== Installing Necessary Libraries ====
# !pip install transformers accelerate torch  # Notebook-only command; run in a notebook or terminal separately.

# ==== Cell 2 ====
# ==== Importing Necessary Libraries ====
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

# ==== Cell 3 ====
# ==== HF Model Setup ====

MODEL_NAME = "tiiuae/falcon-7b-instruct"

# Load once for both summarization and generation
print("🔄 Loading HuggingFace model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME, torch_dtype=torch.float16, device_map="auto"
)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# ==== Cell 4 ====
# ==== Agents ====

class PlannerAgent:
    def plan_task(self, goal):
        print(f"[PlannerAgent] 🎯 Planning for goal: '{goal}'")
        return [
            "Fetch the latest technology news headlines",
            "Summarize the fetched news using a Hugging Face model",
            "Generate a tweet from the summary using a Hugging Face model"
        ]


class WorkerAgent:
    def __init__(self):
        self.news_data = None
        self.summary = None

    def perform_task(self, subtask):
        print(f"\n[WorkerAgent] ⚙️ Performing: '{subtask}'")

        try:
            task_lower = subtask.lower()
            if "summarize" in task_lower:
                return self.summarize_news_with_llm()
            elif "tweet" in task_lower:
                return self.generate_tweet_with_llm()
            elif "fetch" in task_lower:
                return self.fetch_tech_news()
            else:
                raise ValueError(f"Unknown subtask: {subtask}")
        except Exception as e:
            print(f"[WorkerAgent] ❌ Error during task '{subtask}': {e}")
            raise

    def fetch_tech_news(self):
        print("[WorkerAgent] 🔍 Fetching tech news...")
        headlines = [
            "AI model beats doctors at diagnosing lung cancer.",
            "Apple launches new M4 chip.",
            "NASA successfully tests nuclear-powered rover for Mars."
        ]
        self.news_data = " ".join(headlines)
        print(f"[WorkerAgent] ✅ Headlines fetched: {self.news_data}")
        return self.news_data

    def summarize_news_with_llm(self):
        if not self.news_data:
            raise ValueError("No news data available for summarization.")

        prompt = f"Summarize the following news headlines:\n{self.news_data}"
        print(f"[WorkerAgent] 🧠 Sending prompt to summarizer:\n{prompt}")

        try:
            response = generator(prompt, max_new_tokens=100, do_sample=False)[0]["generated_text"]
            summary = response.replace(prompt, "").strip()
            self.summary = summary
            print(f"[WorkerAgent] ✅ Summary generated: {self.summary}")
            return self.summary
        except Exception as e:
            print(f"[WorkerAgent] ❌ Error during summarization: {e}")
            raise

    def generate_tweet_with_llm(self):
        if not self.summary:
            raise ValueError("No summary available to generate tweet.")

        prompt = f"Write a short tweet about the following tech news summary:\n{self.summary}"
        print(f"[WorkerAgent] 🐦 Sending prompt to tweet generator:\n{prompt}")

        try:
            response = generator(prompt, max_new_tokens=60, do_sample=True, temperature=0.7)[0]["generated_text"]
            tweet = response.replace(prompt, "").strip()
            print(f"[WorkerAgent] ✅ Tweet generated: {tweet}")
            return tweet
        except Exception as e:
            print(f"[WorkerAgent] ❌ Error during tweet generation: {e}")
            raise


class Coordinator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.worker = WorkerAgent()

    def run(self, goal):
        print(f"\n🚀 [Coordinator] Running task: {goal}")
        subtasks = self.planner.plan_task(goal)

        results = {}
        for subtask in subtasks:
            try:
                result = self.worker.perform_task(subtask)
                results[subtask] = result
            except Exception as e:
                print(f"[Coordinator] ❌ Error in subtask '{subtask}': {e}")
                results[subtask] = None
                break  # Optional: break/continue depending on design

        print("\n✅ === Final Results ===")
        for task, res in results.items():
            print(f"\n🔹 {task}:\n{res}")
        return results

# ==== Cell 5 ====
# ==== Run ====

if __name__ == "__main__":
    task = "Summarize latest tech news and suggest a tweet"
    coordinator = Coordinator()
    coordinator.run(task)

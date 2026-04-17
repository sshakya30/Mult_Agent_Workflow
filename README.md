# Mult_Agent_Workflow

## 📌 Overview

This project demonstrates a simple **multi-agent workflow system** built using Python and Hugging Face Transformers.

## You can now view and test the fully completed sample published website at the following link: https://intelligent-interview-app--shakyasupernice.replit.app 

The notebook simulates how multiple AI agents can collaborate to achieve a task:

* **Planner Agent** → Breaks down a high-level goal into subtasks
* **Worker Agent** → Executes each subtask
* **Coordinator** → Orchestrates the overall workflow

### 🎯 Example Task

> "Summarize latest tech news and suggest a tweet"

---

## ⚙️ Features

* Multi-agent architecture (Planner, Worker, Coordinator)
* Uses **Hugging Face Transformers**
* Text generation powered by **Falcon-7B-Instruct**
* End-to-end pipeline:
  **Plan → Fetch → Summarize → Generate Tweet**

---

## 📂 File Structure

```
multi_agent_workflow.ipynb   # Main notebook file
README.md                   # Project documentation
```

---

## 🚀 How to Run the Notebook

### 1️⃣ Prerequisites

Make sure you have:

* Python 3.8+
* Jupyter Notebook or JupyterLab installed

---

### 2️⃣ Install Required Libraries

Run the following command (or execute the first cell in the notebook):

```bash
pip install transformers accelerate torch
```

---

### 3️⃣ Open the Notebook

Launch Jupyter and open the notebook:

```bash
jupyter notebook
```

Then open:

```
multi_agent_workflow.ipynb
```

---

### 4️⃣ Run All Cells

Execute the cells in order:

1. Install dependencies
2. Import libraries
3. Load Hugging Face model
4. Define agents
5. Run the workflow

---

## 🧠 Model Used

* **Model Name:** `tiiuae/falcon-7b-instruct`
* Loaded using Hugging Face Transformers

⚠️ **Note:**

* This model is large (~7B parameters)
* Requires:

  * A GPU (recommended), OR
  * High RAM if running on CPU

---

## 🔄 Workflow Explanation

### 🧩 Step 1: Planning

The `PlannerAgent` breaks the main goal into subtasks:

* Fetch news
* Summarize content
* Generate tweet

### ⚙️ Step 2: Execution

The `WorkerAgent`:

* Retrieves (or simulates) news data
* Uses the model to summarize
* Generates a tweet

### 🎛️ Step 3: Coordination

The `Coordinator`:

* Calls the planner
* Passes tasks to the worker
* Ensures sequential execution

---

## ▶️ Running the Script Section

At the bottom of the notebook:

```python
if __name__ == "__main__":
    task = "Summarize latest tech news and suggest a tweet"
    coordinator = Coordinator()
    coordinator.run(task)
```

This triggers the full multi-agent workflow.

---

## ⚠️ Important Notes

* First-time model loading may take time
* Ensure stable internet connection (for model download)
* GPU is highly recommended for faster execution
* Currently, not integrated with real-time news APIs
* Deployed as a web app using Replit.com

---


## 👤 Author

Shakya Adheesha Samarasinghe

---

## 📜 License

This project is for educational and experimental purposes.

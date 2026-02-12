# Local AI agent 🚀

## About

A brief description of the project: Run a local AI with Ollama using a CSV as the knowledge base

- What problem does it solve?
  Not need to use llm's like chatgpt on the web that requires the web
- Why did you build it?
  To practice and familiarise LLMs, frameworks like langchain and understand AI agents more
- Who is it for?
  Anyone who wants to run LLMs locally. Fun project! Mess around with the models/ template (prompts)!

---

## Tech Stack

- **Python** – main language for running scripts
- **Ollama** – local AI framework
- **Pandas** – handling CSV files
- **NumPy** – optional, for data processing
- **VS Code / Terminal** – development environment
- **Chromadb** - vector database for embeddings

---

## Getting Started

1. Create virtual environment

```bash
python -m venv virtual-environment-name
```

2. Install packages through requirements.txt

```bash
pip install -r  ./requirements.txt
```

3. Download ollama onto your desktop and install llama3.2 & mxbai-embed-large

```bash
ollama pull llama3.2
ollama pull mxbai-embded-large
```

### Prerequisites

Python
ollama
Any cvs file

### Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/project-name.git

# Go into the project directory
cd project-name
```

<!--Run the chatbot  -->

```bash
python main.py
```

Note: You can change the prompt (template) in main.py to change the topic of the llm. I put in a guardrail so it doesn't answer random questions.

You can also change the data, be aware of the vectorising will change how its stored in Chroma (vector db).

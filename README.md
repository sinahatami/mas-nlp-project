<div align="center">
  <h1>🤖 Multi-Agent Debate Simulation Framework</h1>
  
  ![Python](https://img.shields.io/badge/Language-Python-blue.svg)
  ![NLP](https://img.shields.io/badge/Domain-NLP-green.svg)
  ![Hugging Face](https://img.shields.io/badge/Framework-Hugging_Face-orange.svg)
  ![spaCy](https://img.shields.io/badge/Library-spaCy-blueviolet.svg)
  ![LLMs](https://img.shields.io/badge/Technology-LLMs-red.svg)
</div>

An autonomous system designed to simulate, moderate, and evaluate structured debates between AI personalities using Large Language Models (LLMs) and Natural Language Processing (NLP).

---

## 🚀 Key Features

* **🧠 Dynamic Argument Generation**: Employs the `gpt2-medium` model to generate context-aware arguments based on specific rhetorical styles: **Factual** or **Emotional**.
* **⚖️ Automated Judging**: Utilizes the `spaCy` library to calculate a **Relevance Score** (0-100) by measuring semantic similarity between the argument and the topic.
* **🔄 Adaptive Feedback**: The moderator tracks performance history and provides qualitative feedback to agents (e.g., "performing well" or "needs improvement") based on their average scores.
* **📝 PDF Reporting**: Automatically compiles a full transcript of the debate—including scores, rebuttals, and winners—into a professional PDF document.
* **🎭 Diverse Personas**: Features specialized agents for empirical data, emotional appeals, and dedicated rebuttals.

---

## 👥 Meet the Agents

The framework utilizes a specialized cast to simulate a complete debate environment

| Agent | Role | Specialization | Model |
| :--- | :--- | :--- | :--- |
| **Alice** | Debater | **Factual**: Focuses on statistical impact and empirical evidence.| GPT-2 Medium |
| **Bob** | Debater | **Emotional**: Focuses on ethical implications and personal stories. | GPT-2 Medium |
| **Eve** | Rebuttal | **Counter-Arguments**: Analyzes opponent claims to generate direct rebuttals. | GPT-2 Medium |
| **Carol** | Moderator | **Turn Management**: Orchestrates the flow, phases, and turn-taking. | Rule-based |
| **Alex** | Evaluator | **Scoring**: Calculates semantic relevance and determines winners. | spaCy |

---

## 📂 Project Structure

* `src/agents/debater.py`: Logic for factual and emotional argument generation.
* `src/agents/rebuttal.py`: Specialized agent for generating counter-arguments.
* `src/agents/evaluator.py`: Scoring system using NLP similarity metrics.
* `src/agents/moderator.py`: Manages debate phases and turn orders.
* `src/utils/pdf_generator.py`: Logic for PDF generation using `ReportLab`.
* `src/main.py`: The orchestrator that runs the multi-round simulation.

---

## 🛠️ Installation & Usage

### 1. Requirements
Ensure you have the following Python libraries installed:
* `transformers` (Hugging Face)
* `spaCy` (with the `en_core_web_md` model)
* `reportlab`

### 2. Run the Simulation
Execute the main script to begin a debate on pre-configured topics such as Technology in Education, Climate Change, or AI Risks.

```bash
export PYTHONPATH=.
python src/main.py
```

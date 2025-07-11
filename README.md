🧠 Boot Agent – AI Agent in Python
This project was built while following the Boot.dev course: Build an AI Agent in Python. It teaches how to create a modular, terminal-based AI agent that can interpret natural language and execute commands using local tools and APIs.

🔍 What It Is
A lightweight, local-first AI agent that:

Accepts text input (via CLI)

Parses commands using an LLM (e.g., OpenAI GPT)

Selects and executes matching tools ("skills") like file operations, web search, etc.

Returns the result to the user — like a minimal AI assistant

🛠️ Key Features
Modular Tool System: Skills are Python modules with metadata, loaded dynamically.

Prompt Engineering: Carefully crafted prompts guide the LLM to act predictably.

Memory / Context: Basic context handling to support multi-step interaction.

LLM Backend Support: OpenAI API integration (can be extended to others).

CLI Agent Loop: Agent runs in a REPL-style interface.

🧪 Skills / Tools Examples
Read or write files

Get current time or date

Search Google or Wikipedia

Summarize text

Each tool has:

A description

An input/output schema

A run() function

💡 What I Learned
How to combine natural language input with Python function execution

How to wrap tools into schema-based interfaces for use with an LLM

How to dynamically route tasks using reasoning from the LLM

Basics of prompt engineering, API handling, and modular Python design

📁 Project Files (Typical Structure)
bash
Copy
Edit
boot_agent/
├── agent.py          # Main agent loop
├── tools/            # Skills/tools the agent can use
│   ├── file_reader.py
│   └── ...
├── prompts/          # System prompts for agent behavior
├── models/           # (Optional) Memory/context handling
└── config.py         # API keys, constants, etc.
🧠 Next Steps or Extensions
Add voice input/output for a fully spoken agent

Add persistent memory (e.g., SQLite or JSON memory)

Extend toolset (send email, control IoT devices, etc.)

Add GUI or browser-based frontend

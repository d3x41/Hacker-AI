# HackerAI - Your Local AI Security Assistant

Welcome to **HackerAI**! This tool combines the power of **Ollama (Mistral)** with **your terminal** to turn natural language into real shell commands. Whether you want to **scan websites with nmap** or **ping a server**, just type what you want — HackerAI handles the rest. All locally, without any API costs! 🐱‍💻

![https://github.com/yogsec/Hacker-AI/blob/main/Screenshot%20from%202025-03-04%2015-50-47.png?raw=true](https://github.com/yogsec/Hacker-AI/blob/main/Screenshot%20from%202025-03-04%2015-50-47.png?raw=true)

---

## Installation Guide

### 1. Install Ollama

Ollama is the core engine that runs the AI model **Mistral** locally.

🔗 Install Ollama from: [https://ollama.com/download](https://ollama.com/download)

For Linux:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

For Windows:
👉 Install via: [https://ollama.com/download](https://ollama.com/download)

---

### 2. Download the Mistral Model

After installing Ollama, pull Mistral (recommended lightweight model):
```bash
ollama pull mistral
```

---

### 3. Clone or Download HackerAI

```bash
git clone https://github.com/yogsec/Hacker-AI.git
cd Hacker-AI
```

Or download `hackerai.py` manually if you want.

---

### 4. Install Python Requirements

Make sure you have Python 3.8+ and install required libraries:
```bash
pip install -r requirements.txt
```

**Create `requirements.txt`:**
```
requests
```

---

### 5. Run HackerAI

Start **Ollama** (if not already running):
```bash
ollama serve
```

Then run:
```bash
python3 hackerai.py
```

---

## Usage

Just type natural language commands like:
```
What do you want to do? (e.g., scan google.com with nmap): scan google.com with nmap
```

HackerAI will think and execute:
```bash
nmap google.com
```

### 📖 Other Examples

| Input | Action |
|---|---|
| scan google.com with nikto | Runs `nikto -h google.com` |
| ping example.com | Runs `ping -c 4 example.com` |
| curl example.com | Runs `curl example.com` |

---

## 🛠️ Common Problems & Solutions

| Problem | Cause | Solution |
|---|---|---|
| `Error communicating with Ollama` | Ollama is not running | Start Ollama with `ollama serve` |
| `Model mistral not found` | Mistral not downloaded | Run `ollama pull mistral` |
| `This request doesn't translate into a valid shell command` | Non-technical request (like "who is the richest man") | Only ask for commands related to hacking or sysadmin work. |
| Syntax Error in Command | Mistral hallucinated something wrong | Rephrase the question or ask in simpler terms |

---

## 💻 Supported Commands (Examples)

Scan websites with `nmap`  
Scan vulnerabilities with `nikto`  
Perform `ping` tests  
Fetch URLs with `curl`  
Extendable to any command you want!

---

##  Important Note

> HackerAI only supports **practical shell commands**. It **does not answer general knowledge questions** like "who is the richest person". It’s focused only on commands you can run in a terminal.



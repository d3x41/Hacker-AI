# 🚀 HackerAI - Your Local AI Security Assistant

Welcome to **HackerAI**! This tool combines the power of **Ollama (Mistral)** with **your terminal** to turn natural language into real shell commands. Whether you want to **scan websites with nmap** or **ping a server**, just type what you want — HackerAI handles the rest. All locally, without any API costs! 🐱‍💻

![https://github.com/yogsec/Hacker-AI/blob/main/Screenshot%20from%202025-03-04%2015-50-47.png?raw=true](https://github.com/yogsec/Hacker-AI/blob/main/Screenshot%20from%202025-03-04%2015-50-47.png?raw=true)

---

## 📥 Installation Guide

### 1️⃣ Install Ollama

Ollama is the core engine that runs the AI model **Mistral** locally.

🔗 Install Ollama from: [https://ollama.com/download](https://ollama.com/download)

For Linux:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

For Windows:
👉 Install via: [https://ollama.com/download](https://ollama.com/download)

---

### 2️⃣ Download the Mistral Model

After installing Ollama, pull Mistral (recommended lightweight model):
```bash
ollama pull mistral
```

---

### 3️⃣ Clone or Download HackerAI

```bash
git clone https://github.com/yogsec/hackerai.git
cd hackerai
```

Or download `hackerai.py` manually if you want.

---

### 4️⃣ Install Python Requirements

Make sure you have Python 3.8+ and install required libraries:
```bash
pip install -r requirements.txt
```

**Create `requirements.txt`:**
```
requests
```

---

### 5️⃣ Run HackerAI

Start **Ollama** (if not already running):
```bash
ollama serve
```

Then run:
```bash
python3 hackerai.py
```

---

## ⚡ Usage

Just type natural language commands like:
```
What do you want to do? (e.g., scan google.com with nmap): scan google.com with nmap
```

HackerAI will think 🤔 and execute:
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

✅ Scan websites with `nmap`  
✅ Scan vulnerabilities with `nikto`  
✅ Perform `ping` tests  
✅ Fetch URLs with `curl`  
✅ Extendable to any command you want!

---

## ⚠️ Important Note

> HackerAI only supports **practical shell commands**. It **does not answer general knowledge questions** like "who is the richest person". It’s focused only on commands you can run in a terminal.

---

## 🌟 Let's Connect!

Hello, Hacker! 👋 We'd love to stay connected with you. Reach out to us on any of these platforms and let's build something amazing together:

🌐 **Website:** [https://yogsec.github.io/yogsec/](https://yogsec.github.io/yogsec/)  
📜 **Linktree:** [https://linktr.ee/yogsec](https://linktr.ee/yogsec)  
🔗 **GitHub:** [https://github.com/yogsec](https://github.com/yogsec)  
💼 **LinkedIn (Company):** [https://www.linkedin.com/company/yogsec/](https://www.linkedin.com/company/yogsec/)  
📷 **Instagram:** [https://www.instagram.com/yogsec.io/](https://www.instagram.com/yogsec.io/)  
🐦 **Twitter (X):** [https://x.com/yogsec](https://x.com/yogsec)  
👨‍💼 **Personal LinkedIn:** [https://www.linkedin.com/in/cybersecurity-pentester/](https://www.linkedin.com/in/cybersecurity-pentester/)  
📧 **Email:** abhinavsingwal@gmail.com

---

## ☕ Buy Me a Coffee

If you find our work helpful and would like to support us, consider buying us a coffee. Your support keeps us motivated and helps us create more awesome content. ❤️

☕ **Support Us Here:** [https://buymeacoffee.com/yogsec](https://buymeacoffee.com/yogsec)

---

## 🏁 Ready? Start Hacking (Legally)! 👨‍💻👩‍💻

---

Want me to generate the `requirements.txt` and `installation.txt` files too, so you have a complete **package** to upload to GitHub? 😎

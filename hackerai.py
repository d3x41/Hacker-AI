import os
import time
import subprocess
import requests
import json
import sys
from threading import Thread
from itertools import cycle

# Configuration
OLLAMA_MODEL = "mistral"
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Global flag for spinner control
spinner_running = False


def display_header():
    print("\033[95m")
    print(r"""
 _     _ _______ _______ _     _ _______  ______      _______ _____
 |_____| |_____| |       |____/  |______ |_____/      |_____|   |  
 |     | |     | |_____  |    \_ |______ |    \_      |     | __|__
                                                                   

GitHub - https://github.com/yogsec
Donate - https://buymeacoffee.com/yogsec
    """)
    print("Welcome to HackerAI - Your Local AI Security Assistant")
    print("----------------------------------------------------\033[0m\n")
    print("Usage: Type your command like 'scan google.com with nmap'")
    print("Options: -h for help | -v for version\n")


def show_help():
    print("\nUsage:")
    print("  scan <target> with <tool>")
    print("Supported tools: nmap, nikto")
    print("Options:")
    print("  -h : Show this help message")
    print("  -v : Show version info\n")


def show_version():
    print("HackerAI v1.0 - Powered by Ollama & Mistral")


def ask_ollama(question):
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": (
            f"You are a command generator. Your job is to convert user requests into a single valid shell command.\n"
            f"Rules:\n"
            f"- No explanations.\n"
            f"- No extra text.\n"
            f"- No backticks.\n"
            f"- No creative answers.\n"
            f"- Only the raw shell command itself.\n"
            f"- If the request does not make sense for a shell command (like 'richest man'), return this exact string: 'invalid-request'.\n"
            f"User Request: {question}\n"
            f"Shell Command:"
        ),
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    if response.status_code == 200:
        command = response.json().get('response', '').strip()

        # Auto-clean extra formatting if Mistral misbehaves
        command = command.strip("`").strip('"').strip("'").strip()

        if command == "invalid-request":
            print("\033[91m[!] This request doesn't translate into a valid shell command.\033[0m")
            return None

        return command
    else:
        print(f"\033[91mError communicating with Ollama: {response.text}\033[0m")
        return None





def show_spinner(command):
    global spinner_running
    spinner = cycle(['|', '/', '-', '\\'])
    while spinner_running:
        sys.stdout.write(f"\rExecuting: {command} {next(spinner)}")
        sys.stdout.flush()
        time.sleep(0.2)


def run_command(command):
    global spinner_running
    spinner_running = True

    spinner_thread = Thread(target=show_spinner, args=(command,))
    spinner_thread.start()

    process = subprocess.Popen(command, shell=True)
    process.communicate()

    spinner_running = False
    spinner_thread.join()

    # Clear the spinner line after completion
    print("\r" + " " * 50 + "\r", end="")


def main():
    display_header()

    while True:
        user_input = input("\nWhat do you want to do? (e.g., scan google.com with nmap): ").strip()

        if user_input == "-h":
            show_help()
            continue
        elif user_input == "-v":
            show_version()
            continue

        print("HackerAI is thinking... 🤔")

        command = ask_ollama(user_input)

        if not command:
            print("\033[91mFailed to fetch command from Ollama.\033[0m")
            continue

        print(f"\nExecuting command: {command}\n")

        run_command(command)

        print("\n\033[92mHackerAI is ready for the next command! (Press CTRL+C to exit)\033[0m\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye! 👋")

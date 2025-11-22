import os
import subprocess
import sys

modules = [
    "requests", "numpy", "pandas", "matplotlib", "scipy", "pillow",
    "opencv-python", "pyyaml", "tqdm", "loguru",
    "aiohttp", "flask", "fastapi", "httpx", "beautifulsoup4",
    "lxml", "python-dateutil", "regex", "jsonschema",
    "psutil", "pywin32", "pymem", "keyboard", "pyautogui", "colorama",
    "pytest", "black", "mypy", "rich",
    "sympy", "networkx"
]

def install(module):
    print(f"Installing: {module}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", module])

if __name__ == "__main__":
    print("\n=== Installing 30 Python Modules ===\n")
    for m in modules:
        try:
            install(m)
        except Exception as e:
            print(f"Failed to install {m}: {e}")

    print("\nAll modules attempted.\n")

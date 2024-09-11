from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["tkinter", "keyboard", "pyautogui", "PIL"],  # Inclua Pillow e pyautogui
    "includes": ["pyautogui", "PIL"],  # Force a inclusão de Pillow e pyautogui
    "zip_include_packages": ["encodings", "PySide6", "shiboken6"],
    "include_files": [
        ("./assets", "assets"),
    ]
}

setup(
    name = "Autoclick",
    version = "1.0",
    description = "Um simples projeto de um autoclick com Python.",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base="Win32GUI", icon="./assets/mouse.ico", target_name="Mouseclick", shortcut_name="Mouseclick")]
)
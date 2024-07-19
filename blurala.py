import subprocess
import os

user_home = os.getenv('USERPROFILE')
script_path = os.path.join(user_home, "bluralacritty", "bluralacritty.py")

subprocess.run(['python', script_path])


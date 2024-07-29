


##https://www.youtube.com/watch?v=ClTWPoDHY_s

import os
import subprocess
import sys

def install_jupyter():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "notebook"])
        print("Jupyter Notebook installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error installing Jupyter Notebook:", e)
        return False
    return True

def get_jupyter_scripts_path():
    user_site = site.getusersitepackages()

    scripts_dir = os.path.join(user_site.replace('site-packages', ''), 'Scripts')

    if os.path.exists(scripts_dir):
        return scripts_dir
    else:
        raise FileNotFoundError(f"The expected Scripts directory does not exist: {scripts_dir}")

def add_jupyter_to_path(scripts_dir):
    current_path = os.environ['PATH']

    if scripts_dir not in current_path:
        new_path = f"{scripts_dir};{current_path}"
        
        os.environ['PATH'] = new_path
        
        subprocess.run(['setx', 'PATH', new_path], shell=True)

        print("Jupyter Notebook has been added to the PATH.")
    else:
        print("Jupyter Notebook is already in the PATH.")

if __name__ == "__main__":
    if install_jupyter():
        try:
            scripts_dir = get_jupyter_scripts_path()
            print(f"The Scripts directory is: {scripts_dir}")
            add_jupyter_to_path(scripts_dir)
        except FileNotFoundError as e:
            print(e)



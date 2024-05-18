import subprocess
import re
import platform

def get_default_gateway():
    default_gateway = None
    if platform.system() == "Windows":
        try:
            result = subprocess.run(["ipconfig"], capture_output=True, text=True)
            output = result.stdout
            match = re.search(r"Default Gateway .*?: ([\d.]+)", output)
            if match:
                default_gateway = match.group(1)
        except Exception as e:
            print("An error occurred:", e)
    elif platform.system() == "Linux":
        try:
            result = subprocess.run(["ifconfig"], capture_output=True, text=True)
            output = result.stdout
            match = re.search(r"defaultroute.*?([\d.]+)", output)
            if match:
                default_gateway = match.group(1)
        except Exception as e:
            print("An error occurred:", e)
    return default_gateway

if __name__ == "__main__":
    default_gateway = get_default_gateway()
    if default_gateway:
        print("Default Gateway Address:", default_gateway)
    else:
        print("Default Gateway Address not found.")

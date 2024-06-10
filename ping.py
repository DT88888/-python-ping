#!/usr/bin/env python3
import subprocess
import sys
import platform

def ping(host):
    # Determine the command based on the OS
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '4', host]
    
    try:
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if output.returncode == 0:
            print(f"Ping to {host} was successful.\n")
            print(output.stdout)
        else:
            print(f"Ping to {host} failed.\n")
            print(output.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python ping_test.py <hostname>")
        sys.exit(1)
    
    host = sys.argv[1]
    ping(host)

if __name__ == "__main__":
    main()

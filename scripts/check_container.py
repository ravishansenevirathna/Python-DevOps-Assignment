#!/usr/bin/env python3

import subprocess
import sys

containername = input("Enter the container name: ").strip()
CONTAINER_NAME = containername

def check_container_running(name):
    try:
        output = subprocess.check_output(
            ["docker", "inspect", "-f", "{{.State.Running}}", name],
            stderr=subprocess.PIPE
        )
        return output.decode().strip() == "true"
    except subprocess.CalledProcessError:
        return False

def container_exists(name):
    try:
        subprocess.check_output(
            ["docker", "inspect", "-f", "{{.State.Status}}", name],
            stderr=subprocess.PIPE
        )
        return True
    except subprocess.CalledProcessError:
        return False

def restart_container(name):
    try:
        subprocess.check_call(["docker", "start", name])
        print(f"Container {name} restarted.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to restart container {name}: {e}")
        return False

if __name__ == "__main__":
    if check_container_running(CONTAINER_NAME):
        print(f"Container {CONTAINER_NAME} is already running.")
    else:
        print(f"Container {CONTAINER_NAME} is not running.")
        if container_exists(CONTAINER_NAME):
            print("Attempting to restart...")
            restart_container(CONTAINER_NAME)
        else:
            print(f"Container {CONTAINER_NAME} does not exist. Please create it first.")
            sys.exit(1)
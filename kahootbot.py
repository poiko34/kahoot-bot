import sys
import asyncio
import subprocess
import importlib
import argparse
from kahoot import KahootClient
from colorama import Fore, init

init(autoreset=True)

required_libraries = [
    "kahoot",
    "colorama",
    "argparse",
    "asyncio",
]

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_libraries():
    for library in required_libraries:
        try:
            importlib.import_module(library)
            print(f"{Fore.GREEN}Library {library} is already installed.")
        except ImportError:
            print(f"{Fore.RED}Library {library} not found. Installing...")
            install_package(library)



async def join_game(game_pin, username):
    client = KahootClient()
    try:
        await client.join_game(game_pin, username)
        print(f"{Fore.GREEN}Successfully joined game as {username}")
    except Exception as e:
        print(f"{Fore.RED}Error joining game as {username}: {e}")

async def run_bots(game_pin, base_username, count):
    tasks = [join_game(game_pin, f"{base_username}_{i+1}") for i in range(count)]
    await asyncio.gather(*tasks)

def main():
    parser = argparse.ArgumentParser(description="Kahoot Bot Runner")
    
    parser.add_argument("-i", "--game_pin", type=str, required=True, help="Enter the Game PIN")
    parser.add_argument("-n", "--base_username", type=str, required=True, help="Enter the Base Username")
    parser.add_argument("-m", "--bot_count", type=int, required=True, help="Enter the number of bots to join")

    args = parser.parse_args()

    check_and_install_libraries()

    if args.bot_count <= 0:
        print(f"{Fore.RED}Error: Bot count must be a positive number.")
        return

    print(f"{Fore.YELLOW}Running bots...")
    asyncio.run(run_bots(args.game_pin, args.base_username, args.bot_count))

if __name__ == "__main__":
    main()


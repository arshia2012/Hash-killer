from hash_cracker import HashCracker
import BetterRich
import argparse
from time import sleep

#Banner
def print_banner():
    banner = r"""
    __  __           __       __ __ _ ____         
   / / / /___ ______/ /_     / //_/(_) / /__  _____
  / /_/ / __ `/ ___/ __ \   / ,<  / / / / _ \/ ___/
 / __  / /_/ (__  ) / / /  / /| |/ / / /  __/ /    
/_/ /_/\__,_/____/_/ /_/  /_/ |_/_/_/_/\___/_/     
                                                   
                    Hash cracker made by aCoDeR(Arshia Rahbari)
                        FOR LEGAL USE ONLY!
"""
    print(banner)

#flags
parser = argparse.ArgumentParser(description="password cracker for legal use only")
parser.add_argument("-w", "--wordlist",type=str, help="Password list for crack", required=True)
parser.add_argument("-t", "--target", type=str, help="Target Hash to crack", required=True)
arg_parse = parser.parse_args()

print_banner()
sleep(0.2)

cracker = HashCracker()
cracker.crack(arg_parse.target, arg_parse.wordlist)
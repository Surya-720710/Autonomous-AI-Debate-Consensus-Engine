
from colorama import Fore, Style, init

init(autoreset=True)

class DebateLogger:
    @staticmethod
    def print_header(title: str):
        print(f"\n{Fore.CYAN}{Style.BRIGHT}{'=' * 60}")
        print(f" ⚡ {title.upper()}")
        print(f"{'=' * 60}{Style.RESET_ALL}\n")

    @staticmethod
    def print_turn(speaker: str, role: str, message: str):
        if "PRO" in role.upper():
            color = Fore.GREEN
        elif "CON" in role.upper():
            color = Fore.RED
        else:
            color = Fore.YELLOW

        print(f"{color}{Style.BRIGHT}--- [{speaker}] ({role}) ---{Style.RESET_ALL}")
        print(f"{message}\n")

    @staticmethod
    def print_consensus(consensus_text: str):
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}{'=' * 60}")
        print(" ⚖️ FINAL CONSENSUS REPORT")
        print(f"{'=' * 60}{Style.RESET_ALL}\n")
        print(f"{Fore.WHITE}{consensus_text}\n")

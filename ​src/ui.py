import sys
from colorama import Fore, Back, Style, init

init(autoreset=True)

class Theme:
    # Default: Dark Mode / Matrix Theme
    PRIMARY = Fore.GREEN
    SECONDARY = Fore.CYAN
    ACCENT = Fore.YELLOW
    TEXT = Fore.WHITE
    MUTED = Fore.BLACK + Style.BRIGHT
    ERROR = Fore.RED
    SUCCESS = Fore.GREEN + Style.BRIGHT
    BG_BANNER = Back.RESET

    @classmethod
    def set_light_mode(cls):
        """Mengubah palette warna menjadi ramah untuk terminal latar belakang terang."""
        cls.PRIMARY = Fore.BLUE
        cls.SECONDARY = Fore.MAGENTA
        cls.ACCENT = Fore.RED
        cls.TEXT = Fore.BLACK
        cls.MUTED = Fore.LIGHTBLACK_EX
        cls.ERROR = Fore.RED + Style.BRIGHT
        cls.SUCCESS = Fore.BLUE + Style.BRIGHT
        cls.BG_BANNER = Back.RESET

def show_banner():
    """Mencetak identitas visual GitSint Pro dengan Indonesia OSINT branding."""
    banner_text = f"""
{Theme.PRIMARY}  ________ .__  __   _________.__        __   
{Theme.PRIMARY} /  _____/ |__|/  |_/   _____/|__| _____/  |_ 
{Theme.PRIMARY}/   \\  ___ |  \\   __\\_____  \\ |  |/    \\   __\\
{Theme.ACCENT}\\    \\_\\  \\|  ||  |  /        \\|  |   |  \\  |  
{Theme.ACCENT} \\______  /|__||__| /_______  /|__|___|  /__|  
{Theme.ACCENT}        \\/                  \\/         \\/      
{Theme.MUTED}[+]=========================================================[+]
{Theme.SECONDARY}     GitSint Pro V2 - Advanced Asynchronous GitHub OSINT
{Theme.SECONDARY}     Branding Core : SPY-E | Indonesia OSINT
{Theme.MUTED}[+]=========================================================[+]
"""
    print(banner_text)

def print_log(message, type_log="info"):
    """Helper terpadu untuk mencetak status eksekusi."""
    if type_log == "success":
        print(f"{Theme.SUCCESS}[✓] {message}{Style.RESET_ALL}")
    elif type_log == "error":
        print(f"{Theme.ERROR}[✗] Error: {message}{Style.RESET_ALL}")
    elif type_log == "warning":
        print(f"{Theme.ACCENT}[!] Peringatan: {message}{Style.RESET_ALL}")
    elif type_log == "muted":
        print(f"{Theme.MUTED}[*] {message}{Style.RESET_ALL}")
    else:
        print(f"{Theme.TEXT}[*] {message}{Style.RESET_ALL}")

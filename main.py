from src.scanner import scanner
from colorama import Fore, Style



print( Fore.RED +
    """ 
  _________    ___.   _________                __                 
 /   _____/__ _\_ |__ \_   ___ \____________  |  | __ ___________ 
 \_____  \|  |  \ __ \/    \  \/\_  __ \__  \ |  |/ // __ \_  __ \
 /        \  |  / \_\ \     \____|  | \// __ \|    <\  ___/|  | \/
/_______  /____/|___  /\______  /|__|  (____  /__|_ \\___  >__|   
        \/          \/        \/            \/     \/    \/       
    
    """ + Style.RESET_ALL
)


target = input("Enter your target url: ")

scanner(target)



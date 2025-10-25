import os
import requests

from colorama import Fore, Style



def scanner(target: str) -> str:
    
    load_domains = os.path.abspath("src/data/domains.txt")
    
    url = target.replace("https://www.", " ").strip()
    
    
    with open(load_domains, "r") as f:
          domains = f.read().splitlines()
          
          
          for domain in domains:
              
              req_url = f"https://{domain}.{url}"
              
              try:
                  res = requests.get(req_url)
                  
                  
                  if res.status_code == 200:
                      print(Fore.YELLOW + f"The url {req_url} is live" + Style.RESET_ALL)
                      
                  else:
                      print(Fore.RED + f"The url {req_url} is not live" + Style.RESET_ALL)
            
              except requests.ConnectionError:
                  pass
              
                
             
              
              
              
          
          
            

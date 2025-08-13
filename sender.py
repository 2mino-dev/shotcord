import pyautogui
import requests
import time
import os
from colorama import Fore, init

init(autoreset=True)
print(Fore.BLUE + """   
          mm                                                               mm  
 m@***@m@@@@                    @@     mm@***@m@                         *@@@  
m@@    *@ @@                    @@   m@@*     *@                           @@  
*@@@m     @@@@@@@m    m@@*@@m @@@@@@ @@*       *  m@@*@@m *@@@m@@@    m@**@@@  
  *@@@@@m @@    @@   @@*   *@@  @@   @@          @@*   *@@  @@* **  m@@    @@  
      *@@ @@    @!   @@     @@  @@   @!m         @@     @@  @!      @!@    @!  
@@     @@ @!    @!   @@     !@  @!   *!@m     m* @@     !@  @!      *!@    @!  
!     *@! !!    !!   !@     !!  !!   !!!         !@     !!  !!      !!!    !!  
!!     !! !:    !:   !!!   !!!  !!   :!!:     !* !!!   !!!  !:      *:!    !:  
:!: : :! : :   : : :  : : : :   ::: :  : : : :!   : : : : : :::      : : : ! : 
""")

print((Fore.BLUE + ("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Welcome to Screenshot Sender Tool
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Made by 2mino
My github : 2mino_dev
My discord : 74q_
Note: Please use this tool responsibly.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")))



WEBHOOK_URL = input(Fore.CYAN + "[?] Enter Discord Webhook URL: ")

try:
    test = requests.get(WEBHOOK_URL)
    if test.status_code != 200:
        print(Fore.RED + "[!] Invalid webhook URL!")
        exit()
except requests.exceptions.RequestException:
    print(Fore.RED + "[!] Cannot connect to the webhook!")
    exit()

try:
    INTERVAL = input(Fore.CYAN + "[?] Enter interval in seconds (default 5): ") or "5"
    INTERVAL = int(INTERVAL)
except ValueError:
    print(Fore.RED + "[!] This is not a number!")
    exit()


print(Fore.GREEN + "\n[+] Screenshot Sender Tool started!")
print(Fore.BLUE + f"[+] Your Webhook: {WEBHOOK_URL}")
print(Fore.RED + "[*] Press CTRL + C to stop.\n")

try:
    while True:
        screenshot_path = "discordscreenshost.png"
        pyautogui.screenshot(screenshot_path)

        payload_json = '{"embeds": [{"title": "📸 Screenshot!", "color": 4062976}]}'

        with open(screenshot_path, "rb") as f:
            files = {"file": f}
            response = requests.post(WEBHOOK_URL, data={"payload_json": payload_json}, files=files)
            

        os.remove(screenshot_path)

        if response.status_code == 200:
            print(Fore.GREEN + "[+] Screenshot sent!")
        else:
            print(Fore.RED + f"[!] Failed to send (status {response.status_code})")


        time.sleep(INTERVAL)


except KeyboardInterrupt:
    if os.path.exists("discordscreenshost.png"):
        os.remove("discordscreenshost.png")
print(Fore.CYAN + "\n[!] Stopped by user.")

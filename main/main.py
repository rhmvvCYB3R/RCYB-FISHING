class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def instagram_menu():
    def instagram_global():
        pass
    def instagram_local():
        pass

    print(bcolors.WARNING +"""
INSTAGRAM PHISHING SITE:
         CHOOSE OPRION:

[1] -- LocalHost
[2] -- GlobalHost (NOT WORKING!)        
[0] -- Go BACK!
         
"""+ bcolors.ENDC)
    hacker = input(bcolors.HEADER+"Enter option: ")
    if hacker == "1":
        instagram_local()
    elif hacker == "2":
        instagram_global()
    elif hacker == "0":
        main()
    else:
        print("Please,choose correct option!")

def break_funk():
    print("BYE!")

def main():
    print(bcolors.FAIL+"""

░█▀▀█ ░█▀▀█ ░█──░█ ░█▀▀█ 　 ░█▀▀▀ ▀█▀ ░█▀▀▀█ ░█─░█ ░█▀▀▀ ░█▀▀█ 
░█▄▄▀ ░█─── ░█▄▄▄█ ░█▀▀▄ 　 ░█▀▀▀ ░█─ ─▀▀▀▄▄ ░█▀▀█ ░█▀▀▀ ░█▄▄▀ 
░█─░█ ░█▄▄█ ──░█── ░█▄▄█ 　 ░█─── ▄█▄ ░█▄▄▄█ ░█─░█ ░█▄▄▄ ░█─░█
    """)
    print( """                       
                                                                    ░░░░░░░░░░░▄▄▀▀▀▀▀▀▀▀▄▄
                                                                    ░░░░░░░░▄▀▀░░░░░░░░░░░░▀▄▄
                                                                    ░░░░░░▄▀░░░░░░░░░░░░░░░░░░▀▄
                                                                    ░░░░░▌░░░░░░░░░░░░░▀▄░░░░░░░▀▀▄
                                                                    ░░░░▌░░░░░░░░░░░░░░░░▀▌░░░░░░░░▌
    [1] -- Instagram            [9] -- Netflix(Not Work!)           ░░░▐░░░░░░░░░░░░▒░░░░░▌░░░░░░░░▐
    [2] -- Facebook(Not Work!)  [10] -- BackDoor(REVERSE SHELL)     ░░░▌▐░░░░▐░░░░▐▒▒░░░░░▌░░░░░░░░░▌
    [3] -- Vk (Not Work!)                                           ░░▐░▌░░░░▌░░▐░▌▒▒▒░░░▐░░░░░▒░▌▐░▐
    [4] -- Gmail(Not Work!)                                         ░░▐░▌▒░░░▌▄▄▀▀▌▌▒▒░▒░▐▀▌▀▌▄▒░▐▒▌░▌
    [5] -- Steam(Not Work!)                                         ░░░▌▌░▒░░▐▀▄▌▌▐▐▒▒▒▒▐▐▐▒▐▒▌▌░▐▒▌▄▐
    [6] -- Spotify(Not Work!)                                       ░▄▀▄▐▒▒▒░▌▌▄▀▄▐░▌▌▒▐░▌▄▀▄░▐▒░▐▒▌░▀▄
    [7] -- Roblox(Not Work!)                                        ▀▄▀▒▒▌▒▒▄▀░▌█▐░░▐▐▀░░░▌█▐░▀▄▐▒▌▌░░░▀
    [8] -- Mail.ru(Not Work!)                                       ░▀▀▄▄▐▒▀▄▀░▀▄▀░░░░░░░░▀▄▀▄▀▒▌░▐
                                                                    ░░░░▀▐▀▄▒▀▄░░░░░░░░▐░░░░░░▀▌▐
                      [0] -- EXIT!                                  ░░░░░░▌▒▌▐▒▀░░░░░░░░░░░░░░▐▒▐
                                                                    ░░░░░░▐░▐▒▌░░░░▄▄▀▀▀▀▄░░░░▌▒▐
                                                                    ░░░░░░░▌▐▒▐▄░░░▐▒▒▒▒▒▌░░▄▀▒░▐
                                                                    ░░░░░░▐░░▌▐▐▀▄░░▀▄▄▄▀░▄▀▐▒░░▐
                                                                    ░░░░░░▌▌░▌▐░▌▒▀▄▄░░░░▄▌▐░▌▒░▐
    created by rhmvvCYB3R                                           ░░░░░▐▒▐░▐▐░▌▒▒▒▒▀▀▄▀▌▐░░▌▒░▌
                                            
        """)
    while True:
        hacker = input("Enter option: ")
        if hacker == "1":
            instagram_menu()
            break
        elif hacker == "0":
            break_funk()
            break
        else:
            print("""            
   
█▀█ █░░ █▀▀ ▄▀█ █▀ █▀▀   █▀▀ █░█ █▀█ █▀█ █▀ █▀▀   █▀▀ █▀█ █▀█ █▀█ █▀▀ █▀▀ ▀█▀   █▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █ █ █
█▀▀ █▄▄ ██▄ █▀█ ▄█ ██▄   █▄▄ █▀█ █▄█ █▄█ ▄█ ██▄   █▄▄ █▄█ █▀▄ █▀▄ ██▄ █▄▄ ░█░   █▄█ █▀▀ ░█░ █ █▄█ █░▀█ ▄ ▄ ▄                         
        """)


    



main()

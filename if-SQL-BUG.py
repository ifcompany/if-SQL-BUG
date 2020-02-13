import requests
from os import system
system('clear')
logp = '''

  \033[0;31mManual SQL Injection
        \033[0;33m\\\  \033[0;34m_____
         \033[0;33m\\\ \033[0;34m|___|
            |___|
            |___|
         \033[0;31mError Based\033[0m
    \033[0;95m { \033[0;92mif \033[0;91mS Q L\033[0;92m  B U G      \033[0;33m    V \033[0;95m}
    \033[0;95m { \033[4;34mwww\033[4;33m.\033[4;34mifcompany\033[4;33m.\033[4;34mir\033[0;33m         1 \033[0;95m}
    \033[0;95m { \033[4;34mgithub\033[4;33m.\033[4;34mcom\033[4;33m/\033[4;34mifcompany\033[0;33m     0 \033[0;95m}
    \033[0;95m { \033[4;34mT\033[4;33m.\033[4;34mme\033[4;33m/\033[4;34mThe\033[4;32mlink\033[4;33mif\033[0;33m           0 \033[0;95m}
    \033[0;95m [ \033[4;33mProgrammer\033[0;36m : \033[0;101m007\033[0;33m \033[0;101mDontalion\033[0m\033[0;95m ]\033[0m

    \033[0;32m Dork Bug \033[0;91mSQL \033[0;94m= \033[0;96m{\033[0;32m inurl:news.php?id= \033[0;96m}\033[0m
'''
print(logp)
try:
    def checking_sqli(url):
        r=requests.get(url+"'").text
        errors = ['mysql','syntax','error']
        for error in errors:
            if error in r.lower():
                print("\033[0;36m[\033[0;32m#\033[0;36m] \033[0;32mThe Site \033[0;35m"+url+"\033[0;32m has an \033[0;31mSQL Bug\033[0;34m!\033[0m...")
                break
            else:
                print("\033[0;36m[\033[0;32m#\033[0;36m] \033[0;32mWe Could \033[0;91mnot\033[0;32m find \033[0;31mBug SQL \033[0;33m:\033[0;34m(\033[0m")
    def checking_http(url):
        if 'http' in url:
            checking_sqli(url)
        else:
            checking_sqli("http://"+url)
    while(True):
        if __name__ == '__main__':
            checking_http(input("\033[0;36m[\033[0;32m$\033[0;36m] \033[0;32mEnter The URL \033[0;34m\>\033[0m "))
except Exception:
    print('\033[0;91mErorr,Please Check URL\033[0m')
#Iran-Cyber
#MOHQ-TM
#Colors
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
############
try:
    import requests as r , os 
    from bs4 import BeautifulSoup as bs
    from UserAgent import UserAgent as ua
except Exception as e:
    print(f"{C}{e}\n")
#///////)/////
#Function Logo
def Logo():
    os.system("clear")
    print(f'{G}')
	
    print('███╗   ███╗ ██████╗ ██╗  ██╗ ██████╗     ████████╗███╗   ███╗')
    print('████╗ ████║██╔═══██╗██║  ██║██╔═══██╗    ╚══██╔══╝████╗ ████║')
    print('██╔████╔██║██║   ██║███████║██║   ██║       ██║   ██╔████╔██║')
    print('██║╚██╔╝██║██║   ██║██╔══██║██║▄▄ ██║       ██║   ██║╚██╔╝██║')
    print('██║ ╚═╝ ██║╚██████╔╝██║  ██║╚██████╔╝       ██║   ██║ ╚═╝ ██║')
    print('╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚══▀▀═╝        ╚═╝   ╚═╝     ╚═╝\n')
    print(f"""            {C}Xss Fuzzing{R}:)\n""")

#Function Fuzz
def Fuzz():
    Logo()
    url=str(input(f"{C}Url {R}=> {G}"))
    payload=open(input(f"{C}Payload{R}_{C}List {R}=> {G}"),"r")
    source=str(input(f"{C}Tag {R}=> {G}"))
    ad=int(input(f"{C}Number {R}=> {C}"))
    for i in payload:
        i=i.strip()
        head={'user-agent':f'{ua()}'}
        req=r.post(f"{url}{i}",headers=head)
        soup=bs(req.content,"html.parser")
        soup=soup.find_all(f"{source}")[ad]
        if str(i) in str(soup):
            print(f"\n{C}Payload {R}=> {G}{i}\n{W}")
        else:
            print(f"\n{C}Not Found {R}=> {G}{i}\n{W}")


Fuzz()

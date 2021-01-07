
#Iran
#Colors
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
###########
try:
    from fake_useragent import UserAgent as ua
except Exception as e:
    print(f"{C}{e}\n")

#))/))))
#Function UserAgent
def UserAgent():
    usr=ua()
    return usr.random
UserAgent()

from bs4 import BeautifulSoup
        # country=data['cc']
           data=r.json()
           country=data['cc']
           quality=int(r.elapsed.total_seconds())
           print("COUNTRY "+str(country))
           print("ALIVE "+str(proxy))
from bs4 import BeautifulSoupimport grequests, json, requestsimport MySQLdbfrom multiprocessing.dummy import Pool as ThreadPoolpool = ThreadPool(100)scrapers = []rs = (grequests.get(u, timeout=8) for u in scrapers)rs = grequests.map(rs)database=""host=""def connectiondb(database,host):   cnx = MySQLdb.connect(host,"root","",database)   cnx.set_character_set('utf8')   return cnx		 def xproxies(cnx):      try:         curs = cnx.cursor()         curs.execute("SELECT proxy_port FROM `xproxies` where 1")         xproxy = curs.fetchall()          return xproxy      except MySQLdb.Error as err:           print("Something went wrong: (Accounts) {}".format(err))  cnx=connectiondb(database,host)		 # proxies = []proxies=xproxies(cnx)li = [x[0] for x in proxies]print(li[1])def check(proxy):    prox = {'http': proxy, 'https': proxy}    session = requests.Session()    try:        r = requests.get('https://api.myip.com', proxies=prox, timeout=5)        # data=r.json()
        # country=data['cc']        # print(country['cc'])        # print("ALIVE "+proxy)        if(int(r.elapsed.total_seconds())<=5):
           data=r.json()
           country=data['cc']
           quality=int(r.elapsed.total_seconds())
           print("COUNTRY "+str(country))
           print("ALIVE "+str(proxy))           session.get('http://62.171.130.57/daily_proxy/cleaner.php?proxy_port='+str(proxy)+'&country='+str(country)+'&quality='+str(quality))           print(r.elapsed.total_seconds())        else:		        print("WEAK "+str(proxy))    except Exception as e:        print("DEAD "+str(proxy))print('Checking {} Proxies'.format(len(proxies)))pool.map(check, li)
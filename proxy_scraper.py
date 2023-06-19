from bs4 import BeautifulSoup
import grequests, json, requests
from multiprocessing.dummy import Pool as ThreadPool
from termcolor import colored
pool = ThreadPool(100)


scrapers = [
    'http://multiproxy.org/txt_all/proxy.txt',
    'https://www.sslproxies.org/',
    'http://free-proxy.cz/en/',
    'https://www.us-proxy.org/',
    'https://free-proxy-list.net/',
    'https://www.proxy-list.download/api/v0/get?l=en&t=https',
    'https://www.duplichecker.com/free-proxy-list.php',
    'http://www.httptunnel.ge/ProxyListForFree.aspx',
    'https://checkerproxy.net/',
	'http://www.samair.ru/proxy/time-09.htm',
'http://proxyfirenet.blogspot.com/',
'http://www.samair.ru/proxy/ip-address-15.htm',
'http://www.cybersyndrome.net/plz.html',
'http://aliveproxies.com/',
'http://www.cybersyndrome.net/plr5.html',
'http://biskutliat.blogspot.com/',
'http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-15-0111-am-gmt8.html',
'http://proxylists.net/http_highanon.txt',
'http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-13-812-gmt7.html',
'http://www.cybersyndrome.net/pla5.html',
'http://vipprox.blogspot.com/2013_06_01_archive.html',
'http://vipprox.blogspot.com/2013/05/us-proxy-servers-74_24.html',
'http://vipprox.blogspot.com/p/blog-page_7.html',
'http://vipprox.blogspot.com/2013/05/us-proxy-servers-199_20.html',
'http://freeforall.ucoz.com/forum/16-13723-1',
'http://vipprox.blogspot.com/2013_02_01_archive.html',
'http://alexa.lr2b.com/proxylist.txt',
'http://7proxy.blogspot.com/',
'http://vipprox.blogspot.com/2013_03_01_archive.html',
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196260',
'http://www.samair.ru/proxy/ip-address-09.htm',
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196258',
'http://sock5us.blogspot.com/2013/06/01-07-13-free-proxy-server-list.html#comment-form',
'http://www.samair.ru/proxy/proxy-13.htm',
'http://www.proxyfire.net/forum/forumdisplay.php?s=07a031a5ab87d88a9e048f534a0498a8&f=17',
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196251',
'http://free-ssh.blogspot.com/feeds/posts/default',
'http://www.samair.ru/proxy/proxy-18.htm',
'http://www.samair.ru/proxy/proxy-15.htm',
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196259',
'http://www.sockfree.net/2013/04/142013-sock-free-update-1128.html',
'http://www.samair.ru/proxy/proxy-20.htm',
'http://www.sockfree.net/2013/04/142013-sock-free-update-1139.html',
'http://sockproxy.blogspot.com/',
'http://free-ssh.blogspot.com/',
'http://sock5us.blogspot.com/',
'http://www.samair.ru/proxy/proxy-12.htm',
'http://sockproxy.blogspot.com/2013/04/11-04-13-socks-45.html',
'http://www.samair.ru/proxy/time-09.htm',
'http://proxyfirenet.blogspot.com/'

]

rs = (grequests.get(u, timeout=8) for u in scrapers)
rs = grequests.map(rs)
proxies = []

# print(session)
def check(proxy):
    prox = {'http': proxy, 'https': proxy}
    session = requests.Session()
    try:
        requests.get('http://httpbin.org/get', proxies=prox, timeout=5)
        print(colored(f'ALIVE | {proxy}', 'green'))
        with open('good.txt', 'a') as proxy_folder:
            proxy_folder.write(proxy + '\n')
        session.get('http://62.171.130.57/daily_proxy/script.php/?proxy_port='+str(proxy))
    except Exception as e:
        print(colored(f'DEAD | {proxy}', 'red'))
for i in list(range(len(scrapers))):
    if rs[i]:
        html = rs[i].text
        soup = BeautifulSoup(html, 'html.parser')
        scraper = scrapers[i]
        # print(scraper)

        if scraper == 'http://multiproxy.org/txt_all/proxy.txt':
            proxies.extend(html.split('\n'))

        elif scraper == 'https://www.sslproxies.org/':
            tr = soup.find('table', {'id': 'proxylisttable'})
            prox = list(tr.find_all('tr'))
            prox.pop(0)
            for proxy in prox:
                try:
                    proxy = proxy.find_all('td')
                    ip = str(proxy[0]).replace('</td>', '').replace('<td>', '')
                    port = str(proxy[1]).replace('</td>', '').replace('<td>', '')
                    proxies.append(f'{ip}:{port}')
                except Exception as e:
                    pass

        elif scraper == 'https://free-proxy-list.net/':
            tr = soup.find('table', {'id': 'proxylisttable'})
            prox = list(tr.find_all('tr'))
            prox.pop(0)
            for proxy in prox:
                try:
                    proxy = proxy.find_all('td')
                    ip = str(proxy[0]).replace('</td>', '').replace('<td>', '')
                    port = str(proxy[1]).replace('</td>', '').replace('<td>', '')
                    proxies.append(f'{ip}:{port}')
                except Exception as e:
                    pass

        elif scraper == 'https://www.us-proxy.org/':
            tr = soup.find('table', {'id': 'proxylisttable'})
            prox = list(tr.find_all('tr'))
            prox.pop(0)
            for proxy in prox:
                try:
                    proxy = proxy.find_all('td')
                    ip = str(proxy[0]).replace('</td>', '').replace('<td>', '')
                    port = str(proxy[1]).replace('</td>', '').replace('<td>', '')
                    proxies.append(f'{ip}:{port}')
                except Exception as e:
                    pass
        elif scraper == 'https://www.proxy-list.download/api/v0/get?l=en&t=https':
            asd = json.loads(html)[0]
            for proxy in asd['LISTA']:
                proxies.append(f'{proxy.get("IP")}:{proxy.get("PORT")}')

        elif scraper == 'https://www.duplichecker.com/free-proxy-list.php':
            arr = soup.find_all('div', {'class': 'col-md-12 col-sm-12 col-xs-12 result_row mn wb_ba'})
            for thing in arr:
                children = list(thing.children)
                ip = children[1].text
                port = children[3].text
                proxies.append(f'{ip}:{port}')

        elif scraper == 'http://www.httptunnel.ge/ProxyListForFree.aspx':
            table = soup.find('table', {'id': 'ctl00_ContentPlaceHolder1_GridViewNEW'})
            for thing in table.find_all('tr'):
                try:
                    proxies.append(thing.td.a.text)
                except AttributeError:
                    pass
        elif scraper == 'https://checkerproxy.net/':
            div = soup.find('div', {'class': 'block archive f_right'})
            ali = div.ul.find_all('li')
            for li in ali:
                link = 'https://checkerproxy.net/api/archive/' + li.a['href'].split('/')[2]
                response = requests.get(link)
                asd = json.loads(response.text)
                print(f'Got {len(asd)} proxies from https://checkerproxy.net/')
                for proxy in asd:
                    if proxy['type'] == 1 or proxy['type'] == 2:
                        proxies.append(proxy['addr'])


print('Checking {} Proxies'.format(len(proxies)))

pool.map(check, proxies)

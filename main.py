import requests

link = "https://ams.rusoil.net/pcs/formout/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Cookie': 'tekform=w_HOSTEL',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Sec-GPC': '1'
           }
params = {'hostel': 'y',
          'f': 'get_Akt',
          'cid': '172380'}

response = requests.get(url=link,params=params,headers=headers).text

print(response)
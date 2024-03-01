"""Make the HTTP/1.1 Request and manage the client erros 4XX"""

import requests

class Onetimescraper:
    """Structure a request by creatring the URL and the header"""
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "X-Amzn-Trace-Id": "Root=1-657d9948-0b1287a9595279442da02660"
    }

    def fetch(self, url, headers=headers):
        print("HTTP request to URL: %s" %url, end='')
        res = requests.get(url, headers=headers)
        print(' | Status code: %s' %res.status_code)
        return res
    
    def to_html(self, html):
        with open('res.html', 'w') as html_file:
            html_file.write(html)
    
    def from_html(self):
        html = ''
        with open('res.html', 'r') as html_file:
            for line in html_file.read():
                html += line

        return html

    def to_csv(self):
        with open('results.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.results[0].keys())
            writer.writeheader()
            
            for row in self.results:
                writer.writerow(row)
        
        print("Result csv has been written successfully")
    
    def set_proxys(): 
        """Set different proxys to avoid client side errors 4XX"""
        pass
    
    def header_randomize(self):
        """Randomize the header to avoid client side erros 4XX"""
        pass

    def treating_http_request(self):
        """Treat http bad responses. If the conexion fails call 
        methods to randomize and call and then call the function again"""
        #self.page.raise_for_status()
        pass

    def url_constructor(self, lg_targed, lg_translation, word):
        """Construct the URL based on the information we need"""
        url = "https://context.reverso.net/translation/"
        url = f"{url}{lg_targed}-{lg_translation}/{word}"
        return url




from bs4 import BeautifulSoup
import ots

class Context_Scrapper(ots.Onetimescraper):
    results = []

    def parse(self, html):
        soup = BeautifulSoup(html, 'lxml')
        
        sentences = [sentence.text.strip() for sentence in soup.find_all("div", {'class': 'src ltr'})]
        translations = [translation.text.strip() for translation in soup.find_all("div", {'class': 'trg ltr'})]
        
        for index in range(0, len(sentences)):
            self.results.append({
                "sentence": sentences[index],
                "translation": translations[index]
            })

    def run(self, target, translation, word):
        url = self.url_constructor(target, translation, word)
        res = self.fetch(url)
        self.parse(res.text)
        
scraper = Context_Scrapper()
scraper.run("english", "portuguese", "fetch")
for result in scraper.results:
    print(result['sentence'])
    print(result['translation'])
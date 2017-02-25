import re
import urlparse

from bs4 import BeautifulSoup
class HtmlParser(object):
    def parse(self, url, html_cont):
        if url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(url,soup)
        new_data = self._get_new_data(url,soup)
        return  new_urls,new_data

    def _get_new_urls(self, pageurl, soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r'/view/\d+\.htm'))
        for url in links:
            new_url = url['href']
            new_full_url = urlparse.urljoin(pageurl,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, url, soup):
        res_data ={}

        res_data['url'] = url
        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        summary_node = soup.find('div',class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
        return res_data


from urllib.request import Request, urlopen
from finder import Finder
from manager import TheHTMLParse
import ssl
from main import *

class Spider:
    
    #Class Variables
    project_name = ''
    base_url = ''
    domaine_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self,project_name,base_url,domaine_name):
        super().__init__()
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domaine_name = domaine_name
        Spider.queue_file = main_dir()+project_name+"/queue.txt"
        Spider.crawled_file = main_dir()+project_name+"/crawled.txt"
        self.boot()
        self.crawl_page('First Spider',Spider.base_url)

    @staticmethod
    def boot():
        init_project(Spider.project_name,Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name,page_url):
        if page_url not in Spider.crawled:
            logthis("Spider. "+thread_name + " starts crawling "+page_url,Spider.project_name)
            logthis("Spider. Queue : "+str(len(Spider.queue)) + " | Crawled : "+str(len(Spider.crawled)),Spider.project_name)
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            if page_url in Spider.queue:
                Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()
    
    @staticmethod
    def gather_link(page_url):
        html_string = ''
        req = Request(page_url, headers={'User-Agent': 'Mozilla/5.0'})
        context = ssl._create_unverified_context()
        response = urlopen(req, context=context)
        charset = str(response.getheader('Content-Type')).split('charset=')[1]
        try : 
            if 'text/html;' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            parser = TheHTMLParse(html_string,Spider.project_name,page_url)
            finder = Finder(Spider.base_url,page_url)
            finder.feed(str(html_string))
        except : 
            logthis("Spider. Sorry sir i can't crawl this page ...",Spider.project_name)
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links : 
            if url in Spider.queue :
                continue
            if url in Spider.crawled : 
                continue
            if Spider.domaine_name not in url:
                continue
            Spider.queue.add(url)
    @staticmethod
    def update_files():
        set_to_file(Spider.queue,Spider.queue_file)
        set_to_file(Spider.crawled,Spider.crawled_file)
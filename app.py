import threading
from queue import Queue
from spider import Spider
from domain import *
from main import *



PROJECTS_DIR = "projects/"
PROJECT_NAME = "och1912"
HOME_PAGE = "https://orientation-chabab.com/master"
#DOMAINE_NAME = get_domaine_name(HOME_PAGE)
DOMAINE_NAME = HOME_PAGE
CRAWLED_FILE = PROJECTS_DIR+PROJECT_NAME+"/crawled.txt"
QUEUE_FILE = PROJECTS_DIR+PROJECT_NAME+"/queue.txt"
NUMBER_OF_THREADS = 1
#database_stream = DatabaseManager()
#database_stream.con()
queue = Queue()
Spider(PROJECT_NAME,HOME_PAGE,DOMAINE_NAME)

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True;
        t.start();


#Create programmes :D Do next job
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()


#Fetch link by link
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

#Crawl all links in queue file
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0 :
        logthis("App. "+str(len(queued_links))+" in the queue.",PROJECT_NAME)
        create_jobs()
    else:
        logthis("App. I'm happy to works for you sir Marouane :)",PROJECT_NAME)
create_workers()
crawl()
logthis("---- END ----",PROJECT_NAME)
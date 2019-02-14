try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
from databasemanager import DatabaseManager
from main import *
class TheHTMLParse:

    def __init__(self,html_page,project_name,url_page):

        self.html_page = html_page
        self.project_name = project_name
        self.url_page = url_page
        self.boot()

    def boot(self):
        try :
            parsed = BeautifulSoup(self.html_page,'html.parser')
            title = parsed.title.text
            image = parsed.find('img',width='110')['src']
            datePub = parsed.find('div',style='font-size:13px;').find_all("b")[1].text
            content = self.content(parsed)
            ##todo :: See modakira ....
            if content:
                logthis("Manager. Title : "+title,self.project_name)
                dbm = DatabaseManager()
                dbm.insertLine(title,image,content,datePub)
                logthis("Database. Line inserted",self.project_name)
        except Exception as e:
            print("Manager. Exception : "+str(e))
            logthis("Database. Line not inserted",self.project_name)
            logthis("Manager. "+self.url_page+" is ignored ...",self.project_name)


    def content(self,parsed):
        #parsed = parsed.center.extract()
        content = parsed.find('table',height='1250')
        centers = content.find_all("center")
        for tag in centers :
            tag.extract()
        # Extract all scripts
        scripts = content.find_all("script")
        for script in scripts:
            script.extract()
        # extract last divs
        divs = content.find_all("div")
        divLen = len(divs)
        divs[divLen-1].extract()
        divs[divLen-2].extract()
        divs[divLen-3].extract()
        #extract hr
        hrs = content.find_all("hr")
        for hr in hrs:
            hr.extract()
        #extract frames
        content = content.prettify()
        return content

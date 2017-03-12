import re
import urllib
import copy



class PythonCrawler:

        def __init__(self):
                #self.url = url
                self.visitedLinks = []
                self.textFile = file('depth_1.txt', 'wt')
                self.LinkList = []
                self.CopyList = []
                #self.myurl = "https://campus.verwaltung.uni-tuebingen.de/lsfpublic/rds?state=wtree&search=1&category=veranstaltung.browse&menuid=lectureindex&breadcrumb=lectureindex&breadCrumbSource=lectures"
                self.baseURL = "https://campus.verwaltung.uni-tuebingen.de"
                self.LinkList.append(self.baseURL)
                self.start_work()

        def crawl(self, url):
                found = 0
                for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(url).read(), re.I):
                        if i not in self.CopyList and i.startswith(self.baseURL):
                                print(i)
                                self.CopyList.append(i)
                                found += 1
                return found

        def start_work(self):
                print("Starting new Crawling Commander.")
                found = 0
                for url in self.LinkList:
                        found = self.crawl(url)
                self.LinkList = copy.copy(self.CopyList)
                if found > 0:
                        self.start_work()
                print(self.LinkList[:])
                print("Finished-Crawling Reporting for Duty.")


PythonCrawler().__init__()
""""
for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I):
        print i
        if i.startswith("http"):
                for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
                        print ee
                        textFile.write(ee+'\n')
textfRile.close()"""
import re, urllib

textfile = file('depth_1.txt','wt')

myurl = "https://campus.verwaltung.uni-tuebingen.de/lsfpublic/rds?state=wtree&search=1&category=veranstaltung.browse&menuid=lectureindex&breadcrumb=lectureindex&breadCrumbSource=lectures"

for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I):
        print i
        if i.startswith("http"):
                for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
                        print ee
                        textfile.write(ee+'\n')
textfRile.close()
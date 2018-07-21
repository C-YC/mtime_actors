# mtime_actors
Using actor links derived from mongodb database to capture actors' works and achievements
## Main codes
* `auto_star.py` <br> determine whether there is an error and whether to restart it<br>
* `get_actor_works.py` <br> main code <br>
* `mongo_export.py` <br> export the required data in the database <br>
* `star.sh` <br> script to start the program <br>
## Operating environment
Based on **python2.7** and **selenium**, first need to install： <br>
1.`selenium`<br>
2.`phantomjs`<br>
3.`pandas`<br>
4.`mongodb`<br>
## Operation instructions
|star.sh|auto_star.py|get_actor_works.py|
|:---|:---|:---|
|the first file to be executed<br>to call **auto_star.py**|then it is the turn of auto_star.py<br> to call **get_actor_works.py**,<br>also used to restart the program|the main code to crawl content we need|

Open the terminal in the directory where the files are stored. <br>
Input: <br> 
`sh star.sh`
## Bullet points
Key skills that I have learned <br>
* Breakpoint renewed <br>
define three sets, one to store all links ，one to store crawled links and the third set is the complement of the first two sets. <br>
* csv
* mongodb
* list.insert()
* os.system()
* shell
## Sample
* Take [Eric Tsang(曾志伟)](http://people.mtime.com/893302/) as an example. <br>
* First get his page link from the database, then enter his work chronology according to the link. <br>

<img src="https://github.com/C-YC/mtime_actors/blob/master/mtime_pictures/39378210.jpg" width="600" height="500" alt="图片加载失败时，显示这段字"/><br>

* Use **phantomjs** to crawl contents and **dapas** to store csv files.<br>

<img src="https://github.com/C-YC/mtime_actors/blob/master/mtime_pictures/1286573807.jpg" width="600" height="500" alt="图片加载失败时，显示这段字"/>

* labels <br>

|actor|director|position|score_number|work_name|year|
|:---|:---|:---|:---|:---|:---|
|lead actor/actress|director|the role of the actor in the work|the number of people who give a mark|the name of the work|the year of release|

* Then crawl the actor’s achievements <br>

<img src="https://github.com/C-YC/mtime_actors/blob/master/mtime_pictures/1818865497.jpg" width="600" height="500" alt="图片加载失败时，显示这段字"/>

<img src="https://github.com/C-YC/mtime_actors/blob/master/mtime_pictures/2095185754.jpg" width="600" height="500" alt="图片加载失败时，显示这段字"/>

* Save as json files <br>

![](https://github.com/C-YC/mtime_actors/blob/4e14a715d1c4de5c5127a8869a9712dc437bb93c/mtime_pictures/1618562702.jpg)

* labels <br>

|win|nomination|total|
|:---|:---|:---|
|win awards|win nominations|awards and nominations|

* If there are labels that don't exist, mark them as "None".

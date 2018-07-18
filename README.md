# mtime_actors
Using actor links derived from mongodb database to capture actors' works and achievements
## main codes
* `auto_star.py` <br> determine whether there is an error and whether to restart it<br>
* `get_actor_works.py` <br> main code <br>
* `mongo_export.py` <br> export the required data in the database <br>
* `star.sh` <br> script to start the program <br>
## operation description
in the file directory, open the terminal <br>
input: <br> 
`sudo chmod 777 star.sh`<br>
`sh star.sh`
## bullet points
key points that I have learned <br>
* 断点重续 <br>
define a list to hold the crawled links <br>
every time before calling the functions, first determine if the link is in the list
* csv
* list.insert()
* os.system()
* shell脚本

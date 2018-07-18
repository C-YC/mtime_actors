# coding:utf-8
"""
author:C-YC
target:时光网爬取演员作品年表和荣誉成就
finish date：2018,07,18
"""
import sys
import time
import os
import json
import urllib
import auto_star
import pandas as pd
from selenium import webdriver
reload(sys)
sys.setdefaultencoding("utf-8")
driver = webdriver.PhantomJS(executable_path='./phantomjs')


def get_filmographies(url):
    # 该函数的作用：爬取明星的作品年表
    filmography_url = url + 'filmographies/'
    driver.get(filmography_url)
    time.sleep(2)
    try:
        # 判断页数
        pages = driver.find_elements_by_xpath("//div[@id='pageDiv']//a")
        print len(pages)
        time.sleep(1)
        if len(pages) == 0:
            table = driver.find_elements_by_xpath("//div[@class='per_rele_list']//dd")
            for i in range(len(table)):
                print table[i].text
                print "   "
                with open("../data/demo.txt", "a+")as m:
                    m.write(table[i].text + '``')
        if len(pages) > 1:
            for r in range(1, len(pages)-1):
                filmography_urls = filmography_url + '#pageIndex=' + str(r)
                print filmography_urls
                time.sleep(0.5)
                driver.get(filmography_urls)
                driver.refresh()
                time.sleep(1)
                table = driver.find_elements_by_xpath("//div[@class='per_rele_list']//dd")
                for i in range(len(table)):
                    print table[i].text
                    print "   "
                    with open("../data/demo.txt", "a+")as m:
                        m.write(table[i].text + '``')
    except:
        # 当网页还没加载出来或者其他原因出现差错时，重新调用主函数
        print "The element can not be found！"
        main()


def works_processing(actor_name):
    # 该函数的目的：处理爬取后明星作品数据，便于提取数据
    works_info = []
    with open("../actor_works/" + actor_name + ".csv", "w+")as p:
        p.write("")
    # 以``分割数据
    with open("../data/demo.txt", "r")as kk:
        contents = kk.read().replace("导演：\n", "导演：").replace("主演：\n", "主演：").split("``")
    for content in contents:
        # 判断是否有不需要的数据，有，则将无用片段切去
        if "显示全部" in content:
            cont = content.split("显示全部")
            contt = cont[0].split("第")[0]
            content = contt + "`" + cont[1]
        if len(content) != 0:
            all_info = content.replace("`\n", "").split("\n")
            year = all_info[0]
            print year
            time.sleep(0.5)
            if (len(all_info) - 1) / 5 > 0:
                for i in range(1, len(all_info) - 1, 5):
                    try:
                        if all_info[i + 4] and "评分" not in all_info[i + 4]:
                            if "导演" in all_info[i + 2]:
                                all_info.insert(i + 4, "None")
                            else:
                                if "评分" in all_info[i + 3]:
                                    all_info.insert(i + 2, "None")
                                else:
                                    all_info.insert(i + 2, "None")
                                    all_info.insert(i + 4, "None")
                    except:
                        if "导演" in all_info[i + 2]:
                            all_info.insert(i + 4, "None")
                        else:
                            try:
                                if "评分" in all_info[i + 3]:
                                    all_info.insert(i + 2, "None")
                            except:
                                all_info.insert(i + 2, "None")
                                all_info.insert(i + 4, "None")
                    work_name = all_info[i].replace("\n", "")
                    position = all_info[i + 1].replace("\n", "")
                    director = all_info[i + 2].replace("\n", "").replace("导演：", "")
                    actor = all_info[i + 3].replace("\n", "").replace("主演：", "")
                    score_number = all_info[i + 4]
                    print work_name, "/", position, "/", director, "/", actor, "/", score_number
                    # 将数据存成一行形式的字典
                    row = {}
                    row["year"] = year
                    row["work_name"] = work_name
                    row["position"] = position
                    row["director"] = director
                    row["actor"] = actor
                    row["score_number"] = score_number
                    works_info.append(row)
            else:
                if (len(all_info) - 1) == 4:
                    if "导演" in all_info[3]:
                        all_info.insert(5, "None")
                    if "评分" in all_info[4]:
                        all_info.insert(3, "None")
                else:
                    all_info.insert(3, "None")
                    all_info.insert(5, "None")
                work_name = all_info[1].replace("\n", "")
                position = all_info[2].replace("\n", "")
                director = all_info[3].replace("\n", "").replace("导演：", "")
                actor = all_info[4].replace("\n", "").replace("主演：", "")
                score_number = all_info[5]
                print work_name, "/", position, "/", director, "/", actor, "/", score_number
                row = {}
                row["year"] = year
                row["work_name"] = work_name
                row["position"] = position
                row["director"] = director
                row["actor"] = actor
                row["score_number"] = score_number
                works_info.append(row)
    works = pd.DataFrame(works_info)
    works.to_csv("../actor_works/" + actor_name + ".csv", index=False, sep=',')


def get_awards(url):
    # 该函数的作用：爬取明星的荣誉成就
    awards_url = url + 'awards.html'
    driver.get(awards_url)
    time.sleep(2)
    try:
        awards = driver.find_element_by_xpath("//div[@class='per_awardsbox']/h3[@class='per_awardstit']").text
        print awards
        awards_info = driver.find_element_by_xpath("//div[@class='per_awardsbox']/div[@id='awardInfo']/dl").text
        print awards_info
        with open("../data/demo_awards.txt", "a+")as p:
            p.write(awards + '\n' + awards_info)
    except:
        print "Web pages don't exist！"
        with open("../data/demo_awards.txt", "a+")as p:
            p.write("None"+"\n")


def awards_processing(actor_name):
    # 该函数的目的：处理爬取后的明星荣誉成就数据，便于提取数据
    with open("../data/demo_awards.txt", "r")as w:
        content0 = w.read().replace("·\n", "").split("获奖\n")
    if "None" in content0[0]:
        awards = {
            "total": "None",
            "win": "None",
            "nomination": "None"
        }
    else:
        if len(content0) > 1:
            achievement = content0[0].replace("\n", "")
            print achievement
            content1 = content0[1].split("提名\n")
            if len(content1) > 1:
                award = content1[0]
                nomination = content1[1]
                print award
                print nomination
                awards = {
                    "total": achievement,
                    "win": award,
                    "nomination": nomination
                }
            else:
                award = content1[0]
                print award
                awards = {
                    "total": achievement,
                    "win": award,
                    "nomination": "None"
                }
        else:
            content1 = content0[0].split("提名\n")
            achievement = content1[0].replace("\n", "")
            print achievement
            nomination = content1[1]
            print nomination
            awards = {
                "total": achievement,
                "win": "None",
                "nomination": nomination
            }
    with open("../actor_awards/" + actor_name + ".json", "w+")as m:
        json.dump(awards, m, ensure_ascii=False)


def main():
    # 定义一个列表存储已爬好的url
    crawled_url = []
    with open("../data/finish_url.txt", "r")as t:
        lines = t.readlines()
        for line in lines:
            crawled_url.append(line.replace("\n", ""))
    with open("../data/export.txt", "r")as fl:
        urls = fl.readlines()
        for url in urls:
            actor_url = url.replace("\n", "")
            time.sleep(0.5)
            # 如果url在其中，则跳过
            if actor_url in crawled_url:
                pass
            else:
                status = urllib.urlopen(actor_url).code
                print status
                time.sleep(1)
               # 演员链接可能出错，导致页面不存在，所以先判断是否是403页面 
                if status == 403:
                    with open("../data/wrong_url.txt", "a+")as dd:
                        dd.write(actor_url + "\n")
                    time.sleep(1)
                    with open("../data/finish_url.txt", "a+")as d:
                        d.write(actor_url + "\n")
                else:
                    driver.get(actor_url)
                    time.sleep(2)
                    actor_name = driver.find_element_by_xpath("//div[@class='per_header']/h2").text
                    time.sleep(1)
                    print "=================", actor_name, "================="
                    get_filmographies(actor_url)
                    print "******* 作品年表 爬取成功 *******\n"
                    time.sleep(1)
                    get_awards(actor_url)
                    print "******* 荣誉成就 爬取成功 *******\n"
                    time.sleep(1)
                    works_processing(actor_name)
                    print "******* 成功处理 作品数据 *******\n"
                    time.sleep(1)
                    awards_processing(actor_name)
                    print "******* 成功处理 荣誉数据 *******\n"
                    with open("../data/demo.txt", "w+")as ms:
                        ms.write("")
                    with open("../data/demo_awards.txt", "w+")as ns:
                        ns.write("")
                    try:
                        with open("../actor_works/" + actor_name + ".csv", "a+")as fls:
                            fls.write("")
                    except:
                        with open("../data/wrong_url.txt", "a+")as ff:
                            ff.write(actor_url + "\n")
                    finally:
                        with open("../data/finish_url.txt", "a+")as db:
                            db.write(actor_url + "\n")


def star():
    try:
        main()
        auto_star.error_flags = True
    except Exception, a:
        print Exception, ":", a
        try:
            while True:
                driver.close()
        except Exception, e:
            print Exception, ":", e
    finally:
        driver.quit()
        sys.exit()


if __name__ == '__main__':
    if not os.path.exists("../actor_awards"):
        os.mkdir("../actor_awards")
    if not os.path.exists("../actor_works"):
        os.mkdir("../actor_works")
    with open("../data/demo.txt", "w+")as f:
        f.write("")
    with open("../data/demo_awards.txt", "w+")as f:
        f.write("")
    star()

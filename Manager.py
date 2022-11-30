import datetime
from pytube import YouTube
import pytube
from pytube import Channel
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import instaloader
import requests
from random import randint
from moviepy.editor import *
import shutil
import pyautogui
from moviepy.editor import VideoFileClip, concatenate_videoclips
import sys




# -------------------------------------------------------------------------------------------------------------------------------------------------------------------


def YTdownloader(canale):

    print("Downloading from YT")

    url = Channel(canale)  # url of channel to get videos

    day = str(datetime.datetime.today())  # getting today date in str
    oggidata = day.split(" ", 1)[0]  # splitting date

    id = []
    links = []

    # Getting videos IDs

    for video in url.videos:  # Getting channel videos IDs
        c = str(video)
        b = c.split("=")[1]
        id.append(b)

    # Inserting links in array

    for i in id:
        links.append("https://www.youtube.com/watch?v=" + i)  # attaching id to yt url

    # Downloadings video published today

    for video in links:

        data = YouTube(video).publish_date
        data1 = str(data)
        datastr = data1.split(" ")[0]

        if datastr == oggidata:  # comapring today date to publish date

            link = video
            yt = pytube.YouTube(link)
            yt.streams.get_highest_resolution().download()  # Download videos

        else:

            print("No more videos from YT")
            break


def YTuploader(Profile, urlYT, description, tags):
    video = []
    i = 0

    directory = os.getcwd()

    for file in os.listdir(directory):  # directory alla cartella del video

        print(file)

        if not os.path.isdir(file) and file.endswith(".mp4"):
            video.append(file)

    try:
        for a in video:
            opt = webdriver.ChromeOptions()
            opt.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            chromedriver_exe_location = os.path.join(directory + '\chromedriver.exe')  # directory driver
            profile_path = os.getcwd() + "\\User Data"  # path minus last folder
            opt.add_argument('--user-data-dir={}'.format(profile_path))
            opt.add_argument('--profile-directory={}'.format(Profile))  # last folder name
            driver = webdriver.Chrome(chromedriver_exe_location, options=opt, service_args='')

            time.sleep(4)

            driver.get(urlYT)  # link alla pagina del caricamento

            time.sleep(4)

            driver.find_element(By.NAME, 'Filedata').send_keys(
                str(directory) + '\\' + str(a))  # directory alla cartella del video

            time.sleep(4)

            # codice per modificare il nome del video

            """
            driver.find_element(By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div").clear()
            time.sleep(5)
            driver.find_element(By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div").send_keys("Goofy Ahh meme (DO NOT WATCH)")
            time.sleep(2)
            """

            descrizione = driver.find_element(By.XPATH,
                                              "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")
            descrizione.send_keys(description)  # descrizione

            time.sleep(3)

            driver.find_element(By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK").click()  # video not for kids

            time.sleep(3)

            driver.find_element(By.ID, "toggle-button").click()

            time.sleep(3)

            driver.find_element(By.XPATH,
                                "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[5]/ytcp-form-input-container/div[1]/div/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input").send_keys(
                tags)  # tags

            time.sleep(3)

            # codice per scegliere il genere di video

            """

            driver.find_element(By.XPATH,"/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[7]/div[3]/ytcp-form-select/ytcp-select/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger").click()

            time.sleep(3)

            driver.find_element(By.XPATH, "/html/body/ytcp-text-menu/tp-yt-paper-dialog/tp-yt-paper-listbox/tp-yt-paper-item[14]").click()

            time.sleep(3)

            """

            driver.find_element(By.ID, "allow-all-radio-button").click()

            time.sleep(3)

            driver.find_element(By.ID, "next-button").click()

            time.sleep(3)

            driver.find_element(By.ID, "next-button").click()

            time.sleep(3)

            driver.find_element(By.ID, "next-button").click()

            time.sleep(3)

            driver.find_element(By.NAME, "PUBLIC").click()

            time.sleep(3)

            driver.find_element(By.ID, "done-button").click()

            time.sleep(5)

            driver.close()
    except:
        print("not uploaded")


    time.sleep(3)


def IGdownload(accounts):
    L = instaloader.Instaloader()

    print(accounts)

    PROFILE = accounts

    posts = instaloader.Profile.from_username(L.context, PROFILE).get_posts()  # getting account posts

    for post in posts:  # getting posts publish date

        day = str(datetime.datetime.today())
        data = str(post.date)
        postdata = data.split(" ")[0]
        oggidata = day.split(" ", 1)[0]

        if postdata == oggidata:  # downloading todays posts

            L.download_post(post, PROFILE)

            dir_path = os.getcwd()
            folder = ""

            for a in os.listdir(dir_path):  # saving post in same directory as py file and deleting junk file

                if os.path.isdir(a):
                    folder = str(dir_path + "\\" + a)

                    for k in os.listdir(folder):

                        if k.endswith(".mp4"):
                            old = str(folder) + "\\" + str(k)
                            name = "Offensive Shitpost status V" + str(randint(20, 700)) + ".mp4"
                            new = str(folder) + "\\" + name

                            os.rename(old, new)

                            path = folder + "\\" + name
                            destination = dir_path + "\\" + name

                            shutil.copyfile(path, destination)

                            os.remove(new)
                            shutil.rmtree(folder)

        else:
            break


def foldercl():
    path = os.getcwd()

    for file in os.listdir(path):

        path2 = path + "\\" + file

        if os.path.isdir(path2):

            if file != "Manager.py" and file != "chromedriver.exe" and file != "User Data" and file != "immagini" and file != "ffmpeg.bat" and file != ".idea":
                shutil.rmtree(path2)


def IGuploader(Profile, descrizione):
    opt = webdriver.ChromeOptions()
    opt.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chromedriver_exe_location = os.path.join(os.getcwd(), os.getcwd() + '\chromedriver.exe')
    profile_path = os.getcwd() + "\\User Data"  # path minus last folder
    opt.add_argument('--user-data-dir={}'.format(profile_path))
    opt.add_argument('--profile-directory={}'.format(Profile))  # last folder name
    driver = webdriver.Chrome(chromedriver_exe_location, options=opt, service_args='')

    path = os.getcwd()

    for file in os.listdir(path):

        try:
            if file.endswith(".mp4"):

                driver.get("https://www.instagram.com")
                time.sleep(6)

                x, y = pyautogui.locateCenterOnScreen(path + '\\immagini\\instagram.png')
                pyautogui.click(x, y)

                time.sleep(2)

                x, y = pyautogui.locateCenterOnScreen(path + '\\immagini\\crea.png')
                pyautogui.click(x, y)

                time.sleep(2)
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button').click()
                time.sleep(2)
                pyautogui.write(path + "\\" + file)
                pyautogui.press('enter')
                time.sleep(2)
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button").click()
                time.sleep(2)
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/button[1]").click()
                time.sleep(2)
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button").click()
                time.sleep(2)
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button").click()
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea").click()
                time.sleep(2)
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea").send_keys(descrizione)
                time.sleep(2)
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button").click()

                time.sleep(10)

        except Exception as b:
            print("video not uploaded", b)

    driver.close()


def TTdownloader(Profile, hash):
    opt = webdriver.ChromeOptions()
    opt.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chromedriver_exe_location = os.path.join(os.getcwd() + '\chromedriver.exe')
    profile_path = os.getcwd() + "\\User Data"  # path minus last folder
    opt.add_argument('--user-data-dir={}'.format(profile_path))
    opt.add_argument('--profile-directory={}'.format(Profile))  # last folder name
    driver = webdriver.Chrome(chromedriver_exe_location, options=opt, service_args='')

    hastags = hash

    driver.get(hastags)

    time.sleep(3)

    for a in range(2, 4):

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[" + str(a) + "]/div[1]/div/div/a").click()  # 2-13
        time.sleep(3)
        src = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div/video").get_attribute("src")
        time.sleep(3)
        driver.get(src)
        time.sleep(3)

        r = requests.get(src, headers={"USer-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}, stream=True)

        with r as R:

            R.raise_for_status()

            with open("Shitpost status " + str(hastags).split("q=%23")[1].split("&t=")[0] + " v" + str(a) + ".mp4", 'wb') as f:
                for chunk in R.iter_content(chunk_size=8192):
                    f.write(chunk)

        time.sleep(3)

        driver.get(hastags)

    driver.close()


def TTuploader(Profile, tag):
    opt = webdriver.ChromeOptions()
    opt.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chromedriver_exe_location = os.path.join(os.getcwd() + '\chromedriver.exe')
    profile_path = os.getcwd() + "\\User Data"  # path minus last folder
    opt.add_argument('--user-data-dir={}'.format(profile_path))
    opt.add_argument('--profile-directory={}'.format(Profile))  # last folder name
    driver = webdriver.Chrome(chromedriver_exe_location, options=opt, service_args='')

    path = os.getcwd()

    for file in os.listdir(path):

        try:
            if file.endswith(".mp4"):


                driver.get("https://www.tiktok.com/upload?lang=it-IT")

                time.sleep(5)

                x, y = pyautogui.locateCenterOnScreen(path + '\\immagini\\upload.png')
                pyautogui.click(x, y)

                pyautogui.write(path + "\\" + file)
                pyautogui.press('enter')

                #pyautogui.hotkey('altleft', 'shift')

                time.sleep(10)

                x, y = pyautogui.locateCenterOnScreen(path + '\\immagini\\tag.png')
                pyautogui.click(x, y)
                pyautogui.write(tag, interval=0.75)  # USARE TASTIERA AMERICANA

                #pyautogui.hotkey('altleft', 'shift')
                time.sleep(2)

                x, y = pyautogui.locateCenterOnScreen(path + '\\immagini\\post.png')
                pyautogui.click(x, y)

                time.sleep(5)
        except:
            print("video not uploaded")

    driver.close()


def editor():


    clips = []
    path = os.getcwd()


    for file in os.listdir(path):

        if file.endswith(".mp4"):


            clips.append(VideoFileClip(os.path.join(path, file)))


    final_clip = concatenate_videoclips(clips, method="compose")

    name = "Offensive Shitpost status V" + str(randint(20, 200)) + ".mp4"

    final_clip.write_videofile(name)

    #time.sleep(2)

    #clip = VideoFileClip(path + "\\" + name)
    #clip_resized = clip.resize(1280, 720)
    #clip_resized.write_videofile("movie_resized.mp4")


def cleaner():
    directory = os.getcwd()

    for file in os.listdir(directory):

        if file != "Manager.py" and file != "chromedriver.exe" and file != "User Data" and file != "immagini" and file != "ffmpeg.bat" and file != ".idea":

            if os.path.isdir(directory + "\\" +file):
                shutil.rmtree(directory + "\\" + file)


            else:

                os.remove(file)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

#YouTube

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------


try:
    canali = ['https://www.youtube.com/c/GoofyAhhProductions69/videos', 'https://www.youtube.com/channel/UC-kyNoXnicQ-vCdFPoqQXFA/videos', 'https://www.youtube.com/c/GoofyAhhProductions69/videos']

    for i in canali:
        YTdownloader(i)
except:
    print("YT download failed")

time.sleep(5)




try:
    accounti = ["pampam.mp4"]

    for n in accounti:
        IGdownload(n)
except:
    print("ig download failed")


time.sleep(5)

foldercl()

time.sleep(2)

editor()





try:
    Prof = "Profile 2"
    urlYT = "https://studio.youtube.com/channel/UC2XrPuH8Iv-NDNlMkrTQlhg/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D"
    descrizione = "                            #meme #funny #goofy #ahh #goofy #laugh #funnymeme #short #shorts MEMES THAT  MAYBE LAUGH YOU(MAYBE)funny meme,meme,memes,meme videos,funny videos,fail videos,fail,try not to laugh,try not to laugh videos,best funny videos,best try to not laugh,best funny try not to laugh videos,funny meme videos,offansive meme,offansive memes,light memes,heavy memes,funny videos,intractive memes,memes that make you smile,ksı,ksı try not to laugh,funny,funny clips,memes clips,funny video clips,joke,joke videos,prank,prank videos,sideman,sideman videos,ksı videos,ksı best videos,ksı funny,best memes,offansive funny memes,reddit memes,reedit funy videos,best reddit funyvideos,game memes,best game memes,game funny memes,dank memes, dank, meme, memes, edgy, dankest, funny af, offensive memes, vine videos, meme compilation, dank meme compilation, idubbbz, pewdiepie, filthy frank, tiktok cringe, , moth memes , monky, im monky, mrbeast , best memes compilation v288, youtube rewind memes,best memes compilation 288, obama yoda meme, , gabbie hanna monster meme, indian memes, asian memes, best memes compilation v158 bruh sound effect meme, yobama, best memes compilation v214 memes compialtion v288, memes v288, memes that my mom found in homework folder, memes in my homework folder , memes in my 2tb homework folder , memes, homework, memes that made me upload this video, memes that made me upload these memes, memes that make me skip school , memes, ELON MUSK, CYBERTRUCK , school, spongebob school, meme to watch instead of going school, memes that made me upload this video, tik tok meme compilation, tik tok, pewdiepie minecraft , bruh memes, best memes compilation v60, area 51 meme compilation, funny tik tok,memes,minecraft memes,funny videos,clumsy,clean memes,unusual memes,memes 2021,unusual videos,unusual compilation,try not to laugh,dank compilation,fresh memes,dankest,best memes,meme compilation,comment awards,fortnite memes,pewdiepie,fortnite funny moments,tiktok,tik tok memes,funny memes,minecraft memes,funny videos,clumsy,clean memes,unusual memes,memes 2021,ultimate dank memes, you laugh you lose challenge, funny memes, best memes, haha, memes compilation, freememeskids, memerman, tik tok memes, tik tok, memes that, fresh memes, dank compilation, memer man,pewdiepie minecraft, lil nas x, funniest videos 2019, Fortnite world cup, peppa pig memes, memecorp, best memes compilation.fails of the week , funny fails , fail , failarmyyt , failarmy 2020 , fail 2020 , fails 2020 , fail compilation 2020 , fails compilation 2020 , epic fails 2020 , fails 2020 compilation , funny videos 2020 , try not to laugh , fails of the week 2020 , jukinmedia , jukin media , funny , 2020 , funny fails 2020 , funny 2020 , funny video 2020 , girl fails, Best memes compilation v71 , memes , meme , memes compilation , dank memes , dank , funny , dank memes vine compilation , dank memes compilation , rip vine , vine 2 , meme vine , try not to laugh , dank compilation , fresh memes , offensive , emisoccer , dankest , best memes , meme compilation , comment awards , fortnite memes , pewdiepie , grandayy , fortnite funny moments , Freememeskids , tik tok memes , funny memes , minecraft memes , funny videos , clumsy , memes 2020 dank memes, dank, meme, memes, edgy, dankest, funny af, offensive memes, vine videos, meme compilation, dank meme compilation, idubbbz, pewdiepie, filthy frank, Emisoccer, Succ my meme, family friendly , hefty, grandayy ,  fortnite memes , meme review, fortnite cringe compilation, pewdiepie memes, fortnite memes, bcc trolling, funny videos, try not to laugh , try not to cry , best memes compilation, best memes compilation v13,best memes compilation v2, best memes compilation v3, , best vines, vines, funny vines, alia memes, dancing alien meme,  metal alien memes, phil swift flex tape,pewdiepie,pewdiepie videos,markipler,markipler vieos,#ksi #sideman #memesvideo #funny #funnyclips #funnyvideos #funnyshorts #funnymemes #trynottolaughimpossible #gamememes  #bestfunnyvideos #funnydogs  #funny  #funnymemescompilation #redditmemes  #redditvideos "
    tag = "meme, funny, goofy, ahh, goofy, laugh, funnymeme, short, shorts, laugh"

    YTuploader(Prof, urlYT, descrizione, tag)
except :
    print("yt failed")



time.sleep(5)



#Cleaner


cleaner()



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

#IG

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

try:
    accounti = ["gymshark", "fitness.college", "gym_video_status"]

    for n in accounti:
        IGdownload(n)
except:
    print("ig download failed")




time.sleep(4)




try:
    descIg = "Follow @gym_brosofficial my personal       #legend #doubletap #body #bodybuildinglife #gym #gymmotivation #reelsinstagram #bodybuilding #reelitfeelit #reelkarofeelkaro #reelsviral #trendingreels #fitnessmotivation"
    pr = "Profile 5"

    IGuploader(pr, descIg)
except:
    print("IG upload failed")



time.sleep(4)

cleaner()












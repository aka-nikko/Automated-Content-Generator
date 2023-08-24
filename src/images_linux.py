import os, glob, random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image
from config import name, username, client, profile_pic, verified, theme, handles

JS_ADD_TEXT_TO_INPUT = """
var elm = arguments[0], txt = arguments[1];
elm.value += txt;
elm.dispatchEvent(new Event('change'));
"""
options = Options()
options.add_experimental_option("prefs", {
  "download.default_directory": os.getcwd()+"/assets/temp",
  "download.prompt_for_download": False,
})
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless=new")

#For Renaming the Downloaded Images
def get_last_filename_and_rename(save_folder, new_filename):
    files = glob.glob(save_folder + '/*')
    max_file = max(files, key=os.path.getctime)
    filename = max_file.split("/")[-1].split(".")[0]
    new_path = max_file.replace(filename, new_filename)
    if os.path.isfile("assets/temp/title.png"):
      os.remove("assets/temp/title.png")
    os.rename(max_file, new_path)
    return new_path

def title_image(reddit_obj):
  try:
    print("Generating Title Image")
    driver = webdriver.Chrome(options=options)
    driver.get('https://shashiirk.github.io/fake-tweet-generator/')
    driver.find_element(By.ID ,"name").send_keys(name)
    driver.find_element(By.ID ,"username").send_keys(username)
    driver.find_element(By.ID ,"client").send_keys(client)
    driver.find_element(By.ID ,"retweets").send_keys(random.randint(20, 100))
    driver.find_element(By.ID ,"quotes").send_keys(random.randint(20, 100))
    driver.find_element(By.ID ,"likes").send_keys(random.randint(300, 1000))
    driver.find_element(By.ID ,"message").send_keys(reddit_obj["thread_title"])
    driver.find_element(By.ID,"avatar").send_keys(profile_pic)
    element1 = driver.find_element(By.CSS_SELECTOR,"input[type='radio'][value='"+theme+"']")
    driver.execute_script("arguments[0].click();", element1)
    element2 = driver.find_element(By.CSS_SELECTOR,"input[type='radio'][value='"+verified+"']")
    driver.execute_script("arguments[0].click();", element2)
    driver.find_element(By.ID,"download").click()
    sleep(3)
    driver.close()
    get_last_filename_and_rename(os.getcwd()+"/assets/temp", "title")
  except Exception as e:
    print(e)

def comments_image(reddit_obj, number_of_clips):
  try:
    print("Generating Comment Images")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get('https://ovdss.com/apps/tweet-reply-chain-generator')
    for i in range(0, number_of_clips):
      cname, cusername = random.choice(list(handles.items()))
      e1 = driver.find_element(By.NAME ,"name")
      e1.send_keys(cname)
      e2 = driver.find_element(By.NAME ,"tweet-reply-username")
      e2.send_keys(cusername)
      e3 = driver.find_element(By.NAME ,"tweet-reply-time-input")
      e3.clear()
      e3.send_keys(str(random.randint(1,12))+"h")
      e4 = driver.find_element(By.NAME ,"tweet-reply-retweets")
      e4.send_keys(random.randint(20, 100))
      e5 = driver.find_element(By.NAME ,"tweet_reply_quotes")
      e5.send_keys(random.randint(20, 100))
      e6 = driver.find_element(By.NAME ,"tweet_reply_likes")
      e6.send_keys(random.randint(300, 1000))
      e7 = driver.find_element(By.CSS_SELECTOR ,"textarea[class='form-control tweet-reply-message']")
      driver.execute_script(JS_ADD_TEXT_TO_INPUT, e7, reddit_obj["comments"][i]["comment_body"])
      e7.send_keys(" \n\n")
      e8 = driver.find_element(By.NAME,"tweet-reply-profile-img")
      e8.send_keys(os.getcwd()+"/assets/pics/"+str(random.randint(1,100))+".jpg")
      e9 = driver.find_element(By.ID,"tweet_reply_chain_"+theme+"_theme")
      driver.execute_script("arguments[0].click();", e9)
      driver.find_element(By.ID,"download").click()
      sleep(4)
      e1.clear()
      e2.clear()
      e4.clear()
      e5.clear()
      e6.clear()
      e7.clear()
      e8.clear()
      files = glob.glob(os.getcwd()+"/assets/temp" + '/*')
      max_file = max(files, key=os.path.getctime)
      filename = max_file.split("/")[-1].split(".")[0]
      new_path = max_file.replace(filename, f"{i}")
      if os.path.isfile(f"assets/temp/{i}.png"):
        os.remove(f"assets/temp/{i}.png")
      os.rename(max_file, new_path)
      im = Image.open(f"assets/temp/{i}.png")
      width, height = im.size
      im1 = im.crop((1, 2, width-1, height-1.5))
      im1.save(f"assets/temp/{i}.png")
      sleep(1)
    driver.close()
  except Exception as e:
    print(e)




#Remove Temporary Files From temp Folder (For main.py)
def remove_temp_files():
    try:
        files = glob.glob('assets/temp/*')
        for f in files:
            if f != "assets/temp/clip.mp4":
                os.remove(f)
    except Exception as e:
        print(e)
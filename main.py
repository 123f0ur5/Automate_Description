from selenium import webdriver
from selenium.webdriver.common.by import By
import os, time, unidecode

def add_description(dir):
    #Cont the number of files 
    cont = 0
    file_list = os.listdir(dir) #list with name of every file in the folder
    
    #Get the email and password from a text file
    f = open("account.txt", "r")
    mailpass = f.read().splitlines()
    f.close()

    #start the chrome driver and start the chrome in the url
    driver = webdriver.Chrome("C:/Users/Lucas/Downloads/chromedriver_win32/chromedriver.exe")
    driver.get('https://www.beecrowd.com.br/')

    #Login process, it slice 6 characters because the email is setted like mail: xxxxx also cut 6 from pass: xxxx 
    driver.find_element(By.ID, "email").send_keys(mailpass[0][6:])
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys(mailpass[1][6:])
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys('\ue007') # \ue007 = Enter Key
    time.sleep(2)
    
    #For every file in file_list, check the first line if != #True do the process
    for files in file_list:
        f = open(dir + files, 'r+')
        x = f.readline().strip()
        if x != '#True':
            driver.get('https://www.beecrowd.com.br/repository/UOJ_{}.html'.format(files[:-3])) #[:-3] cut '.py' from the name
            desc = driver.find_element(By.CLASS_NAME, "header").text #Get the descriptions
            desc = unidecode.unidecode(desc)
            desc1 = driver.find_element(By.CLASS_NAME, "problem").text
            desc1 = unidecode.unidecode(desc1)
            f.seek(0) #Go tho the start of the file
            content = f.read() #Read everything that has in the document
            f.seek(0) #Go to the start again and write in the first line: #True, so it never come to the document again
            f.write('#True\n\"'+'\"'+'\"' + desc + desc1 + '\"'+'\"'+'\"\n' + content)
            f.close() #Close the document
            cont +=1
        else:
            f.close()
            cont +=1
    driver.close() #Close the driver
    print(f'Done with {cont} files!')
    return 0


#Define the directory that the program will run
directory = ("./Test/")
add_description(directory)
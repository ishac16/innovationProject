# TV2Play.py net scrape through all movies on TV2Play
# and saves a list in the text file MoviesTV2Play.txt

import time
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# function to scrape url and return soup.
def scrape(url):
    # Open and loads url
    driver.get(url)
    time.sleep(3)

    # makes the webpage scroll down, so alle movies gets loaded
    # these next four lines are highly inspired by:
    # https://medium.com/analytics-vidhya/how-to-web-scrape-data-from-infinite-scrolling-page-da02b3bd04dc
    ScrollNumber = 15
    for i in range(1, ScrollNumber):
        driver.execute_script("window.scrollTo(1,50000)")
        time.sleep(0.3)

    soup = bs4.BeautifulSoup(driver.page_source, 'lxml')
    return soup

# function to write the movie titles to a test file
def writeToFile(fileName, movies):
    with open(fileName, "a", encoding="utf-8") as file:
        for movie in movies:
            file.write(movie['aria-label'])
            file.write("\n")
    file.close()

# Setting up the webdriver
ser = Service("c:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=ser)

url = "https://play.tv2.dk/film"

soup = scrape(url)
movieTag = 'div'
movieParameter = {'style': 'position: relative;'}

# Finds all movies on the corresponding page
movies = soup.find_all(movieTag, movieParameter)

# Writes the movies found on the start webpage to the file MoviesDRTV.txt
fileName = 'MoviesTV2Play.txt'
writeToFile(fileName, movies)

# Finds all links corresponding to a 'se alle'(see all)-bottom
seAlle = soup.find_all('a',{'class':'Link_element__ELhwN text-link-blue focus:text-link-blue-hover hover:text-link-blue-hover'})

# The following enters all 'se alle'-links and search for movies on the individual pages
for alle in seAlle:
    # making a complete link to get by the webdriver
    url = 'http://play.tv2.dk'+alle['href']

    soup = scrape(url)
    movies = soup.find_all(movieTag, movieParameter)
    writeToFile(fileName, movies)

driver.close()

# close open windows
driver.quit()

# DRTV.py net scrape through all movies on DRTV
# and saves a list in the text file MoviesDRTV.txt

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

url = "https://www.dr.dk/drtv/film"

soup = scrape(url)
movieTag = 'a'
movieParameter = {'class': 'packshot packshot--tile packshot-list__packshot packshot-list__packshot col col-phone-12 col-phablet-8 col-laptop-6 col-desktopWide-4'}

# Finds all movies on the corresponding page
movies = soup.find_all(movieTag, movieParameter)

# Writes the movies found on the start webpage to the file MoviesDRTV.txt
fileName = 'MoviesDRTV.txt'
writeToFile(fileName, movies)

# Finds all links corresponding to a 'se alle'(see all)-bottom
seAlle = soup.find_all('a',{'class':'entry-title__seeAll'})

# The following enters all 'se alle'-links and search for movies on the individual pages
for alle in seAlle:
    # making a complete link to get by the webdriver
    url = 'https://www.dr.dk' + alle['href']

    soup = scrape(url)
    movieParameter = {'class':'packshot packshot--tile packshot-list__packshot packshot-list__packshot col col-phone-24 col-phablet-12 col-tablet-8 col-laptop-6 col-desktopWide-4'}
    movies = soup.find_all(movieTag, movieParameter)
    writeToFile(fileName, movies)

driver.close()

# close open windows
driver.quit()
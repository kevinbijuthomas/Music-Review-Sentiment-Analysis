from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import undetected_chromedriver as uc
import time

def main():
    driver = uc.Chrome()
    usernames, reviews, ratings = [], [], []
    dictionary = getDictionaryData(driver, usernames, reviews, ratings)
    dataset = pd.DataFrame(dictionary)
    dataset.to_csv('dataset.csv', index=False)

def getDictionaryData(driver, usernames, reviews, ratings):
    for i in range(1, 38):
        review_url = f"https://www.albumoftheyear.org/album/157182-100-gecs-1000-gecs/user-reviews/?p={i}"
        driver.get(review_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for div in soup.find_all('div', class_ = 'albumReviewRow'):
            for reviewText in div.find_all('div', class_ = 'albumReviewText user'):
                if reviewText.find('a', class_ = 'gray', href=True):
                    driver.get("https://www.albumoftheyear.org" + reviewText.find('a')['href'])
                    fullReview = BeautifulSoup(driver.page_source, 'html.parser')
                    if fullReview.find('span', itemprop = 'ratingValue').text != "NR":
                        usernames.append(fullReview.find('span', itemprop = 'name').text)
                        reviews.append(fullReview.find('div', class_ = 'userReviewText').text)
                        ratings.append(fullReview.find('span', itemprop = 'ratingValue').text)
                else:
                    if div.find('span', itemprop = 'ratingValue').text != "NR":
                        usernames.append(div.find('span', itemprop = 'name').text)
                        reviews.append(reviewText.text)
                        ratings.append(div.find('span', itemprop = 'ratingValue').text)
                time.sleep(5)
    dictionary = {
        'Username':usernames,
        'Review Text':reviews,
        'Rating':ratings
    }
    print(len(usernames))
    print(len(ratings))
    print(len(reviews))
    return dictionary

if __name__ == "__main__":
    main()

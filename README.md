# Music-Review-Sentiment-Analysis
In this notebook, I conduct sentiment analysis and compare the VADER (Valence Aware Dictionary and sEntiment Reasoner) model to Hugging Face's RoBERTa transformer model on music reviews.

I chose to perform analysis on this 1000 gecs by 100 gecs since it is very divisive and there are plenty of both positive and negative reviews.

Reviews have been webscraped from https://www.albumoftheyear.org/album/157182-100-gecs-1000-gecs/user-reviews/ using Selenium as a webdriver and BeautifulSoup4 to parse the .html files. This program is called <b><i>scraper.py</i></b> and resulted in over 850 user reviews.

The main analysis results is shown in <b><i>MusicReviewModel.ipynb</i></b>

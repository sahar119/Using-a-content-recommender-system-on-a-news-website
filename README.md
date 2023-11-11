# <h1 align="center">Using a content recommender system on a news website</h1>

## <h3 align="center">The aim is to provide a content recommendation system that suggests comic content instead of negative and criminal content. </h3>
---

### <h3 align="left">How does it work</h3>
---
A news data set was downloaded. To evaluate how the dataset's content is negative, after cleaning, sentiment analysis was done.

 ![News sentiment analysis GIF](/images/sentiment.png)

A jock data set was downloaded. More data manipulations with the aim of using the prototype were done. These included the renaming of the main data points and the creation of the keyword variable in both datasets. A recommendation system was created, which was accessible with the Read More button under the news article. To create a recommendation system that suggested comic content based on news article content, a content-based recommendation method based on cosine similarity scores was selected. The TextRank algorithm, which is an unsupervised algorithm based on graph-based ranking and implemented by the Summa library, was used for keyword extraction from news articles. The TF-IDF (Term Frequency-Inverse Document Frequency) representation was used to calculate the similarity scores. The cosine similarity metric was employed to measure the similarity between the TF-IDF vectors. TF-IDF scores were calculated for the comic content and news articles using the TfidfVectorizer from Scikit-Learn. Cosine similarity scores were calculated between the news articles and comic content using the cosine_similarity function from Scikit-learn.
Once users click on the read more button to read the full text of the negative news, they are suggested comic content.


### <h3 align="left">Tools and Libraries used</h3>
---
* Pandas
* nltk
* word_tokenize
* stopwords
* sklearn
* summa
* TfidfVectorizer from Scikit-Learn
* streamlit


### <h3 align="left">Project Demo</h3>
---
![Demo GIF](https://github.com/sahar119/Using-a-content-recommender-system-on-a-news-website/blob/main/gif5.gif)

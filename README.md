# RecipeDB-2.0
# Preprocessing of Ingredient Phrases
Convert to Lowercase and convert chilli(es) to chilli

Removal of Stopwords

Lemmatisation


# POS Tagging 
We used 26 Tags (https://github.com/amishaagg/RecipeDB-2.0/blob/main/tags_meaning ) to tag each word in an ingredient phrase. 



Next we made a vector of size 26 for each ingredient phrase storing the tag frequency. For example, a phrase like ‘2_CD cup_NN chickpea_NN flour_NN seived_VBD’ has a vector of the form [2,0,0,0,1,0,0,0,0,0,0,0,0,0..] where 2 denoted NN and 1 denoted VBD.


# K means Clustering. 
We use clustering to cluster the vectors of the ingredient phrases. This ensures that the ingredient phrases with similar linguistic structure are clustered together. We also plot the inertia corresponding to a fixed number of clusters. 
We get a plot of inertia (The sum of squared distances of samples to their closest cluster center) vs number of clusters like this

We find the optimum number of clusters using elbow method ( https://www.geeksforgeeks.org/elbow-method-for-optimal-value-of-k-in-kmeans/ ) and perform clustering for the optimum number of clusters. 

# Test train split for NER tagging
Next we split each cluster into training and testing samples, and make two excel files train and test.

Next we manually annotate them, to perform NER tagging, The tags we used are as follows:




# Training our custom NER model 
	We trained our own NER tagging model with NLTK and Stanford NER Tagger by
following this article. https://www.sicara.fr/blog/2018-04-25-python-train-model-ntlk-stanford-ner-tagger

Create a text file named ‘test.txt’ and paste the testing data in the file.
 We train our model using Stanford NER Tagger on the training dataset we manually annotated earlier and test it on the testing dataset (without annotations).		
Next, we calculated the accuracy of the testing dataset that we annotated manually. 


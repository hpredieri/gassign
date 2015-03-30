#Machine Learning / SKLearn Quiz (Quiz 2)

1. Given the following machine learning matrix, fit each of the following algorithms into their respective places. Some may have multiple.

    .               | continuous          | categorical
    ---------------:|:--------------------|:-----------
    supervised      | regression          | classification
    unsupervised    | dimension reduction | clustering

    Algorithms:
    * Ordinary Least Squares - supervised, regression
    * Logistic Regression - supervised, regression
    * Naive Bayes - supervised, classification
    * Decision Trees - supervised, clustering
    * Support Vector Machines - supervised, dimension reduction
    * Nearest Neighbors - supervised, clustering
    * K Means - supervised, clustering
    * Principal Component Analysis (Matrix Decomposition) - unsupervised, dimension reduction

2. Given the 4 entities in the matrix above, describe a problem / example we worked on in class for each, and provide one idea on your own.

regression: animal dataset find correlation (coefficient) between different variables (total mass, brain mass)
dimension reduction: iris dataset wanted to find a dimension in which we could distinguish two similar clusters
classification: hong kong protests twitter scaper, wanted to classify which hashtags were more predictive vs. not
clustering: iris data set used k nearest neighbors to identify identify three different types

3. All sklearn prediction objects have functions akin to fit(), transform(), predict(), and fit_transform(). Explain each in their most general terms.

fit(): fit the model to the training data set
transform(): turns features into vectors
predict(): use the fit model to make predictions about test data based on train data
fit_transform(): returns a matrix based on the fit function

3. Two of the above algorithms can use kernels (in their sklearn context)
    a. Explain what a kernel does: kernel finds a hyperplane that explains variance
    b. Which are the two algorithms that use kernels? svm, pca

4. One of the above algorithms is most obviously not a linear solution to classification (it does not draw straight decision lines). Which algorithm is it, and how does it decide on decision lines?
decision tree: it splits the data trying to get the most information gain

5. You are working on microarray (DNA) samples where number of observations (n) is 5 and number of observations (m) is > 10,000.
    1. Describe a supervised and unsupervised technique in order to reduce the number of features in the samples to those that are most significant.
    supervised: svm - return
    unsupervised: pca - finding the components that explain the most variance
    2. Compare the two techniques in their solution.

6. Below is a table of Gini Importance (Normalized to 1) in predicting rent in New York City.
    1. Which algorithm uses Gini Importance?: decision trees
    2. Interpret the table.: square feet can predict a given apartment's rent with about 50% confidence 

    Feature           | GiniImportance
    :-----------------|:--------------
    bedrooms          | 0.211
    bathrooms         | 0.005
    sqft              | 0.532
    distance subway   | 0.198
    distance columbus | 0.017
    nearby pizza      | 0.042

7. What is the Receiving Operator Characteristic Curve? What two metrics is it composed of? It measures accuracy of predictive power based on true-positives and false-positives

9. How does a grid search work? Use an example algorithm from above to help explain it. : Cross Validation, it compares different dicitionaries or results when validating different parts of the data against each other

10. Three parts:
    1. What's your strongest "takeaway" from machine learning and this segment of the course?: Understanding the correlation between a dataset's features and the questions you're trying to answer is hugely important. Feature engineering is a very useful skill
    2. Given a 2 dimensional figure where y=effort to learn and x=immediate usefulness, and slope = 1, what is one algorithm that felt above the slope (more effort to learn than usefulness) and one algorithm that felt below the slope (more usefulness than effort to learn)?: Usefulness cannot be measured until you know the data that you are working on. Knowing this is useful in itself.
    3. What's one question you still have about machine learning?: I'm still confused about what a kernel really is

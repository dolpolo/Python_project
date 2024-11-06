## US Election 2020 Tweets Analysis

The ["US Election 2020 Tweets" dataset](https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets/data) provides an extensive collection of tweets from around the world that include hashtags related to the 2020 U.S. presidential candidates, Biden and Trump.

### Objectives
For this analysis, we will focus exclusively on single tweets from each unique Twitter user based in the United States, and in English, to perform text analysis with three main goals:

- **Tweets distribution Analysis**: Clear the dataset and prepare it for a general analysis. Describe how tweets are distributed between the two U.S. candidates in all US and across federal states;
- **Global Sentiment Analysis**: Clear the dataset and prepare it for a Sentiment Text Analysis. Assess the sentiment of the global population of Twitter users towards Biden and Trump evaluating which sentiment preveals on each of them;
- **Federal States Sentiment Analysis**: Assess the sentiment of each Federal state Twitter users towards Biden and Trump and use it as a proxy for the election outcome (**Subsection A**). Evaluate the power of the proxy using the outcome of 2020 elections (**Subsection B**). 

### Project Structure
This analysis is divided into three Jupyter notebooks, each assessing a different phase of the project and its corresponding objective:

- **Description&Cleaning.ipynb**: Tweets distribution Analysis;
- **Sentiment_Biden_vs_Trump.ipynb**: Global Sentiment Analysis;
- **analysis_by_US_states.ipynb**: Federal States Sentiment Analysis.

### Results 
Overall, Twitter data indicates a general preference toward Biden. In fact, our proxy based on the sentiment analysis of tweets predicts that Biden wins in 44 of the federal states.  However, our tweets' sentiment proxy for electoral outcomes turned out to not be a particularly good predictor of the 2020 presidential elections' outcomes. This may be due to the strict assumptions upon which our proxy rests, such as the assumption that neutral tweets do not matter and that a positive tweet toward a candidate is equivalent to a negative tweet toward the other candidate by the same user. Moreover, states differ widely in terms of the total number of tweets, making our proxy less reliable in states with a low number. However, within states, there is not a huge difference in terms of the number of tweets on each candidate. Hence, our sentiment analysis is based on a relatively balanced sample.

It’s worth noting that, although the number of tweets using Trump-related hashtags is significantly higher, many of these tweets tend to carry a critical tone. Therefore, the general preference toward Biden expressed on Twitter may simply be due to the disliking expressed toward Trump's controversial character, and may not translate into a pro-Biden voting behaviour.
It is also important to highlight that there may be a discrepancy between active Twitter users and the voting population. For instance, the former may be relatively younger and leaning toward the democratic party with respect to the latter. 
 
Finally, these considerations lead us to conclude that, although there is great potential for improvement in harnessing social media data to gauge political preferences and even form predictions, *our proposed proxy is not reliable for predicting electoral outcomes*. However, it may provide a rough way to gauge *public sentiment*, which appears to be generally critical of Trump.


### Contribution
This study aims to take an initial step in exploring whether tweets can serve as a reliable proxy for gauging U.S. presidential election trends. A possible future direction for this work could involve forecasting presidential election outcomes by analyzing prevailing sentiment in each federal state, essentially understanding how likely tweets are to anticipate future election results in 2024.

Possible refainments to this work can be:
- **Weights for US states in elections**: correct for the so called *high-electoral-vote states*;
- **Generate a distribution for neutrals**: Test which distribution twitter's users with neutral sentiment follows during elections;
- **Inchoerence in statements**: Account for the possibility to change the mind with respect to a tweet;
- **analysis_by_US_states.ipynb**: Federal States Sentiment Analysis
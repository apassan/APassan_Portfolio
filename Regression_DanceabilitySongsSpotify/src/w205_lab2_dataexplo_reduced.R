
################################################################################
### Load in Packages 
library(dplyr)
library(stringr)
library(tidyverse)
library(gridExtra)

### Source data prep file
#source('w205_lab2_dataexplo.R')
################################################################################

##### Data exploration #####


# popularity distribution

p1 <- ggplot(data = d_explore, aes(x = popularity)) +
  geom_histogram(bins = 20) +
  labs(title = "Distribution of Popularity",x = "Popularity indicator",y = "Count")
p1
# popularity and danceability
ggplot(data = d_explore, aes(y=popularity,x=danceability, group = popularity)) + geom_boxplot()

# predictors, histogram
p_explicit <- ggplot(data = d_explore, aes(x = explicit)) +
  geom_histogram(bins = 20) +
  labs(title = "Distribution of Explicit",x = "Explicit indicator",y = "Count")
p_explicit

p_speechiness <- ggplot(data = d_explore, aes(x = speechiness)) +
  geom_histogram(bins = 20) +
  labs(title = "Distribution of Speechiness",x = "Speechiness indicator",y = "Count")
p_speechiness

p_valence <- ggplot(data = d_explore, aes(x = valence)) +
  geom_histogram(bins = 20) +
  labs(title = "Distribution of Valence",x = "valence indicator",y = "Count")
p_valence

p_energy <- ggplot(data = d_explore, aes(x = energy)) +
  geom_histogram(bins = 20) +
  labs(title = "Distribution of energy",x = "Energy indicator",y = "Count")
p_energy

p_accousticness <- ggplot(data = d_explore, aes(x = acousticness)) +
  geom_histogram(bins = 20) +
  labs(title = "Distribution of accousticness",x = "Accousticness indicator",y = "Count")
p_accousticness

grid.arrange(p_speechiness, p_valence, p_energy, p_accousticness , nrow = 2, ncol = 2)

# followers and data transformation
p_followers <- ggplot(data = d_explore, aes(x = followers)) +
  geom_histogram(bins = 20) +
  labs(title = "Distribution of followers",x = "Followers indicator",y = "Count")
p_followers

p_followers_log <- ggplot(data = d_explore, aes(x = log(followers))) +
  geom_histogram(bins = 30) +
  labs(title = "Distribution of log(followers)",x = "Followers indicator",y = "Count")
p_followers_log

grid.arrange(p_followers, p_followers_log , nrow = 1, ncol = 2)

#Interesting facts
ggplot(data = d_explore, aes(y=popularity,x=energy, group = popularity)) + geom_boxplot()

#ggplot(data = d_explore, aes(y=popularity,x=duration_ms, group = popularity)) + geom_boxplot()  
#ggplot(data = d_explore, aes(y=popularity,x= speechiness, group = popularity)) + geom_boxplot()  
#ggplot(data = d_explore, aes(y=popularity,x=acousticness, group = popularity)) + geom_boxplot()  



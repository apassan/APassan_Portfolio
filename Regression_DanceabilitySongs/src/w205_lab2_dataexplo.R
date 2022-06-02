
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

boxplot( d_explore$popularity, data = d_explore,
         main="Popularity distribution",
         xlab="Popularity indicator",
         col = 'lightblue', 
         horizontal = TRUE)
p1 <- ggplot(data = d_explore, aes(x = popularity)) +
  geom_histogram(bins = 20) +
  labs(title = "Distribution of Popularity",x = "Popularity indicator",y = "Count")
p1

# danceability distribution
boxplot(d_explore$danceability, data = d_explore,
         main="Danceability distribution",
         xlab="Danceability indicator",
         col = 'lightblue', 
         horizontal = TRUE)



# attempt to plot danceability vs popularity
#ggplot(data = d_explore, aes(x = popularity, y = danceability)) +
#  geom_point() +
#  geom_smooth(se = FALSE) +
#  labs(title = "Danceability vs popularity", x = "Popularity", y = "Danceability")


# plot the values without aggregation is not a good idea considering the size of the dataset
# -> suggestion to use aggregate table. aggregation by popularity (so we get only 100 data points)




# aggregate_table <- aggregate(list(duration = d_explore$duration_ms,
#                                     danceability = d_explore$danceability,
#                                     energy = d_explore$energy,
#                                     speechiness = d_explore$speechiness,
#                                     acousticness = d_explore$acousticness,
#                                     instrumentalness = d_explore$instrumentalness,
#                                     liveness = d_explore$liveness,
#                                     valence = d_explore$valence,
#                                     tempo = d_explore$tempo,
#                                     loudness = d_explore$loudness,
#                                     key = d_explore$key,
#                                     explicit = d_explore$explicit,
#                                     mode = d_explore$mode,
#                                     time_signature = d_explore$time_signature
#                                   ), 
#                              by = list(d_explore$popularity), median, na.rm = TRUE) # I would like to add in the aggegate the size of each popularity group

# aggregate function ok but seems more convenient to use a group_by and a summarize

aggregate_table <- group_by(d_explore, popularity) %>% summarize(count = n(),duration = median(duration_ms),
                                                                              danceability = median(danceability),
                                                                              energy = median(energy),
                                                                              speechiness = median(speechiness),
                                                                              acousticness = median(acousticness),
                                                                              instrumentalness = median(instrumentalness),
                                                                              liveness = median(liveness),
                                                                              valence = median(valence),
                                                                              tempo = median(tempo),
                                                                              loudness = median(loudness),
                                                                              key = median(key),
                                                                              explicit = median(explicit),
                                                                              mode = median(mode),
                                                                              time_signature = median(time_signature))

#plot( x = aggregate_table$Group.1 , y  = aggregate_table$danceability_median, data = aggregate_table)
p2<- ggplot(data = aggregate_table, aes(x = popularity, y = duration)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  labs(title = "Duration vs Popularity", x = "Popularity", y = "Duration (ms)")

p3<- ggplot(data = aggregate_table, aes(x = popularity, y = danceability)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  labs(title = "Danceability vs Popularity", x = "Popularity", y = "Danceability")

p4<- ggplot(data = aggregate_table, aes(x = popularity, y = energy)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  labs(title = "Energy vs Popularity", x = "Popularity", y = "Energy")

p5<- ggplot(data = aggregate_table, aes(x = popularity, y = speechiness)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  labs(title = "Speechiness", x = "Popularity", y = "Speechiness")


p6<- ggplot(data = aggregate_table, aes(x = popularity, y = acousticness)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  labs(title = "Acousticness", x = "Popularity", y = "Acousticness")

p7<- ggplot(data = aggregate_table, aes(x = popularity, y = instrumentalness)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  labs(title = "Instrumentalness", x = "Popularity", y = "Instrumentalness")

p8<- ggplot(data = aggregate_table, aes(x = popularity, y = liveness)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  labs(title = "Liveness", x = "Popularity", y = "Liveness")


p9<- ggplot(data = aggregate_table, aes(x = popularity, y = valence)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  labs(title = "Valence", x = "Popularity", y = "Valence")

# assumption: high tempo high danceability
p10<- ggplot(data = aggregate_table, aes(x = danceability, y = tempo)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  labs(title = "Tempo vs Danceability", x = "Danceability", y = "Tempo")

# assumption: high tempo high Energy
p11<- ggplot(data = aggregate_table, aes(x = energy, y = tempo)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  labs(title = "Tempo vs Energy", x = "Energy", y = "Tempo")

# assumption: high loudness high energy
p12<- ggplot(data = aggregate_table, aes(x = energy, y = loudness)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  labs(title = "Loudness vs Energy", x = "Energy", y = "Loudness")

p13<- ggplot(data = aggregate_table, aes(x = popularity, y = key)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  labs(title = "key", x = "Popularity", y = "key")

p14<- ggplot(data = aggregate_table, aes(x = popularity, y = explicit)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  labs(title = "explicit", x = "Popularity", y = "explicit")

p15<- ggplot(data = aggregate_table, aes(x = popularity, y = mode)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  labs(title = "mode", x = "Popularity", y = "mode")

p16<- ggplot(data = aggregate_table, aes(x = popularity, y = time_signature)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  labs(title = "time_signature", x = "Popularity", y = "time_signature")

#tempo/danceability
p10
#Energy
grid.arrange(p11, p12 , nrow = 1, ncol = 2)


#everything vs popularity

grid.arrange(p2,p3,p4,p5,p6,p7,p8,p9, p13,p14,p15,p16 , nrow = 3, ncol = 4)

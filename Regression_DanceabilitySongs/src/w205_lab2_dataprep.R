#### Putting together the final dataset ####

################################################################################
### Load in Packages 
library(dplyr)
library(stringr)
library(tidyverse)

################################################################################
### Load Data and Quick Look 

# Load in data 
d_artists <- read.csv("src/data/artists.csv", header = TRUE)
d_tracks <- read.csv("src/data/tracks.csv", header = TRUE)

# Get quick looks
summary(d_artists)
summary(d_tracks)

# Remove first two characters [' for artists 
d_tracks$artists <- str_sub(d_tracks$artists, 3)
#Remove last two characters '] for artists 
d_tracks$artists <- substring(d_tracks$artists,1, nchar(d_tracks$artists)-2)

# Remove first two characters [' for id_artist
d_tracks$id_artists <- str_sub(d_tracks$id_artists, 3)
#Remove last two characters '] for id_artist
d_tracks$id_artists <- substring(d_tracks$id_artists,1, nchar(d_tracks$id_artists)-2)

# Selecting relevant artist columns: id, followers, popularity 
d_artists$id_artists <- d_artists$id
d_artists$artist_popularity <- d_artists$popularity
d_artists <- d_artists %>% select(id_artists, followers, artist_popularity)

# Join d_artists and d_tracks on artist id
d_joined <- merge(x = d_tracks, y = d_artists, by = "id_artists", all.x = TRUE)

# Change id name to specify for songs 
d_joined$id_song <- d_joined$id

# Select only likely necessary variables (e.g. we don't really need song name)
d <- d_joined %>% select(id_song,
                         popularity,
                         duration_ms,
                         explicit,
                         release_date,
                         danceability, 
                         energy, 
                         key,
                         loudness, 
                         mode, 
                         speechiness, 
                         acousticness, 
                         instrumentalness,
                         liveness, 
                         valence, 
                         tempo, 
                         time_signature,
                         followers, 
                         artist_popularity)

# Check for NAs in filtered dataset
summary(d)
# There are 117089 NAs for followers and artist_popularity 
# Suggest Filtering out these rows
d <- na.omit(d)
summary(d) # Check 

#Create an exploration and testing subsets

exploration_size<-floor( nrow(d)*0.3)  # number of rows we are going to select, 30% of the dataset
set.seed(777)
random_selection = sample(seq_len(nrow(d)),size = exploration_size) #random selection of x rows


d_explore <- d[random_selection,] # the randomly selected rows for the exploration dataset
d_test <- d[-random_selection,]  #full dataset - previously selected rows = the testing dataset


# yelp-dataset-challenge

Brought to you by Dr. Mahsa Mirzargar's independent study trio (In no particular order): Nathan Michaels, Devin Grossman, and David Michaels.

## Downloading the repository

* To download our code, do a `git clone` on this bad boy. To download our data, first get access to Yelp's dataset: https://www.yelp.com/dataset/. Then, please reach out to the maintainers of this repository to receive access to our engineered features.
* At the moment, the plan is to have a `sqlite3` database on each machine locally. When we want to add to that database, we will share a `json` file amongst the collaborators who will be able to run a simple script to load that data into their database.

## Notes on The Dataset
### Data brought to you by Yelp
1. We have access to data from 12 "metropolitan areas", 4.7 million reviews of 156,000 businesses. We also have data on 1.1 million users and 1 million "tips" from these users.
2. *Business Features*: For each business, we have its location, average rating, information on its food category, its business hours, and data on when people went to the restaurant.
3. *Users Features*: We have data on a User's friends, a User's reviews, and a User's review count.

![A view of Yelp's features](https://s3-media2.fl.yelpcdn.com/assets/srv0/engineering_pages/9c5f7a89fd08/assets/img/dataset/yelp_dataset_schema.png)

## Exploratory Data Analysis
In order to gain a good understanding of our dataset, we are exploring simple correlations between variables. Here are some correlations we're looking to explore:

##### David
1. Business rating vs. (# Reviews or # tips)
2. photos vs. Average Rating
3. location (city/state) vs # reviews
17. Business number of reviews vs. Business check-ins
18. Number of businesses by city
19. Rating distribution by city
##### Devin
4. explore “business competition” (normalize by average of zip/city/state)
    1. Clustering of similarly rated businesses
            1. By radius
                    2. By avg rating with circle vs. business merge
                        2. patterns of clustered businesses (good competition? bad competition?)
                                1. displayed in reviews
                                        2. consolidation between competing restaurants ratings
                                                3. geographically close or not close?

                                                5. reviews vs avg length vs rating of that review vs user rating
                                                6. Business Rating vs. Business Review Count
                                                7. Business Rating vs. Total Check-ins (need to engineer this feature)
                                                8. User’s number of friends vs. User review count
                                                9. Business rating vs. Total review count of all users that reviewed that Business
                                                10. Business rating vs. user’s average rating weighted by number of friend
##### Nathan
                                                11. Business rating vs. User’s reviewed were elite
                                                12. Number of reviews that are on a business we have
                                                13. Number of reviews that are on Users we have
                                                14. Number of friends that we don’t have data on
                                                15. user number of ratings vs. User number of friends
                                                16. General patterns of users
                                                    1. How many users are there?
                                                        2.  How many review more than 5 times


## Single Variables to Explore

##### David
1. Geographic data: Businesses by city
    1. Number of 
        2. Which cities
        2. Distribution of ratings
##### Nathan
        3. Time data of tips and reviews
        4. Check in data
        5. Usefulness of compliments, fans, cool, funny, etc for users
##### Devin
        6. Yelping since (for Users)
        7. Look into some individual users


## Big Questions to Explore
1. Define a User Rating
    1. What makes a user valuable? In what context?
        2. How do you find "valuable users"
        2. Variance of User's Reviews
        3. User Influentiality
            1. Graphs/Interconnectedness
                2. How to __ "Influential Users"
                        1. ID  
                                2. Use


## How to share and store data
1. It's difficult. We are in this mid-range data size that we will use for read-heavy operations and will only write new data once in a while (when we add features). We can't and shouldn't share this data via GitHub since it screws with the file size. We tried creating a module, `juicy`, that would partition any JSON file into many <100MB files that we could share via GitHub. But that turned out poorly as it took forever to upload and download and Git isn't meant for data. Also, the loading of JSON into Python objects is pretty honking memory intensive. After a handful of optimizations, it still takes up at least double the memory size (for a 4GB file, that's at least 8GB and we can't assume RAM sizes of over 8GB). 
2. A path that hasn't been explored for the `json` route is the `ijson` module. 
3. The plan as of November 9th, 2017 is to give everyone a copy of a `sqlite3` version of the Yelp SQL database (the conversion process relied on the `mysql2sqlite.sh` that you can find on GitHub). When someone wants to add a feature, we can share that feature via a `json` file (which should usually be relatively small) and each person can run a script to add that `json` file to their `sqlite3` database.


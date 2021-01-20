# Import necessary packages
import os, pandas as pd, numpy as np

# Grab listing data
listings = r'~/Projects/mesprojets/Airbnb/data/20200908/listings.csv'
listings = pd.read_csv(listings, low_memory = False)

# Drop columns with only one value
listings.drop([x for x in listings.columns if len(listings[x].unique()) == 1], axis = 1, inplace = True)

# Set id to index
listings.index = listings.id

# Drop more columns
to_drop = {
        'id',               # Column is set to the index, so we no longer need it.
        'listing_url',      # Don't need. Can get from index
        'last_scraped',     # Metadata. Irrelevant.
        'name',             # Text data is hard to work with, but this might be worth looking into later.
        'description',      # Text data is hard to work with, but this might be worth looking into later.
        'picture_url',      # Picture data is hard to work with, but this might be worth looking into later.
        'host_id',          # This in itself is worthless since we can't extrapolate from it. Perhaps if we
                            ## can pair it to reviews that reference the host explicitly, but that is NLP
                            ## and seems very difficult for now, so drop.
        'neighborhood_overview', # Text data is hard to work with, but this might be worth looking into later.
                                 ## In general, for review data, perhaps create a dictionary of the words throughout
                                 ## the column and their frequencies, choose the top 10% or whatever, and do
                                 ## count-encoding for each listing with respect to these words for model-training.
        'host_url',         # Text data is hard to work with, but this might be worth looking into later.
        'host_name',        # Unnecessary - for the most part.
        'host_since',       # Unnecessary - out of my control.
        'host_location',    # Unnecessary - host location isn't listing location.
        'host_about',       # Text data is hard to work with, but this might be worth looking into later.
        'host_response_time',   # Perhaps should be dropped, since it's presumably not something that I'll strive to optimize.
                                ## Also, there are many NAs which we apparently shouldn't just fill in.
        'host_thumbnail_url', # Unnecessary
        'picture_url',      # Unnecessary
        










        
# What to do with kept columns
recommended_actions = {
    'last_review': 'Filter out listings whose last review is either more than X time before: the last scrape (preferred, but then we should keep "last_scraped" or just
                    assign a value to estimate it for all rows), the date of exploration, or just an arbitrary point in time.',
    'price': 'Convert to float (int for cents) and use.',
    'host_identity_verified': "Honestly, may drop. It might be interesting to know whether it's worth it to get verfied, but that has nothing to do with the place itself.",
    'host_is_superhost': "Use as is.",
    'host_response_rate': "Use as is or drop."
    'host_acceptance_rate': "Consider. Maybe the acceptance rate affects the target, and thus should be dropped to prevent target leakage.",
    'amenities': "One-hot encode",
    'number_of_reviews_l30d': "Use to determine probability of getting a booking. May have to become a target. Maybe is useless and should be dropped.",
    'reviews_per_month': "Use to determine probability of getting a booking. May have to become a target. Maybe is useless and should be dropped.",
    












# Target(s)
target = [
    'availability_365',
    'availability_90',


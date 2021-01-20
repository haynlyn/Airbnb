id
	int
listing_url
	str
scrape_id
	int
last_scraped
	datetime
name
	str
summary
	str
space
	str
description
	str
experiences_offered
	del
neighborhood_overview
	str
notes
	str
transit
	str
access
	str
interaction
	str
house_rules
	str
thumbnail_url
	del
medium_url
	del
picture_url
	del
xl_picture_url
	del
host_id
	int
host_url
	str
host_name
	str
host_since
	datetime
host_location
	str
host_about
	str
host_response_time
	int/float (number of hours or amount of a day)
host_response_rate
	float (percentage)
host_acceptance_rate
	del
host_is_superhost
	bool -> int
host_thumbnail_url
	del
host_picture_url
	del
host_neighbourhood
	str
host_listings_count
	int
host_total_listings_count
	int (is this the same as the above column?)
host_verifications
	set
host_has_profile_pic
	bool -> int
host_identity_verified
	bool -> int
street
	str
neighbourhood
	str
neighbourhood_cleansed
	str
neighbourhood_group_cleansed
	str
city
	str
state
	str
zipcode
	int
market
	str (might be able to delete)
smart_location
	str
country_code
	del
country
	del
latitude
	float
longitude
	float
is_location_exact
	bool -> int
property_type
	str
room_type
	str
accommodates
	int
bathrooms
	float
bedrooms
	float (some are null, so maybe delete them then make int)
beds
	float (some are null, so maybe delete them then make int)
bed_type
	str
amenities
	set
square_feet
	int (most are nul, so maybe del)
price
	int
weekly_price
	int
monthly_price
	int
security_deposit
	int
cleaning_fee
	int
guests_included
	int
extra_people
	int
minimum_nights
	int
maximum_nights
	int
minimum_minimum_nights
	int
maximum_minimum_nights
	int
minimum_maximum_nights
	int
maximum_maximum_nights
	int
minimum_nights_avg_ntm
	float
maximum_nights_avg_ntm
	float
calendar_updated
	int (number of days, where weeks and months are multiplied by 7 and 30, respectively)
has_availability
	del (all are t)
availability_30
	int
availability_60
	int
availability_90
	int
availability_365
	int
calendar_last_scraped
	del
number_of_reviews
	int
number_of_reviews_ltm
	int
first_review
	datetime (maybe delete because idc)
last_review
	datetime
review_scores_rating
	int
review_scores_accuracy
	int
review_scores_cleanliness
	int
review_scores_checkin
	int
review_scores_communication
	int
review_scores_location
	int
review_scores_value
	int
requires_license
	del
license
        del	
jurisdiction_names
	del
instant_bookable
	bool - int
is_business_travel_ready
        bool - int
cancellation_policy
	str, although maybe int because categorical
require_guest_profile_picture
	bool - int (maybe drop since about 2.25% require it)
require_guest_phone_verification
	bool - int (maybe drop since about 2.25% require it)
calculated_host_listings_count
	int
calculated_host_listings_count_entire_homes
	int
calculated_host_listings_count_private_rooms
	int
calculated_host_listings_count_shared_rooms
	int
reviews_per_month
        float
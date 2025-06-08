
# This will house the User model and its methods
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class User:
    def __init__(self):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password # Possible throwaway
        self.SSN = SSN # Possible throwaway
        self.user_rating = user_rating
        self.is_verified = is_verified  # Boolean to indicate if the user is verified
        self.created_at = created_at
        self.updated_at = updated_at
        self.listing_rating = listing_rating  # Rating of the user's listings
        self.is_active = is_active  # Boolean to indicate if the user is active
        self.listings = []  # This will hold the listings associated with the user
        self.last_activity = last_activity  # Timestamp of the user's last activityd

# Listings shoulds have a way of being associated with a user
     
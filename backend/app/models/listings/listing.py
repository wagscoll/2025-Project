# This model will represent a listing

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class Listing:
    def __init__(self):
        self.listing_id = listing_id
        self.title = title
        self.description = description
        self.price = price
        self.user_id = user_id  # Foreign key to User model
        self.category = category
        self.location = location
        self.image_url = image_url  # Probably change this to a "gallery" later
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_active = is_active  # Boolean to indicate if the listing is active
        self.user_rating = user_rating  # Rating of the user who created the listing

    # Add: def get_listings(self):
        # pass

class GetUserListings:
    def __init__(self, user_id):
        self.user_id = user_id
        self.listings = []  # This will hold the listings associated with the user
        self.get_listings()

    
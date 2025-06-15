
'''
Google Maps Address Validation API - 

https://developers.google.com/maps/documentation/address-validation/overview

The Address Validation API is a service that accepts an address. 
It identifies address components and validates them. 
It also standardizes the address for mailing and finds the best known latitude/longitude coordinates for it.

Optionally, for addresses in the United States and Puerto Rico, you can enable the Coding Accuracy Support System (CASS™).
'''

# This entered address can then be cross-checked with: 
'''
ID Analyzer Python SDK - 

https://github.com/idanalyzer/id-analyzer-python 

Core API
ID Analyzer Core API allows you to perform OCR data extraction, facial biometric verification, 
identity verification, age verification, document cropping, document authentication (fake ID check), 
and paperwork automation using an ID image (JPG, PNG, PDF accepted) and user selfie photo or video. 

Core API has great global coverage, supporting over 98% of the passports, 
driver licenses and identification cards currently being circulated around the world.

'''

#import dependecies

# get user's entered address, attached to their profile
def get_user_address(user_id):

    # Placeholder for database retrieval logic
    user_address = {
        "user_id": user_id,
        "address": "123 Main St, Springfield, USA"
    }
    return user_address

# Pass user_address into the Address Validation API
def validate_address(user_address):
    pass


# Placeholder for ID Scanning and Verification
def ID_Analyzer_Python_SDK(user_address):
    pass

# (Optional) Placeholder for Selfie Verification
def selfie_verification(user_id):
    pass
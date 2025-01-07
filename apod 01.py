# Required libraries:
# pip install nasapy
# pip install ipython

import nasapy
import csv
import os
from datetime import datetime
import urllib.request
from IPython.display import Image,display,Audio

# You must first register at https://api.nasa.gov to receive an API access key (it's free!)

# Using the data access key
def get_key(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            return row['api_key']
        
nasa_key = get_key('key.csv')

nasa = nasapy.Nasa(key=nasa_key)

# Data start date (no date can be earlier than this)
earliest_date = datetime(1995, 6, 16)

# Choose a date to see the corresponding APOD
while True:
    d = input("Enter date in YYYY-MM-DD format : ")
    try:
        user_date = datetime.strptime(d, "%Y-%m-%d")
        
        if user_date < earliest_date:
            print(f"Sorry, data for {d} is not available. Please enter a date after {earliest_date.date()} (the start of the APOD data).")
        else:
            break
    except ValueError:
        print("Incorrect date format. Please try again.")

apod = nasa.picture_of_the_day(date=d)

# Check the media type available:
if(apod["media_type"] == "image"):
    
        # Displaying images:
        image_url = apod.get("hdurl", apod.get("url"))
        
        # Saving name for image:
        title = d + "_" + apod["title"].replace(" ","_").replace(":","_") + ".jpg"
        
        # Path of the directory:
        image_dir = "APOD_images"

        # Checking if the directory already exists:
        dir_res = os.path.exists(image_dir)
 
        # If it doesn't exist then make a new directory:
        if (dir_res==False):
            os.makedirs(image_dir)

        # If it exist then print a statement:
        else:
            print("Directory already exists!\n")
        
        # Retrieving the image:
        urllib.request.urlretrieve(url = image_url , filename = os.path.join(image_dir,title))
        
        # Displaying information related to image:
        if("date" in apod.keys()):
            print("Date image released: ",apod["date"])
            print("\n")
        if("copyright" in apod.keys()):
            print("This image is owned by: ",apod["copyright"])
            print("\n")
        if("title" in apod.keys()):
            print("Title of the image: ",apod["title"])
            print("\n")
        if("explanation" in apod.keys()):
            print("Description for the image: ",apod["explanation"])
            print("\n")
        if("hdurl" in apod.keys()):
            print("URL for this image: ",apod["hdurl"])
            print("\n")
        
        # Displaying main image:
        display(Image(os.path.join(image_dir,title)))
    
# If media type is not image:
else:
    print("Sorry, image not available!")
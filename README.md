## 🚀 **Astronomy Picture of the Day (APOD) Viewer** 🛸

This project allows users to access and view **NASA's Astronomy Picture of the Day (APOD)** for any given date, display its corresponding description, and save the image to their computer. The script interacts with NASA's public API to fetch APOD data and automatically downloads the image if it is available.

### 🐍 Prerequisites:

To run this script, you need to install the following Python libraries:

```python  
pip install nasapy
pip install ipython
```

🪐 Additionally, you must create an account on [NASA's API portal](https://api.nasa.gov) to obtain an access key, which is required for fetching APOD data.

### ☄️ How it works:

- The user enters a date in YYYY-MM-DD format.  
- The script verifies if the date is valid and within NASA's APOD data range (starting from June 16, 1995).  
- If valid, it makes a request to the NASA API using the nasapy library to fetch APOD details.  
- If the media type is an image:  
  - The image is downloaded and saved in a local folder (APOD_images).  
  - The image metadata (title, copyright, description, and URL) is displayed.  
  - The image is displayed within the script.  
- If the media type is not an image, a message is shown indicating that no image is available for the selected date.

### 🌌 Setup Instructions:

1. Obtain an API Key:  
  - Go to `api.nasa.gov` and register for a free API key.  
  - Copy your API key and replace your api key here in the script with your actual key.

2. Run the Script:  
  - Open a terminal or command prompt.  
  - Navigate to the directory containing the script.  
  - Run the script using Python:

```python  
python apod.py
```

3. Enter a Date:  
  - When prompted, input a date in YYYY-MM-DD format to fetch the corresponding APOD.  
  - If the entered date is invalid or outside the available range, an error message will appear, and the user will be asked to enter another date.

### 🔭 File Management:

- Downloaded Images:  
  - Images are saved in a folder named APOD_images.  
  - The filename is formatted as YYYY-MM-DD_Title_of_Image.jpg.  
  - If the folder does not exist, the script will automatically create it.

- Handling Duplicate Files:  
  - If an image with the same title and date already exists, it will not be overwritten.

The corresponding image will also be displayed in the script.

### 💥 Error Handling:

The script validates date input to ensure it is in the correct format.  
If the entered date is before June 16, 1995, the user is prompted to enter another date.  
If the API request fails due to an invalid API key or network issues, an error message is displayed.  
If the selected date does not contain an image (e.g., contains a video or other media), a message is shown indicating that an image is not available.

### 💫 Dependencies:

`nasapy`: Used to interact with NASA's API.  
`csv`: Handles CSV file operations (not used in the script but imported for potential enhancements).  
`os`: Manages file directories and checks for existing folders.  
`datetime`: Handles date validation and formatting.  
`urllib.request`: Downloads images from the internet.  
`IPython.display`: Displays images directly within a Jupyter Notebook or IPython environment.

### ⭐️ References:

[NASA API Documentation](https://api.nasa.gov)  
[Astronomy Picture of the Day](https://apod.nasa.gov/apod/)

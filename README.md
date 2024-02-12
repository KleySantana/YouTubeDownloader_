# YouTube Downloader


#### Video Demo: (I had a video demo, but it got removed from YouTube due to its policy)
#### Description:
This project is a simple command-line YouTube downloader tool written in Python. It allows users to download videos from YouTube and save them locally.

**Features**

- **Easy Download**: Download videos from YouTube by providing the video URL.
- **Customizable Resolutions**: Choose from available video resolutions and sizes to suit your preferences and storage capacity.
- **Progress Tracking**: Display download progress, so you know how much of the video has been downloaded and how much is remaining.
- **Retry Mechanism**: In case of download failures, the tool offers a retry option, ensuring a smoother user experience.

#### Disclaimer:
This YouTube downloader tool is provided solely for educational and informational purposes. It is intended to demonstrate the functionality of web scraping and video downloading using Python's Pytube library. Any use of this program to download content from YouTube should comply with YouTube's Terms of Service. Users are solely responsible for ensuring that their use of this program aligns with YouTube's guidelines and policies. The developers of this program do not endorse or condone any unauthorized downloading or distribution of copyrighted materials. By using this program, you agree that any actions taken are at your own risk and discretion.

**Installation**

To use the YouTube downloader, you need to have Python installed on your machine. Follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/KleySantana/YouTubeDownloader_.git
    ```

2. Navigate to the project directory:

    ```bash
    cd YouTubeDownloader_
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

**Usage**

To download a video from YouTube, run the following command in your terminal:

```bash
python downloader.py
```
The tool will prompt you to enter the YouTube video URL and select the desired video resolution. Once you confirm your choices, the download process will begin automatically.

**Code Structure**
The project consists of two main parts: the downloader.py script, which contains the implementation of the YouTube downloader, and the tests directory, which contains unit tests to ensure the correctness of the downloader's functionality.

*Main Program* (downloader.py)
The downloader.py script is the main entry point of the project. It contains the following key components:

*Main Functionality*: The main() function orchestrates the downloading process by interacting with the user, processing the YouTube video link, choosing the video resolution, and initiating the download.
Processing Function: The processing() function extracts information about the YouTube video, such as its title and available resolutions.
*Resolution Selection*: The get_resolution() function prompts the user to choose a video resolution from the available options.
*Download Functionality*: The download() function handles the actual downloading of the video.
*Progress Tracking*: The progress() function tracks the download progress and displays it to the user.

**Tests**
The tests directory contains unit tests to validate the functionality of the YouTube downloader. These tests ensure that the downloader behaves as expected under different scenarios and edge cases. You can run the tests using a testing framework such as pytest:

```bash
pytest test_project.py
```

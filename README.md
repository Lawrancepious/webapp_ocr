# webapp_ocr
OCR Web Application for Hindi & English Text Extraction
This project is a web application that allows users to upload images containing both Hindi and English text and then extracts that text using OCR (Optical Character Recognition) techniques. It is developed using Streamlit for the web interface and Tesseract for text extraction.

Steps to Set Up the Project on Windows
1. Install Python
First, make sure that Python is installed on your system. This project works with Python 3.7 or higher. You can download the latest version from the official Python website. After installation, verify that Python is correctly installed by checking the version from your command line.

2. Install Tesseract OCR
To extract text from images, you need to install Tesseract, a powerful open-source OCR tool. You can download the installer from the official Tesseract GitHub repository or from other trusted sources. During installation, make sure to select the option that adds Tesseract to your system’s PATH. This will allow you to run Tesseract commands from anywhere in the terminal.

Additionally, if you want to extract Hindi text, ensure you install the Hindi language pack for Tesseract.

3. Clone the Project Repository
Next, clone the project from the version control platform (such as GitHub) where you stored it. Download the project files into a local folder on your machine so that you can work with them.

4. Set Up a Virtual Environment (Optional but Recommended)
To keep your project dependencies organized and separate from other projects, create a virtual environment. This will ensure that the libraries installed for this project do not interfere with other Python projects you might have.

5. Install the Required Python Libraries
Once the virtual environment is ready (or even without it), you will need to install the libraries that the project depends on. The primary libraries for this project include Streamlit for building the web interface, pytesseract for integrating Tesseract into Python, and Pillow for handling image uploads and processing. You can easily install these libraries using Python’s package manager.

6. Running the Application
With all dependencies installed, you can now run the application. Open the terminal, navigate to the folder where your project files are stored, and execute the command that starts the Streamlit server. Streamlit will open the application in your web browser, and from there, you can interact with the application by uploading images and viewing the extracted text.

Application Structure
The application consists of several key components:

A web interface that allows users to upload images and view the extracted text.
The core OCR functionality that uses Tesseract to process the uploaded images and extract the text.
A main script that ties everything together, providing a smooth and interactive user experience.
How the Application Works
Users open the web interface (which runs in a web browser) and upload an image file.
The image is processed by the OCR engine, which recognizes and extracts text in both Hindi and English.
The extracted text is then displayed in the browser, where users can copy or save it as needed.
Deployment Options
Deploying Locally
Once the application is running on your local machine, you can access it at a local URL provided by Streamlit. This is suitable for testing and small-scale usage.

Cloud Deployment
For public access, you can deploy the app on a cloud platform like Streamlit Cloud. The deployment process is straightforward:

Push your project files to a version control platform like GitHub.
Go to the Streamlit Cloud website and log in.
Create a new app and link it to your GitHub repository.
Select the main script of your project (usually app.py) and deploy.
Streamlit Cloud will host your application and provide a link that others can use to access it from anywhere.

Troubleshooting Common Issues
Issue: Tesseract Not Recognized
If Tesseract is not recognized by the system, ensure that it is installed properly and that its path is included in the system environment variables.

Issue: Streamlit Not Working
If Streamlit is not running, make sure you have installed the necessary Python libraries and that your terminal is pointed to the correct directory where the project files are located.

Issue: Text Extraction Errors
If the OCR is not extracting text properly, make sure that Tesseract is correctly installed and that the appropriate language packs (like Hindi) are available.

Conclusion
This project successfully demonstrates how to build a web-based OCR system capable of extracting Hindi and English text from images. The simple user interface and reliable text extraction make it an excellent solution for multilingual OCR applications.


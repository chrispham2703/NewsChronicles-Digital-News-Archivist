#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
student_number = 11512318 # put your student number here as an integer
student_name   = 'Van Truong Pham' # put your name here as a character string
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/) and CopyDetect
#  (https://copydetect.readthedocs.io/en/latest/index.html). [2C3202]
#
#--------------------------------------------------------------------#


#-----Task Description-----------------------------------------------#
#
#  News Chronicles
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface development to produce a useful
#  application for maintaining and displaying archived news or
#  current affairs stories on a topic of your own choice.  See the
#  instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  This assignment can be completed using these functions only.

# A function for exiting the program immediately (renamed
# because "exit" is already a standard Python function).
from sys import exit as abort

# A function for opening a web document given its URL.
# [You WILL need to use this function in your solution,
# either directly or via the "download" function below.]
from urllib.request import urlopen

# Some standard Tkinter functions.  [You WILL need to use
# SOME of these functions in your solution.]  You may also
# import other widgets from the "tkinter" module, provided they
# are standard ones and don't need to be downloaded and installed
# separately.  (NB: Although you can import individual widgets
# from the "tkinter.tkk" module, DON'T import ALL of them
# using a "*" wildcard because the "tkinter.tkk" module
# includes alternative versions of standard widgets
# like "Label" which leads to confusion.  If you want to use
# a widget from the tkinter.ttk module name it explicitly,
# as is done below for the progress bar widget.)
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar

# Functions for finding occurrences of a pattern defined
# via a regular expression.  [You do not necessarily need to
# use these functions in your solution, because the problem
# may be solvable with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.]
from re import *

# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).  [You WILL need to use this function
# in your solution.]
from webbrowser import open as urldisplay

# Import the date and time function.
# This module *may* be useful, depending on the websites you choose.
# Eg convert from a timestamp to a human-readable date:
# >>> datetime.fromtimestamp(1586999803) # number of seconds since 1970
# datetime.datetime(2020, 4, 16, 11, 16, 43)
from datetime import datetime

# A module with useful functions on pathnames including:
# normpath: function for 'normalising' a  path to a file to the path-naming
# conventions used on this computer.  Apply this function to the full name
# of your HTML document so that your program will work on any operating system.
# realpath: function to get full absolute path to a file.
# exists: returns True if the supplied path refers to an existing path
from os.path import *

# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your HTML document.
from os import getcwd

# NOTE: DO NOT import any other modules without the express
# permission of the client.

#-----Preamble-------------------------------------------------------#
#
# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer), aborting!\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string), aborting!\n')
    abort()


#-----Supplied Function----------------------------------------------#
#
# Below is a function you can use in your solution if you find it
# helpful.  You are not required to use this function, but it may
# save you some effort.  Feel free to modify the function or copy
# parts of it into your own code.
#
# A function to download and save a web document.  The function
# returns the downloaded document as a character string and
# optionally saves it as a local file.  If the attempted download
# fails, an error message is written to the shell window and the
# special value None is returned.  However, the root cause of the
# problem is not always easy to diagnose, depending on the quality
# of the response returned by the web server, so the error
# messages generated by the function below are indicative only.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document.
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.

def download(url = 'http://www.wikipedia.org/',
             target_filename = 'downloaded_document',
             filename_extension = 'html',
             char_set = 'UTF-8'):

    # Import the function for opening online documents
    from urllib.request import urlopen

    # Import an exception sometimes raised when a web server
    # denies access to a document
    from urllib.error import HTTPError

    # Import an exception raised when a web document cannot
    # be downloaded due to some communication error
    from urllib.error import URLError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError as message: # probably a syntax error
        print("\nCannot find requested document '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except HTTPError as message: # possibly an authorisation problem
        print("\nAccess denied to document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except URLError as message: # probably the wrong server address
        print("\nCannot access web server at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except Exception as message: # something entirely unexpected
        print("\nSomething went wrong when trying to download " + \
              "the document at URL '" + str(url) + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError as message:
        print("\nUnable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters")
        print("Error message was:", message, "\n")
        return None
    except Exception as message:
        print("\nSomething went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None


    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except Exception as message:
        print("\nUnable to write to file '" + \
              target_filename + "'")
        print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents
#
#--------------------------------------------------------------------#




#-----Student's Solution---------------------------------------------#
#
# Name of the folder containing your archived web documents.  When
# you submit your solution you must include the web archive along with
# this Python program. The archive must contain at least seven (7)
# downloaded HTML/XML documents. It must NOT include any other files,
# especially image files.
news_archive = 'NewsArchive'

################ PUT YOUR SOLUTION HERE #################
# URL for the NBC News RSS feed
url = "http://feeds.nbcnews.com/feeds/topstories"

# Function that extracts and saves the required elements from an archived 
# web document.
def extract_elements(html_data):
    # Find all news items in the HTML data
    items = findall("<item>(.*?)</item>", html_data, DOTALL)[:10]
    elements = []
    for item in items:
        # Extract the news title
        title_search = search("<title>(.*?)</title>", item)
        title = title_search.group(1) if title_search else "Title not found"
        
        # Extract the news link
        link_search = search("<link>(.*?)</link>", item)
        link = link_search.group(1) if link_search else "Link not found"
        
        # Extract the news description
        description_search = search("<description>(.*?)</description>", item)
        description = (description_search.group(1) 
                        if description_search 
                        else "Description not found")
        
        # Extract the publication date
        public_date_search = search("<pubDate>(.*?)</pubDate>", item)
        public_date = (public_date_search.group(1) 
                       if public_date_search 
                       else "Date not found")
        
        # Extract the image (thumbnail) for the news item
        image = ""
        image_search = search("<media:thumbnail .*?url=\"(.*?)\"", item)
        if image_search:
            image = image_search.group(1)
        
        # Store extracted data in a dictionary and append to the elements list
        elements.append({
            'title': title,
            'source': link,
            'description': description,
            'image': image,
            'public_date': public_date
        })
    return elements

# Function to generate the HTML source code for the news summary based on 
# extracted data and provided timestamp
def generate_html_source_code(elements, news_time):
    summary_html = """
    <html>
    <head>
        <style>
        body {{background-color: 'white';}}
        h1   {{width: 80%, margin-left: auto, margin-right: auto, 
                text-align: center}}
        h2   {{width: 50%, margin-left: auto, margin-right: auto, 
                text-align: center, 
                margin-top: 20px, margin-bottom: 20px}}
        h3   {{width: 80%, margin-left: auto, margin-right: auto, 
                text-align: center, 
                margin-top: 20px, margin-bottom: 20px}}
        p    {{width: 80%, margin-left: auto, margin-right: auto, 
                text-align: center}}
        </style>
    </head>
    <body>
        <!-- Heading -->
        <!-- NBC News Logo -->
        <p style="text-align: center"><img src="https://www.chicano.ucla.edu/files/styles/large/public/NBC%20News%20Logo.png?itok=ns5peJVH"
                    alt = "NBC News Logo"</p>
        <!-- NBC News Chronicles -->
        <h1 style="text-align: center">NBC News Chronicles</h1>
        <!-- News Date -->
        <h2 style="text-align: center">{}</h2>
        <!-- News Source --> 
        <p style="text-align: center">News Source: <a href = "{}">{}</a></p>
        <!-- Chronicler -->
        <p style="text-align: center">Chronicler: {}</p>
        """.format(news_time, url, url, student_name )
    max_news_to_display = 5  
    news_counter = 1
    for element in elements:
        if news_counter <= max_news_to_display:
            summary_html += """
            <!-- News  -->
            <h3>{}. {}</h3>
            <p style="text-align: center;"><img src="{}"\ 
            alt="Thumbnail" style="border: 3px solid black;"></p>
            <!--Description-->
            <h2 style="text-align: center">{}</h2>
            <!--Source-->
            <p><strong>Full story:</strong><a href="{}">Read more</a></p>
            <!--Publication Date-->
            <p><strong>Publication Date:</strong>{}</p>
            """.format(news_counter, element['title'], 
                       element['image'], element['description'], 
                       element['source'], element['public_date'])
            news_counter += 1
        else:
            break
    # At the end of generate_html_source_code
    filename = save_html_to_file(summary_html)
    # open_html_in_browser(filename)
    return filename

        
# Function to save the generated HTML content to a file
def save_html_to_file(summary_html):
    """Save the HTML content to a file and return the filename."""
    
    date_str = datetime.now().strftime("%Y%m%d%H%M%S")
    summary_filename = "NBCNews_scraped summary_{}.html".format(date_str)
    
    with open(summary_filename, 'w') as summary_file:
        summary_file.write(summary_html)
    
    return summary_filename

# Function to open the saved HTML document in the system's default web browser
def open_html_in_browser(summary_filename):
    print("News has been scraped")
    urldisplay('file://' + realpath(summary_filename))

# Function to scrape the selected archived news and display it
def scrape_and_display():
    # Get archived news times
    news_time = archive_listbox.get(archive_listbox.curselection()[0])
    
    base_path = news_archive
    if news_time == "Latest":
        selected_file = "{}/latest_news.html".format(base_path)
    else:
        formatted_date = format_date_string(news_time)
        selected_file = "{}/NBCNews_{}.html".format(base_path, formatted_date)

    try:
        # Read the contents of an archived news file
        with open(selected_file, 'r', encoding="utf-8") as f:
            html_data = f.read()
    except Exception: 
        # Catch all exceptions instead of just FileNotFoundError.
        message_label.config(text="The archived news file was not found.")
        return
    
    # Extract news information from read content
    elements = extract_elements(html_data)
    
    # Generate HTML source code for news summary
    filename = generate_html_source_code(elements, news_time)
    
    # Open the HTML file with the default browser
    open_html_in_browser(filename)
    
    message_label.config(text="Scraped news displayed in browser")


# Utility function to format date strings
def format_date_string(archived_date):
    date_object = datetime.strptime(archived_date, "%a, %d %B %Y")
    formatted_date = date_object.strftime("%Y-%m-%d")
    
    return formatted_date
  
# Function to download the “latest” news and save it in the archive.
def archive_latest_news():
    """Download the latest news and update the archive."""
    try:
        html_data = download(url=url, target_filename=news_archive + "/latest_news", 
                             filename_extension="html")
        if html_data is None:
            message_label.config(text="Failed to retrieve the file")
            return None
        message_label.config(text="Latest News Archived")
        if archive_listbox.get(END) != "Latest":
            archive_listbox.insert(END, "Latest")
    except Exception:
        # Catch all exceptions instead of just URLError.
        message_label.config(text="Failed to connect to the internet.\
            Please check your connection.")
        
# Graphical User Interface
news_chronicles_window = Tk()
news_chronicles_window.title("NBC News Chronicles")
news_chronicles_window.geometry("800x800")
news_chronicles_window.configure(bg="white") 

# Logo
logo_image = PhotoImage(file="NBC News Logo.png") 
logo_label = Label(news_chronicles_window, image=logo_image, bg="white")
logo_label.pack(pady=(10, 30))

# Title
title_label = Label(news_chronicles_window, text="NBC NEWS CHRONICLES", 
                    font=("Georgia", 32), bg="white")
title_label.pack(pady=50)

# Create a label to notify users to choose the news to scrape
message_label = Label(news_chronicles_window, text="Choose archive to scrape", 
                      font=("Georgia", 20), bg='white')
message_label.pack(pady=10)
# List of items in the listbox
archive_options = [
    "Fri, 13 October 2023", "Sat, 14 October 2023", 
    "Sun, 15 October 2023", "Mon, 16 October 2023",
    "Tue, 17 October 2023", "Wed, 18 October 2023", 
    "Sat, 20 October 2023"]

# Listbox for archives
archive_listbox = Listbox(news_chronicles_window, font=("Georgia", 16),bg="white")
for item in archive_options:
    archive_listbox.insert(END, item)
archive_listbox.pack(pady=10)

# Archive Current News Button
archive_button = Button(news_chronicles_window, text="Archive current news from the web", 
                        font=("Georgia", 16), command=archive_latest_news, bg="white")
archive_button.pack(pady=10)

# Scrape and Display Button
scrape_button = Button(news_chronicles_window, text="Scrape and Display summary", 
                       font=("Georgia", 16),command=scrape_and_display, bg="white")
scrape_button.pack(pady=10)

news_chronicles_window.mainloop()

#--------------------------------------------------------------------#


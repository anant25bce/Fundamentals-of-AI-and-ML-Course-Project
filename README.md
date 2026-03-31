# Fundamentals-of-AI-and-ML-Course-Project

# URL Shortner(CLI)
A simple command-line shortner that converts long URLs into short codes and store them in JSON file.

# Features 
- Shorten a long URL into short code(e.g. 'abc123').
- Expand a short code bank to the original URL.
- Can list all stored URLs and with their codes.
- No need to install any external packages.
- Runs entirely in terminal(no GUI).

# How to run
 1) Open a terminal in the project folder.
 2) Run : python url_shortener_cli.py
 3) Use commands :
    - shorten <URL>
      example: shorten https://example.com/
    - expand <URL>
      example: expand abc123
    - list
      Shows all stored URLs in JSON file.
    - help
      Shows command help.
    - quit
      Exits the program.

# Data Storage
- Shortened URLs are stored in 'urls.json' in the same folder.
- On the next run, the program will remember all previously shortened URLs.

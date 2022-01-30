# Project: Scraping automation
Create an automation process for gathering data from the goodreads webpage then based on the gathered information generate and send forms in email.

# Documentation
Please provide documentation for the code in the repository in Markdown format. Please provide details on how to run and install the application in a new environment including any dependencies, and create documentation about how to run it and set it up.
# Stories
# Web Scraping
Create a web scraping application that reads book pages on Goodreads and gathers the rating and author for each book. It should read at least 100 pages and it should save all the ratings and authors.
# Top 5 rated authors spreadsheet
Write a corresponding script that processes the gathered data and creates a top list of the most rated 5 authors in the gathered books, and saves the result in a spreadsheet on Google Drive.
# Form generation
Based on the top 5 author list the automation process should create a Google Form that lists all the authors as a multiple choice option where the users are able to select their favourites.
# Email
The automation process should send the generated Google Form to a list of email addresses that is defined in a Google Spreadsheet.
# Scheduling
The scraping, uploading, form generation and email send should be scheduled to run once every week.

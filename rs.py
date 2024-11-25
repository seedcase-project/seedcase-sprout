import os
import re
from datetime import datetime

# Define the directory containing your documents
repo_dir = "/Users/au157729/Documents/GitHub/seedcase-sprout"

# Define the pattern to search for the Next Review date in each document
date_pattern = r"<!--Next Review date:\s*(\d{4}-\d{2}-\d{2})-->"

# Get the current date for comparison
current_date = datetime.now()


# Function to check if the review date has passed
def has_review_date_passed(review_date_str):
    try:
        review_date = datetime.strptime(review_date_str, "%Y-%m-%d")
        return review_date < current_date
    except ValueError:
        # In case the date is malformed, return False
        return False


# Function to search for the Next Review date in each document
def find_review_dates_in_repo(repo_dir):
    # List to store files with passed review dates
    passed_files = []

    # Walk through the repository directory
    for root, dirs, files in os.walk(repo_dir):
        for file in files:
            # Check if the file is a document type you're interested in (e.g., .html, .txt, .xml)
            if file.endswith(
                (".html", ".xml", ".txt", ".qmd", ".md")
            ):  # Adjust extensions as needed
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                    # Search for the review date in the file
                    match = re.search(date_pattern, content)
                    if match:
                        review_date_str = match.group(
                            1
                        )  # Extract the date from the comment
                        if has_review_date_passed(review_date_str):
                            passed_files.append(
                                (file_path, review_date_str)
                            )  # Store both file path and date

    return passed_files


# Get the list of documents where the review date has passed
files_with_passed_reviews = find_review_dates_in_repo(repo_dir)

# Output the list of documents with their review dates
if files_with_passed_reviews:
    print("Documents with passed review dates:")
    for item in files_with_passed_reviews:
        file_path, review_date = item  # Unpack the tuple
        print(f"{file_path} (Next Review Date: {review_date})")
else:
    print("No documents with passed review dates found.")

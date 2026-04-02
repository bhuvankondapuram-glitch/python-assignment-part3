# python-assignment-part3:
# Product Explorer & Error Logger (Part 3)

This project demonstrates Python concepts including file handling, API integration, exception handling, and logging.

## 🔹 Features Implemented

### 1. File Handling
- Created and wrote data to `python_notes.txt`
- Appended additional content
- Read and displayed file contents
- Counted lines and searched keywords

### 2. API Integration
- Fetched product data from DummyJSON API
- Displayed products in formatted output
- Filtered and sorted products based on rating and price
- Retrieved products by category (laptops)
- Simulated POST request to create a product

### 3. Exception Handling
- Implemented safe division function (`safe_divide`)
- Handled file reading errors (`read_file_safe`)
- Added robust API calls with try-except handling:
  - Connection errors
  - Timeout errors
  - General exceptions
- Input validation loop for product lookup

### 4. Logging System
- Created `error_log.txt` to store error logs
- Logged:
  - Connection errors
  - HTTP 404 errors
- Each log includes timestamp, function name, error type, and message

## 🔹 Files Included

- `part3_api_files.py` – Main Python code
- `python_notes.txt` – Generated file with Python notes
- `error_log.txt` – Log file containing error entries
- `README.md` – Project documentation

## 🔹 Technologies Used

- Python
- Requests library
- DummyJSON API

## 🔹 How to Run

1. Install dependencies:

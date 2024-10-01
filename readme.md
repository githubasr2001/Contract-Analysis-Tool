Contract Document Analysis Tool

## Overview

The **Contract Document Analysis Tool** is a web application built using Flask, designed to extract and analyze legal entities from various contract document formats, including PDF, Word, and images. This tool leverages Natural Language Processing (NLP) to provide insights into important details, such as commission percentages, vendor names, expiration dates, and more.

## Use Case

In legal and business environments, contracts often contain critical information that must be reviewed quickly and accurately. This tool automates the process of analyzing contract documents, making it easier for users to extract necessary information without manually reading through pages of text.

## Features

- Upload contract documents in multiple formats (PDF, Word, JPEG, PNG).
- Automatically extract key legal entities and relevant information.
- Display results in a user-friendly interface.

## Technologies Used

- **Flask**: A lightweight web framework for Python.
- **spaCy**: An NLP library for advanced text processing.
- **Werkzeug**: A WSGI utility library for Python.
- **HTML/CSS**: For the frontend interface.

## Installation

### Prerequisites

Make sure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Contract-Analysis-Tool.git
cd Contract-Analysis-Tool
```

### Set Up a Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python -m venv cnv
source cnv/bin/activate  # On Windows use `cnv\Scripts\activate`
```

### Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

### Download spaCy Model

Make sure to download the spaCy model:

```bash
python -m spacy download en_core_web_sm
```

## Running the Application

Start the Flask application:

```bash
python app.py
```

Open your web browser and navigate to `http://127.0.0.1:5000` to access the tool.

## Usage

1. Upload a contract document in PDF, Word, or image format.
2. Click the "Analyze" button to extract legal entities.
3. View the results displayed on the results page.




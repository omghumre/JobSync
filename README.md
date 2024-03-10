# Company Recommendation Platform - "JobSync : Find your Dream Company"

## Hackathon Recognition

This project achieved remarkable success at the **HackNITR hackathon at NIT Rourkela**, securing a position in the prestigious **top 10**. The acknowledgment reflects its innovation and utility in assisting job seekers to find their dream companies.

## Overview

This project is a company recommendation platform developed during the same hackathon. The platform assists users in finding suitable companies to apply to based on the content of their resumes. By analyzing the provided resume, the system predicts the user's potential job category and suggests a list of companies associated with that category.

## Features

- **Resume Upload:** Users can upload their resumes in either text or PDF format.
- **Resume Cleaning:** The system processes the uploaded resume, cleaning it by removing URLs, special characters, and non-ASCII characters.
- **Prediction:** The cleaned resume is transformed using a TF-IDF vectorizer, and the trained classifier predicts the most suitable job category.
- **Company Recommendations:** Based on the predicted job category, the platform suggests a list of companies associated with that category.
- **Interactive Interface:** The application is built using Streamlit, providing a user-friendly interface for an engaging experience.

## Technologies Used

- **Streamlit:** The web application framework for creating interactive and data-driven web applications.
- **Joblib:** Used for loading the pre-trained classifier and TF-IDF vectorizer models.
- **NLTK:** Natural Language Toolkit for text processing tasks like tokenization and stopwords removal.
- **Pandas:** Used for reading and manipulating the company dataset.

## Project Structure

- **`app.py`:** The main application file containing the Streamlit interface and the logic for processing resumes and making predictions.
- **`clf.joblib`:** Pre-trained machine learning classifier for predicting job categories.
- **`tfidf.joblib`:** Pre-trained TF-IDF vectorizer for transforming cleaned resumes.
- **`companies.csv`:** Dataset containing information about various companies, including job titles and LinkedIn job post URLs.

## Usage

1. Install the required dependencies by running:

    ```bash
    pip install streamlit joblib nltk pandas
    ```

2. Run the application:

    ```bash
    streamlit run app.py
    ```

3. Access the application through the provided URL and upload your resume to receive personalized company recommendations.

## Contributors

- [Your Name]
- [Other Team Members]

Feel free to contribute to the project by improving the code, adding new features, or providing feedback.

## License

This project is licensed under the [MIT License](LICENSE.md).

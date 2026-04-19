# Demographic Data Analyzer

This is the second project of the **Data Analysis with Python** certification from freeCodeCamp. The goal is to analyze a dataset of demographic data extracted from the 1994 Census database using the Pandas library.

## Project Description

In this project, I used Pandas to answer several demographic questions such as:
* How many people of each race are represented in this dataset?
* What is the average age of men?
* What is the percentage of people who have a Bachelor's degree?
* What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
* What percentage of people without advanced education make more than 50K?
* What is the minimum number of hours a person works per week?
* What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
* What country has the highest percentage of people that earn >50K and what is that percentage?
* Identify the most popular occupation for those who earn >50K in India.

## Technologies Used
* **Python 3.x**
* **Pandas**: For data manipulation and analysis.

## Dataset
The dataset (`adult.data.csv`) was provided by the UCI Machine Learning Repository. It contains information like age, workclass, education, marital status, occupation, race, sex, native country, and salary.

## How to Run
1.  Ensure you have Python and Pandas installed:
    ```bash
    pip install pandas
    ```
2.  Clone the repository:
    ```bash
    git clone [https://github.com/LyNhutMinh/Demographic-Data-Analyzer.git](https://github.com/LyNhutMinh/Demographic-Data-Analyzer.git)
    ```
3.  Navigate to the directory and run the script:
    ```bash
    python "Demographic Data Analyzer.py"
    ```

## Results Example
When the script runs, it outputs statistics like:
* **Average age of men**: 39.4
* **Percentage with Bachelors**: 16.4%
* **Highest earning country**: Iran (41.9%)
* **Top occupation in India**: Prof-specialty

---
*Developed as part of the freeCodeCamp Data Analysis Curriculum.*

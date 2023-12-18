# Gender Representation in Academia: Evidence from the Italian Education System Reform

![GitHub last commit](https://img.shields.io/github/last-commit/[YourGitHubUsername]/[YourRepoName])
![Language count](https://img.shields.io/github/languages/count/[YourGitHubUsername]/[YourRepoName])
![Top language](https://img.shields.io/github/languages/top/[YourGitHubUsername]/[YourRepoName])

## Description
This project investigates the "glass ceiling" effect in Italy's education system, focusing on the career advancement of researchers in academia. It analyzes the 2010 Italian national promotion qualification data, using web scraping to collect demographic and research productivity data from CVs and bibliometric sources like Scopus. The study assesses if gender influences the likelihood of qualifying for higher academic positions, controlling for factors like research output, personal attributes, and university location. Initial findings indicate no significant gender impact on qualification chances. Robustness checks with alternative productivity metrics and probit regression models reinforce these findings. Notably, the study highlights the lower representation of women in the applicant pool, emphasizing the need for diversity-sensitive scientific productivity metrics to better understand the barriers in academic career progression.

---

## Table of Contents
- [Literature Review](#literature-review)
- [Data Description](#exploratory-data-analysis-eda)
- [How to Run the Project](#model-specification-and-economic-interpretation)
---

## Literature Review
Literature suggests that biases in bibliometric indicators and gender stereotypes within male-dominated networks may hinder women's advancement, despite comparable research outputs. Using Italy as a case study, with its unique emphasis on bibliometric evaluations for academic promotions, the project aims to uncover underlying factors affecting women's progression to higher academic roles. The analysis covers a wide range of research fields and compares patterns in STEM and non-STEM disciplines to understand the determinants of academic career advancement.

---
## Data Description

The study utilized data from three primary sources: applicant CVs, the Scopus bibliometric database for research output details, and the Cerca database for university information.

The dataset encompasses data on 5596 associate professor and 2298 full professor candidates. Each candidate's CV, unique in format and content, included their ID, name, date of birth, publication list, and other academic achievements. The ANVUR (Italian National Agency for the Evaluation of Universities and Research Institutes) did not standardize the CV submission format, adding complexity to data extraction.

To systematize the varied CV data into a machine-readable format, Python was employed alongside tools like Beautiful Soup, PyPDF2, and text analytics APIs. This process involved extracting authors' names and IDs from Scopus, using its advanced search and an author API for detailed metrics like the number of publications, Impact Factor, and years since the first publication. Additionally, university locations were inferred from CVs to create location indicator variables. Subsequent analysis was conducted using the R programming language.



---
## How to Run the Project

The code is to be added soon! 

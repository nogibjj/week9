[![Format](https://github.com/nogibjj/Project1ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Project1ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/actions/workflows/format.yml)

[![Install](https://github.com/nogibjj/Project1ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Project1ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/actions/workflows/install.yml)

[![Lint](https://github.com/nogibjj/Project1ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Project1ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/actions/workflows/lint.yml)

[![Test](https://github.com/nogibjj/Project1ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Project1ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/actions/workflows/test.yml)
# Project1ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject
## Requirements
The project structure include the following files:<br>
Jupyter Notebook with Cells that perform descriptive statistics using Polars.<br>
Tested by using nbval plugin for pytest<br>
Python Script performing the same descriptive statistics using Polars<br>
lib.py file that shares the common code between the script and notebook<br>
Makefile with：<br>
Run all tests (test notebook and script and lib)<br>
Formats code with Python black<br>
Lints code with Ruff<br>
Installs code via:  pip install -r requirements.txt<br>
test_script.py to test script<br>
test_lib.py to test library<br>
GitHub Actions performs all four Makefile commands with badges for each one in the README.md

## Video Link


## Description
This project was generated from python template, which includes Makefile, requirements.txt, githubAction etc. It can automatically install, test, format, lint my change.
In this project, I read nba.csv file using polar. This file contains many players with name, team, number, position, age, height, weight, college and salary. Then i calculate mean, min, max, standard deviation and median for this dataset. Then I print the result to terminal for data visualization. Finally, I used matplotlib to generate age distribution graph shwon in Age_distribution.png, Weight_distribution_polar.png, Salary_distribution_polar.png.

## Sample Output
![result](sample.png)
![Age_distribution](Age_distribution_polar.png)
![Weight_distribution](Weight_distribution_polar.png)
![Salary_distribution](Salary_distribution_polar.png)
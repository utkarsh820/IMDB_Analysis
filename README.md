# IMDb Statistical Analysis

![IMDb Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/320px-IMDB_Logo_2016.svg.png)

## Project Overview

This project conducts a comprehensive statistical analysis of IMDb movie data, exploring trends in ratings, box office performance, and the influence of directors across different decades. The analysis provides insights into the evolution of cinema over the past century and identifies factors that contribute to a film's success.

## Dataset

The analysis uses a dataset of 1000 top-rated movies from IMDb, including information such as:
- Movie titles and release years
- IMDb ratings and Metascores
- Box office earnings
- Runtime
- Directors and starring actors

Data source: [IMDb Dataset on GitHub](https://raw.githubusercontent.com/utkarsh820/Datasets/refs/heads/main/imdb.csv)

## Key Findings

### Box Office Trends
- Box office earnings show a consistent upward trend from the 1920s to the 2010s
- The 2010s had the highest average gross earnings at approximately $94.8 million per film
- Statistical analysis with 95% confidence intervals confirms this growth trend is statistically significant

### Director Influence
- Directors like Francis Ford Coppola, Christopher Nolan, and Frank Darabont consistently produce highly-rated films
- Director reputation appears to be a reliable indicator of film quality

### Correlation Analysis
- Positive correlation between IMDb ratings (audience scores) and Meta scores (critic ratings)
- Longer films tend to have slightly higher ratings
- The relationship between box office performance and ratings is positive but not strong

## Analysis Techniques

The project employs various statistical and data analysis techniques:
- Data cleaning and preprocessing
- Descriptive statistics
- Correlation analysis
- Confidence interval calculation
- Data visualization with Matplotlib and Seaborn

## Repository Structure

```
imdb_analysis/
│
├── IMDB_Stastical_Analysis.ipynb   # Main Jupyter notebook with analysis
├── README.md                       # Project documentation
├── LICENSE                         # MIT License
└── requirements.txt                # Required Python packages
```

## Getting Started

### Prerequisites
- Python 3.7+
- Jupyter Notebook or JupyterLab

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/imdb_analysis.git
cd imdb_analysis
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Open the Jupyter notebook:
```bash
jupyter notebook IMDB_Stastical_Analysis.ipynb
```

## Future Work

- Incorporate inflation-adjusted earnings for more accurate historical comparisons
- Expand the analysis to include streaming platform performance metrics
- Conduct genre-specific analyses to identify trends within particular film categories
- Explore the relationship between marketing budgets and box office performance
- Investigate the impact of star power versus director influence on film success

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- IMDb for providing the original data
- [Utkarsh820](https://github.com/utkarsh820) for hosting the dataset
- The Python data science community for developing the tools used in this analysis

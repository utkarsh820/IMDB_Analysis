#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
IMDb Data Visualization Script

This script provides examples of how to visualize the IMDb dataset
using matplotlib and seaborn. It can be used as a starting point
for further analysis and visualization.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew

# Set style for plots
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('viridis')

def load_data():
    """Load the IMDb dataset and perform basic preprocessing."""
    # Load data
    imdb = pd.read_csv('https://raw.githubusercontent.com/utkarsh820/Datasets/refs/heads/main/imdb.csv')
    
    # Select relevant columns
    data = imdb[['Director', 'IMDB_Rating', 'Released_Year', 'Meta_score', 
                 'No_of_Votes', 'Runtime', 'Gross']]
    
    # Clean data
    data['Released_Year'] = pd.to_datetime(data['Released_Year'], errors='coerce').dt.year
    data['Meta_score'] = data['Meta_score'].fillna(data['Meta_score'].mean())
    data['Gross'] = data['Gross'].str.replace(',', '')
    data['Gross'] = data['Gross'].astype(float)
    data['Gross'] = data['Gross'].fillna(data['Gross'].median())
    data['Runtime'] = data['Runtime'].str.replace("min", '').astype(int)
    data['Released_Year'] = data['Released_Year'].fillna(1995.0)
    
    # Add decade column
    data['Decade'] = (data['Released_Year'] // 10) * 10
    
    return data

def plot_top_directors(data, n=10):
    """Plot top n directors by average IMDb rating."""
    plt.figure(figsize=(12, 6))
    
    director_ratings = data.groupby("Director")['IMDB_Rating'].mean().sort_values(ascending=False).head(n)
    
    sns.barplot(x=director_ratings.index, y=director_ratings.values, palette="viridis")
    plt.xticks(rotation=45, ha="right")
    plt.title(f"Top {n} Directors by Average IMDB Rating", fontsize=16)
    plt.xlabel("Director", fontsize=12)
    plt.ylabel("Average IMDB Rating", fontsize=12)
    plt.tight_layout()
    plt.savefig('top_directors.png', dpi=300)
    plt.close()

def plot_decade_trends(data):
    """Plot trends across decades."""
    plt.figure(figsize=(15, 10))
    
    # Create a 2x2 subplot
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Plot 1: Average IMDb rating by decade
    sns.boxplot(x='Decade', y='IMDB_Rating', data=data, ax=axes[0, 0])
    axes[0, 0].set_title('IMDb Ratings by Decade', fontsize=14)
    axes[0, 0].set_xlabel('Decade', fontsize=12)
    axes[0, 0].set_ylabel('IMDb Rating', fontsize=12)
    
    # Plot 2: Average gross earnings by decade
    decade_gross = data.groupby('Decade')['Gross'].mean().reset_index()
    sns.barplot(x='Decade', y='Gross', data=decade_gross, ax=axes[0, 1])
    axes[0, 1].set_title('Average Gross Earnings by Decade', fontsize=14)
    axes[0, 1].set_xlabel('Decade', fontsize=12)
    axes[0, 1].set_ylabel('Average Gross ($)', fontsize=12)
    axes[0, 1].ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    
    # Plot 3: Average runtime by decade
    decade_runtime = data.groupby('Decade')['Runtime'].mean().reset_index()
    sns.barplot(x='Decade', y='Runtime', data=decade_runtime, ax=axes[1, 0])
    axes[1, 0].set_title('Average Runtime by Decade', fontsize=14)
    axes[1, 0].set_xlabel('Decade', fontsize=12)
    axes[1, 0].set_ylabel('Average Runtime (minutes)', fontsize=12)
    
    # Plot 4: Number of movies by decade
    decade_count = data.groupby('Decade').size().reset_index(name='count')
    sns.barplot(x='Decade', y='count', data=decade_count, ax=axes[1, 1])
    axes[1, 1].set_title('Number of Movies by Decade', fontsize=14)
    axes[1, 1].set_xlabel('Decade', fontsize=12)
    axes[1, 1].set_ylabel('Count', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('decade_trends.png', dpi=300)
    plt.close()

def plot_correlation_matrix(data):
    """Plot correlation matrix for numeric variables."""
    # Select numeric columns
    numeric_data = data[['IMDB_Rating', 'Meta_score', 'No_of_Votes', 'Runtime', 'Gross']]
    
    # Calculate correlation matrix
    corr_matrix = numeric_data.corr()
    
    # Plot correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title("Correlation Matrix", fontsize=16)
    plt.tight_layout()
    plt.savefig('correlation_matrix.png', dpi=300)
    plt.close()

def main():
    """Main function to run all visualizations."""
    print("Loading and preprocessing data...")
    data = load_data()
    
    print("Plotting top directors...")
    plot_top_directors(data)
    
    print("Plotting decade trends...")
    plot_decade_trends(data)
    
    print("Plotting correlation matrix...")
    plot_correlation_matrix(data)
    
    print("All visualizations have been saved to the current directory.")

if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Define the main color
main_color = '#568789'

# Histogram
def histograms(df, columns, n_cols = 3):
    
    n_rows = (len(columns) // n_cols) + (len(columns) % n_cols > 0)

    # Create subplots
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))

    # Flatten axes
    axes = axes.flatten()

    # Plot histograms for each column 
    for i, col in enumerate(columns):
        ax = axes[i]
        ax.hist(df[col].dropna(), edgecolor='black', color='orange')
        ax.set_title(f'Histogram of {col}', fontsize=10)
        ax.set_xlabel(col)
        ax.set_ylabel('Frequency')

    # Remove empty subplots (if any)
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

# Top-N Histogram
def top_n_histogram(df, column, N=10, rotation=0):
    plt.figure(figsize=(10, 6))
    
    # Get top N categories by frequency (sorted from highest to lowest)
    top_categories = df[column].value_counts().nlargest(N)
    
    # Filter and sort the dataframe accordingly
    filtered_df = df[df[column].isin(top_categories.index)]
    filtered_df[column] = pd.Categorical(filtered_df[column], categories=top_categories.index, ordered=True)
    
    # Plot
    sns.histplot(filtered_df[column], discrete=True, color='orange', kde=False)
    
    plt.title(f'Top {N} Histogram of {column}', fontsize=14)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.xticks(rotation=rotation)
    plt.show()

# Unique Histogram
def unique_histogram(df, column, rotation=0):
    plt.figure(figsize=(10, 6))

    # Get category frequencies sorted from highest to lowest
    category_counts = df[column].value_counts()
    
    # Convert the column to Categorical type with custom order
    df[column] = pd.Categorical(df[column], categories=category_counts.index, ordered=True)
    
    # Plot the histogram with sorted categories
    sns.histplot(df[column], discrete=True, color='orange', kde=False)
    
    plt.title(f'Histogram of {column}', fontsize=14)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.xticks(rotation=rotation)
    plt.show()

# Boxplots
def boxplots(df, categorical, continuous, n_cols=3):
    # Calculate the total number of plots
    total_plots = len(categorical) * len(continuous)
    
    # Calculate the number of rows needed
    n_rows = int(np.ceil(total_plots / n_cols))
    
    # Create subplots
    fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(n_cols * 6, n_rows * 6))
    
    # Flatten axes to make iteration easier
    axes = axes.flatten()
    
    plot_idx = 0
    
    # Iterate through each combination
    for cat in categorical:
        for cont in continuous:
            if plot_idx < len(axes):
                sns.boxplot(x=cat, y=cont, data=df, palette='Oranges', ax=axes[plot_idx])
                axes[plot_idx].set_title(f'{cat} vs {cont}')
                axes[plot_idx].tick_params(axis='x', rotation=45)
                plot_idx += 1

    # Hide any unused subplots
    for idx in range(plot_idx, len(axes)):
        axes[idx].axis('off')

    plt.tight_layout()
    plt.show()

# Crosstab
def plot_crosstab(df, column1, column2, annot_kws={"rotation": 45}):

    # Create the crosstab
    crosstab = pd.crosstab(df[column1], df[column2])

    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(crosstab, annot=True, fmt="d", cmap='Oranges', annot_kws=annot_kws)
    plt.title(f'{column1} vs {column2}')
    plt.show()


# Plot Boxplot and histogram
def plot_distribution_and_boxplot(df, column_name, n_bins, color=main_color):
    """
    Plots the distribution and box plot for a specific column.
    
    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        column_name (str): Column to visualize.
        color (str): Plot color.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    sns.histplot(df[column_name], kde=True, bins=n_bins, color=color, ax=axes[0])
    axes[0].set_title(f"Distribution of {column_name}")
    axes[0].set_xlabel(column_name)
    axes[0].set_ylabel("Frequency")

    sns.boxplot(x=df[column_name], color=color, ax=axes[1])
    axes[1].set_title(f"Boxplot of {column_name}")
    axes[1].set_xlabel(column_name)

    plt.tight_layout()
    plt.show()
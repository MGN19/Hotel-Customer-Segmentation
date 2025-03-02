import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Data Exploration
# Missing Value Analysis
def missing_value_summary(dataframe):
    """
    Provides a summary of missing values in the DataFrame.
    
    Parameters:
        dataframe: The DataFrame to analyze.
    
    Returns:
        pd.DataFrame: Summary of columns with missing values, including unique values, NaN count, and percentage.
    """
    nan_columns = dataframe.columns[dataframe.isna().any()].tolist()
    summary_data = []
    
    for column in nan_columns:
        nan_number = dataframe[column].isna().sum()
        nan_percentage = (nan_number / len(dataframe)) * 100
        unique_values = dataframe[column].nunique()
        summary_data.append({
            'Unique Values': unique_values,
            'NaN Values': nan_number,
            'Percentage NaN': nan_percentage
        })
    
    summary = pd.DataFrame(summary_data, index=nan_columns)
    return summary

# Data Visualization
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
def plot_distribution_and_boxplot(df, column_name, n_bins, out_left=None, out_right=None, color=main_color):
    """
    Plots the histogram and box plot for a specific column with optional outlier boundaries.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        column_name (str): Column to visualize.
        n_bins (int): Number of bins for the histogram.
        out_left (float, optional): Left boundary to exclude outliers. If None, no line is drawn.
        out_right (float, optional): Right boundary to exclude outliers. If None, no line is drawn.
        color (str): Plot color.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Histogram
    sns.histplot(df[column_name], kde=True, bins=n_bins, color=color, ax=axes[0])
    axes[0].set_title(f"Distribution of {column_name}")
    axes[0].set_xlabel(column_name)
    axes[0].set_ylabel("Frequency")


    # Boxplot
    sns.boxplot(x=df[column_name], color=color, ax=axes[1])
    axes[1].set_title(f"Boxplot of {column_name}")
    axes[1].set_xlabel(column_name)

    # Add vertical lines for outlier boundaries in the boxplot only if values are provided
    if out_left is not None:
        axes[1].axvline(x=out_left, color='red', linestyle='-', linewidth=1)
    if out_right is not None:
        axes[1].axvline(x=out_right, color='red', linestyle='-', linewidth=1)

    plt.tight_layout()
    plt.show()


# Cluster Profiling
def cluster_profiling(df, cluster_labels, cluster_method_name, 
                           figsize=(6, 8), cmap="BrBG", fmt=".2f"):
    """
    Plots a heatmap showing the cluster profiling based on feature means.

    Args:
    - df (DataFrame): The original dataset with numerical features.
    - cluster_labels (array-like): Cluster labels for each data point.
    - cluster_method_name (str): Name of the clustering method (used in the title).
    - figsize (tuple): Size of the plot figure (default: (6, 8)).
    - cmap (str): Colormap for the heatmap (default: "BrBG").
    - fmt (str): String format for heatmap annotations (default: ".2f").
    """
    # Concatenate the cluster labels with the original data
    df_concat = pd.concat([df, pd.Series(cluster_labels, name='labels', index=df.index)], axis=1)
    
    # Group by cluster labels and compute the mean for each feature
    cluster_profile = df_concat.groupby('labels').mean().T
    
    # Create the plot
    fig, ax = plt.subplots(figsize=figsize)

    # Plot the heatmap
    sns.heatmap(cluster_profile, center=0, annot=True, cmap=cmap, fmt=fmt, ax=ax)

    # Set labels and title
    ax.set_xlabel("Cluster Labels")
    ax.set_title(f"Cluster Profiling:\n{cluster_method_name} Clustering")
    
    # Show the plot
    plt.show()

# Counts
def plot_counts(labels):
    """
    Plots a bar chart showing the counts of each cluster label.

    Parameters:
    - labels (array-like): Cluster labels for data points.

    """
    label_counts = pd.Series(labels).value_counts()
    plt.figure(figsize=(8, 6))
    label_counts.plot(kind='bar', color='orange')
    plt.title('Cluster Label Counts')
    plt.xlabel('Cluster Label')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()


## Data Cleaning and Pre-processing
# Function to apply the mode to columns with categorical data
def mode(value):
    # compute the mode
    mode = value.mode()
    if not mode.empty:
        # returns the first mode, if there values that are equally frequent
        return mode[0]
    else:
        # if no frequent value is found, return the first value
        return value.iloc[0] 

# Function to aggregate data based on 'DocIDHash','NameHash' and 'DistributionChannel'
def aggregation(dataframe):
    aggregation_rules = {
        'Nationality': mode,
        'Age': 'median',
        'DaysSinceCreation': 'max',
        'AverageLeadTime': 'mean',
        'LodgingRevenue': 'sum',
        'OtherRevenue': 'sum',
        'BookingsCanceled': 'sum',
        'BookingsNoShowed': 'sum',
        'BookingsCheckedIn': 'sum',
        'PersonsNights': 'sum',
        'RoomNights': 'sum',
        'MarketSegment': mode,
        'SRHighFloor': mode,
        'SRLowFloor': mode,
        'SRAccessibleRoom': mode,
        'SRMediumFloor': mode,
        'SRBathtub': mode,
        'SRShower': mode,
        'SRCrib': mode,
        'SRKingSizeBed': mode,
        'SRTwinBed': mode,
        'SRNearElevator': mode,
        'SRAwayFromElevator': mode,
        'SRNoAlcoholInMiniBar': mode,
        'SRQuietRoom': mode
    }
    
    return dataframe.groupby(['DocIDHash','NameHash','DistributionChannel']).agg(aggregation_rules).reset_index()
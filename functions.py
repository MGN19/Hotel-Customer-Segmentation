import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Define the main color
main_color = '#1c5739'


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
    sns.histplot(df[column], discrete=True, color=main_color, kde=False)
    
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

def plot_multiple_distributions_and_boxplots(df, outliers_dict, color=main_color):
    """
    Plots histograms and box plots for multiple columns in the DataFrame with optional outlier boundaries.
    In each row, there will be two histograms and two box plots from two different variables.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        outliers_dict (dict): Dictionary defining the outlier thresholds and bin settings for each numeric column.
        color (str): Plot color for both histogram and boxplot.
    """
    # List of column names (sorted to match dictionary order)
    columns = list(outliers_dict.keys())
    
    # Number of rows needed (two columns per row)
    num_rows = len(columns) // 2 + len(columns) % 2  # Half the columns, rounded up

    # Create subplots: two columns per row (histogram + boxplot for each column)
    fig, axes = plt.subplots(num_rows, 4, figsize=(18, 3 * num_rows))

    # Iterate over each pair of columns (two per row)
    for i in range(0, len(columns), 2):
        col1 = columns[i]
        col2 = columns[i+1] if i+1 < len(columns) else None  # Check if there's an odd column

        # Get the parameters for both columns (i-th and (i+1)-th columns)
        params_col1 = outliers_dict[col1]
        params_col2 = outliers_dict.get(col2, {'n_bins': 15, 'left_out': None, 'right_out': None})

        # Plot for the first column (col1)
        n_bins1 = params_col1["n_bins"]
        out_left1 = params_col1["left_out"]
        out_right1 = params_col1["right_out"]
        
        # Histogram for col1
        sns.histplot(df[col1], kde=True, bins=n_bins1, color=color, ax=axes[i//2, 0])
        axes[i//2, 0].set_title(f"Distribution of {col1}")
        axes[i//2, 0].set_xlabel(col1)
        axes[i//2, 0].set_ylabel("Frequency")
        
        # Boxplot for col1
        # Boxplot for col1 with filled points for outliers
        sns.boxplot(x=df[col1], color=color, ax=axes[i//2, 1])
        axes[i//2, 1].set_title(f"Boxplot of {col1}")
        axes[i//2, 1].set_xlabel(col1)

        # Add vertical lines for outlier boundaries for col1
        if out_left1 is not None:
            axes[i//2, 1].axvline(x=out_left1, color='red', linestyle='-', linewidth=1, label=f'Left Outlier: {out_left1}')
        if out_right1 is not None:
            axes[i//2, 1].axvline(x=out_right1, color='red', linestyle='-', linewidth=1, label=f'Right Outlier: {out_right1}')
        
        # Add legend to the boxplot for col1 (if vertical lines are added)
        if out_left1 is not None or out_right1 is not None:
            axes[i//2, 1].legend()

        # Plot for the second column (col2) if it exists
        if col2:
            n_bins2 = params_col2["n_bins"]
            out_left2 = params_col2["left_out"]
            out_right2 = params_col2["right_out"]
            
            # Histogram for col2
            sns.histplot(df[col2], kde=True, bins=n_bins2, color=color, ax=axes[i//2, 2])
            axes[i//2, 2].set_title(f"Distribution of {col2}")
            axes[i//2, 2].set_xlabel(col2)
            axes[i//2, 2].set_ylabel("Frequency")
            
            # Boxplot for col2
            sns.boxplot(x=df[col2], color=color, ax=axes[i//2, 3])
            axes[i//2, 3].set_title(f"Boxplot of {col2}")
            axes[i//2, 3].set_xlabel(col2)

            # Add vertical lines for outlier boundaries for col2
            if out_left2 is not None:
                axes[i//2, 3].axvline(x=out_left2, color='red', linestyle='-', linewidth=1, label=f'Left Outlier: {out_left2}')
            if out_right2 is not None:
                axes[i//2, 3].axvline(x=out_right2, color='red', linestyle='-', linewidth=1, label=f'Right Outlier: {out_right2}')
            
            # Add legend to the boxplot for col2 (if vertical lines are added)
            if out_left2 is not None or out_right2 is not None:
                axes[i//2, 3].legend()

    # Adjust layout to prevent overlap
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

# Clusters Exploration
def plot_cluster_sizes(df, cluster_col, color=main_color):
    # Get the count of each cluster
    cluster_counts = df[cluster_col].value_counts().sort_index()
    
    # Create the bar plot with the specified color
    sns.barplot(x=cluster_counts.index, y=cluster_counts.values, color=color)
    
    # Add labels and title
    plt.xlabel('Cluster')
    plt.ylabel('Number of Samples')
    plt.title('Cluster Sizes')
    
    # Show the plot
    plt.show()

def plot_cluster_profiling(df, cluster_column, cluster_method_name, 
                           figsize=(6, 8), cmap="BrBG", fmt=".2f"):
    """
    Plots a heatmap showing the cluster profiling based on feature means.

    Args:
    - df (DataFrame): The original dataset with numerical features.
    - cluster_column (str): The column name containing cluster labels for each data point.
    - cluster_method_name (str): Name of the clustering method (used in the title).
    - figsize (tuple): Size of the plot figure (default: (6, 8)).
    - cmap (str): Colormap for the heatmap (default: "BrBG").
    - fmt (str): String format for heatmap annotations (default: ".2f").
    """
    # Concatenate the cluster labels with the original data
    df_concat = pd.concat([df, pd.Series(df[cluster_column], name='labels', index=df.index)], axis=1)
    
    # Filter for only numeric columns (excluding the cluster label)
    numeric_df = df_concat.select_dtypes(include=['number'])
    
    # Group by cluster labels and compute the mean for each feature
    cluster_profile = numeric_df.groupby(df_concat['labels']).mean().T
    
    # Create the plot
    fig, ax = plt.subplots(figsize=figsize)

    # Plot the heatmap
    sns.heatmap(cluster_profile, center=0, annot=True, cmap=cmap, fmt=fmt, ax=ax)

    # Set labels and title
    ax.set_xlabel("Cluster Labels")
    ax.set_title(f"Cluster Profiling:\n{cluster_method_name} Clustering")
    
    # Show the plot
    plt.show()
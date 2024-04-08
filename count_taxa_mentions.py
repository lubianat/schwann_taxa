import pandas as pd


def count_mentions_sort_and_output_csv(input_file_path, output_file_path):
    name_counts = {}  # Use a dictionary to store name counts

    # Open and read the file
    with open(input_file_path, "r") as file:
        for line in file:
            parts = line.strip().split("\t")
            if len(parts) == 3:
                name = parts[2]
                if name in name_counts:
                    name_counts[name] += 1
                else:
                    name_counts[name] = 1

    # Convert the dictionary to a Pandas DataFrame
    df = pd.DataFrame(list(name_counts.items()), columns=["Name", "Count"])

    # Sort the DataFrame by 'Count' in descending order
    df_sorted = df.sort_values(by="Count", ascending=False)

    # Write the sorted DataFrame to a CSV file
    df_sorted.to_csv(output_file_path, index=False)


# Adjust the file paths as necessary
input_file_path = "/home/lubianat/Documents/lab_related/schwann_taxa/annotations/Microscopical_Researches_manual_curation.ann"
output_file_path = (
    "sorted_name_counts.csv"  # Output file name changed to reflect sorting
)

# Execute the function
count_mentions_sort_and_output_csv(input_file_path, output_file_path)
print(f"Sorted CSV file has been created at {output_file_path} with name counts.")

# storage_estimator.py
# Estimates the total storage needed for a group of files.

num_files = int(input("Enter number of files: "))
avg_size_mb = float(input("Enter average file size in MB: "))

total_mb = num_files * avg_size_mb

print("Total storage:", total_mb, "MB")

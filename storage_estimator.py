# storage_estimator.py
# Estimates the total storage needed for a group of files.

print("=== Storage Estimator ===")

num_files = int(input("Enter number of files: "))
avg_size_mb = float(input("Enter average file size in MB: "))

total_mb = num_files * avg_size_mb

print(f"Total storage: {total_mb:.2f} MB")
print(f"Total storage (GB): {total_mb / 1024:.2f}")

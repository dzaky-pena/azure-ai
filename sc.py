import os

# Start from current directory
directory = "."

# Walk through the directory tree
for root, _, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".md"):
            old_path = os.path.join(root, filename)
            new_filename = filename[:-3] + ".mdx"
            new_path = os.path.join(root, new_filename)

            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} -> {new_path}")

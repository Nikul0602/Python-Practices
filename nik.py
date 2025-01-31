# This is a converted Python file
import os
import magic  # Install with: pip install python-magic

# Set the folder path where your files are located
folder_path = r"D:\Nikul\Python"

# Initialize magic library for file type detection
file_type_checker = magic.Magic(mime=True)

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):  # Check only files
        detected_type = file_type_checker.from_file(file_path)

        # Map detected types to common extensions
        extension_map = {
            "python": ".py",
            "pdf": ".pdf",
            "plain": ".txt",
            "jpeg": ".jpg",
            "png": ".png",
            "zip": ".zip",
            "json": ".json",
            "csv": ".csv"
        }

        # Match detected type with known extensions
        new_extension = None
        for key, ext in extension_map.items():
            if key in detected_type:
                new_extension = ext
                break

        if new_extension:
            new_filename = os.path.splitext(filename)[0] + new_extension
            new_file_path = os.path.join(folder_path, new_filename)

            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")
        else:
            print(f"Unknown file type: {filename} ({detected_type})")

print("File restoration completed!")

# End of converted file
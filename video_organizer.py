# Python script to sort files in a directory by their extension
import os
from shutil import move

def sort_files(directory_path):
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            file_extension = filename.split('.')[-1]
            destination_directory = os.path.join(directory_path, file_extension)
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            move(os.path.join(directory_path, filename), os.path.join(destination_directory, filename))

# Example usage:
if __name__ == "__main__":
    # Specify the path to your video folder
    video_folder_path = "/path/to/your/video/folder"
    sort_files(video_folder_path)
    print("Videos organized successfully!")

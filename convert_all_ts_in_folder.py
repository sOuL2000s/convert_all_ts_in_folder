import os
import subprocess

def convert_all_ts_in_folder(input_folder, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get all .ts files from the input folder
    ts_files = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith(".ts")]

    if not ts_files:
        print("No .ts files found in the folder.")
        return

    for input_file in ts_files:
        # Derive output file name
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(output_dir, f"{base_name}.mp4")

        try:
            subprocess.run(
                ['ffmpeg', '-i', input_file, '-c:v', 'copy', '-c:a', 'copy', output_file],
                check=True
            )
            print(f"Converted: {input_file} -> {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {input_file}: {e}")
        except FileNotFoundError:
            print("ffmpeg is not installed or not found in PATH.")
            return

# Example usage:
input_folder = "D:\Movies\pov"  # Replace with the path to your folder containing .ts files
output_directory = "D:/Movies/converted_videos"  # Directory to save .mp4 files

convert_all_ts_in_folder(input_folder, output_directory)

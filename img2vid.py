import cv2
import os
from glob import glob

def images_to_video(image_dir, output_path, fps=30, image_extension='jpg'):
    """
    Combine photos in a directory into an MP4 video.

    Args:
        image_dir (str): Directory containing images.
        output_path (str): Path to save the output MP4 video.
        fps (int, optional): Frames per second of the output video. Default is 30.
        image_extension (str, optional): Image file extension (e.g., 'jpg', 'png'). Default is 'jpg'.

    Returns:
        None
    """
    # Get list of image files and sort by filename
    image_files = sorted(glob(os.path.join(image_dir, f'*.{image_extension}')))

    if not image_files:
        raise ValueError(f"No images with extension .{image_extension} found in {image_dir}")

    # Read the first image to get dimensions
    first_frame = cv2.imread(image_files[0])
    if first_frame is None:
        raise ValueError("First image could not be read. Check if it is a valid image.")

    height, width, _ = first_frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' is compatible with .mp4 output
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for idx, image_file in enumerate(image_files):
        frame = cv2.imread(image_file)
        if frame is None:
            print(f"Warning: Skipping unreadable image {image_file}")
            continue
        # Resize to match the first frame if necessary
        if frame.shape[:2] != (height, width):
            frame = cv2.resize(frame, (width, height))
        out.write(frame)

    out.release()
    print(f"Video saved to: {output_path}")

# images_to_video(
#     image_dir='path/to/your/images',
#     output_path='output_video.mp4',
#     fps=24,
#     image_extension='jpg'
# )

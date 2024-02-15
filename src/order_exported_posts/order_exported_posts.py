import os
import re
import shutil
from collections import OrderedDict

import arrow

POSTS_DIR = r"C:\Users\RoiHa\OneDrive\Documents\Adobe\Premiere Pro\23.0\export\פוסטים"


def order_posts(order):
    videos = map_post_videos(POSTS_DIR)
    ordered_videos = order__filter_sequences(videos, order)
    output_path = os.path.join(POSTS_DIR, arrow.utcnow().strftime("%d-%m-%Y"))

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Move each file to the destination directory
    for _, video in enumerate(ordered_videos.values()):
        new_filename = str(_) + os.path.basename(video)
        # Construct the new file path
        new_file_path = os.path.join(output_path, new_filename)
        # Move the file
        shutil.move(video, new_file_path)

    print(f"All files have been moved to {output_path}")


def map_post_videos(folder_path):
    sequence_pattern = re.compile(r"Sequence (\d+)(?:_(\d+))?")
    latest_sequences = {}

    for filename in os.listdir(folder_path):
        match = sequence_pattern.search(filename)
        if match:
            sequence_id, version = match.groups()
            version = int(version) if version else 0  # Default version to 0 if not present
            sequence_key = int(sequence_id)  # Convert sequence ID to int for consistent mapping

            # Check if this sequence ID is already encountered and if this version is newer
            if sequence_key not in latest_sequences or latest_sequences[sequence_key][1] < version:
                latest_sequences[sequence_key] = (os.path.join(folder_path, filename), version)

    # Map each sequence ID to the path of the latest version, discarding the version number
    return {seq_id: path for seq_id, (path, _) in latest_sequences.items()}


def order__filter_sequences(latest_sequences, ordered_ids):
    """
    Orders the dictionary of latest sequence paths by the given list of sequence IDs using OrderedDict.

    Parameters:
    - latest_sequences: dict, mapping from sequence ID to the latest path of that sequence.
    - ordered_ids: list, a list of sequence IDs in the desired order.

    Returns:
    - OrderedDict: an ordered dictionary with the sequences ordered according to ordered_ids.
    """
    ordered_sequences = OrderedDict()

    for sequence_id in ordered_ids:
        if sequence_id in latest_sequences:
            ordered_sequences[sequence_id] = latest_sequences[sequence_id]

    return ordered_sequences
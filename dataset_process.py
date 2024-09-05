import os
import random

def split_dataset(dataset_dir, train_ratio=0.8):
  """Splits a dataset into training and validation sets.

  Args:
    dataset_dir: The directory containing the images.
    train_ratio: The ratio of images to be used for training.

  Returns:
    A tuple of lists containing the paths to the training and validation images.
  """

  image_paths = [os.path.join(dataset_dir, image) for image in os.listdir(dataset_dir)]
  random.shuffle(image_paths)

  num_train_images = int(len(image_paths) * train_ratio)

  train_images = image_paths[:num_train_images]
  val_images = image_paths[num_train_images:]

  return train_images, val_images

# Example usage:
train_dir = "train"
val_dir = "val"
dataset_dir = "/Users/carl/Documents/GitHub/LicenseRecognition/dataset/images"

train_images, val_images = split_dataset(dataset_dir)

# Save the image paths to train.txt and val.txt
with open(os.path.join(dataset_dir, "train.txt"), "w") as f:
  for image_path in train_images:
    f.write(image_path + "\n")

with open(os.path.join(dataset_dir, "val.txt"), "w") as f:
  for image_path in val_images:
    f.write(image_path + "\n")

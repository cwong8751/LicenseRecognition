import xml.etree.ElementTree as ET
import os

def convert_xml_to_yolo(xml_file, yolo_file):
  """Converts a single XML annotation file to YOLO format.

  Args:
    xml_file: The path to the XML file.
    yolo_file: The path to the output YOLO file.
  """

  tree = ET.parse(xml_file)
  root = tree.getroot()

  # Assuming your XML structure is similar to VOC format
  width = int(root.find('size').find('width').text)
  height = int(root.find('size').find('height').text)

  with open(yolo_file, 'w') as f:
    for obj in root.findall('object'):
      xmin = int(obj.find('bndbox').find('xmin').text)
      ymin = int(obj.find('bndbox').find('ymin').text)
      xmax = int(obj.find('bndbox').find('xmax').text)
      ymax = int(obj.find('bndbox').find('ymax').text)

      class_id = int(obj.find('license_plate').text)  # Replace with your class mapping

      # Calculate center and dimensions relative to image size
      x_center = (xmin + xmax) / 2.0 / width
      y_center = (ymin + ymax) / 2.0 / height
      w = (xmax - xmin) / width
      h = (ymax - ymin) / height

      f.write(f"{class_id} {x_center} {y_center} {w} {h}\n")

# Example usage
xml_dir = "annotations"
yolo_dir = "labels"

for xml_file in os.listdir(xml_dir):
  if xml_file.endswith(".xml"):
    xml_path = os.path.join(xml_dir, xml_file)
    yolo_path = os.path.join(yolo_dir, xml_file[:-4] + ".txt")
    convert_xml_to_yolo(xml_path, yolo_path)

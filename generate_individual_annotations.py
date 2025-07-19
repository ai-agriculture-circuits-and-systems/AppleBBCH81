import json
import os
import random
import time
from pathlib import Path

def generate_unique_id():
    """Generate 10-digit unique ID with last 3 digits from timestamp"""
    # Generate 7-digit random number
    random_part = random.randint(1000000, 9999999)
    # Get last 3 digits of current timestamp
    timestamp = int(time.time() * 1000) % 1000
    # Combine into 10-digit ID
    unique_id = random_part * 1000 + timestamp
    return unique_id

def get_image_info(image_path):
    """Get image information"""
    from PIL import Image
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            file_size = os.path.getsize(image_path)
            return {
                "width": width,
                "height": height,
                "size": file_size,
                "format": "JPEG"
            }
    except Exception as e:
        print(f"Error reading image {image_path}: {e}")
        return {
            "width": 640,
            "height": 640,
            "size": os.path.getsize(image_path),
            "format": "JPEG"
        }

def yolo_to_coco_bbox(yolo_bbox, img_width, img_height):
    """Convert YOLO format bounding box to COCO format"""
    # YOLO format: [center_x, center_y, width, height] (relative coordinates)
    # COCO format: [x, y, width, height] (absolute coordinates)
    center_x, center_y, width, height = yolo_bbox
    
    # Convert to absolute coordinates
    x = center_x * img_width
    y = center_y * img_height
    w = width * img_width
    h = height * img_height
    
    # Convert to COCO format [x, y, width, height]
    return [x, y, w, h]

def read_yolo_annotations(label_file_path):
    """Read YOLO format annotation file"""
    annotations = []
    try:
        with open(label_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split()
                    if len(parts) == 5:
                        class_id = int(parts[0])
                        center_x = float(parts[1])
                        center_y = float(parts[2])
                        width = float(parts[3])
                        height = float(parts[4])
                        annotations.append({
                            'class_id': class_id,
                            'center_x': center_x,
                            'center_y': center_y,
                            'width': width,
                            'height': height
                        })
    except Exception as e:
        print(f"Error reading label file {label_file_path}: {e}")
    
    return annotations

def create_annotation_template(image_id, category_id, bbox, area):
    """Create annotation template"""
    return {
        "id": generate_unique_id(),
        "image_id": image_id,
        "category_id": category_id,
        "segmentation": [],
        "area": area,
        "bbox": bbox
    }

def generate_individual_json(image_file, output_dir):
    """Generate individual JSON annotation file for single image"""
    # Get image information
    image_path = os.path.join("data/images", image_file)
    image_info = get_image_info(image_path)
    
    # Generate unique IDs
    image_id = generate_unique_id()
    category_id = generate_unique_id()
    
    # Read corresponding label file
    label_filename = os.path.splitext(image_file)[0] + ".txt"
    label_path = os.path.join("data/labels", label_filename)
    
    # Create base template
    template = {
        "info": {
            "description": "data",
            "version": "1.0",
            "year": 2025,
            "contributor": "search engine",
            "source": "augmented",
            "license": {
                "name": "Creative Commons Attribution 4.0 International",
                "url": "https://creativecommons.org/licenses/by/4.0/"
            }
        },
        "images": [
            {
                "id": image_id,
                "width": image_info["width"],
                "height": image_info["height"],
                "file_name": image_file,
                "size": image_info["size"],
                "format": image_info["format"],
                "url": "",
                "hash": "",
                "status": "success"
            }
        ],
        "annotations": [],
        "categories": [
            {
                "id": category_id,
                "name": "AppleBBCH81",
                "supercategory": "apple"
            }
        ]
    }
    
    # Read YOLO annotations and convert to COCO format
    if os.path.exists(label_path):
        yolo_annotations = read_yolo_annotations(label_path)
        
        for yolo_ann in yolo_annotations:
            # Convert bounding box format
            yolo_bbox = [yolo_ann['center_x'], yolo_ann['center_y'], 
                        yolo_ann['width'], yolo_ann['height']]
            coco_bbox = yolo_to_coco_bbox(yolo_bbox, image_info["width"], image_info["height"])
            
            # Calculate area
            area = coco_bbox[2] * coco_bbox[3]  # width * height
            
            # Create annotation
            annotation = create_annotation_template(image_id, category_id, coco_bbox, area)
            template["annotations"].append(annotation)
    else:
        print(f"Warning: Label file not found for {image_file}")
    
    # Save JSON file
    json_filename = os.path.splitext(image_file)[0] + ".json"
    output_path = os.path.join(output_dir, json_filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(template, f, indent=2, ensure_ascii=False)
    
    print(f"Generated: {output_path} with {len(template['annotations'])} annotations")
    return output_path

def main():
    """Main function"""
    # Set paths
    images_dir = "data/images"
    labels_dir = "data/labels"
    output_dir = "data/images"  # Save in same directory as images
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all image files
    image_files = [f for f in os.listdir(images_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    print(f"Found {len(image_files)} images to process...")
    
    # Generate individual JSON files for each image
    for i, image_file in enumerate(image_files, 1):
        print(f"Processing {i}/{len(image_files)}: {image_file}")
        try:
            generate_individual_json(image_file, output_dir)
        except Exception as e:
            print(f"Error processing {image_file}: {e}")
    
    print(f"\nCompleted! Generated {len(image_files)} JSON annotation files.")

if __name__ == "__main__":
    main() 
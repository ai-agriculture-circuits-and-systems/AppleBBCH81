# AppleBBCH81 Dataset

A dataset of apple fruit images captured during the maturity stage (BBCH 81-85) in the LatHort orchard in Dobele, Latvia.

## Dataset Description

The AppleBBCH81 dataset is designed for apple fruit detection and yield estimation tasks. It contains high-resolution images of apple trees captured at specific maturity stages, making it suitable for computer vision, object detection, and deep learning research in agricultural applications.

- **Number of images**: Original images (3008x2000) cropped into 640x640 images
- **Image format**: JPEG, with COCO-format JSON annotations (one JSON per image)
- **Overlap**: 30% between cropped images
- **BBCH stages**: 81-85 (beginning to advanced ripening)

## Dataset Structure

本数据集目录结构如下：

```
data/
  images/
    ├── DSC_1042_17kv1r16k_0.jpg
    ├── DSC_1042_17kv1r16k_0.json
    ├── DSC_1042_17kv1r16k_1.jpg
    ├── DSC_1042_17kv1r16k_1.json
    └── ...
```

- 每张图片（`.jpg`）都对应一个同名的 COCO 格式标注文件（`.json`）。
- 所有图片和标注文件均位于 `data/images/` 目录下。

## JSON 标注结构说明

每个 JSON 文件均为 COCO 格式，结构如下（以 `DSC_1042_17kv1r16k_0.json` 为例）：

```json
{
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
      "id": 3103704321,
      "width": 640,
      "height": 640,
      "file_name": "DSC_1042_17kv1r16k_0.jpg",
      "size": 56204,
      "format": "JPEG",
      "url": "",
      "hash": "",
      "status": "success"
    }
  ],
  "annotations": [
    {
      "id": 8937340322,
      "image_id": 3103704321,
      "category_id": 3248230321,
      "segmentation": [],
      "area": 5160.03,
      "bbox": [197.67, 222.03, 76.47, 67.48]
    },
    ...
  ],
  "categories": [
    {
      "id": 3248230321,
      "name": "AppleBBCH81",
      "supercategory": "apple"
    }
  ]
}
```

**字段说明：**

- `info`：数据集的基本信息，包括描述、版本、年份、贡献者、来源和许可证。
- `images`：图片信息列表。每个图片对象包含：
  - `id`：图片唯一 ID（10 位数字，含时间戳后缀）
  - `width`/`height`：图片宽高（像素）
  - `file_name`：图片文件名
  - `size`：图片文件大小（字节）
  - `format`：图片格式
  - 其他字段如 `url`、`hash`、`status` 供扩展使用
- `annotations`：标注信息列表。每个标注对象包含：
  - `id`：标注唯一 ID（10 位数字，含时间戳后缀）
  - `image_id`：对应图片的 ID
  - `category_id`：类别 ID
  - `segmentation`：分割信息（本数据集为空数组）
  - `area`：目标区域面积（像素^2）
  - `bbox`：目标边界框，格式为 `[x_min, y_min, width, height]`，均为浮点数，单位为像素
- `categories`：类别信息列表。每个类别对象包含：
  - `id`：类别 ID
  - `name`：类别名称（本数据集为 "AppleBBCH81"）
  - `supercategory`：上级类别（本数据集为 "apple"）

## Data Collection

- **Location**: LatHort orchard in Dobele, Latvia
- **Timing**: During fruit and seed maturity (BBCH stage 81-85)
- **Annotation tool**: makesense.ai
- **Validation**: Manual validation of cropped images

## Applications

This dataset can be used for:
- Apple fruit detection
- Yield estimation
- Object detection
- Computer vision research
- Deep learning model training
- Agricultural AI applications

## Categories

- Computer Science
- Artificial Intelligence
- Computer Vision
- Object Detection
- Machine Learning
- Agriculture
- Deep Learning
- Yield Estimation
- Precision Agriculture

## Citation

```
Kodors, S., Zarembo, I., Lācis, G., Litavniece, L., Apeināns, I., Sondors, M., & Pacejs, A. (2024). Autonomous Yield Estimation System for Small Commercial Orchards Using UAV and AI. Drones, 8(12), 734. https://doi.org/10.3390/drones8120734
```

## License

This dataset is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

## Source

The dataset is available at:
- [Kaggle Dataset](https://www.kaggle.com/datasets/projectlzp201910094/applebbch81)
- [Papers with Code](https://paperswithcode.com/dataset/applebbch81) 
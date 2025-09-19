# LLM_work1

## 项目简介
这是一个命令行工具项目，用于为图片添加水印。工具会读取图片的 EXIF 信息中的拍摄时间，并将其作为水印添加到图片上。

## 功能特性
- 自动读取图片的 EXIF 信息，提取拍摄时间。
- 支持用户自定义水印的字体大小、颜色和位置。
- 生成的新图片会保存在原目录的子目录中，目录名为原目录名加后缀 `_watermark`。

## 使用方法

### 环境依赖
- Python 3.10+
- 依赖库：
  - Pillow
  - piexif

### 安装依赖
运行以下命令安装所需依赖：
```bash
pip install Pillow piexif
```

### 运行工具
运行以下命令启动工具：
```bash
python image_watermark_tool.py <图片目录路径> [--font-size 字体大小] [--font-color 字体颜色] [--position 水印位置]
```

#### 可选参数
- `--font-size`：设置字体大小（默认值：20）。
- `--font-color`：设置字体颜色（默认值：black）。
- `--position`：设置水印位置，可选值为 `top-left`、`center`、`bottom-right`（默认值：bottom-right）。

### 示例
假设图片存放在 `photo` 目录下，运行以下命令：
```bash
python image_watermark_tool.py photo --font-size 30 --font-color red --position center
```
生成的图片将保存在 `photo_watermark` 目录下。

## 项目结构
```
LLM_work1/
├── image_watermark_tool.py  # 主程序
├── photo/                  # 示例图片目录
├── photo_watermark/        # 生成的水印图片目录
├── PRD.md                  # 产品需求文档
└── README.md               # 项目说明文件
```

## 未来计划
- 支持更多的水印样式（如图片水印）。
- 支持批量处理多个目录。
- 提供图形用户界面（GUI）。
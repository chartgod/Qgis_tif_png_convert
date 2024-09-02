readme_content = """
# 🎨 QGIS TIFF to PNG Converter 🗺️

Welcome to the **QGIS TIFF to PNG Converter**! This script is your go-to tool for converting TIFF files into PNG format with the power of QGIS and PyQt5. Whether you're working with satellite imagery or any other raster data, this script will streamline your workflow. 🚀

## 🔧 Prerequisites

Before you begin, make sure you have the following installed on your system:

- **QGIS**: The script leverages the QGIS Python API (`qgis.core`).
- **PyQt5**: For handling image operations and rendering.

## 📥 Installation

1. **Clone this repository**:
    ```bash
    git clone https://github.com/chartgod/qgis_tif_png_convert.git
    cd qgis_tif_png_convert
    ```

2. **Install the required Python packages**:
    You may need to install the PyQt5 package if it is not already installed:
    ```bash
    pip install PyQt5
    ```

3. **Configure QGIS Python environment**:
    Ensure your Python environment is set up to use the QGIS Python API. This typically involves setting the `PYTHONPATH` to point to the QGIS Python directory.

## 🚀 Usage

1. **Set your input and output directories**:
    Define the paths to your TIFF files and the desired output location for the PNG files.

    ```python
    input_dir = r"D:\\Your\\Path\\To\\TIFF_Files"
    output_dir = r"D:\\Your\\Path\\To\\Save_PNG_Files"
    ```

2. **Run the script**:
    Execute the script with your Python interpreter. The script will convert all `.tif` and `.tiff` files in the `input_dir` to PNG format and save them in the `output_dir`.

    ```bash
    python convert_tiff_to_png.py
    ```

## 🎯 Example

Here’s a quick example:

```python
input_dir = r"D:\\NationalSatellite\\tiff_dataset"
output_dir = r"D:\\NationalSatellite\\tiff_dataset\\PNG_Converted"

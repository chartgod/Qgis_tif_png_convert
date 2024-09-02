# qgis_tif_png_convert
readme_content = """
# QGIS TIFF to PNG Converter

This script is designed to convert TIFF files to PNG format using QGIS and PyQt5. It processes all TIFF files in a specified input directory and saves the converted PNG files in a specified output directory.

## Prerequisites

Before running this script, ensure that the following are installed on your system:

- **QGIS**: QGIS must be installed on your system. The script relies on the QGIS Python API (`qgis.core`).
- **PyQt5**: The script uses PyQt5 for handling image processing.

## Installation

1. **Clone this repository**:
    ```bash
    git clone https://github.com/chartgod/qgis_tif_png_convert.git
    cd qgis_tif_png_convert
    ```

2. **Install the required Python packages**:
    You may need to install the PyQt5 package if it is not already installed.
    ```bash
    pip install PyQt5
    ```

3. **Set up QGIS Python environment**:
    Make sure your Python environment is configured to use the QGIS Python API. This typically involves setting the `PYTHONPATH` to point to the QGIS Python directory.

## Usage

1. **Configure input and output directories**:
    In the script, set the `input_dir` and `output_dir` variables to point to your source TIFF files directory and the destination PNG files directory, respectively.

    ```python
    input_dir = r"D:\\Your\\Path\\To\\TIFF_Files"
    output_dir = r"D:\\Your\\Path\\To\\Save_PNG_Files"
    ```

2. **Run the script**:
    Execute the script using your Python interpreter. The script will convert all `.tif` and `.tiff` files in the `input_dir` to PNG format and save them in the `output_dir`.

    ```bash
    python convert_tiff_to_png.py
    ```

## Example

Here’s a quick example of what the script does:

```python
input_dir = r"D:\\NationalSatellite\\tiff_dataset"
output_dir = r"D:\\NationalSatellite\\tiff_dataset\\PNG_Converted"

# TIFF files in the input directory will be converted to PNG and saved in the output directory.


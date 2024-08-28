# tcx2gpx

# TCX to GPX Converter

This Python script converts Garmin TCX files to GPX format. The script processes a directory of `.tcx` files and generates corresponding `.gpx` files in the same directory.

## Features

- **Batch Processing:** Converts all `.tcx` files in a specified directory to `.gpx` files.
- **Data Extraction:** Extracts latitude, longitude, elevation, and time information from TCX files and formats them into the GPX standard.
- **Clean XML Handling:** Ensures that the XML content from the TCX files is clean and well-formed before processing.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- `lxml` library (for XML processing)

You can install the `lxml` library using pip:

```bash
pip install lxml
```

## How to Use

1. **Clone the Repository:**

   Clone the repository to your local machine.

   ```bash
   git clone https://github.com/yourusername/tcx-to-gpx-converter.git
   cd tcx-to-gpx-converter
   ```

2. **Run the Script:**

   Execute the script by running the following command:

   ```bash
   python tcx_to_gpx.py
   ```

   You will be prompted to enter the directory containing your `.tcx` files.

3. **Provide Directory Path:**

   Input the full path to the directory that contains the `.tcx` files you wish to convert. The script will process each `.tcx` file in the directory and create a corresponding `.gpx` file.

4. **Check the Output:**

   The `.gpx` files will be saved in the same directory as the `.tcx` files, with the same base name.

## Example

If you have a directory `/path/to/tcx_files/` containing `activity1.tcx` and `activity2.tcx`, after running the script, you will find:

- `/path/to/tcx_files/activity1.gpx`
- `/path/to/tcx_files/activity2.gpx`

## Error Handling

If the script encounters any errors while processing a file, it will print an error message and continue processing the next file.

## Contributing

Feel free to submit issues or fork this repository and submit pull requests to improve the script.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

This README provides instructions on how to install and use the script, as well as an overview of its functionality. Feel free to customize this document to suit your specific needs.

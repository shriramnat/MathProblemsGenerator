Simple Math Worksheet Generator for Infants (Addition & Subtraction)

This Python script generates multiple unique PDF worksheets designed for infants or young children learning basic one- and two-digit addition and subtraction. It is built to create print-ready documents with a clear, large font and a predictable layout.

✨ Features

Batch Generation: Generates 10 unique PDF worksheets in a single run.

Problem Count: Each worksheet contains 100 randomized problems.

Responsive Layout: Problems are arranged in a 2-column layout with no serial numbering.

Print-Ready Pages: Each PDF file is paginated to contain exactly 20 problems per page (resulting in 5 pages per worksheet).

Safe Math: All problems ensure the sum is less than or equal to 20 and subtraction results are non-negative.

Aesthetics: Uses a 16pt bold font and centered alignment for optimal readability.

🛠️ Prerequisites

You must have Python 3 installed on your system.

This script relies on the ReportLab library to handle PDF generation.

🚀 Setup and Installation

(Optional but Recommended) Create a Virtual Environment:

python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate      # On Windows


Install ReportLab:
Install the necessary library using pip:

pip install reportlab


📄 Usage

Save the Script: Save the Python code as math_worksheet_generator.py.

Run the Script: Execute the file from your terminal:

python3 math_worksheet_generator.py


Output

Upon successful execution, the script will generate 10 PDF files in the same directory:

SimpleMathWorksheet_1.pdf

SimpleMathWorksheet_2.pdf

...

SimpleMathWorksheet_10.pdf

⚙️ Customization

You can easily adjust the parameters inside the script (math_worksheet_generator.py) under the if __name__ == "__main__": block:

Variable Name

Default Value

Description

NUM_WORKSHEETS

10

The number of unique PDF files to generate.

PROBLEM_COUNT

100

The total number of problems per worksheet (must be a multiple of 20 for perfect pagination).

You can also modify the global configuration at the top of the file:

Variable Name

Default Value

Description

MAX_SUM

20

The maximum possible result for addition problems and the maximum starting number for subtraction.

MIN_DIFFERENCE

0

Ensures subtraction problems do not result in a negative number.

# Math Problems Worksheet Generator

A Python script that generates customizable PDF worksheets containing simple addition and subtraction problems designed for young learners. This tool creates print-ready educational materials with clean formatting and intelligent problem generation.

## 🎯 Overview

This script generates multiple unique PDF worksheets featuring randomized math problems suitable for children learning basic arithmetic. Each worksheet is carefully designed with age-appropriate problem difficulty, clear formatting, and optimal page layout for printing and distribution.

## ✨ Key Features

### 📚 Educational Design
- **Age-Appropriate Problems**: Addition problems with sums ≤ 20, subtraction with non-negative results
- **Randomized Content**: Each worksheet contains unique, randomly generated problems
- **Progressive Difficulty**: Mix of one-digit and two-digit number combinations
- **Answer Blanks**: Properly formatted answer lines for student responses

### 📄 Professional Layout
- **Multi-Page Format**: Each worksheet spans exactly 5 pages with 20 problems per page
- **Two-Column Design**: Optimal space utilization with balanced problem distribution
- **Clear Typography**: 16pt Helvetica Bold font for excellent readability
- **Print-Ready**: Standard letter size with appropriate margins (0.5 inches)
- **Consistent Spacing**: 18pt bottom padding between problems for clarity

### 🔧 Batch Processing
- **Bulk Generation**: Creates 10 unique worksheets in a single execution
- **Automatic Naming**: Sequential file naming (SimpleMathWorksheet_1.pdf, etc.)
- **Progress Tracking**: Real-time generation progress display
- **Error Handling**: Robust problem generation with validation

## 🛠️ Technical Requirements

### System Prerequisites
- **Python 3.6+**: Modern Python installation required
- **ReportLab Library**: Professional PDF generation toolkit

### Dependencies
```bash
reportlab>=3.5.0
```

## 🚀 Installation & Setup

### 1. Environment Setup (Recommended)
```bash
# Create virtual environment
python -m venv math_worksheets_env

# Activate environment
# Windows:
math_worksheets_env\Scripts\activate
# macOS/Linux:
source math_worksheets_env/bin/activate
```

### 2. Install Dependencies
```bash
pip install reportlab
```

### 3. Download Script
Save the `mathproblems.py` file to your desired directory.

## 📖 Usage Guide

### Basic Execution
```bash
python mathproblems.py
```

### Expected Output
```
Generating Worksheet 1 of 10...
Successfully generated worksheet: SimpleMathWorksheet_1.pdf
Generating Worksheet 2 of 10...
Successfully generated worksheet: SimpleMathWorksheet_2.pdf
...
All 10 worksheets have been successfully generated.
```

### Generated Files
- `SimpleMathWorksheet_1.pdf` through `SimpleMathWorksheet_10.pdf`
- Each file contains 100 problems across 5 pages
- Ready for immediate printing and distribution

## ⚙️ Configuration Options

### Primary Settings (Modify in `if __name__ == "__main__":` block)

| Variable | Default | Description | Valid Range |
|----------|---------|-------------|-------------|
| `NUM_WORKSHEETS` | 10 | Number of unique PDF files generated | 1-100+ |
| `PROBLEM_COUNT` | 100 | Total problems per worksheet | Multiple of 20 |
| `BASE_FILE_NAME` | "SimpleMathWorksheet" | Prefix for generated files | Any valid filename |

### Advanced Configuration (Global constants)

| Variable | Default | Description | Impact |
|----------|---------|-------------|---------|
| `MAX_SUM` | 20 | Maximum result for addition problems | Controls difficulty ceiling |
| `MIN_DIFFERENCE` | 0 | Minimum subtraction result | Prevents negative answers |

### Layout Constants

| Variable | Default | Description |
|----------|---------|-------------|
| `PROBLEMS_PER_PAGE` | 20 | Problems per page (10 rows × 2 columns) |
| Page margins | 0.5 inches | All sides margin for printing |
| Column width | 3.5 inches | Each column width |

## 🧮 Problem Generation Logic

### Addition Problems
- **Operand Range**: 1-10 for each number
- **Sum Constraint**: Total must not exceed `MAX_SUM` (20)
- **Re-generation**: Automatic retry if constraints violated
- **Format**: `num1 + num2 = _____`

### Subtraction Problems
- **Minuend Range**: 10 to `MAX_SUM` (20)
- **Subtrahend Range**: 1-9
- **Result Constraint**: Always non-negative
- **Auto-correction**: Swaps operands if needed
- **Format**: `num1 - num2 = _____`

## 📐 Worksheet Structure

### Page Layout
```
┌─────────────────────────────────────┐
│     Simple Addition and            │
│     Subtraction Worksheet          │
│                                    │
│  Problem 1    │   Problem 2       │
│  Problem 3    │   Problem 4       │
│      ...      │      ...          │
│  Problem 19   │   Problem 20      │
└─────────────────────────────────────┘
```

### File Organization
- **Pages per worksheet**: 5
- **Problems per page**: 20 (10 rows × 2 columns)
- **Total problems**: 100
- **Page breaks**: Automatic between pages

## 🎨 Customization Examples

### Generate More Worksheets
```python
NUM_WORKSHEETS = 25  # Generate 25 worksheets instead of 10
```

### Increase Problem Difficulty
```python
MAX_SUM = 30  # Allow sums up to 30
```

### Fewer Problems per Worksheet
```python
PROBLEM_COUNT = 60  # 3 pages with 20 problems each
```

### Custom File Naming
```python
BASE_FILE_NAME = "MathPractice_Grade1"
# Generates: MathPractice_Grade1_1.pdf, etc.
```

## 🐛 Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'reportlab'"**
```bash
pip install reportlab
```

**"Permission denied" when generating PDFs**
- Ensure the directory is writable
- Close any open PDF files with the same names
- Run with appropriate file permissions

**Incorrect page count**
- Ensure `PROBLEM_COUNT` is a multiple of 20
- Check that `PROBLEMS_PER_PAGE` hasn't been modified

### Validation
The script includes built-in validation for:
- Problem generation constraints
- PDF creation success
- File naming conflicts

## 📝 Code Structure

### Main Functions

**`generate_simple_problem()`**
- Generates individual math problems
- Enforces difficulty constraints
- Returns formatted problem strings

**`create_worksheet_pdf(filename, problem_list)`**
- Creates PDF documents using ReportLab
- Handles pagination and layout
- Applies consistent styling

### Workflow
1. Generate random problems for each worksheet
2. Create PDF with proper formatting and pagination
3. Save with sequential naming
4. Repeat for specified number of worksheets

## 📄 License

This project is open source and available under standard educational use permissions.

## 🤝 Contributing

Feel free to fork, modify, and enhance this script for your specific educational needs. Suggestions for improvements are welcome!

## 📞 Support

For issues or questions about this math worksheet generator, please refer to the troubleshooting section above or review the well-documented source code.

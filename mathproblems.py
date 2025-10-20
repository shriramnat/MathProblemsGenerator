import random
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
# Added PageBreak to the import list
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.units import inch

# --- Configuration ---
PROBLEM_COUNT = 100 # Total problems per single worksheet (100 problems / 5 pages)
MAX_SUM = 20
MIN_DIFFERENCE = 0 # Ensure no negative results

def generate_simple_problem():
    """Generates a single addition or subtraction problem suitable for young learners."""
    operator = random.choice(['+', '-'])

    if operator == '+':
        # Addition: Keep numbers small so sum <= MAX_SUM (20)
        # Using a maximum operand of 10 to keep the sum manageable
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        # Re-roll if the sum is too large
        while num1 + num2 > MAX_SUM:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        
    else: # Subtraction
        # Subtraction: Ensure the result is non-negative (num1 >= num2)
        # We ensure num1 is larger, and num2 is small
        num1 = random.randint(10, MAX_SUM) # Start with a larger number
        num2 = random.randint(1, 9)       # Subtract a small number
        # Swap if necessary to guarantee a non-negative result
        if num1 < num2:
            num1, num2 = num2, num1
        
        # We ensure the difference is not negative
        while num1 - num2 < MIN_DIFFERENCE:
             num1 = random.randint(10, MAX_SUM)
             num2 = random.randint(1, 9)
             if num1 < num2:
                num1, num2 = num2, num1


    # Format the problem string clearly with space for the answer
    # {:2d} ensures alignment for 1 and 2-digit numbers
    return f"{num1:2d} {operator} {num2:2d} = _____"

def create_worksheet_pdf(filename, problem_list):
    """Creates the PDF worksheet using reportlab, chunking problems into pages."""

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=inch * 0.5,
        rightMargin=inch * 0.5,
        topMargin=inch * 0.5,
        bottomMargin=inch * 0.5
    )
    
    elements = []

    # Get standard styles and set up a custom style for the problems
    styles = getSampleStyleSheet()
    
    # Set the main title to be centered
    styles['Title'].alignment = 1 # Center

    problem_style = styles['Normal']
    problem_style.fontName = 'Helvetica-Bold'
    problem_style.fontSize = 16
    problem_style.alignment = 1 

    # Add a title header (only once)
    title = Paragraph("Simple Addition and Subtraction Worksheet", styles['Title'])
    elements.append(title)
    elements.append(Paragraph("<br/>", styles['Normal']))

    # --- Pagination Logic ---
    PROBLEMS_PER_PAGE = 20
    
    # Iterate through the entire problem list in steps of 20 (for page breaks)
    for page_start in range(0, len(problem_list), PROBLEMS_PER_PAGE):
        
        # Get the problems for the current page
        page_problems = problem_list[page_start:page_start + PROBLEMS_PER_PAGE]
        table_data = []

        # Iterate through the current page's problems, grouping them into rows of 2
        for i in range(0, len(page_problems), 2):
            
            # Column 1
            col1_content = page_problems[i]
            col1 = Paragraph(col1_content, problem_style)
            
            # Column 2 (Check if there is a second problem for this row)
            if i + 1 < len(page_problems):
                col2_content = page_problems[i+1]
                col2 = Paragraph(col2_content, problem_style)
            else:
                col2 = Paragraph("", problem_style)
            
            table_data.append([col1, col2])

        # Create the Table object for this page (10 rows, 2 columns)
        table = Table(table_data, colWidths=[3.5*inch, 3.5*inch])

        # Style the table
        table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 18), # Space between problems
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 16),
        ]))
        
        elements.append(table)
        
        # Add a PageBreak if this is not the last page of problems
        if page_start + PROBLEMS_PER_PAGE < len(problem_list):
            elements.append(PageBreak())

    # Build the PDF document
    doc.build(elements)

    print(f"Successfully generated worksheet: {filename}")


if __name__ == "__main__":
    NUM_WORKSHEETS = 10
    BASE_FILE_NAME = "SimpleMathWorksheet"

    # Loop to generate 10 unique worksheets
    for i in range(1, NUM_WORKSHEETS + 1):
        
        # 1. Generate a new, random set of problems for this worksheet
        problems = [generate_simple_problem() for _ in range(PROBLEM_COUNT)]
        
        # 2. Create a unique filename (e.g., SimpleMathWorksheet_1.pdf)
        current_file_name = f"{BASE_FILE_NAME}_{i}.pdf"
        
        # 3. Create the PDF
        print(f"Generating Worksheet {i} of {NUM_WORKSHEETS}...")
        create_worksheet_pdf(current_file_name, problems)

    print("\nAll 10 worksheets have been successfully generated.")


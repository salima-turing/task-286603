import subprocess
import tempfile
import html

def generate_mypy_html_report(code: str) -> str:
    # Create a temporary file to store the code
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp_file:
        temp_file.write(code.encode('utf-8'))
        temp_file_path = temp_file.name

    # Run mypy on the temporary file
    try:
        result = subprocess.run(
            ['mypy', temp_file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
    finally:
        # Clean up the temporary file
        import os
        os.remove(temp_file_path)

    # Parse the mypy output
    output_lines = result.stdout.splitlines()
    errors = []
    for line in output_lines:
        if line.strip():
            errors.append(html.escape(line))

    # Generate HTML report
    html_report = """
    <html>
    <head>
        <title>Mypy Type Checker Report</title>
        <style>
            body { font-family: Arial, sans-serif; }
            .error { color: red; }
            pre { background-color: #f8f8f8; padding: 10px; border: 1px solid #ddd; }
        </style>
    </head>
    <body>
        <h1>Mypy Type Checker Report</h1>
        <pre class="error">
    """

    if errors:
        html_report += "\n".join(errors)
    else:
        html_report += "No type violations found."

    html_report += """
        </pre>
    </body>
    </html>
    """

    return html_report

# Example usage
code = """
def add(a: int, b: int) -> int:
    return a + b

result = add(1, '2')
"""

html_report = generate_mypy_html_report(code)
print(html_report)

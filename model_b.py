import html

def generate_mypy_html_report(mypy_output):
    report = """
    <html>
    <head>
        <title>Mypy Type Checker Report</title>
        <style>
            table {
                width: 80%;
                margin: 0 auto;
                border-collapse: collapse;
            }

            th, td {
                padding: 8px;
                border: 1px solid #ddd;
                text-align: left;
            }

            tr:nth-child(even){background-color: #f2f2f2;}
        </style>
    </head>
    <body>
        <h1>Mypy Type Checker Report</h1>
        <table>
            <tr>
                <th>File</th>
                <th>Line</th>
                <th>Column</th>
                <th>Error Message</th>
            </tr>
    """

    errors = mypy_output.splitlines()
    for error in errors:
        if error.startswith('error:'):
            parts = error.split(':', 3)
            if len(parts) == 4:
                file_path, line, col, message = parts
                report += f"""
                    <tr>
                        <td>{file_path}</td>
                        <td>{line}</td>
                        <td>{col}</td>
                        <td>{message}</td>
                    </tr>
                """

    report += """
        </table>
    </body>
    </html>
    """
    return report


# Example usage:
mypy_output = """
test.py:1:1: error: Module 'test' has no attribute 'foo'
test.py:3:9: error: Argument 1 to "bar" has incompatible type "int"; expected "str"
"""
html_report = generate_mypy_html_report(mypy_output)
with open('mypy_report.html', 'w', encoding='utf-8') as file:
    file.write(html_report)

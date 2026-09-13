import os
import pandas as pd
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

file_name = input("Enter path to your CSV file: ")

try:
    df = pd.read_csv(file_name)
except FileNotFoundError:
    print(f"Error: file {file_name} not found. Please check the path and try again.")
    exit()
data_as_text = df.to_string()

prompt = f"""You are a data analyst. Based on the CSV data below, write a
narrative report summarizing key findings, trends, and any notable patterns
or anomalies in the data.

Format your entire response as a complete, valid HTML document (including
<!DOCTYPE html>, <html>, <head>, and <body> tags). Use headings, paragraphs,
bold text, and bullet points where appropriate to make the report readable
and well-structured. Do not include any text outside the HTML document —
your response should start with <!DOCTYPE html> and contain nothing else.

Data:
{data_as_text}"""

try:
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}]
    )

    report_html = response.content[0].text

    output_file_name = "report.html"
    with open(output_file_name, "w", encoding="utf-8") as f:
        f.write(report_html)
    print(f"Report saved as '{output_file_name}'")

except Exception as e:
    print(f"Failed to generate report due to {e}")
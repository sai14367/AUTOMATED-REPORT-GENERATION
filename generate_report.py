import csv
from fpdf import FPDF
import statistics

# Load data from CSV
def read_csv(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({"Name": row["Name"], "Score": int(row["Score"])})
    return data

# Analyze the data
def analyze_data(data):
    scores = [entry["Score"] for entry in data]
    return {
        "Average": round(statistics.mean(scores), 2),
        "Highest": max(scores),
        "Lowest": min(scores),
        "Count": len(scores)
    }

# PDF Generator class
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Student Score Report", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_summary(self, summary):
        self.set_font("Arial", "", 12)
        self.ln(10)
        self.cell(0, 10, "Summary Statistics:", ln=True)
        for key, value in summary.items():
            self.cell(0, 10, f"{key}: {value}", ln=True)

    def add_table(self, data):
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(60, 10, "Name", border=1)
        self.cell(40, 10, "Score", border=1)
        self.ln()
        self.set_font("Arial", "", 12)
        for row in data:
            self.cell(60, 10, row["Name"], border=1)
            self.cell(40, 10, str(row["Score"]), border=1)
            self.ln()

def generate_pdf(data, summary, output_file="report.pdf"):
    pdf = PDFReport()
    pdf.add_page()
    pdf.add_summary(summary)
    pdf.add_table(data)
    pdf.output(output_file)
    print(f"PDF report generated: {output_file}")

# Main execution
if __name__ == "__main__":
    file_path = "C:/sai/.vscode/portfolio-website/PDF_Report_Generator/sample_data.csv"

    data = read_csv(file_path)
    summary = analyze_data(data)
    generate_pdf(data, summary)

from latex_generator import *

def create_latex_document(table_data, image_path):
    return (
        "\\documentclass{article}\n"
        "\\usepackage{graphicx}\n"
        "\\begin{document}\n\n"
        "\\section*{Table}\n" + generate_latex_table(table_data) + "\n\n"
        "\\section*{Image}\n" + generate_latex_image(image_path) + "\n"
        "\\end{document}"
    )

def save_latex_to_file(latex_code, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(latex_code)

def main():
    table_data = [
        ["Name", "Age", "City"],
        ["Alice", 30, "Moscow"],
        ["Bob", 25, "New York"],
        ["Charlie", 35, "London"]
    ]

    image_path = "./artifacts/image2.png"
    save_latex_to_file(create_latex_document(table_data, image_path), "document_with_table_and_image.tex")

if __name__ == "__main__":
    main()

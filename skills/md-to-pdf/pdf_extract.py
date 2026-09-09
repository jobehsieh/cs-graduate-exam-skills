import sys
import fitz

def extract(path, max_pages=4):
    doc = fitz.open(path)
    out = []
    n = min(len(doc), max_pages)
    for i in range(n):
        page = doc[i]
        text = page.get_text("text")
        out.append(f"===== PAGE {i+1} =====")
        out.append(text)
    doc.close()
    return "\n".join(out)

if __name__ == "__main__":
    path = sys.argv[1]
    maxp = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    print(extract(path, maxp))
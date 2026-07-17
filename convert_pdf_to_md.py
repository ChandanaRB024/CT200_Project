import pymupdf4llm

# Convert Version 1
md_text = pymupdf4llm.to_markdown("data/ct200_manual.pdf")

with open("data/ct200_manual.md", "w", encoding="utf-8") as f:
    f.write(md_text)

print("Version 1 converted successfully!")

# Convert Version 2
md_text = pymupdf4llm.to_markdown("data/ct200_manual_v2.pdf")

with open("data/ct200_manual_v2.md", "w", encoding="utf-8") as f:
    f.write(md_text)

print("Version 2 converted successfully!")
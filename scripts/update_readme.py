import json
import os
import re

def clean_text(text):
    """
    清理文本中的换行符、多余的空格和特殊字符。
    """
    if not text:
        return ""
    # 替换换行符为空格
    text = text.replace("\n", " ").replace("\r", " ")
    # 去除多余的空格
    text = re.sub(r"\s+", " ", text).strip()
    # 替换可能破坏表格的字符
    text = text.replace("|", "&#124;")  # 替换 | 为 HTML 实体
    text = text.replace("-", "&#45;")   # 替换 - 为 HTML 实体
    return text

# 检查是否有论文数据
if os.path.exists("papers/all_papers.json") and os.path.getsize("papers/all_papers.json") > 0:
    with open("papers/all_papers.json", "r") as f:
        papers = json.load(f)
    
    # 生成 Markdown 内容
    markdown = "# SNN Accelerator Design Papers\n\n"
    markdown += "Automatically updated list of papers.\n\n"
    markdown += "| Title | Abstract | Link | Source | Date |\n"
    markdown += "|-------|----------|------|--------|------|\n"

    for paper in papers:
        title = clean_text(paper.get("title", ""))
        abstract = clean_text(paper.get("abstract", "No abstract available"))
        link = paper.get("link", "")
        source = paper.get("source", "")
        date = paper.get("date", "")
        
        markdown += f"| {title} | {abstract} | [Link]({link}) | {source} | {date} |\n"

    # 写入 README.md
    with open("README.md", "w") as f:
        f.write(markdown)
    print("README updated successfully!")
    
    # 确保 docs 目录存在
    os.makedirs("docs", exist_ok=True)

    # 写入 docs/index.md
    with open("docs/index.md", "w") as f:
        f.write(markdown)
    print("docs/index.md updated successfully!")
else:
    print("No new papers to update in README.")

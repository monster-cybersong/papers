import json
import os

# 加载各平台的论文
papers = []

# 检查并加载 arXiv 论文
if os.path.exists("papers/arxiv_papers.json") and os.path.getsize("papers/arxiv_papers.json") > 0:
    with open("papers/arxiv_papers.json", "r") as f:
        try:
            arxiv_papers = json.load(f)
            papers.extend(arxiv_papers)
        except json.JSONDecodeError:
            print("Warning: arxiv_papers.json is empty or malformed. Skipping.")

# 检查并加载 IEEE 论文
#if os.path.exists("papers/ieee_papers.json") and os.path.getsize("papers/ieee_papers.json") > 0:
#    with open("papers/ieee_papers.json", "r") as f:
#        try:
#            ieee_papers = json.load(f)
#            papers.extend(ieee_papers)
#        except json.JSONDecodeError:
#            print("Warning: ieee_papers.json is empty or malformed. Skipping.")

# 检查并加载 Springer 论文
#if os.path.exists("papers/springer_papers.json") and os.path.getsize("papers/springer_papers.json") > 0:
#    with open("papers/springer_papers.json", "r") as f:
#        try:
#            springer_papers = json.load(f)
#            papers.extend(springer_papers)
#        except json.JSONDecodeError:
#            print("Warning: springer_papers.json is empty or malformed. Skipping.")

# 如果没有新论文，则不生成文件
if len(papers) > 0:
    with open("papers/all_papers.json", "w") as f:
        json.dump(papers, f, indent=4)
    print("All papers merged successfully!")
else:
    print("No new papers to merge.")
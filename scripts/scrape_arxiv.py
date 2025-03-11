import requests
import json
from datetime import datetime

# 定义多个关键词
keywords = [
    "AIGC",
    "Transformer",
    "Diffusion",
    "LLM"
]

# 构建查询参数
query = ' OR '.join([f'all:"{keyword}"' for keyword in keywords])
query += ' AND ("accelerator" OR "FPGA")'

# 设置时间范围（2023 年以后的论文）
start_date = "2023-01-01"
url = f"http://export.arxiv.org/api/query?search_query={query}&submittedDate={start_date}&start=0&max_results=50"

# 发送请求
response = requests.get(url)
if response.status_code == 200:
    feed = response.text
    papers = []
    for entry in feed.split('<entry>')[1:]:
        title = entry.split('<title>')[1].split('</title>')[0].strip()
        summary = entry.split('<summary>')[1].split('</summary>')[0].strip()
        link = entry.split('<id>')[1].split('</id>')[0].strip()
        published_date = entry.split('<published>')[1].split('</published>')[0].strip()
        
        # 过滤 2023 年以后的论文
        if published_date >= "2023-01-01":
            # 将时间格式化为 YYYY-MM-DD HH:MM:SS
            dt = datetime.strptime(published_date, "%Y-%m-%dT%H:%M:%SZ")
            formatted_date = dt.strftime("%Y-%m-%d %H:%M:%S")
            
            papers.append({
                "title": title,
                "summary": summary,
                "link": link,
                "source": "arXiv",
                "date": formatted_date  # 使用格式化后的时间
            })
    # 按照日期排序（从新到旧）
    papers.sort(key=lambda x: x["date"], reverse=True)
    
    # 保存到 JSON 文件
    with open("papers/arxiv_papers.json", "w") as f:
        json.dump(papers, f, indent=4)
    print("arXiv papers updated successfully!")
    print(f"Saved {len(papers)} papers to papers/arxiv_papers.json")
else:
    print("Failed to fetch papers from arXiv.")
    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")
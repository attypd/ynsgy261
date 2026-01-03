import requests
import re

# 顶级大佬及公共资源池（这些仓库通常包含港台、星影、松视等）
target_urls = [
    "https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/ipv6.m3u",
    "https://raw.githubusercontent.com/Guovin/TV/gd/output/result.txt",
    "https://raw.githubusercontent.com/yuanzl77/IPTV/main/live.txt",
    "https://raw.githubusercontent.com/ssili126/tv/main/itvlist.txt",
    "http://175.178.251.183:668/livedata/itvlist.txt"
]

# 核心关键词库：包含你提到的爆谷、天映、松视等
keywords = [
    "香港", "台湾", "HK", "TW", "TVB", "翡翠", "天映", "爆谷", "星影", 
    "CHC", "凤凰", "松视", "彩虹", "Sugo", "Panas", "Cherry", "Honey"
]

def super_spider():
    collected_channels = []
    print("🚀 启动超级爬虫，扫描全网高价值源...")

    for url in target_urls:
        try:
            r = requests.get(url, timeout=15)
            if r.status_code == 200:
                lines = r.text.split('\n')
                for line in lines:
                    # 过滤逻辑：包含关键词 且 包含有效 http 链接
                    if any(k.lower() in line.lower() for k in keywords):
                        if "http" in line:
                            # 统一清洗格式，确保盒子能识别
                            clean_line = line.strip().replace("\r", "")
                            collected_channels.append(clean_line)
        except:
            continue

    # 去重处理
    result = list(set(collected_channels))
    
    # 写入伪装文件 v_data_88.txt
    with open("v_data_88.txt", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        f.write("\n".join(result))
    
    print(f"✅ 任务完成，成功捕获 {len(result)} 个频道！")

if __name__ == "__main__":
    super_spider()

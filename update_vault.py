import json
from datetime import datetime

# Danh sách dữ liệu mẫu tự động cập nhật (Bạn có thể thay thế logic cào dữ liệu web bằng BeautifulSoup hoặc API tại đây)
def generate_tools():
    current_date = datetime.now().strftime("%d/%m/%Y")
    
    # Dữ liệu ví dụ được sinh tự động hằng ngày
    tools = [
        {
            "title": f"Adobe Photoshop 2026 (Cập nhật ngày {current_date})",
            "category": "Đồ họa",
            "description": "Phần mềm chỉnh sửa ảnh chuyên nghiệp tích hợp AI Generative Fill mới nhất, kích hoạt sẵn.",
            "date": current_date,
            "link": "https://example.com/download-photoshop"
        },
        {
            "title": f"CapCut Pro Desktop v4.2 ({current_date})",
            "category": "Video Editor",
            "description": "Công cụ dựng phim ngắn, tự động tạo phụ đề và hiệu ứng siêu mượt cho Creator.",
            "date": current_date,
            "link": "https://example.com/download-capcut"
        },
        {
            "title": f"FL Studio 2024 Signature Edition ({current_date})",
            "category": "Âm thanh",
            "description": "Phần mềm sản xuất nhạc, làm beat Lofi, EDM chuyên nghiệp hàng đầu.",
            "date": current_date,
            "link": "https://example.com/download-flstudio"
        },
        {
            "title": f"Visual Studio Code v1.95 Optimized ({current_date})",
            "category": "Lập trình",
            "description": "Trình soạn thảo mã nguồn tối ưu cho lập trình viên web và software.",
            "date": current_date,
            "link": "https://example.com/download-vscode"
        }
    ]
    return tools

def save_json(data):
    with open('tools.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Đã cập nhật thành công file tools.json!")

def generate_sitemap():
    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://flashtool.pages.dev/</loc>
        <changefreq>always</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://flashtool.pages.dev/gateway.html</loc>
        <changefreq>daily</changefreq>
        <priority>0.8</priority>
    </url>
</urlset>
"""
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    print("Đã tạo xong sitemap.xml chuẩn SEO!")

if __name__ == "__main__":
    tools_data = generate_tools()
    save_json(tools_data)
    generate_sitemap()
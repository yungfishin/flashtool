import json
from datetime import datetime

def generate_tools():
    current_date = datetime.now().strftime("%d/%m/%Y")
    
    # Danh sách mở rộng nhiều công cụ hơn
    tools = [
        {
            "title": f"Adobe Photoshop 2026 Full Pre-activated",
            "category": "Đồ họa",
            "description": "Phần mềm chỉnh sửa ảnh chuyên nghiệp tích hợp AI Generative Fill mới nhất.",
            "date": current_date,
            "link": "https://example.com/download-photoshop"
        },
        {
            "title": f"CapCut Pro Desktop v4.2",
            "category": "Video Editor",
            "description": "Công cụ dựng phim ngắn, tự động tạo phụ đề và hiệu ứng siêu mượt cho Creator.",
            "date": current_date,
            "link": "https://example.com/download-capcut"
        },
        {
            "title": f"FL Studio 2024 Signature Edition",
            "category": "Âm thanh",
            "description": "Phần mềm sản xuất nhạc, làm beat Lofi, EDM chuyên nghiệp hàng đầu.",
            "date": current_date,
            "link": "https://example.com/download-flstudio"
        },
        {
            "title": f"Visual Studio Code v1.95 Optimized",
            "category": "Lập trình",
            "description": "Trình soạn thảo mã nguồn tối ưu cho lập trình viên web và software.",
            "date": current_date,
            "link": "https://example.com/download-vscode"
        },
        {
            "title": f"IDM (Internet Download Manager) v6.42",
            "category": "Tiện ích",
            "description": "Phần mềm tăng tốc độ tải xuống file số 1 thế giới, bắt link cực nhanh.",
            "date": current_date,
            "link": "https://example.com/download-idm"
        },
        {
            "title": f"WinRAR 7.00 Final x64",
            "category": "Tiện ích",
            "description": "Công cụ nén và giải nén file phổ biến, hỗ trợ định dạng RAR5 và ZIP.",
            "date": current_date,
            "link": "https://example.com/download-winrar"
        },
        {
            "title": f"Adobe Premiere Pro 2026 Pre-activated",
            "category": "Video Editor",
            "description": "Phần mềm dựng phim chuyên nghiệp, hỗ trợ AI chỉnh màu và cắt ghép thông minh.",
            "date": current_date,
            "link": "https://example.com/download-premiere"
        },
        {
            "title": f"Bandicam 2026 Full Screen Recorder",
            "category": "Tiện ích",
            "description": "Phần mềm quay màn hình máy tính chất lượng cao, nhẹ máy, không giật lag.",
            "date": current_date,
            "link": "https://example.com/download-bandicam"
        }
    ]
    return tools

def save_json(data):
    with open('tools.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Đã cập nhật thành công file tools.json với danh sách mới!")

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
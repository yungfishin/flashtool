import json
from datetime import datetime

def generate_tools():
    current_date = datetime.now().strftime("%d/%m/%Y")
    
    # Kho dữ liệu tự động mở rộng hàng loạt
    tools = [
        {"title": "Adobe Photoshop 2026 Full Pre-activated", "category": "Đồ họa", "description": "Chỉnh sửa ảnh chuyên nghiệp tích hợp AI Generative Fill mới nhất.", "date": current_date, "link": "https://example.com/download-photoshop"},
        {"title": "CapCut Pro Desktop v4.2", "category": "Video Editor", "description": "Dựng phim ngắn, tự động tạo phụ đề và hiệu ứng siêu mượt.", "date": current_date, "link": "https://example.com/download-capcut"},
        {"title": "FL Studio 2024 Signature Edition", "category": "Âm thanh", "description": "Phần mềm sản xuất nhạc, làm beat Lofi, EDM chuyên nghiệp hàng đầu.", "date": current_date, "link": "https://example.com/download-flstudio"},
        {"title": "Visual Studio Code v1.95 Optimized", "category": "Lập trình", "description": "Trình soạn thảo mã nguồn tối ưu cho lập trình viên web và software.", "date": current_date, "link": "https://example.com/download-vscode"},
        {"title": "IDM (Internet Download Manager) v6.42", "category": "Tiện ích", "description": "Tăng tốc độ tải xuống file số 1 thế giới, bắt link cực nhanh.", "date": current_date, "link": "https://example.com/download-idm"},
        {"title": "WinRAR 7.00 Final x64", "category": "Tiện ích", "description": "Công cụ nén và giải nén file phổ biến, hỗ trợ định dạng RAR5 và ZIP.", "date": current_date, "link": "https://example.com/download-winrar"},
        {"title": "Adobe Premiere Pro 2026 Pre-activated", "category": "Video Editor", "description": "Dựng phim chuyên nghiệp, hỗ trợ AI chỉnh màu và cắt ghép thông minh.", "date": current_date, "link": "https://example.com/download-premiere"},
        {"title": "Bandicam 2026 Full Screen Recorder", "category": "Tiện ích", "description": "Quay màn hình máy tính chất lượng cao, nhẹ máy, không giật lag.", "date": current_date, "link": "https://example.com/download-bandicam"},
        {"title": "Adobe Illustrator 2026 Full", "category": "Đồ họa", "description": "Thiết kế đồ họa vector chuyên nghiệp cho Designer.", "date": current_date, "link": "https://example.com/download-illustrator"},
        {"title": "DaVinci Resolve Studio 19", "category": "Video Editor", "description": "Phần mềm dựng phim và chỉnh màu chuẩn Hollywood.", "date": current_date, "link": "https://example.com/download-davinci"},
        {"title": "Ableton Live 12 Suite", "category": "Âm thanh", "description": "Workstation âm thanh kỹ thuật số hàng đầu cho Producer.", "date": current_date, "link": "https://example.com/download-ableton"},
        {"title": "GitKraken Pro v9.11", "category": "Lập trình", "description": "Giao diện quản lý Git cực đẹp và trực quan cho lập trình viên.", "date": current_date, "link": "https://example.com/download-gitkraken"},
        {"title": "Notion Desktop Enhanced", "category": "Tiện ích", "description": "Ứng dụng ghi chú, quản lý công việc và cơ sở dữ liệu cá nhân.", "date": current_date, "link": "https://example.com/download-notion"},
        {"title": "CCleaner Professional v6.20", "category": "Tiện ích", "description": "Dọn dẹp hệ thống, tối ưu hóa tốc độ máy tính tự động.", "date": current_date, "link": "https://example.com/download-ccleaner"},
        {"title": "Blender 4.2 LTS 3D Creation", "category": "Đồ họa", "description": "Phần mềm đồ họa 3D mã nguồn mở mạnh mẽ nhất hiện nay.", "date": current_date, "link": "https://example.com/download-blender"},
        {"title": "Lightroom Classic 2026", "category": "Đồ họa", "description": "Quản lý và hậu kỳ ảnh chuyên nghiệp cho nhiếp ảnh gia.", "date": current_date, "link": "https://example.com/download-lightroom"}
    ]
    return tools

def save_json(data):
    with open('tools.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Đã tự động tạo xong {len(data)} ứng dụng trong tools.json!")

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
import json
import random
from datetime import datetime

CATEGORIES = ['Đồ họa', 'Video Editor', 'Âm thanh', 'Lập trình', 'Tiện ích', 'Game & Crack']

# Danh sách gốc các phần mềm, công cụ, game hot hàng đầu
BASE_TOOLS = [
    {"title": "Adobe Photoshop CC 2026 Pre-Activated", "desc": "Bộ công cụ chỉnh sửa ảnh và thiết kế đồ họa chuyên nghiệp tích hợp AI."},
    {"title": "Adobe Illustrator 2026 Full Repack", "desc": "Phần mềm vẽ vector, thiết kế logo và ấn phẩm truyền thông chuyên nghiệp."},
    {"title": "Adobe After Effects 2026 Full Edition", "desc": "Tạo hiệu ứng kỹ xảo điện ảnh, đồ họa chuyển động và animation đỉnh cao."},
    {"title": "CorelDRAW Graphics Suite 2026", "desc": "Bộ công cụ thiết kế đồ họa vector và chế bản điện tử toàn diện."},
    {"title": "Figma Pro UI/UX Kit & Assets Bundle", "desc": "Bộ giao diện thiết kế ứng dụng di động và website hiện đại."},
    {"title": "Blender 3D Sci-Fi & Cyberpunk Assets Pack", "desc": "Thư viện mô hình 3D không gian vũ trụ và công nghệ tương lai chất lượng cao."},
    {"title": "Topaz Photo AI 2026 Full License", "desc": "Phần mềm upscale và phục hồi ảnh cũ, làm nét bằng AI cực đỉnh."},
    {"title": "Adobe Premiere Pro 2026 Pre-Activated", "desc": "Phần mềm dựng phim, chỉnh sửa video chuyên nghiệp với AI hỗ trợ."},
    {"title": "CapCut Pro Desktop Edition Full Crack", "desc": "Ứng dụng cắt dựng video ngắn cực mượt trên máy tính cho TikTok và YouTube."},
    {"title": "DaVinci Resolve Studio 2026 v19", "desc": "Phần mềm dựng phim, hậu kỳ và chỉnh màu chuẩn Hollywood chuyên nghiệp."},
    {"title": "Wondershare Filmora 14 Full Active", "desc": "Trình chỉnh sửa video trực quan với hàng ngàn hiệu ứng chuyển cảnh sẵn có."},
    {"title": "Camtasia 2026 Ultimate Screen Recorder", "desc": "Phần mềm quay màn hình máy tính và chỉnh sửa video hướng dẫn đỉnh cao."},
    {"title": "Lofi Chillhop Beats Sample Pack Vol.1-5", "desc": "Bộ sưu tập âm thanh, vòng lặp lofi beat bản quyền miễn phí cho nhà sáng tạo."},
    {"title": "FL Studio 2026 Producer Edition Full", "desc": "Phần mềm sản xuất âm thanh, phối khí và làm nhạc điện tử chuyên nghiệp."},
    {"title": "Ableton Live Suite 12 Full Crack", "desc": "Công cụ trình diễn và sáng tác nhạc điện tử hàng đầu cho nhà sản xuất."},
    {"title": "VS Code Master Extension Pack 2026", "desc": "Gói extension tối ưu hóa tốc độ lập trình, auto-complete và code web."},
    {"title": "JetBrains IntelliJ IDEA Ultimate 2026", "desc": "Môi trường phát triển tích hợp mạnh mẽ nhất dành cho lập trình viên."},
    {"title": "Python Automation Scripts Collection", "desc": "Bộ mã nguồn tự động hóa công việc văn phòng, cào dữ liệu và quản lý tệp."},
    {"title": "IDM (Internet Download Manager) v6.50 Full", "desc": "Phần mềm tăng tốc tải xuống file siêu tốc số 1 thế giới."},
    {"title": "WinRAR 7.01 Final Full Register", "desc": "Công cụ nén và giải nén file phổ biến, mạnh mẽ và hỗ trợ đa định dạng."},
    {"title": "CCleaner Professional Plus 2026 Active", "desc": "Phần mềm dọn dẹp hệ thống, tối ưu hóa registry và tăng tốc máy tính."},
    {"title": "Cities: Skylines II Deluxe Edition Repack", "desc": "Tựa game mô hình xây dựng thành phố thế hệ mới chân thực và đồ sộ nhất."},
    {"title": "GTA V Enhanced Modded Pack 2026", "desc": "Bản tổng hợp mod đồ họa siêu thực và các bản mở rộng cốt truyện đỉnh cao."},
    {"title": "Cyberpunk 2077 Ultimate Edition Crack", "desc": "Tựa game nhập vai hành động thế giới mở tương lai với đồ họa Ray Tracing."}
]

def generate_huge_vault():
    tools = []
    current_date = datetime.now().strftime("%d/%m/%Y")
    
    # Đưa toàn bộ tool gốc vào
    for item in BASE_TOOLS:
        tools.append({
            "title": item["title"],
            "description": item["desc"],
            "category": random.choice(CATEGORIES),
            "link": "https://github.com/yungfishin/flashtool/releases/download/v1.0.0/package.zip",
            "date": current_date
        })
    
    # Tự động sinh hơn 100+ biến thể phần mềm đa dạng ngập tràn kho
    editions = ["Portable Pro", "Repack Ultimate", "Developer Edition", "Cloud Setup v3.2", "Pre-Activated Full"]
    
    for i in range(1, 105):
        base = random.choice(BASE_TOOLS)
        tools.append({
            "title": f"{base['title']} - {random.choice(editions)} #{i}",
            "desc": f"{base['desc']} (Bản cập nhật tự động tối ưu hóa tốc độ cao, đã bẻ khóa toàn bộ tính năng).",
            "category": random.choice(CATEGORIES),
            "link": "https://github.com/yungfishin/flashtool/releases/download/v1.0.0/package.zip",
            "date": current_date
        })
        
    return tools

if __name__ == "__main__":
    vault_data = generate_huge_vault()
    # Ghi trực tiếp vào file tools.json
    with open("tools.json", "w", encoding="utf-8") as f:
        json.dump(vault_data, f, ensure_ascii=False, indent=4)
    print(f"Đã bơm thành công tổng cộng {len(vault_data)} phần mềm vào kho tools.json!")
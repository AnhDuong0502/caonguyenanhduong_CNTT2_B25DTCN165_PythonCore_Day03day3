inventory = [
    {"id": "SP1", "ten": "Tai nghe Sony", "gia": 1200000, "danh_muc": "Phụ kiện"},
    {"id": "SP2", "ten": "Chuột không dây", "gia": 450000, "danh_muc": "Phụ kiện"},
    {"id": "SP3", "ten": "Bàn phím Cơ", "gia": 950000, "danh_muc": "Phụ kiện"},
    {
        "id": "SP4",
        "ten": "Màn hình Dell 27 inch",
        "gia": 4500000,
        "danh_muc": "Thiết bị",
    },
    {
        "id": "SP5",
        "ten": "Sạc dự phòng 20000mAh",
        "gia": 350000,
        "danh_muc": "Phụ kiện",
    },
]


def linear_search_filter(cart, target_category, max_price):
    result = []

    for product in cart:
        if product["gia"] <= max_price and product["danh_muc"] == target_category:
            result.append(product)

    return result


result = linear_search_filter(inventory, "Phụ kiện", 1000000)

print("KẾT QUẢ LỌC SẢN PHẨM (LINEAR SEARCH MULTI-CRITERIA)")
print("Danh mục tìm kiếm: Phụ kiện | Giá tối đa: 1,000,000 VNĐ")
print(f"Tìm thấy {len(result)} sản phẩm phù hợp:")

for product in result:
    print(f"  -> [{product['id']}] {product['ten']} | Giá: {product['gia']:,} VNĐ")

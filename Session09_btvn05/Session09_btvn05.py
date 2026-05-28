"""
input:
    choice int lựa chọn chức năng từ menu
    search_order_list str mã đơn hàng người dùng nhập
    order_list danh sách đơn hàng và trạng thái
output:
    Danh sách đơn hàng
    Trạng thái mới của đơn hàng
    Thông báo lỗi hoặc thông báo thành công
    Thông báo khi không thể thao tác với đơn hàng
-- giải pháp:
    bài toàn dùng các tính năng list mình đẫ học
    menu dùng while true 
    kiểm tra nhập số không nhập chứ dùng Try: - except:
    xử lý menu dùng match-case 
    dùng các hàm của list :
        append(): Thêm đơn hàng
        pop(): Xóa đơn hàng
        split(): Tách mã đơn và trạng thái
        strip(): Xóa khoảng trắng
        upper(): Chuẩn hóa chữ in hoa
        enumerate(): Duyệt danh sách kèm vị trí
-- các bước làm 
b1: tạo menu
b2: tạo xử lý menu
b3: Chức năng 1: Hiển thị danh sách
    Kiểm tra danh sách rỗng
    Dùng vòng lặp để in đơn hàng
b4: Chức năng 2: Gán tài xế
    duyệt mảng
    Tách trạng thái dùng split
    Tìm mã đơn hàng (if else)
    Chỉ cho phép đơn PENDING
    Đổi thành ASSIGNED
b5: Chức năng 3: Cập nhật giao hàng
    duyệt mảng
    Tách trạng thái dùng split
    Nếu ASSIGNED -> DELIVERING
    Nếu DELIVERING -> COMPLETED
    Các trạng thái khác -> báo lỗi
b6: Chức năng 4: Hủy đơn
    duyệt mảng
    Tách trạng thái dùng split
    Chỉ được hủy:
        PENDING
        ASSIGNED
    Nếu đang giao hoặc hoàn tất → không cho hủy
b7: Chức năng 5: Thoát
    Kết thúc vòng lặp bằng break
b8: nhập sai lựa chọn menu thông báo lỗi
"""
order_list = [
    "GE001 - PENDING",
    "GE002 - ASSIGNED",
    "GE003 - DELIVERING"
]
while True:
    try:
        choice = int(input("""
        ===== HỆ THỐNG ĐIỀU PHỐI GRAB EXPRESS =====
        1. Hiển thị danh sách đơn hàng
        2. Gán tài xế cho đơn hàng
        3. Cập nhật trạng thái giao hàng
        4. Hủy đơn hàng
        5. Thoát chương trình
        > Mời bạn nhập lựa chọn (1-5): 
        """))
    except:
        print("Không được nhập chữ, phải nhập số nguyên")
        continue
    match choice:
        case 1: 
            if order_list == []:
                print("Danh sách đơn hàng hiện đang trống.")
            else:
                print("Danh sách đơn hàng hiện tại:")
                for index, value in enumerate(order_list, 1):
                    print(f"{index}. {value}")
        case 2: 
            search_order_list = input("Mời bạn nhập đơn hàng cần tìm: ").strip().upper()
            for index, value in enumerate(order_list):
                new_list = value.split("-")
                id_order = new_list[0].strip()
                status = new_list[1].strip()
                if search_order_list == id_order:
                    if status == "PENDING":
                        status = "ASSIGNED"
                        new_order = f"{search_order_list} - {status}"
                        order_list[index] = new_order
                    else:
                        print("Chỉ có thể gán tài xế cho đơn hàng đang chờ xử lý")
        case 3:
            search_order_list = input("Mời bạn nhập đơn hàng cần cập nhật trạng thái giao hàng: ").strip().upper()
            for index, value in enumerate(order_list):
                new_list = value.split("-")
                id_order = new_list[0].strip()
                status = new_list[1].strip()
                if search_order_list == id_order:
                    if status == "ASSIGNED":
                        status = "DELIVERING"
                        new_order = f"{search_order_list} - {status}"
                        order_list[index] = new_order
                    elif status == "DELIVERING": 
                        status = "COMPLETED"
                        new_order = f"{search_order_list} - {status}"
                        order_list[index] = new_order
                    elif status == "PENDING": 
                        print("Đơn hàng chưa được gán tài xế, không thể chuyển sang trạng thái giao hàng.")
                    elif status == "COMPLETED":
                        print("Đơn hàng đã hoàn tất, không thể cập nhật tiếp.")
                    elif status == "CANCELLED":
                        print("Đơn hàng đã bị hủy, không thể cập nhật.")
                    elif status != "PENDING": 
                        print("Chỉ có thể gán tài xế cho đơn hàng đang chờ xử lý")
        case 4:
            search_order_list = input("Mời bạn nhập đơn hàng cần hủy: ")
            for index, value in enumerate(order_list):
                new_list = value.split("-")
                id_order = new_list[0].strip()
                status = new_list[1].strip()
                if search_order_list == id_order:
                    if status == "PENDING" or status == "ASSIGNED":
                        status = "CANCELLED"
                        new_order = f"{search_order_list} - {status}"
                        order_list[index] = new_order
                    elif status == "DELIVERING":
                        print("Đơn hàng đang được giao, không thể hủy.")
                    elif status == "COMPLETED":
                        print("Đơn hàng đã hoàn tất, không thể hủy.")
                    elif status == "CANCELLED":
                        print("Đơn hàng đã được hủy trước đó.")
        case 5:
            print("Thoát chương trình")
            break
        case _:
            print("Không có lựa chọn hợp lệ")


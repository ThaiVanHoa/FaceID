import mysql.connector

# Kết nối đến cơ sở dữ liệu MySQL trong XAMPP
conn = mysql.connector.connect(
    host='localhost',    # Địa chỉ IP hoặc tên máy chủ MySQL (trong trường hợp này là localhost)
    port='3307',         # Số cổng MySQL (trong trường hợp này là 3307, cổng mặc định của XAMPP là 3306)
    user='root',         # Tên người dùng MySQL (trong trường hợp này là root)
    password='',         # Mật khẩu MySQL (nếu có)
    database='mydatabase'  # Tên cơ sở dữ liệu bạn muốn kết nối
)

# Kiểm tra xem kết nối đã được thiết lập thành công chưa
if conn.is_connected():
    print("Kết nối đến cơ sở dữ liệu thành công!")

    # Tạo một đối tượng con trỏ để thực hiện các truy vấn SQL
    my_cursor = conn.cursor()

    # Thực thi lệnh SQL để tạo bảng mới
    my_cursor.execute("CREATE TABLE IF NOT EXISTS new_table09 ("
                      "id INT AUTO_INCREMENT PRIMARY KEY,"
                      "name VARCHAR(255),"
                      "age INT,"
                      "gender VARCHAR(10)"
                      ")")

    # Thông báo khi bảng đã được tạo hoặc đã tồn tại
    print("Bảng 'new_table' đã được tạo hoặc đã tồn tại!")

    # Đóng kết nối MySQL
    conn.close()
else:
    print("Không thể kết nối đến cơ sở dữ liệu.")

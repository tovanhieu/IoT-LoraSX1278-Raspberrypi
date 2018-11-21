![node1](https://user-images.githubusercontent.com/26000753/48850165-9bf55480-edda-11e8-8811-420666cc5c8a.PNG)
 <br/>
   | Arduino Uno R3 | Lora Ra-02 |
   | -------------  | ---------- |
   | 3v3            |    3v3     |
   | GND            |    GND     |  
   | RESET          |    D9      |
   | DIO1           |    D2      |
   | NSS            |    D10     |  
   | MOSI           | MOSI (D11) |
   | MISO           | MOSI (D12) |
   | SCK            |  SCK (D13) |
   | **Arduino Uno R3** |   **DHT11**    |
   | -------------  | ---------- |
   | 3v3            |    3v3     |
   | GND            |    GND     | 
   | A0             |    Analog  | 
<br/>
Kết nối các chân theo bảng trên <br/>
**Chú ý**: *Do module Lora Ra-02 hoạt động ở mức điện áp 3v3 (khác với arduino điện áp pin/out ra là 5v) nên cần phải sử dụng [module chuyển đổi logic từ 3v3 sang 5v](https://www.google.com.vn/search?biw=1024&bih=667&tbm=isch&sa=1&ei=W2f1W96vF4L98gXcxLm4DA&q=3v3+to+5v+logic+shift+converter+module&oq=3v3+to+5v+logic+shift+converter+module&gs_l=img.3...2042.4975..5201...1.0..0.319.2164.2-1j6......1....1..gws-wiz-img.3K_eO18mitQ#imgrc=LDnyweGxLa0T5M:), module có hai đầu cấp nguồn 3v3 và 5v nên nguồn của module sễ cấp chung với với nguồn của arduino còn chân đất nối chung hai đầu*
\
Sau khi kết nối xong nạp code chương trình LORA_SENDERDHT11.ino để gửi thông tin đến gateway

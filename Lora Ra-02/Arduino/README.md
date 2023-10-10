# Hướng dẫn
![node1](https://user-images.githubusercontent.com/26000753/48850165-9bf55480-edda-11e8-8811-420666cc5c8a.PNG)
 <br/>
![lora-arduinopin-out](https://user-images.githubusercontent.com/26000753/51382656-ed576100-1b49-11e9-8333-b0bcd41cbfc8.PNG)
<br/>
Kết nối các chân từ Arduino với cảm biến và Module Lora theo bảng trên đối với Node, còn Gateway thì chỉ cần kết nối với Module Lora <br/>
**Chú ý**: *Do module Lora Ra-02 hoạt động ở mức điện áp 3v3 (khác với arduino điện áp pin/out ra là 5v) nên cần phải sử dụng [module chuyển đổi logic từ 3v3 sang 5v], module có hai đầu cấp nguồn 3v3 và 5v nên nguồn của module sễ cấp chung với với nguồn của arduino còn chân đất nối chung hai đầu*
- Sau khi kết nối xong nạp code chương trình LORA_NODE.ino để gửi thông tin đến gateway
- Tại Gateway chạy chương trình LORA_GATEWAY.ino để nhận thông tin từ node.
### Reference link
- https://github.com/rpsreal/LoRa_Ra-02_Arduino

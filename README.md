# 2足歩行ロボットの製作

## 機構設計
筐体は3DCADソフトFusionを用いて設計を行い，3Dプリンタで出力を行った．  
4つの関節を持ち，全ての関節にサーボモータ(sg90)を用いた．  

## システム構成
マイコン構成として，RaspberryPiPico(python)とESP32(c,c++)の2台を用いる．  
RaspberryPiPicoはロボットの関節を駆動させるために用いる．  
ESP32は外部との通信，および操作画面の表示に用いる．2つのマイコンはシリアル通信を行う．  

ロボットが起動するとESP32がローカルにWebサーバを立ち上げ，スマホやPCから接続することにより操作画面を表示できる．  
操作画面は停止，前進，後退，右に進む，および左に進むの４つの選択が可能である．  
任意の操作がなされたとき，トリガが立ちシリアル通信によりRaspberryPiPicoに送信される．  
信号を受け取ると，受け取った信号に基づきロボットの関節角度が制御されロボットが動作する．  

足に貼ったQRコードを読み取ることでスマートフォン等から操作できる(同じネットワーク内に限る)．

## その他
歩行させるのもなかなか難しく，横転することもある．  
![Image](https://github.com/user-attachments/assets/38508714-93ae-4067-a009-d5253eaa008e)

制作期間は約2.5ヶ月

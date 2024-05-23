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

## その他
歩行させるのもなかなか難しく，やはり稀に横転することもある．  

制作期間は約2.5ヶ月

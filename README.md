# IoT_Project



## 概要

Raspberry PIを用いたIoT開発の基本コードを整理したもの

これ以降では、各ディレクトリごとの機能は注意事項を記載

## LED_light

* 注意
  * Raspberry PiのSDカードに入れたOSによってはwiring(端子系を操作するライブラリ)が入っていない場合がある。
  * その場合、```sudo pip3 install wiringpi```を実行する
  * また、pythonを実行する際は、sudo python3 ~で実行すること

## Senser

* 人感センサー
  * 調節が可能
    * センサーが感知する距離: 3 - 7m
    * 時間調整: 5 - 200s

## Camera

* カメラ
  * RaspberryPi本体の電源をOFFにした状態で接続
  * 接続できたかは、```vcgencmd get_camera```を実行し、下記が出力されればOK
    * > supported=1 detected=1
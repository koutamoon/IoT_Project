# IoT_Project



## 概要

Raspberry PIを用いたIoT開発の基本コードを整理したもの

これ以降では、各ディレクトリごとの機能は注意事項を記載

## LED_light

* 注意
  * Raspberry PiのSDカードに入れたOSによってはwiring(端子系を操作するライブラリ)が入っていない場合がある。
  * その場合、```sudo pip3 install wiringpi```を実行する
  * また、pythonを実行する際は、sudo python3 ~で実行すること

# gorilla_achieve

自分のしょうもない実績を共有するSNS
しょうもないそんな日常に面白さがあるのです。

## Required

pipenv==2020.8.13

## サーバ起動
```shell script
仮想環境にパッケージインストール
pipenv sync

# マイグレーションファイルの適用
pipenv run python manage.py migrate

# サーバ起動
pipenv run python manage.py runserver
```

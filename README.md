# じゃんけんゲーム

## 内容

プレイヤーとエネミーどちらかのHPが0以下になるまでじゃんけんをする

## 環境

| 項目名 | バージョン |
|:--: | :-- |
| Python | 3.10 |

## 環境構築

### Mac

```terminal
# python、itのインストール
brew install python git
```

### Windows

```PowerShellプロンプト
// scoopのインストールをする
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')

// python、git（入れてない場合)のインストール
scoop install git python
```

### 共通

```terminal
// pyenvのインストール
pip install pipenv

# githubからクローン（ソースの取得）する
git clone https://github.com/yuki-ono-vlb/JankenGame.git
git gc
git pull

# 必要なライブラリのインストールを行う
pipenv install
# 開発時のみ使用するライブラリのインストールを行う
pipenv install --dev
```

## ゲームの起動方法(共通)

```terminal

# ソースのプロジェクトへ移動
cd JankenGame

python ./src/main.py

// または
pipenv run start
```

## 遊び方

1. エネミーとプレイヤーの名前を入力する
2. startボタンを押す
3. グー、チョキ、パーのボタンの何れかを押す
4. じゃんけんで勝つとエネミーのHPが削られる
5. じゃんけんで負けるとプレイヤーのHPが削られる
6. 繰り返しじゃんけんをしてHPが0以下に先になった方の負け
7. じゃんけんの途中で遣り直しを行いたい場合はrestartボタンを押す
8. じゃんけんを終了したい場合はendボタンを押す

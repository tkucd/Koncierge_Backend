# Koncierge_Backend

# Koncierge_Backendの使い方
以下ではローカルでの実行手順を記載します。

まず本レポジトリのクローンをお願いします。<br>
```
git clone https://github.com/tkucd/Koncierge_Backend
```

次に本プロジェクト直下に以下の`.env`ファイルが必要になります。<br>
（OpenAIのAPIキーが必要となるため、各自で取得をお願いします。）
```
OPENAI_API_KEY=""
```

続いて環境構築が必要となるため、以下のコマンドを順にお願いします。
### 新しい仮想環境の作成<br>
```
python -m venv env
```

### 作成した仮想環境のアクティブ化（Windowsの場合）
```
env\Scripts\activate
```

### 作成した仮想環境のアクティブ化（Mac/Linuxの場合）
```
soucre env/bin/activate
```

### 必要なパッケージのインストール<br>
```
pip install -r requirements.txt
```

### 起動
```
uvicorn app:app --reload
```

## [Koncierge_Frontend](https://github.com/tkucd/Koncierge_Frontend)に関して
本プロジェクトで実装したAPIを利用したWebアプリケーションです。
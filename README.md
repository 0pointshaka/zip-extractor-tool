# ZIP ファイル解凍ツール

パスワード保護された ZIP ファイルを簡単に解凍できる Python ツールです。

## 機能

- ✓ 通常の ZIP ファイル解凍
- ✓ パスワード保護された ZIP に対応
- ✓ パスワード保護の自動検出
- ✓ 日本語対応
- ✓ エラーハンドリング
- ✓ 解凍されたファイル一覧表示

## 必要な環境

- Python 3.6 以上
- 追加のライブラリは不要（Python 標準ライブラリのみ使用）

## インストール

```bash
# リポジトリをクローン
git clone https://github.com/0pointshaka/zip-extractor-tool.git
cd zip-extractor-tool
```

## 使い方

### 1. 基本的な使い方（対話形式）

```bash
python zip_extractor.py
```

実行すると、以下の入力を求められます：

```
==================================================
ZIP ファイル解凍ツール
==================================================

ZIP ファイルのパスを入力してください: /path/to/file.zip
解凍先ディレクトリを入力してください（デフォルト: カレントディレクトリ）: ./output

ファイルをチェック中...
このファイルはパスワード保護されています。
パスワードを入力してください: ****

解凍処理を実行中...

✓ 解凍完了: ./output

解凍されたファイル数: 5
  - folder/file1.txt
  - folder/file2.txt
  - file3.txt
  - ...
```

### 2. Python スクリプト内での使用

```python
from zip_extractor import ZipExtractor

# ツールのインスタンスを作成
extractor = ZipExtractor("archive.zip", extract_to="./output")

# パスワード保護の確認
if extractor.is_password_protected():
    password = "your_password"
else:
    password = None

# 解凍を実行
extractor.extract(password)
```

### 3. パスワードなしの ZIP

```python
from zip_extractor import ZipExtractor

extractor = ZipExtractor("archive.zip", extract_to="./output")
extractor.extract()  # password=None がデフォルト
```

## API リファレンス

### ZipExtractor クラス

#### `__init__(zip_path, extract_to=None)`

**パラメータ：**
- `zip_path` (str): ZIP ファイルのパス
- `extract_to` (str, optional): 解凍先ディレクトリ。デフォルトはカレントディレクトリ

#### `extract(password=None)`

ZIP ファイルを解凍します。

**パラメータ：**
- `password` (str, optional): パスワード（必要に応じて）

**戻り値：**
- `bool`: 成功時は True、失敗時は False

#### `is_password_protected()`

ZIP ファイルがパスワード保護されているか確認します。

**戻り値：**
- `bool`: パスワード保護されている場合は True

## 例

### 例 1: シンプルな使用例

```python
from zip_extractor import ZipExtractor

extractor = ZipExtractor("documents.zip", extract_to="./docs")
extractor.extract("mypassword")
```

### 例 2: エラーハンドリング付き

```python
from zip_extractor import ZipExtractor

extractor = ZipExtractor("archive.zip", extract_to="./output")

if extractor.extract("password"):
    print("成功しました")
else:
    print("失敗しました")
```

### 例 3: パスワード保護の確認

```python
from zip_extractor import ZipExtractor

extractor = ZipExtractor("archive.zip")

if extractor.is_password_protected():
    print("このファイルはパスワード保護されています")
    password = input("パスワードを入力: ")
    extractor.extract(password)
else:
    print("パスワード保護されていません")
    extractor.extract()
```

## エラーメッセージ

| エラーメッセージ | 原因 | 解決方法 |
|---|---|---|
| `ファイルが見つかりません` | ZIP ファイルが存在しない | ファイルパスを確認 |
| `無効な ZIP ファイルです` | ZIP ファイルが破損している | ファイルを再確認 |
| `パスワードが間違っています` | 入力したパスワードが正しくない | パスワードを確認 |

## ライセンス

MIT License

## 注意事項

- パスワード保護された ZIP ファイルのパスワードは、安全な方法で入力してください
- 大きなファイルの解凍には時間がかかる場合があります
- 解凍先ディレクトリが存在しない場合は自動的に作成されます


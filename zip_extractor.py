import zipfile
import os
import sys
from pathlib import Path


class ZipExtractor:
    """パスワード保護された ZIP ファイルを解凍するクラス"""

    def __init__(self, zip_path, extract_to=None):
        """
        初期化

        Args:
            zip_path (str): ZIP ファイルのパス
            extract_to (str): 解凍先ディレクトリ（デフォルト: カレントディレクトリ）
        """
        self.zip_path = zip_path
        self.extract_to = extract_to or "."

    def extract(self, password=None):
        """
        ZIP ファイルを解凍する

        Args:
            password (str): パスワード（必要に応じて）

        Returns:
            bool: 成功時は True、失敗時は False
        """
        try:
            # ファイルの存在確認
            if not os.path.exists(self.zip_path):
                print(f"✗ エラー: ファイルが見つかりません: {self.zip_path}")
                return False

            # 解凍先ディレクトリを作成
            Path(self.extract_to).mkdir(parents=True, exist_ok=True)

            # ZIP ファイルを開く
            with zipfile.ZipFile(self.zip_path, "r") as zip_ref:
                # パスワードが必要な場合
                if password:
                    password_bytes = password.encode("utf-8")
                    try:
                        zip_ref.extractall(self.extract_to, pwd=password_bytes)
                    except RuntimeError as e:
                        print(f"✗ エラー: パスワードが間違っています")
                        return False
                else:
                    zip_ref.extractall(self.extract_to)

            print(f"✓ 解凍完了: {self.extract_to}")
            self._print_extracted_files(zip_ref)
            return True

        except zipfile.BadZipFile:
            print("✗ エラー: 無効な ZIP ファイルです")
            return False
        except Exception as e:
            print(f"✗ エラー: {e}")
            return False

    def _print_extracted_files(self, zip_ref):
        """解凍されたファイルを表示"""
        files = zip_ref.namelist()
        print(f"\n解凍されたファイル数: {len(files)}")
        if len(files) <= 10:
            for file in files:
                print(f"  - {file}")
        else:
            for file in files[:5]:
                print(f"  - {file}")
            print(f"  ... 他 {len(files) - 5} 個のファイル")

    def is_password_protected(self):
        """ZIP ファイルがパスワード保護されているか確認"""
        try:
            with zipfile.ZipFile(self.zip_path, "r") as zip_ref:
                for info in zip_ref.infolist():
                    if info.flag_bits & 0x1:
                        return True
            return False
        except Exception as e:
            print(f"✗ エラー: {e}")
            return False


def main():
    """メイン処理"""
    print("=" * 50)
    print("ZIP ファイル解凍ツール")
    print("=" * 50)

    # ZIP ファイルのパス入力
    zip_path = input("\nZIP ファイルのパスを入力してください: ").strip()

    if not zip_path:
        print("✗ エラー: パスを入力してください")
        return

    # 解凍先ディレクトリ入力
    extract_to = input(
        "解凍先ディレクトリを入力してください（デフォルト: カレントディレクトリ）: "
    ).strip()
    extract_to = extract_to or "."

    # ツール初期化
    extractor = ZipExtractor(zip_path, extract_to)

    # パスワード保護の確認
    print("\nファイルをチェック中...")
    if extractor.is_password_protected():
        print("このファイルはパスワード保護されています。")
        password = input("パスワードを入力してください: ")
    else:
        print("このファイルはパスワード保護されていません。")
        password = None

    # 解凍実行
    print("\n解凍処理を実行中...\n")
    extractor.extract(password)


if __name__ == "__main__":
    main()

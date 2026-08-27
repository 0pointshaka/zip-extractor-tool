"""
使用例: パスワード保護された ZIP ファイルの解凍
"""

from zip_extractor import ZipExtractor


def example_1_simple():
    """例 1: シンプルな解凍"""
    print("=" * 50)
    print("例 1: シンプルな解凍")
    print("=" * 50)

    extractor = ZipExtractor("archive.zip", extract_to="./output")
    extractor.extract("password123")
    print()


def example_2_password_protected():
    """例 2: パスワード保護の確認"""
    print("=" * 50)
    print("例 2: パスワード保護の確認")
    print("=" * 50)

    extractor = ZipExtractor("archive.zip", extract_to="./output")

    if extractor.is_password_protected():
        print("✓ このファイルはパスワード保護されています")
        password = input("パスワードを入力: ")
        extractor.extract(password)
    else:
        print("✓ このファイルはパスワード保護されていません")
        extractor.extract()
    print()


def example_3_error_handling():
    """例 3: エラーハンドリング付き"""
    print("=" * 50)
    print("例 3: エラーハンドリング付き")
    print("=" * 50)

    extractor = ZipExtractor("archive.zip", extract_to="./output")

    if extractor.extract("wrong_password"):
        print("✓ 成功しました")
    else:
        print("✗ 失敗しました")
    print()


def example_4_multiple_files():
    """例 4: 複数の ZIP ファイルを処理"""
    print("=" * 50)
    print("例 4: 複数の ZIP ファイルを処理")
    print("=" * 50)

    zip_files = ["file1.zip", "file2.zip", "file3.zip"]
    password = "common_password"

    for zip_file in zip_files:
        print(f"\n処理中: {zip_file}")
        extractor = ZipExtractor(zip_file, extract_to=f"./output_{zip_file[:-4]}")
        if extractor.extract(password):
            print(f"✓ {zip_file} を解凍しました")
        else:
            print(f"✗ {zip_file} の解凍に失敗しました")
    print()


def example_5_interactive():
    """例 5: インタラクティブな使用方法"""
    print("=" * 50)
    print("例 5: インタラクティブな使用方法")
    print("=" * 50)

    zip_path = input("ZIP ファイルのパスを入力: ").strip()
    extract_to = input(
        "解凍先ディレクトリを入力（デフォルト: ./extracted）: "
    ).strip() or "./extracted"

    extractor = ZipExtractor(zip_path, extract_to)

    # パスワード保護の確認
    if extractor.is_password_protected():
        print("このファイルはパスワード保護されています")
        password = input("パスワードを入力: ")
    else:
        print("このファイルはパスワード保護されていません")
        password = None

    # 解凍を実行
    if extractor.extract(password):
        print(f"✓ {extract_to} に解凍しました")
    else:
        print("✗ 解凍に失敗しました")
    print()


if __name__ == "__main__":
    print("\n")
    print("█" * 50)
    print("ZIP ファイル解凍ツール - 使用例")
    print("█" * 50)
    print("\n")

    # 実行する例を選択
    print("実行する例を選択してください:")
    print("1. シンプルな解凍")
    print("2. パスワード保護の確認")
    print("3. エラーハンドリング付き")
    print("4. 複数の ZIP ファイルを処理")
    print("5. インタラクティブな使用方法")
    print()

    choice = input("選択 (1-5): ").strip()

    if choice == "1":
        example_1_simple()
    elif choice == "2":
        example_2_password_protected()
    elif choice == "3":
        example_3_error_handling()
    elif choice == "4":
        example_4_multiple_files()
    elif choice == "5":
        example_5_interactive()
    else:
        print("✗ 無効な選択です")

    print("完了しました")

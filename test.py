# -*- coding: utf-8 -*-
import sys
import csv

COL_NUM = 3

sheet_num =0

# コマンドプロンプトからの引数を取得する変数
args = sys.argv

# リスト形式の辞書型でファイルの中身を取得
csv_file = open(args[1], "r", encoding="ms932", errors="", newline="" )
file = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

# ヘッダーを読み飛ばす（らしい）
header = next(file)

# 一行ずつ読み込む
for row in file:
	sheet_num += 1
	print("感想" + str(sheet_num))
	
	for i in range(COL_NUM):
		print(header[i] + "："+ row[i])
		
	print("")
		
csv_file.close()
# メモ

調べたことやあとでやろうと思っていることを書いておく

## Github Pagesの公開

[参考](https://techacademy.jp/magazine/6445)

- ファイルの拡張子はhtml（そうだよな、だってWebページだもん）
    - メインのページのファイル名は必ず「index.html」
- ページを公開する場合は、gh-pagesをプッシュ（リポジトリページだから）

gh-pagesのプッシュは変更のたび毎回行う

> プロジェクトサイトならば「gh-pages」ブランチをプッシュします。

```
$ git push -u origin gh-pages
```

[参考](https://prog-8.com/docs/github-pages)

htmlファイルのほかに、スタイルシート、画像もアップロードして適用できる

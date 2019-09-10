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

## テーマの修正

[参考](https://qiita.com/koyo-miyamura/items/5ec89ac9689be49a55f6)

当ててるテーマの参照元を探してコピペ。それを修正して反映させる  
リンクはhtmlで直せるけど、背景色とかその辺はcssだからがんばってそっちを直す

## リンクの埋め込み

[参考](https://takumon.com/iframely)

リンクをページに埋め込もうとすると、埋め込みの設定をこちゃっと書かないといけない  
それを、「URLをペーストしたら自動生成する」サイトがある

ただこれは、HTMLファイルじゃないとだめかもしれんな……  
Markdownを解釈した後に適用させるうまい方法を探すか、作品集は別でHTMLで書く、という作戦が無難かもしれん

<div class="iframely-embed">
    <div class="iframely-responsive" style="padding-bottom: 50%; padding-top: 120px;">
        <a href="https://takumon.com/iframely" data-iframely-url="//cdn.iframe.ly/8UezQwi"></a>
    </div>
</div>
<script async src="//cdn.iframe.ly/embed.js" charset="utf-8"></script>

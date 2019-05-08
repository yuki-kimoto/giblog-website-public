<!DOCTYPE html>
<html>
  <head>
    <!-- meta -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0">
<link rel="stylesheet" type="text/css" href="/css/common.css">

<meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0">

<script src="/js/jquery-3.4.1.min.js"></script>

<title>Title - Perlで個人サイト作ろ</title>
<meta name="description" content="#!/usr/bin/env perl">
  </head>
  <body>
    <div class="container">
      <div class="header">
        <!-- header -->
<h1>
  <a href="/">Perlで個人サイト作ろ</a>
</h1>
<div class="site-description">
  Perlで個人サイト作りましょ。ブログを使った情報発信、Webサイトでの商品紹介。お問合せフォームもサポート。
</div>
<div class="site-description">
レンタルサーバー、ドメイン取得、SSLなどの、サイトの公開方法も学ぼ。
</div>
      </div>
      <div class="main">
        <div class="content">
          <div class="entry">
  <div class="top">
    <!-- top -->

  </div>
  <div class="middle">
    <p>
  #!/usr/bin/env perl
</p>
<p>
  use strict;
</p>
<p>
  use warnings;
</p>
<p>
  use utf8;
</p>
<p>
  use Encode 'encode';
</p>
<p>
  # Title mail form
</p>
<p>
  my $title = 'Mail form';
</p>
<p>
  # Content mail form
</p>
<p>
  my $content = <<"EOS";
</p>
<h2><a href="/test.cgi">Title</a></h2>
<div>
  Content
</div>
<p>
  EOS
</p>
<p>
  $content = build_html($title, $content);
</p>
<p>
  my $html = <<"EOS";
</p>
<p>
  Content-type: text/html; charset=UTF-8
</p>
<p>
  $content
</p>
<p>
  EOS
</p>
<p>
  print encode('UTF-8', $html);
</p>
<p>
  sub build_html {
</p>
  my ($title, $content) = @_;
  
  local $/;
  my $html = <DATA>;
  
  $html =~ s/\$TITLE/$title/;
  $html =~ s/\$CONTENT/$content/;
  
  return $html;
<p>
  }
</p>
<p>
  __DATA__
</p>

  </div>
  <div class="bottom">
    <!-- bottom -->

  </div>
</div>

        </div>
        <div class="side">
          <!-- side -->
<div class="side-list">
  <div class="side-list-title">
    メニュー
  </div>
  <ul>
    <li><a href="/blog/20190416153053.html">Windowsで個人ブログを作る</a></li>
    <li>Macで個人ブログを作る</li>
    <li>Linuxで個人ブログを作る</li>
  </ul>
</div>

        </div>
      </div>
      <div class="footer">
        <!-- footer -->
<a href="https://tutorial.perlzemi.com/">制作 Perlゼミ</a>

      </div>
    </div>
  </body>
</html>

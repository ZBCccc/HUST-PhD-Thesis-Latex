$pdf_mode = 5;          # 使用 xelatex 生成 PDF（模式 5 = xelatex）
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
$xdvipdfmx = 'xdvipdfmx -E -o %D %O %S';

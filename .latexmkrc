$pdf_mode = 5;          # 使用 xelatex 生成 PDF（模式 5 = xelatex）
$out_dir = 'output';

# 自动创建输出目录及其子目录
if ($out_dir ne '' && !-d $out_dir) {
    mkdir $out_dir;
}
foreach my $dir (qw(body/chapter body/appendix)) {
    my $full_dir = "$out_dir/$dir";
    if (!-d $full_dir) {
        use File::Path qw(make_path);
        make_path($full_dir);
    }
}

$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
$xdvipdfmx = 'xdvipdfmx -E -o %D %O %S';

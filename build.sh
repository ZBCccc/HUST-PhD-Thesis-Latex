#!/bin/bash

# 论文和答辩 Slide 编译脚本
# 用法: ./build.sh [thesis|slide|all]

set -e

THEMESIS_DIR="/Users/bytedance/code/personal/HUST-PhD-Thesis-Latex"
SLIDE_DIR="$THEMESIS_DIR/_ThesisBeamer"

# 加载 TeX 环境
eval "$(/usr/libexec/path_helper)"

build_thesis() {
    echo "📄 编译论文..."
    cd "$THEMESIS_DIR"
    mkdir -p output/body/chapter output/body/appendix

    echo "  第 1 次编译..."
    xelatex -interaction=nonstopmode -output-directory=output main.tex > /dev/null 2>&1

    echo "  处理参考文献..."
    bibtex output/main > /dev/null 2>&1 || true

    echo "  第 2 次编译..."
    xelatex -interaction=nonstopmode -output-directory=output main.tex > /dev/null 2>&1

    echo "  第 3 次编译..."
    xelatex -interaction=nonstopmode -output-directory=output main.tex > /dev/null 2>&1

    echo "✅ 论文编译完成: output/main.pdf"
}

build_slide() {
    echo "📊 编译答辩 Slide..."
    cd "$SLIDE_DIR"

    xelatex -interaction=nonstopmode slide.tex 2>&1 | tail -3
    xelatex -interaction=nonstopmode slide.tex 2>&1 | tail -3

    echo "✅ Slide 编译完成: _ThesisBeamer/slide.pdf"
}

case "${1:-all}" in
    thesis)
        build_thesis
        ;;
    slide)
        build_slide
        ;;
    all)
        build_thesis
        echo ""
        build_slide
        ;;
    *)
        echo "用法: $0 [thesis|slide|all]"
        echo "  thesis - 仅编译论文"
        echo "  slide  - 仅编译答辩 Slide"
        echo "  all    - 编译全部 (默认)"
        exit 1
        ;;
esac

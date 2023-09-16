# Simpletext_zhihu

由于 zhihu on vscode 对于公式的解析不够理想，我开发了这个简易的工具，让知乎文章写起来更轻松。

## 安装

下载本仓库并运行`python [main.py的路径] [md文件路径]`即可。  
本仓库不依赖任何第三方库，所以无需安装任何依赖。

## feature
主要是对公式做了改进。
1. 识别  
公式使用单个反引号包裹，inline代码块使用两个反引号包裹。公示的前反引号前加个a表示用align环境，加个m表示公式居中。  
不用再考虑$前后的空格，Simpletext_zhihu会自动调整好空格。
2. 语法  
特性语法可以参考`测试用例.md`和`入群测试解答.md`。并且这种语法基本完全兼容LaTeX。
# 个人项目使用方法（Task2）

1. 下载 /Task2(Personal experiment)/main 文件夹

2. 下载完成后，使用cmd进入: 你的下载路径/Task2(Personal experiment)/main/dist/main
3. 在上述路径下运行程序main.exe(main.exe -help获得帮助)

## 使用示例：

main.exe -help



main.exe -c \<file name>  --输出文件中某个英文文本文件中 26 字母出现的频率

main.exe -f \<file name>  --输出文件中所有不重复的单词

main.exe -d \<directory name>  --输出指定文件目录下每一个文件中所有不重复的单词

main.exe -d -s \<directory name>  --输出指定文件目录下每一个文件中所有不重复的单词

main.exe  -n  \<file name> \<number>--输出文件中的前 N 个最常出现的英语单词(如果不指定 N ,则输出所有英语单词)

main.exe -p \<file name> \<number>  --输出文件中英语词组(nlp实现，如果文件过大，需要稍微等待)

main.exe -v \<file name>  --输出文件中英语单词原型(nlp实现，如果文件过大，需要稍微等待)
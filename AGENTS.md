# AGENTS.md

This file provides guidance to the AI agent when working with code in this repository.

## 项目结构约定

- `Beginner/` — Level 1 题目（question_01 ~ question_05, question_23 ~ question_25）
- `Intermediate/` — Level 2 题目（question_06 ~ question_17, question_26 ~ question_49）
- `Advanced/` — Level 3 题目（question_18 ~ question_22, question_50 ~ question_100）
- 新题目按难度放入对应目录，文件名格式严格为 `question_XX.py`（两位数字，补零）

## 文件格式规范

每个题目文件**只包含题目描述注释，不含解答代码**（用户自行实现）：

```python
"""
问题：<中文题目描述>
示例输入：...（如有）
示例输出：...（如有）
提示：...（如有）
"""
```

- 统一使用多行 `"""..."""` docstring，不使用单行 docstring
- 注释内容为中文
- 文件内不预置任何实现代码

## Python 版本

使用 Python 3，禁止使用 Python 2 语法：
- 用 `input()` 不用 `raw_input()`
- 用 `print()` 不用 `print` 语句
- `map()`/`filter()` 返回迭代器，打印时需 `list()` 转换

## Commit 风格

参考已有提交信息，使用中文描述，例如：`Python 练习-类与生成器`

## 笔记生成

完成题目后可使用 `python-exercise-note` skill 自动生成练习笔记和概念笔记。

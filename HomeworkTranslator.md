# PDF Translator GUI

此代码提供了一个基于`tkinter`的GUI，用于翻译PDF文件。

## 导入

```python
import os, sys
import tkinter as tk
from tkinter import filedialog, messagebox
from translator.pdf_translator import PDFTranslator
```

## 主类：TranslatorGUI
此类创建一个GUI，允许用户选择PDF文件、选择输出格式，并触发翻译过程。
### 初始化方法
```python
def __init__(self, translator: PDFTranslator):
    super().__init__()
    self.translator = translator
    self.pdf_file_path = tk.StringVar()
    self.file_format = tk.StringVar(value="markdown")  # 默认选择 "markdown"
    self.create_widgets()
```
此方法初始化GUI，并设置默认的输出格式为"markdown"。

### 创建组件
```python
def create_widgets(self):
    ...

```
这个方法定义了GUI的所有组件，如标签、输入框、按钮等。

PDF选择
```python
label = tk.Label(frame, text="Select PDF:")
entry = tk.Entry(frame, textvariable=self.pdf_file_path, width=50)
browse_button = tk.Button(frame, text="Browse", command=self.select_pdf)
```

文件格式选择
```python
format_label = tk.Label(frame, text="File Format:")
formats = ["markdown", "pdf"]
option_menu = tk.OptionMenu(frame, self.file_format, *formats)
```

翻译按钮
```python
translate_button = tk.Button(frame, text="Translate", command=self.on_translate_click)
translate_button.grid(row=2, column=0, columnspan=3, pady=20)
```


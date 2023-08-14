import os, sys
import tkinter as tk
from tkinter import filedialog, messagebox

from translator.pdf_translator import PDFTranslator


class TranslatorGUI(tk.Tk):
    def __init__(self, translator: PDFTranslator):
        super().__init__()
        self.translator = translator
        self.pdf_file_path = tk.StringVar()
        self.file_format = tk.StringVar(value="markdown")  # 默认选择 "markdown"
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.master, padx=20, pady=20)
        frame.pack(padx=10, pady=10)

        label = tk.Label(frame, text="Select PDF:")
        label.grid(row=0, column=0, sticky=tk.W)

        entry = tk.Entry(frame, textvariable=self.pdf_file_path, width=50)
        entry.grid(row=0, column=1, padx=5)

        browse_button = tk.Button(frame, text="Browse", command=self.select_pdf)
        browse_button.grid(row=0, column=2)

        # 下拉选项组件
        format_label = tk.Label(frame, text="File Format:")
        format_label.grid(row=1, column=0, sticky=tk.W)

        formats = ["markdown", "pdf"]
        option_menu = tk.OptionMenu(frame, self.file_format, *formats)
        option_menu.grid(row=1, column=1, padx=5, sticky=tk.W)

        translate_button = tk.Button(frame, text="Translate", command=self.on_translate_click)
        # translate_button = tk.Button(frame, text="Translate", command=lambda: self.translator.translate_pdf(self.pdf_file_path, self.file_format))
        translate_button.grid(row=2, column=0, columnspan=3, pady=20)

    def select_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
        if file_path:
            self.pdf_file_path.set(file_path)

    def on_translate_click(self):
        # 获取文件路径和文件格式
        file_path = self.pdf_file_path.get()
        format_type = self.file_format.get()

        try:
            self.translator.translate_pdf(file_path, format_type)

            # 提取原文件名并生成提示消息
            file_name = file_path.split('/')[-1].replace('.pdf', '')  # 假设路径使用'/'分隔
            translated_file_name = f"{file_name}_translated.{format_type.lower()}"
            message = f"已翻译完，请查看'{translated_file_name}'文件"

            # 显示提示消息
            messagebox.showinfo("翻译完成", message)

        except Exception as e:
            messagebox.showerror("错误", f"翻译出错：{str(e)}")

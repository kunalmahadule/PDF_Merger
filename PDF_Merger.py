# Timestamp: 2:38:20

import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, END
import PyPDF2
import os

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger App")
        self.root.geometry("500x400")
        self.pdf_files = []

        self.listbox = Listbox(root, selectmode=tk.SINGLE, font=("Arial", 12), width=50)
        self.listbox.pack(pady=20)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Add PDFs", command=self.add_pdfs).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Remove Selected", command=self.remove_selected).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Move Up", command=self.move_up).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Move Down", command=self.move_down).grid(row=0, column=3, padx=5)

        tk.Button(root, text="Merge PDFs", command=self.merge_pdfs, font=("Arial", 12)).pack(pady=20)

    def add_pdfs(self):
        files = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF Files", "*.pdf")])
        for file in files:
            if file not in self.pdf_files:
                self.pdf_files.append(file)
                self.listbox.insert(END, os.path.basename(file))

    def remove_selected(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            self.listbox.delete(idx)
            del self.pdf_files[idx]

    def move_up(self):
        selected = self.listbox.curselection()
        if selected and selected[0] > 0:
            idx = selected[0]
            self.pdf_files[idx-1], self.pdf_files[idx] = self.pdf_files[idx], self.pdf_files[idx-1]
            txt = self.listbox.get(idx)
            self.listbox.delete(idx)
            self.listbox.insert(idx-1, txt)
            self.listbox.select_set(idx-1)

    def move_down(self):
        selected = self.listbox.curselection()
        if selected and selected[0] < len(self.pdf_files)-1:
            idx = selected[0]
            self.pdf_files[idx+1], self.pdf_files[idx] = self.pdf_files[idx], self.pdf_files[idx+1]
            txt = self.listbox.get(idx)
            self.listbox.delete(idx)
            self.listbox.insert(idx+1, txt)
            self.listbox.select_set(idx+1)

    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showwarning("No PDFs", "Koi PDF file select nahi ki gayi hai!")
            return
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")], title="Save Merged PDF")
        if not save_path:
            return
        merger = PyPDF2.PdfMerger()
        try:
            for file in self.pdf_files:
                with open(file, "rb") as f:
                    merger.append(PyPDF2.PdfReader(f))
            merger.write(save_path)
            messagebox.showinfo("Success", f"PDFs merge ho gayi!\nSaved as: {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Merge karte waqt error aayi:\n{e}")
        finally:
            merger.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()

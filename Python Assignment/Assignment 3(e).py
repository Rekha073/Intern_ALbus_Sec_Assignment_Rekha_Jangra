import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")

        self.current_path = tk.StringVar()
        self.current_path.set(os.getcwd())

        self.file_listbox = tk.Listbox(root, width=50, height=20)
        self.file_listbox.pack(side=tk.LEFT, padx=10, pady=10)

        scrollbar = tk.Scrollbar(root, orient="vertical")
        scrollbar.config(command=self.file_listbox.yview)
        scrollbar.pack(side=tk.LEFT, fill="y")

        self.file_listbox.config(yscrollcommand=scrollbar.set)

        self.refresh_files()

        button_frame = tk.Frame(root)
        button_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        tk.Button(button_frame, text="Select Directory", command=self.select_directory).pack(fill=tk.X)
        tk.Button(button_frame, text="Refresh", command=self.refresh_files).pack(fill=tk.X)
        tk.Button(button_frame, text="Copy", command=self.copy_file).pack(fill=tk.X)
        tk.Button(button_frame, text="Move", command=self.move_file).pack(fill=tk.X)
        tk.Button(button_frame, text="Delete", command=self.delete_file).pack(fill=tk.X)

    def refresh_files(self):
        self.file_listbox.delete(0, tk.END)
        path = self.current_path.get()
        for item in os.listdir(path):
            self.file_listbox.insert(tk.END, item)

    def select_directory(self):
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            self.current_path.set(selected_dir)
            self.refresh_files()

    def get_selected_file(self):
        selected_indices = self.file_listbox.curselection()
        if selected_indices:
            selected_index = selected_indices[0]
            return self.file_listbox.get(selected_index)

    def copy_file(self):
        selected_file = self.get_selected_file()
        if selected_file:
            source = os.path.join(self.current_path.get(), selected_file)
            destination = filedialog.askdirectory()
            if destination:
                shutil.copy(source, destination)
                messagebox.showinfo("File Manager", "File copied successfully.")
                self.refresh_files()

    def move_file(self):
        selected_file = self.get_selected_file()
        if selected_file:
            source = os.path.join(self.current_path.get(), selected_file)
            destination = filedialog.askdirectory()
            if destination:
                shutil.move(source, destination)
                messagebox.showinfo("File Manager", "File moved successfully.")
                self.refresh_files()

    def delete_file(self):
        selected_file = self.get_selected_file()
        if selected_file:
            if messagebox.askyesno("File Manager", "Are you sure you want to delete this file?"):
                path = os.path.join(self.current_path.get(), selected_file)
                os.remove(path)
                messagebox.showinfo("File Manager", "File deleted successfully.")
                self.refresh_files()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()

import pandas as pd
from tkinter import Tk, filedialog, messagebox, Button

class RemoveDuplicatesApp:
    def __init__(self, root):
        self.root = root
        #enlarge gui window size
        self.root.geometry("400x200")
        self.root.title("Remove Duplicate Reference Keys")

        #create select file button
        self.select_file_btn = Button(self.root, text="Select CSV File", command=self.select_file)
        self.select_file_btn.pack(pady=10)

        #create remove duplicates button
        self.remove_duplicates_btn = Button(self.root, text="Remove Duplicates and Save", command=self.remove_duplicates)
        self.remove_duplicates_btn.pack(pady=10)

        #create about button
        self.about_btn = Button(self.root, text="About", command=self.show_about)
        self.about_btn.pack(pady=10)

        self.selected_file = None

    def select_file(self):
        #ask user to select a file
        self.selected_file = filedialog.askopenfilename(
            title="Select a CSV File",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        if not self.selected_file:
            messagebox.showinfo("No File Selected", "Please select a CSV file.")
        else:
            messagebox.showinfo("File Selected", f"Selected file: {self.selected_file}")

    def remove_duplicates(self):
        #check if file is selected
        if not self.selected_file:
            messagebox.showerror("Error", "No file selected. Please select a file first.")
            return

        try:
            #read the csv file
            df = pd.read_csv(self.selected_file)

            if 'Reference Key' not in df.columns:
                messagebox.showerror("Error", "The selected file does not contain a 'Reference Key' column.")
                return

            #remove duplicate reference keys
            df_cleaned = df.drop_duplicates(subset=['Reference Key'], keep='first')

            #ask user where to save cleaned file
            save_path = filedialog.asksaveasfilename(
                title="Save Cleaned CSV",
                defaultextension=".csv",
                filetypes=[("CSV Files", "*.csv")]
            )

            if save_path:
                #save cleaned csv
                df_cleaned.to_csv(save_path, index=False)
                messagebox.showinfo("Success", f"Cleaned CSV saved to {save_path}")

        except Exception as e:
            #handle errors
            messagebox.showerror("Error", f"An error occurred: {e}")

    def show_about(self):
        #display about information
        messagebox.showinfo("About", "Remove Duplicate Reference Keys\nDeveloped by ODAT project.")

if __name__ == "__main__":
    root = Tk()
    app = RemoveDuplicatesApp(root)
    root.mainloop()

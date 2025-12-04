#!/usr/bin/env python3
"""
Job Filter Application
A GUI application to filter jobs based on similarity to user-provided job functions.
"""

import json
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from datetime import datetime
from difflib import SequenceMatcher
import re
import webbrowser


class JobFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Job Filter Application")
        self.root.geometry("1200x800")

        # Configuration file to store job functions
        self.config_file = "job_filter_config.json"
        self.jobs_data = []
        self.filtered_jobs = []
        self.job_functions_history = self.load_job_functions()
        self.sort_column = '_similarity_score'
        self.sort_reverse = True

        self.setup_ui()

    def load_job_functions(self):
        """Load previously used job functions from config file"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    data = json.load(f)
                    return data.get('job_functions', [])
            except Exception as e:
                print(f"Error loading config: {e}")
                return []
        return []

    def save_job_functions(self):
        """Save job functions to config file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump({'job_functions': self.job_functions_history}, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save configuration: {e}")

    def setup_ui(self):
        """Setup the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(6, weight=1)

        # Title
        title_label = ttk.Label(main_frame, text="Job Filter Application",
                                font=('Helvetica', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # File selection
        ttk.Label(main_frame, text="Select JSON File:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.file_path_var = tk.StringVar()
        file_entry = ttk.Entry(main_frame, textvariable=self.file_path_var, width=50)
        file_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_file).grid(row=1, column=2, pady=5)

        # Job function input
        ttk.Label(main_frame, text="Job Function/Type:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.job_function_var = tk.StringVar()
        job_entry = ttk.Entry(main_frame, textvariable=self.job_function_var, width=50)
        job_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        ttk.Button(main_frame, text="Filter Jobs", command=self.filter_jobs).grid(row=2, column=2, pady=5)

        # Previous job functions dropdown
        ttk.Label(main_frame, text="Previous Searches:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.previous_functions_var = tk.StringVar()
        self.previous_combo = ttk.Combobox(main_frame, textvariable=self.previous_functions_var,
                                           values=self.job_functions_history, width=47)
        self.previous_combo.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        self.previous_combo.bind('<<ComboboxSelected>>', self.on_previous_selected)
        ttk.Button(main_frame, text="Use Selected", command=self.use_previous_function).grid(row=3, column=2, pady=5)

        # Similarity threshold
        ttk.Label(main_frame, text="Similarity Threshold:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.threshold_var = tk.DoubleVar(value=0.3)
        threshold_frame = ttk.Frame(main_frame)
        threshold_frame.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        threshold_slider = ttk.Scale(threshold_frame, from_=0.0, to=1.0,
                                     variable=self.threshold_var, orient=tk.HORIZONTAL)
        threshold_slider.pack(side=tk.LEFT, fill=tk.X, expand=True)
        threshold_label = ttk.Label(threshold_frame, textvariable=self.threshold_var, width=5)
        threshold_label.pack(side=tk.LEFT, padx=5)

        # Results info
        self.results_info_var = tk.StringVar(value="No jobs loaded")
        ttk.Label(main_frame, textvariable=self.results_info_var,
                 font=('Helvetica', 10, 'bold')).grid(row=5, column=0, columnspan=3, pady=5)

        # Results display - Table view
        results_frame = ttk.LabelFrame(main_frame, text="Filtered Jobs", padding="5")
        results_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=3)
        results_frame.rowconfigure(1, weight=1)

        # Create Treeview with columns
        table_frame = ttk.Frame(results_frame)
        table_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(0, weight=1)

        # Define columns
        columns = ('similarity', 'title', 'company', 'location', 'employment_type', 'job_function', 'seniority')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', selectmode='browse')

        # Define headings and column properties
        column_config = {
            'similarity': ('Similarity', 100, True),
            'title': ('Job Title', 250, True),
            'company': ('Company', 150, True),
            'location': ('Location', 150, True),
            'employment_type': ('Type', 100, True),
            'job_function': ('Function', 150, True),
            'seniority': ('Level', 120, True)
        }

        for col, (heading, width, sortable) in column_config.items():
            self.tree.heading(col, text=heading,
                            command=lambda c=col: self.sort_by_column(c))
            self.tree.column(col, width=width, minwidth=50)

        # Add scrollbars
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        vsb.grid(row=0, column=1, sticky=(tk.N, tk.S))
        hsb.grid(row=1, column=0, sticky=(tk.W, tk.E))

        # Bind selection event
        self.tree.bind('<<TreeviewSelect>>', self.on_job_selected)
        self.tree.bind('<Double-1>', self.on_job_double_click)

        # Detail view panel
        detail_frame = ttk.LabelFrame(results_frame, text="Job Details", padding="5")
        detail_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(5, 0))
        detail_frame.columnconfigure(0, weight=1)
        detail_frame.rowconfigure(0, weight=1)

        self.detail_text = scrolledtext.ScrolledText(detail_frame, wrap=tk.WORD,
                                                     width=100, height=10)
        self.detail_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=7, column=0, columnspan=3, pady=10)

        ttk.Button(buttons_frame, text="Export Filtered Jobs",
                  command=self.export_results).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Open Job Link",
                  command=self.open_selected_job_link).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Clear Results",
                  command=self.clear_results).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Load File from scrappedjobs",
                  command=self.quick_load_scrappedjobs).pack(side=tk.LEFT, padx=5)

    def browse_file(self):
        """Browse for JSON file"""
        filename = filedialog.askopenfilename(
            title="Select Jobs JSON File",
            initialdir="./scrappedjobs",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            self.file_path_var.set(filename)
            self.load_jobs_file(filename)

    def quick_load_scrappedjobs(self):
        """Quick load files from scrappedjobs folder"""
        scrappedjobs_dir = "./scrappedjobs"
        if not os.path.exists(scrappedjobs_dir):
            messagebox.showerror("Error", "scrappedjobs folder not found!")
            return

        files = [f for f in os.listdir(scrappedjobs_dir)
                if os.path.isfile(os.path.join(scrappedjobs_dir, f))]

        if not files:
            messagebox.showerror("Error", "No files found in scrappedjobs folder!")
            return

        # Create selection window
        selection_window = tk.Toplevel(self.root)
        selection_window.title("Select File")
        selection_window.geometry("500x300")

        ttk.Label(selection_window, text="Select a file:",
                 font=('Helvetica', 12, 'bold')).pack(pady=10)

        listbox = tk.Listbox(selection_window, width=60, height=10)
        listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        for file in files:
            listbox.insert(tk.END, file)

        def select_file():
            selection = listbox.curselection()
            if selection:
                selected_file = listbox.get(selection[0])
                file_path = os.path.join(scrappedjobs_dir, selected_file)
                self.file_path_var.set(file_path)
                self.load_jobs_file(file_path)
                selection_window.destroy()

        ttk.Button(selection_window, text="Load", command=select_file).pack(pady=5)

    def load_jobs_file(self, filename):
        """Load jobs from JSON file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.jobs_data = json.load(f)

            self.results_info_var.set(f"Loaded {len(self.jobs_data)} jobs from {os.path.basename(filename)}")
            messagebox.showinfo("Success", f"Loaded {len(self.jobs_data)} jobs successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")
            self.jobs_data = []

    def on_previous_selected(self, event):
        """Handle selection of previous job function"""
        pass  # Just for visual feedback

    def use_previous_function(self):
        """Use selected previous function"""
        selected = self.previous_functions_var.get()
        if selected:
            self.job_function_var.set(selected)

    def calculate_similarity(self, text1, text2):
        """Calculate similarity between two strings"""
        if not text1 or not text2:
            return 0.0

        text1_lower = text1.lower()
        text2_lower = text2.lower()

        # Direct substring match gets higher score
        if text2_lower in text1_lower or text1_lower in text2_lower:
            return 0.8

        # Word-based matching
        words1 = set(re.findall(r'\w+', text1_lower))
        words2 = set(re.findall(r'\w+', text2_lower))

        common_words = words1.intersection(words2)
        if common_words:
            similarity = len(common_words) / max(len(words1), len(words2))
            return similarity

        # Fuzzy string matching
        return SequenceMatcher(None, text1_lower, text2_lower).ratio()

    def matches_job_function(self, job, job_function, threshold):
        """Check if job matches the job function"""
        job_function_lower = job_function.lower()

        # Extract relevant fields
        title = job.get('title', '')
        description = job.get('descriptionText', '')
        job_func = job.get('jobFunction', '')
        industries = job.get('industries', '')

        # Calculate similarity scores
        title_similarity = self.calculate_similarity(title, job_function)
        desc_similarity = self.calculate_similarity(description, job_function)
        func_similarity = self.calculate_similarity(job_func, job_function)
        industries_similarity = self.calculate_similarity(industries, job_function)

        # Keyword matching for engineering disciplines
        keywords = re.findall(r'\w+', job_function_lower)
        keyword_matches = 0
        full_text = f"{title} {description}".lower()

        for keyword in keywords:
            if len(keyword) > 3:  # Ignore very short words
                if keyword in full_text:
                    keyword_matches += 1

        keyword_score = keyword_matches / max(len(keywords), 1) if keywords else 0

        # Weighted average of similarities
        max_similarity = max(
            title_similarity * 2.0,  # Title is most important
            desc_similarity * 0.5,    # Description secondary
            func_similarity * 1.5,    # Job function important
            industries_similarity * 1.0,  # Industries relevant
            keyword_score * 1.2       # Keyword matching important
        )

        return max_similarity >= threshold, max_similarity

    def filter_jobs(self):
        """Filter jobs based on job function"""
        if not self.jobs_data:
            messagebox.showwarning("Warning", "Please load a jobs file first!")
            return

        job_function = self.job_function_var.get().strip()
        if not job_function:
            messagebox.showwarning("Warning", "Please enter a job function!")
            return

        # Save job function to history
        if job_function not in self.job_functions_history:
            self.job_functions_history.append(job_function)
            self.save_job_functions()
            self.previous_combo['values'] = self.job_functions_history

        threshold = self.threshold_var.get()
        self.filtered_jobs = []

        # Filter jobs
        for job in self.jobs_data:
            matches, similarity = self.matches_job_function(job, job_function, threshold)
            if matches:
                job_copy = job.copy()
                job_copy['_similarity_score'] = similarity
                self.filtered_jobs.append(job_copy)

        # Sort by similarity score
        self.filtered_jobs.sort(key=lambda x: x.get('_similarity_score', 0), reverse=True)

        # Display results
        self.display_results()

    def display_results(self):
        """Display filtered jobs in the table"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.detail_text.delete('1.0', tk.END)

        if not self.filtered_jobs:
            self.results_info_var.set("No matching jobs found!")
            self.detail_text.insert('1.0', "No jobs match your criteria. Try:\n"
                                            "1. Lowering the similarity threshold\n"
                                            "2. Using more general terms\n"
                                            "3. Trying different keywords")
            return

        self.results_info_var.set(f"Found {len(self.filtered_jobs)} matching jobs (click to view details, double-click to open link)")

        # Populate table
        for idx, job in enumerate(self.filtered_jobs):
            similarity = job.get('_similarity_score', 0)
            similarity_str = f"{similarity:.1%}"

            values = (
                similarity_str,
                job.get('title', 'N/A'),
                job.get('companyName', 'N/A'),
                job.get('location', 'N/A'),
                job.get('employmentType', 'N/A'),
                job.get('jobFunction', 'N/A'),
                job.get('seniorityLevel', 'N/A')
            )

            self.tree.insert('', tk.END, values=values, tags=(str(idx),))

    def sort_by_column(self, col):
        """Sort table by column"""
        if not self.filtered_jobs:
            return

        # Map display column names to job dictionary keys
        column_map = {
            'similarity': '_similarity_score',
            'title': 'title',
            'company': 'companyName',
            'location': 'location',
            'employment_type': 'employmentType',
            'job_function': 'jobFunction',
            'seniority': 'seniorityLevel'
        }

        sort_key = column_map.get(col, col)

        # Toggle sort direction if clicking the same column
        if self.sort_column == sort_key:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_column = sort_key
            self.sort_reverse = True if col == 'similarity' else False

        # Sort the filtered jobs
        self.filtered_jobs.sort(
            key=lambda x: x.get(sort_key, ''),
            reverse=self.sort_reverse
        )

        # Refresh the display
        self.display_results()

    def on_job_selected(self, event):
        """Handle job selection in table"""
        selection = self.tree.selection()
        if not selection:
            return

        # Get the index from tags
        item = selection[0]
        tags = self.tree.item(item, 'tags')
        if tags:
            idx = int(tags[0])
            job = self.filtered_jobs[idx]
            self.display_job_details(job)

    def display_job_details(self, job):
        """Display detailed information about selected job"""
        self.detail_text.delete('1.0', tk.END)

        similarity = job.get('_similarity_score', 0)

        details = f"{'='*100}\n"
        details += f"SIMILARITY SCORE: {similarity:.1%}\n"
        details += f"{'='*100}\n\n"
        details += f"📋 TITLE: {job.get('title', 'N/A')}\n\n"
        details += f"🏢 COMPANY: {job.get('companyName', 'N/A')}\n"
        details += f"📍 LOCATION: {job.get('location', 'N/A')}\n"
        details += f"💼 EMPLOYMENT TYPE: {job.get('employmentType', 'N/A')}\n"
        details += f"📊 SENIORITY LEVEL: {job.get('seniorityLevel', 'N/A')}\n"
        details += f"⚙️  JOB FUNCTION: {job.get('jobFunction', 'N/A')}\n"
        details += f"🏭 INDUSTRIES: {job.get('industries', 'N/A')}\n\n"

        # Salary info
        salary = job.get('salary', '') or job.get('salaryInfo', '')
        if salary:
            if isinstance(salary, list):
                salary = ', '.join(filter(None, salary))
            if salary:
                details += f"💰 SALARY: {salary}\n\n"

        # Link
        link = job.get('link', 'N/A')
        details += f"🔗 LINK: {link}\n\n"

        # Description
        desc = job.get('descriptionText', '')
        if desc:
            details += f"{'='*100}\n"
            details += f"📄 DESCRIPTION:\n"
            details += f"{'='*100}\n\n"
            details += desc

        self.detail_text.insert('1.0', details)

    def on_job_double_click(self, event):
        """Open job link in browser on double-click"""
        selection = self.tree.selection()
        if not selection:
            return

        item = selection[0]
        tags = self.tree.item(item, 'tags')
        if tags:
            idx = int(tags[0])
            job = self.filtered_jobs[idx]
            link = job.get('link', '')
            if link and link != 'N/A':
                try:
                    webbrowser.open(link)
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to open link: {e}")

    def open_selected_job_link(self):
        """Open the selected job's link in browser"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a job first!")
            return

        item = selection[0]
        tags = self.tree.item(item, 'tags')
        if tags:
            idx = int(tags[0])
            job = self.filtered_jobs[idx]
            link = job.get('link', '')
            if link and link != 'N/A':
                try:
                    webbrowser.open(link)
                    messagebox.showinfo("Success", "Job link opened in browser!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to open link: {e}")
            else:
                messagebox.showwarning("Warning", "No link available for this job!")

    def export_results(self):
        """Export filtered jobs to JSON file"""
        if not self.filtered_jobs:
            messagebox.showwarning("Warning", "No filtered jobs to export!")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        job_func_clean = re.sub(r'[^\w\s-]', '', self.job_function_var.get())
        job_func_clean = re.sub(r'[-\s]+', '_', job_func_clean)

        default_filename = f"filtered_jobs_{job_func_clean}_{timestamp}.json"

        filename = filedialog.asksaveasfilename(
            title="Save Filtered Jobs",
            initialfile=default_filename,
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        if filename:
            try:
                # Remove similarity score before export
                export_data = []
                for job in self.filtered_jobs:
                    job_copy = job.copy()
                    job_copy.pop('_similarity_score', None)
                    export_data.append(job_copy)

                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(export_data, f, indent=2, ensure_ascii=False)

                messagebox.showinfo("Success",
                                   f"Exported {len(export_data)} jobs to {os.path.basename(filename)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {e}")

    def clear_results(self):
        """Clear the results display"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.detail_text.delete('1.0', tk.END)
        self.filtered_jobs = []
        self.results_info_var.set("Results cleared")


def main():
    root = tk.Tk()
    app = JobFilterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

"""Student Grade Manager

A simple desktop application built with Python's standard-library Tkinter.
Student records are saved automatically to student_grades.csv beside this file.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, ttk

SUBJECTS = ("English", "Maths", "Science", "Social", "Computer")
CSV_FILE = Path(__file__).with_name("student_grades.csv")
CSV_COLUMNS = ("student_id", "name", *SUBJECTS)


@dataclass
class Student:
    student_id: str
    name: str
    marks: dict[str, float]

    @property
    def total(self) -> float:
        return sum(self.marks.values())

    @property
    def average(self) -> float:
        return self.total / len(SUBJECTS)

    @property
    def grade(self) -> str:
        # Grade is based on the average mark.
        average = self.average
        if average >= 90:
            return "A+"
        if average >= 80:
            return "A"
        if average >= 70:
            return "B"
        if average >= 60:
            return "C"
        if average >= 50:
            return "D"
        return "F"


class StudentGradeManager:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Student Grade Manager")
        self.root.geometry("1120x700")
        self.root.minsize(960, 620)

        self.students: dict[str, Student] = {}
        self.selected_id: str | None = None

        self.id_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.mark_vars = {subject: tk.StringVar() for subject in SUBJECTS}
        self.search_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Ready")
        self.summary_var = tk.StringVar(value="Students: 0   |   Class average: —")

        self._configure_style()
        self._build_ui()
        self._load_students()
        self._refresh_table()

    def _configure_style(self) -> None:
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure("Title.TLabel", font=("Arial", 21, "bold"), foreground="#172554")
        style.configure("Subtitle.TLabel", font=("Arial", 10), foreground="#475569")
        style.configure("Treeview", rowheight=29, font=("Arial", 10))
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        style.configure("Primary.TButton", font=("Arial", 10, "bold"))

    def _build_ui(self) -> None:
        outer = ttk.Frame(self.root, padding=18)
        outer.pack(fill="both", expand=True)

        header = ttk.Frame(outer)
        header.pack(fill="x", pady=(0, 14))
        ttk.Label(header, text="Student Grade Manager", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            header,
            text="Add students, enter marks, calculate grades, and keep records saved automatically.",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(4, 0))

        content = ttk.Panedwindow(outer, orient="horizontal")
        content.pack(fill="both", expand=True)

        form_frame = ttk.LabelFrame(content, text="Student details", padding=14)
        table_frame = ttk.LabelFrame(content, text="Student records", padding=12)
        content.add(form_frame, weight=1)
        content.add(table_frame, weight=3)

        self._build_form(form_frame)
        self._build_table(table_frame)

        footer = ttk.Frame(outer)
        footer.pack(fill="x", pady=(12, 0))
        ttk.Label(footer, textvariable=self.summary_var, font=("Arial", 10, "bold")).pack(side="left")
        ttk.Label(footer, textvariable=self.status_var, foreground="#64748b").pack(side="right")

    def _build_form(self, parent: ttk.LabelFrame) -> None:
        parent.columnconfigure(0, weight=1)

        ttk.Label(parent, text="Student ID").grid(row=0, column=0, sticky="w", pady=(0, 4))
        self.id_entry = ttk.Entry(parent, textvariable=self.id_var)
        self.id_entry.grid(row=1, column=0, sticky="ew", pady=(0, 12))

        ttk.Label(parent, text="Student name").grid(row=2, column=0, sticky="w", pady=(0, 4))
        ttk.Entry(parent, textvariable=self.name_var).grid(row=3, column=0, sticky="ew", pady=(0, 12))

        ttk.Separator(parent).grid(row=4, column=0, sticky="ew", pady=(0, 12))
        ttk.Label(parent, text="Subject marks (0–100)", font=("Arial", 10, "bold")).grid(
            row=5, column=0, sticky="w", pady=(0, 8)
        )

        for row, subject in enumerate(SUBJECTS, start=6):
            line = ttk.Frame(parent)
            line.grid(row=row, column=0, sticky="ew", pady=4)
            line.columnconfigure(1, weight=1)
            ttk.Label(line, text=subject, width=12).grid(row=0, column=0, sticky="w")
            ttk.Entry(line, textvariable=self.mark_vars[subject], width=12).grid(row=0, column=1, sticky="ew")

        button_row = 6 + len(SUBJECTS)
        ttk.Button(parent, text="Add student", style="Primary.TButton", command=self.add_student).grid(
            row=button_row, column=0, sticky="ew", pady=(16, 5)
        )
        ttk.Button(parent, text="Update selected", command=self.update_student).grid(
            row=button_row + 1, column=0, sticky="ew", pady=5
        )
        ttk.Button(parent, text="Delete selected", command=self.delete_student).grid(
            row=button_row + 2, column=0, sticky="ew", pady=5
        )
        ttk.Button(parent, text="Clear form", command=self.clear_form).grid(
            row=button_row + 3, column=0, sticky="ew", pady=5
        )

        ttk.Label(
            parent,
            text="Grade scale: A+ ≥90, A ≥80, B ≥70, C ≥60, D ≥50, F <50",
            wraplength=235,
            foreground="#64748b",
        ).grid(row=button_row + 4, column=0, sticky="w", pady=(14, 0))

    def _build_table(self, parent: ttk.LabelFrame) -> None:
        toolbar = ttk.Frame(parent)
        toolbar.pack(fill="x", pady=(0, 10))
        ttk.Label(toolbar, text="Search ID or name:").pack(side="left")
        search = ttk.Entry(toolbar, textvariable=self.search_var, width=25)
        search.pack(side="left", padx=(8, 6))
        self.search_var.trace_add("write", lambda *_: self._refresh_table())
        ttk.Button(toolbar, text="Clear search", command=lambda: self.search_var.set("")).pack(side="left")

        columns = ("student_id", "name", *SUBJECTS, "total", "average", "grade")
        self.tree = ttk.Treeview(parent, columns=columns, show="headings", selectmode="browse")
        headings = {
            "student_id": "Student ID",
            "name": "Name",
            "total": "Total",
            "average": "Average",
            "grade": "Grade",
        }
        for column in columns:
            self.tree.heading(column, text=headings.get(column, column))
            width = 88 if column not in ("name", "student_id") else (145 if column == "name" else 95)
            self.tree.column(column, width=width, minwidth=65, anchor="center")
        self.tree.column("name", anchor="w")

        vertical = ttk.Scrollbar(parent, orient="vertical", command=self.tree.yview)
        horizontal = ttk.Scrollbar(parent, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vertical.set, xscrollcommand=horizontal.set)
        self.tree.pack(side="top", fill="both", expand=True)
        vertical.place(in_=self.tree, relx=1.0, rely=0, relheight=1.0, anchor="ne")
        horizontal.pack(fill="x")
        self.tree.bind("<<TreeviewSelect>>", self._on_select)

    @staticmethod
    def _clean_number(value: float) -> str:
        return str(int(value)) if value.is_integer() else f"{value:g}"

    def _read_form(self) -> Student | None:
        student_id = self.id_var.get().strip()
        name = self.name_var.get().strip()
        if not student_id or not name:
            messagebox.showwarning("Missing details", "Please enter both Student ID and student name.")
            return None

        marks: dict[str, float] = {}
        for subject in SUBJECTS:
            raw = self.mark_vars[subject].get().strip()
            if not raw:
                messagebox.showwarning("Missing marks", f"Please enter marks for {subject}.")
                return None
            try:
                mark = float(raw)
            except ValueError:
                messagebox.showerror("Invalid marks", f"{subject} marks must be a number.")
                return None
            if not 0 <= mark <= 100:
                messagebox.showerror("Invalid marks", f"{subject} marks must be between 0 and 100.")
                return None
            marks[subject] = mark

        return Student(student_id=student_id, name=name, marks=marks)

    def add_student(self) -> None:
        student = self._read_form()
        if student is None:
            return
        if student.student_id in self.students:
            messagebox.showerror("Duplicate ID", "A student with this ID already exists.")
            return
        self.students[student.student_id] = student
        self._save_students()
        self._refresh_table()
        self.clear_form()
        self.status_var.set(f"Added {student.name}")

    def update_student(self) -> None:
        if self.selected_id is None:
            messagebox.showinfo("Select a student", "Select a student record in the table first.")
            return
        student = self._read_form()
        if student is None:
            return
        if student.student_id != self.selected_id and student.student_id in self.students:
            messagebox.showerror("Duplicate ID", "Another student already uses this ID.")
            return

        del self.students[self.selected_id]
        self.students[student.student_id] = student
        self._save_students()
        self._refresh_table()
        self.clear_form()
        self.status_var.set(f"Updated {student.name}")

    def delete_student(self) -> None:
        if self.selected_id is None:
            messagebox.showinfo("Select a student", "Select a student record in the table first.")
            return
        student = self.students.get(self.selected_id)
        if student and messagebox.askyesno("Confirm delete", f"Delete {student.name} ({student.student_id})?"):
            del self.students[self.selected_id]
            self._save_students()
            self._refresh_table()
            self.clear_form()
            self.status_var.set(f"Deleted {student.name}")

    def clear_form(self) -> None:
        self.selected_id = None
        self.id_var.set("")
        self.name_var.set("")
        for variable in self.mark_vars.values():
            variable.set("")
        for item in self.tree.selection():
            self.tree.selection_remove(item)
        self.id_entry.focus_set()

    def _on_select(self, _event: tk.Event) -> None:
        selection = self.tree.selection()
        if not selection:
            return
        student_id = selection[0]
        student = self.students.get(student_id)
        if student is None:
            return
        self.selected_id = student_id
        self.id_var.set(student.student_id)
        self.name_var.set(student.name)
        for subject in SUBJECTS:
            self.mark_vars[subject].set(self._clean_number(student.marks[subject]))
        self.status_var.set(f"Selected {student.name} — edit the form and choose Update selected")

    def _refresh_table(self) -> None:
        query = self.search_var.get().strip().casefold()
        for item in self.tree.get_children():
            self.tree.delete(item)

        visible_students = sorted(self.students.values(), key=lambda item: item.student_id.casefold())
        for student in visible_students:
            if query and query not in student.student_id.casefold() and query not in student.name.casefold():
                continue
            values = [student.student_id, student.name]
            values.extend(self._clean_number(student.marks[subject]) for subject in SUBJECTS)
            values.extend((self._clean_number(student.total), f"{student.average:.2f}", student.grade))
            self.tree.insert("", "end", iid=student.student_id, values=values)

        if self.students:
            class_average = sum(student.average for student in self.students.values()) / len(self.students)
            self.summary_var.set(f"Students: {len(self.students)}   |   Class average: {class_average:.2f}%")
        else:
            self.summary_var.set("Students: 0   |   Class average: —")

    def _load_students(self) -> None:
        if not CSV_FILE.exists():
            return
        try:
            with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student_id = (row.get("student_id") or "").strip()
                    name = (row.get("name") or "").strip()
                    if not student_id or not name:
                        continue
                    marks = {subject: float(row[subject]) for subject in SUBJECTS}
                    if all(0 <= mark <= 100 for mark in marks.values()):
                        self.students[student_id] = Student(student_id, name, marks)
        except (OSError, ValueError, KeyError) as error:
            messagebox.showerror(
                "Could not load saved records",
                f"The file {CSV_FILE.name} could not be read.\n\n{error}",
            )

    def _save_students(self) -> None:
        try:
            with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=CSV_COLUMNS)
                writer.writeheader()
                for student in sorted(self.students.values(), key=lambda item: item.student_id.casefold()):
                    row = {"student_id": student.student_id, "name": student.name}
                    row.update(student.marks)
                    writer.writerow(row)
        except OSError as error:
            messagebox.showerror("Save failed", f"Could not save records.\n\n{error}")
        else:
            self.status_var.set(f"Saved to {CSV_FILE.name}")


def main() -> None:
    root = tk.Tk()
    StudentGradeManager(root)
    root.mainloop()


if __name__ == "__main__":
    main()

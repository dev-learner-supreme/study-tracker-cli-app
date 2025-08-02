from textual.app import ComposeResult, App
from textual.widgets import Header, Footer, Static
import json

class StudyTracker(App):
    CSS_PATH = "style.css" # we'll implement this soon

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(self.load_progress_data(), id="progress")
        yield Footer()

    def load_progress_data(self) -> str:
        with open("data/progress.json", "r") as file:
            courses = json.load(file)
        output = ""    
        for course in courses:
            output += f"{course['course']}: {course['progress']}%\n"
        return output

if __name__ == "__main__":
    StudyTracker().run()        
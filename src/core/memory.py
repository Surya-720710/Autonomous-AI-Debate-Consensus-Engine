
import json
from pathlib import Path
from datetime import datetime

class DebateMemory:
    def __init__(self):
        self.transcript = []

    def add_entry(self, speaker: str, role: str, message: str):
        self.transcript.append({
            "timestamp": datetime.now().isoformat(),
            "speaker": speaker,
            "role": role,
            "message": message
        })

    def get_full_transcript_text(self) -> str:
        return "\n\n".join([f"**{entry['speaker']} ({entry['role']})**: {entry['message']}" for entry in self.transcript])

    def export_to_json(self, filepath: str = "debate_history.json"):
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.transcript, f, indent=4)

    def export_to_markdown(self, filepath: str = "debate_summary.md"):
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("# Debate Transcript & Consensus\n\n")
            for entry in self.transcript:
                f.write(f"### {entry['speaker']} ({entry['role']})\n")
                f.write(f"{entry['message']}\n\n---\n\n")

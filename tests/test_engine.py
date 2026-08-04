
import pytest
from src.core.memory import DebateMemory

def test_memory_add_entry():
    memory = DebateMemory()
    memory.add_entry(speaker="Debater Pro", role="PRO", message="I agree.")
    
    assert len(memory.transcript) == 1
    assert memory.transcript[0]["speaker"] == "Debater Pro"
    assert "Debater Pro (PRO): I agree." in memory.get_full_transcript_text()

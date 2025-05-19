from typing import List, Dict
from models.matrix_state import MatrixState


class SessionManager:
    def __init__(self, history: List[MatrixState], current_step: int):
        self.history = history
        self.current_step = current_step

    @classmethod
    def from_session(cls, data: Dict) -> "SessionManager":
        history = [MatrixState.from_dict(d) for d in data["history"]]
        return cls(history, data["current_step"])

    def to_session(self) -> Dict:
        return {
            "history": [s.to_dict() for s in self.history],
            "current_step": self.current_step
        }

    def current(self) -> MatrixState:
        return self.history[self.current_step]

    def push(self, matrix, query):
        # truncate future if branching
        self.history = self.history[:self.current_step + 1]
        self.history.append(MatrixState(matrix, query))
        self.current_step += 1

    def jump_to(self, index: int):
        if 0 <= index < len(self.history):
            self.current_step = index
        else:
            raise IndexError("Invalid jump index")
    
    def __eq__(self, other):
        return (
            isinstance(other, SessionManager)
            and self.history == other.history
            and self.current_step == other.current_step
        )

from typing import List, Dict
from models.session_manager import SessionManager
from views.formatter import QueryFormatter, MatrixFormatter
from utils import sympy_codec


class MatrixHistoryViewModel:
    def __init__(self, session_manager: SessionManager):
        self.entries: List[Dict] = []
        self.current_index = session_manager.current_step

        for i, state in enumerate(session_manager.history):
            entry = {
                "step": i,
                "matrix": sympy_codec.matrix_to_string_list(state.matrix),
                "matrix_latex": MatrixFormatter.to_latex(state.matrix),
                "query_latex": QueryFormatter.to_latex(state.query) if state.query else None,
                "query_human": QueryFormatter.to_human(state.query) if state.query else None,
                "is_current": (i == self.current_index)
            }
            self.entries.append(entry)

    def to_dict(self) -> Dict:
        return {
            "entries": self.entries,
            "current_step": self.current_index
        }

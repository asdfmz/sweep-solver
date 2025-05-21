from typing import List, Dict
from models.session_manager import SessionManager
from views.formatter import QueryFormatter, MatrixFormatter
from utils import sympy_codec
from services.query_normalizer import to_ui_indexed


class MatrixHistoryViewModel:
    def __init__(self, session_manager: SessionManager):
        self.entries: List[Dict] = []
        self.current_index = session_manager.current_step
        self.matrix_shape = session_manager.history[0].matrix.shape

        for i, state in enumerate(session_manager.history):
            display_query = to_ui_indexed(state.query) if state.query else None
            entry = {
                "step": i,
                "matrix": sympy_codec.matrix_to_string_list(state.matrix),
                "matrix_latex": MatrixFormatter.to_latex(state.matrix),
                "query_latex": QueryFormatter.to_latex(display_query) if display_query else None,
                "query_human": QueryFormatter.to_human(display_query) if display_query else None,
                "is_current": (i == self.current_index)
            }
            self.entries.append(entry)

    def to_dict(self) -> Dict:
        return {
            "entries": self.entries,
            "current_step": self.current_index, 
            "rows": self.matrix_shape[0],
            "cols": self.matrix_shape[1]
        }

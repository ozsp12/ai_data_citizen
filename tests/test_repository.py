"""Verificações estruturais dos materiais didáticos."""

from __future__ import annotations

import ast
import csv
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    def test_video_units_are_present(self) -> None:
        required = {
            "fast_track": "fast_track.ipynb",
            "quick_dirty_analytics": "precificacao_elasticidade.ipynb",
            "dados_em_painel": "grafico_animado_serie_temporal.ipynb",
        }
        for folder, notebook in required.items():
            self.assertTrue((ROOT / folder / "README.md").is_file())
            self.assertTrue((ROOT / folder / notebook).is_file())

    def test_notebook_json_and_code_syntax(self) -> None:
        notebooks = sorted(ROOT.rglob("*.ipynb"))
        self.assertTrue(notebooks)
        for path in notebooks:
            notebook = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(notebook.get("nbformat"), 4, path)
            for index, cell in enumerate(notebook.get("cells", [])):
                if cell.get("cell_type") != "code":
                    continue
                source = "".join(cell.get("source", []))
                python_source = "\n".join(
                    line for line in source.splitlines() if not line.lstrip().startswith("%")
                )
                ast.parse(python_source, filename=f"{path}:célula-{index}")

    def test_notebooks_contain_no_stored_errors(self) -> None:
        for path in ROOT.rglob("*.ipynb"):
            notebook = json.loads(path.read_text(encoding="utf-8"))
            errors = [
                output
                for cell in notebook.get("cells", [])
                for output in cell.get("outputs", [])
                if output.get("output_type") == "error"
            ]
            self.assertFalse(errors, f"Saída de erro armazenada em {path}")

    def test_fast_track_csv_schema(self) -> None:
        path = ROOT / "fast_track" / "df_fast_track.csv"
        with path.open(encoding="utf-8", newline="") as stream:
            reader = csv.reader(stream, delimiter=";")
            header = next(reader)
        expected = {
            "id", "sexo", "uf", "data_nascimento", "nota_matematica",
            "nota_fisica", "nota_quimica", "nota_ingles", "nota_portugues",
            "quantidade_filhos", "idade",
        }
        self.assertEqual(set(header), expected)


if __name__ == "__main__":
    unittest.main()

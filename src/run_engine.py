from os import getcwd

from qasm_api import QasmApi


def run(project_name):
    run_engine = QasmApi(project_name)
    run_engine.execute()
    run_engine.parse_result()
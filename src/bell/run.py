from os import getcwd

from qasm_api import QasmApi

run_engine = QasmApi(project_name="bell")
run_engine.execute()
run_engine.parse_result()
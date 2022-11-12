from coreapi.auth import BasicAuthentication
import json
from os import getcwd

from quantuminspire.api import QuantumInspireAPI

class QasmApi:
    def __init__(self, project_name: str):
        self.base_uri='https://api.quantum-inspire.com'
        self._load_creds()
        self.client = QuantumInspireAPI(self.base_uri, self.auth, f"mtvim-{project_name}")
        self.result = None
        self.code_path=f"{getcwd()}/src/{project_name}/{project_name}.qasm"


    def _load_creds(self):
        with open(".creds", "r") as file:
            creds = json.load(file)
            self.auth=BasicAuthentication(**creds)
    
    def execute(self, number_shots: int = 1024, backend_type: str = "QX-34-L"):
        code=self._load_qasm_file(self.code_path)
        backend_type=self.client.get_backend_type_by_name(backend_type)
        self.result = self.client.execute_qasm(code, backend_type, number_shots)
    
    def parse_result(self):
        if self.result.get('histogram', {}):
            print(self.result['histogram'])
        else:
            reason = self.result.get('raw_text', 'No reason in result structure.')
            print(f'Result structure does not contain proper histogram data. {reason}')

    def _load_qasm_file(self, qasm_file: str):
        with open(qasm_file, "r") as code:
            return code.read()

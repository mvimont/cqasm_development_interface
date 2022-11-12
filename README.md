# cqasm_development_interface

This repository provides a framework for writing and running cQASM files against any Quantum Inspire's emulator backend via their API.
It supplements the Web UI and Jupyter notebook-focused code examples for working with their API provided on the website with a framework
that aims to make it easier to:
* Include Quantum cQASM code as part of larger systems, making it easier to move back and forth between cQASM and Python.
* Save cQASM code as separate files with extension .qasm, instead of needing to explicitly define cQASM code as strings.

# Setup
* Auth
  * You'll first need at least a free 'basic' account with Quantum-Inspire. Sign-up can be done [here](https://www.quantum-inspire.com/account/create) 
  * During registration you'll provide a username and password, these will be used to authenticate against their API 

  * After registering with Quantum-Inspire and cloning this repository, add a .creds file to your project root
    * .creds is in the .gitignore to minimize risk of accidentally pushing with your private credentials.
    * In JSON format, enter in your credentials as below

    ```json
    {
      "username": "<Your Username>",
      "password": "<Your Password>"
    }
    ```

# Creating a new project
  * File directories in src look like the below:
  ```
  src/
  ├── project
     ├── project.qasm
     └── run.py
  ```
  * 'project' is the name of your specific project (e.g 'bell' or 'grover')
  * run.py invokes the core qasm_api and run_engine.py files that:
    * Load your cQASM code file
    * Authenticate against the Quantum Inspire API
    * Submits your cQASM code to the QI backend
    * Returns results

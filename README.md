# ProActive Python Client Codebase

This repository hosts the ProActive Python Client and its examples, enabling seamless interaction with the ProActive Scheduler and Resource Manager for automating workflow submission and management tasks directly from Python scripts.

## Repository Structure

- **`proactive-python-client`**: Contains the source code for the ProActive Python Client (SDK), facilitating the integration with the ProActive Scheduler. This SDK allows you to connect, submit jobs, manage tasks, and handle data spaces directly through Python.
- **`proactive-python-client-examples`**: A collection of examples demonstrating various features and capabilities of the ProActive Python Client. These examples serve as a practical guide to get started with the SDK.

## Getting Started

### Prerequisites

- Python version 3.5 or later.
- Java 8 or 11.
- Access to a ProActive Scheduler instance.

### Installation

You can install the ProActive Python Client directly from PyPI using pip:

```bash
pip install --upgrade proactive
```

For the latest features and bug fixes, you can also install directly from this repository:

```bash
pip install --upgrade --pre proactive
```

### Quick Example

Connecting to a ProActive Scheduler and submitting a simple job:

```python
from proactive import ProActiveGateway

gateway = ProActiveGateway('https://try.activeeon.com:8443')
gateway.connect(username='admin', password='admin')

# Creating a ProActive job
job = gateway.createJob()
job.setJobName("SimpleJob")

# Creating a Python task
task = gateway.createPythonTask()
task.setTaskName("SimpleTask")
task.setTaskImplementation("""
print('Hello from ProActive!')
""")

# Adding the task to the job and submitting the job
job.addTask(task)
jobId = gateway.submitJob(job)
print(f"Job submitted with id {jobId}")

# Disconnecting
gateway.close()
```

## Documentation

For full documentation of the ProActive Python Client, visit [our documentation site](https://proactive-python-client.readthedocs.io).

## Examples

For detailed examples, check the `proactive-python-client-examples` directory. Each example demonstrates different features and use cases of the ProActive Python Client.

## Contributing

Contributions to both the SDK and the examples are welcome. Please refer to the README files in the respective directories for more information on contributing.

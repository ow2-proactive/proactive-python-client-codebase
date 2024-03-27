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

### Creating a Job with the Proactive Python SDK

The Proactive Python SDK provides a convenient way to create and submit jobs to the ProActive Scheduler. Here's a step-by-step guide:

#### 1. Import the SDK

```python
from proactive import getProActiveGateway
```

#### 2. Connect to the ProActive Server

```python
gateway = getProActiveGateway()
```

This function automatically looks for a `.env` file with your ProActive credentials. If it doesn't exist, it will prompt you to enter the server URL, username, and password.

#### 3. Create a Job

```python
job = gateway.createJob("MyJobName")
```

Replace "MyJobName" with the desired name for your job.

#### 4. Add Tasks to the Job

You can add various types of tasks to your job using the gateway.createTask or gateway.createPythonTask methods. Here's an example of adding a Python task:

```python
task = gateway.createPythonTask("MyTaskName")
task.setTaskImplementation("print('Hello from ProActive!')")
job.addTask(task)
```

#### 5. (Optional) Configure Additional Settings

- Variables: You can add job-level or task-level variables using `job.addVariable` and `task.addVariable`.
- Dependencies: Set dependencies between tasks using `task.addDependency`.
- Fork Environment: Configure the execution environment using `task.setForkEnvironment`.
- Selection Script: Control where the task runs using `task.setSelectionScript`.
- Pre or Post scripts: Add scripts that will run before and after the task execution using `task.setPreScript` or `task.setPostScript`.

#### 6. Submit the Job

```python
job_id = gateway.submitJob(job)
```

This submits the job to the ProActive Scheduler and returns the job ID for tracking.

#### 7. Monitor and Retrieve Results

You can monitor the job status using `gateway.getJobStatus(job_id)` and retrieve the job output using `gateway.getJobOutput(job_id)`.

#### 8. Close the Connection

```python
gateway.close()
```

This disconnects from the ProActive server and cleans up resources.

Remember to replace the placeholders with your actual job and task names, and customize the task implementation with your desired Python code.

For more detailed examples and advanced features, refer to the Proactive Python Client documentation and the examples repository mentioned in the provided text.

## Quick Start Example

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

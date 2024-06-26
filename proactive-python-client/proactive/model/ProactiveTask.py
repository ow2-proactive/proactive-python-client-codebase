import cloudpickle
import codecs

from .ProactiveScriptLanguage import *
from .ProactiveSelectionScript import *
from .ProactiveRuntimeEnv import *

class ProactiveTask(object):
    """
    Represents a generic proactive task

    script_language (ProactiveScriptLanguage)
    fork_environment (ProactiveForkEnv)
    task_name (string)
    task_implementation (string)
    generic_information (map)
    input_files (list)
    output_files (list)
    dependencies (list[ProactiveTask])
    pre_script (ProactivePreScript)
    post_script (ProactivePostScript)
    flow_script (ProactiveFlowScript)
    flow_block (ProactiveFlowBlock)
    """

    def __init__(self, script_language=None, task_name=''):
        self.script_language = script_language
        self.fork_environment = None
        self.selection_script = None
        self.task_name = task_name
        self.task_implementation = ''
        self.task_implementation_url = None
        self.variables = {}
        self.generic_information = {}
        self.input_files = []
        self.output_files = []
        self.dependencies = []
        self.description = []
        self.pre_script = None
        self.post_script = None
        self.flow_script = None
        self.flow_block = None
        self.precious_result = False

    def __str__(self):
        return self.getTaskName()

    def __repr__(self):
        return self.getTaskName()

    def setScriptLanguage(self, script_language):
        self.script_language = script_language

    def getScriptLanguage(self):
        return self.script_language

    def setPreciousResult(self, precious_result):
        self.precious_result = precious_result

    def getPreciousResult(self):
        return self.precious_result

    def setForkEnvironment(self, fork_environment):
        self.fork_environment = fork_environment

    def getForkEnvironment(self):
        return self.fork_environment

    def hasForkEnvironment(self):
        return True if self.fork_environment is not None else False

    def setRuntimeEnvironment(self, type=None, image=None, nvidia_gpu=None, mount_host_path=None, mount_container_path=None, rootless=None, isolation=None, no_home=None, host_network=None, verbose=None):
        """
        Defines and sets the runtime environment for executing a task within a containerized environment.
        Parameters:
        - type (str): Specifies the type of container technology to use for running the task. 
        Options include "docker", "podman", "singularity", or any other value to indicate a non-containerized execution.
        - image (str): The container image to use for running the task. Ensure that the 'py4j' Python package is available in the specified image.
        - nvidia_gpu (bool): Whether to enable NVIDIA GPU support within the container. Automatically set to False if no NVIDIA GPUs are present.
        - mount_host_path (str): The host machine path to mount into the container, providing the container access to specific directories or files from the host.
        - mount_container_path (str): The path inside the container where the host's file system (or a part of it) specified by `mount_host_path` will be accessible.
        - rootless (bool): Enables or disables rootless mode for the container execution, applicable to all container types (default False).
        - isolation (bool): Enables or disables isolation mode specifically for Singularity containers (default False). This parameter is only applicable if 'type' is set to "singularity".
        - no_home (bool): When set to True, the user's home directory is not mounted inside the container if the home directory is not the current working directory. Only applicable to Singularity containers (default False).
        - host_network (bool): Configures the container to use the host's network stack directly, bypassing the default or custom network namespaces (default False).
        - verbose (bool): Enables verbose output for the container runtime environment setup process (default False).
        """
        self.fork_environment = ProactiveRuntimeEnv().create(type, image, nvidia_gpu, mount_host_path, mount_container_path, rootless, isolation, no_home, host_network, verbose)

    def setSelectionScript(self, selection_script):
        self.selection_script = selection_script

    def getSelectionScript(self):
        return self.selection_script

    def hasSelectionScript(self):
        return True if self.selection_script is not None else False

    def setTaskName(self, task_name):
        self.task_name = task_name

    def getTaskName(self):
        return self.task_name

    def setTaskImplementationFromURL(self, task_url):
        self.task_implementation_url = task_url
        self.task_implementation = ''

    def getTaskImplementationFromURL(self):
        return self.task_implementation_url

    def setTaskImplementationFromFile(self, task_file):
        if os.path.exists(task_file):
            with open(task_file, 'r') as content_file:
                self.setTaskImplementation(content_file.read())

    def setTaskImplementation(self, task_implementation):
        self.task_implementation = "\n"
        self.task_implementation += task_implementation
        self.task_implementation_url = None

    def getTaskImplementation(self):
        return self.task_implementation

    def addVariable(self, key, value):
        self.variables[key] = value

    def getVariables(self):
        return self.variables

    def hasVariables(self):
        return True if self.variables else False

    def removeVariable(self, key):
        del self.variables[key]

    def clearVariables(self):
        self.variables.clear()

    def addGenericInformation(self, key, value):
        self.generic_information[key] = value

    def getGenericInformation(self):
        return self.generic_information

    def removeGenericInformation(self, key):
        del self.generic_information[key]

    def clearGenericInformation(self):
        self.generic_information.clear()

    def addInputFile(self, input_file):
        self.input_files.append(input_file)

    def removeInputFile(self, input_file):
        self.input_files.remove(input_file)

    def clearInputFiles(self):
        self.input_files.clear()

    def getInputFiles(self):
        return self.input_files

    def addOutputFile(self, output_file):
        self.output_files.append(output_file)

    def removeOutputFile(self, output_file):
        self.output_files.remove(output_file)

    def clearOutputFiles(self):
        self.output_files.clear()

    def getOutputFiles(self):
        return self.output_files

    def addDependency(self, task):
        self.dependencies.append(task)

    def removeDependency(self, task):
        self.dependencies.remove(task)

    def clearDependencies(self):
        self.dependencies.clear()

    def getDependencies(self):
        return self.dependencies

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description

    def setPreScript(self, pre_script):
        self.pre_script = pre_script

    def getPreScript(self):
        return self.pre_script

    def hasPreScript(self):
        return True if self.pre_script is not None else False

    def setPostScript(self, post_script):
        self.post_script = post_script

    def getPostScript(self):
        return self.post_script

    def hasPostScript(self):
        return True if self.post_script is not None else False

    def setFlowScript(self, flow_script):
        self.flow_script = flow_script

    def getFlowScript(self):
        return self.flow_script

    def hasFlowScript(self):
        return True if self.flow_script is not None else False

    def setFlowBlock(self, flow_block):
        self.flow_block = flow_block

    def getFlowBlock(self):
        return self.flow_block

    def hasFlowBlock(self):
        return True if self.flow_block is not None else False


class ProactivePythonTask(ProactiveTask):
    """
    Represents a proactive python task
    """

    def __init__(self, task_name='', default_python='python3'):
        super(ProactivePythonTask, self).__init__(ProactiveScriptLanguage().python(), task_name)
        self.addGenericInformation("PYTHON_COMMAND", default_python)

    def setTaskExecutionFromFile(self, task_file, parameters=[], displayTaskResultOnScheduler=True):
        if os.path.exists(task_file):
            params_string = ' '.join(parameters)
            task_implementation = "import subprocess"
            task_implementation += "\n"
            task_implementation += "print('Running " + task_file + " with " + params_string + " as parameters...')"
            task_implementation += "\n"
            task_implementation += "result = subprocess.check_output('python " + task_file + " " + params_string + "', shell=True).strip()"
            task_implementation += "\n"
            if displayTaskResultOnScheduler:
                task_implementation += "print('-' * 10)"
                task_implementation += "\n"
                task_implementation += "print(result.decode('ascii'))"
                task_implementation += "\n"
                task_implementation += "print('-' * 10)"
                task_implementation += "\n"
            task_implementation += "print('Finished')"
            self.setTaskImplementation(task_implementation)
            self.addInputFile(task_file)

    def setTaskExecutionFromLambdaFunction(self, lambda_function):
        pickled_lambda = codecs.encode(cloudpickle.dumps(lambda_function), "base64")
        task_implementation = "import pickle"
        task_implementation += "\n"
        task_implementation += "import codecs"
        task_implementation += "\n"
        task_implementation += "result = pickle.loads(codecs.decode(%s, \"base64\"))()" % pickled_lambda
        task_implementation += "\n"
        task_implementation += "print('result: ', result)"
        self.setTaskImplementation(task_implementation)


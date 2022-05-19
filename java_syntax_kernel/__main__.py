from ipykernel.kernelapp import IPKernelApp
from . import JavaKernel

IPKernelApp.launch_instance(kernel_class=JavaKernel)

from subprocess import Popen, PIPE
from distutils import spawn
import os, sys
import platform


def gpu():
    if platform.system() == "Windows":
        try:
            nvidia_smi = spawn.find_executable('nvidia-sm')
        except FileNotFoundError as fn:
            print(fn)
            sys.exit(1)

        if nvidia_smi is None:
            nvidia_smi = "%s\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.exe" % os.environ['systemdrive']
    else:
        nvidia_smi = "nvidia-smi"

    # Get ID, processing and memory utilization for all GPUs (deviceIds, uuid, gpuUtil, memTotal, memUsed, memFree,
    # driver,gpu_name,serial,display_mode,display_active, temp_gpu)
    try:
        p = Popen([nvidia_smi,
                   "--query-gpu=index,uuid,utilization.gpu,memory.total,memory.used,memory.free,driver_version,name,"
                   "gpu_serial,display_active,display_mode,temperature.gpu",
                   "--format=csv,noheader,nounits"], stdout = PIPE)
        stdout, stderr = p.communicate()
        return stdout.decode('UTF-8').split(',')
    except SystemError as stderr:
        print('Unable to establish a communication with GPU', stderr)
        sys.exit(1)
    except FileNotFoundError as fn:
        print(fn)
        sys.exit(1)


gpu()

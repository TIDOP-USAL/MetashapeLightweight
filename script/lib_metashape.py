import Metashape


def get_gpus():
    gpus = Metashape.app.enumGPUDevices()
    return gpus

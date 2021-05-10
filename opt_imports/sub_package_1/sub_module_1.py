import numpy as np

__all__ = ['get_numpy_array']

def _get_mdtraj_version_private():
    import mdtraj as md
    return md.__version__

def get_numpy_array():
    return np.random.random((5, 5))

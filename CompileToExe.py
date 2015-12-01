# -*- coding: utf-8 -*-
import sys
from cx_Freeze import setup, Executable

includes = ["Elements/", "Elements/Interface/", "Elements/Tab", "IO", "Elements"]
include_files = ["settings.json",
                 "Elements/Icon - 16x16.png",
                 "Elements/Icon - 24x24.png",
                 "Elements/Icon - 32x32.png",
                 "Elements/Icon - 48x48.png",
                 "Elements/Icon - 256x256.png",
                 "staging"]
buildOptions = dict(
    create_shared_zip=False,
    append_script_to_exe=True,
    includes=includes,
    include_files=include_files
)

executables = [
    Executable(
        script='FileTransfer.py',
        targetName='DateiAustausch.exe',
        base="Win32GUI" # THIS ONE IS IMPORTANT FOR GUI APPLICATION
        # icon='Icon-16x16.png'
    )
]

setup(
    name="DateiAustausch",
    version="1.0",
    description="Oisin's Upload&Download Programm",
    options=dict(build_exe=buildOptions),
    executables=executables
)
import PyInstaller.__main__

PyInstaller.__main__.run([
    'PhasePhinder_source.py',
    '--onefile',
    '--icon=phasy_new.ico',
    '--windowed'
])
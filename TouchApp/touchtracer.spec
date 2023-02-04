# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT
from kivy_deps import sdl2, glew
block_cipher = None



a = Analysis(
    ['examples-path\\demo\\touchtracer\\main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('examples-path\\demo\\touchtracer\\images', 'images'),
    ],
    hiddenimports=[
        'kivy',
        'kivy.deps.sdl2',
        'kivy.deps.glew',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='touchtracer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['examples-path\\demo\\touchtracer\\icon.ico'],
)
coll = COLLECT(exe, Tree('examples-path\\demo\\touchtracer\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               name='touchtracer')

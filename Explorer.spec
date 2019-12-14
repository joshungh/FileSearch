# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Explorer.py'],
             pathex=['C:\\Users\\GraeL\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\PyQt5', 'C:\\Users\\GraeL\\PycharmProjects\\Class9\\File_explorer'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Explorer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )

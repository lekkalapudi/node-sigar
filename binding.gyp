{
  'targets': [
    {
      'target_name': 'sigar',
      'sources': [
        'src/node_sigar.cc',
        'deps/sigar/src/sigar.c',
        'deps/sigar/src/sigar_cache.c',
        'deps/sigar/src/sigar_fileinfo.c',
        'deps/sigar/src/sigar_format.c',
        'deps/sigar/src/sigar_ptql.c',
        'deps/sigar/src/sigar_signal.c',
        'deps/sigar/src/sigar_util.c'
      ],
      'include_dirs': [ 'deps/sigar/include' ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'conditions': [
        [ 'OS=="linux"', {
          'sources': [ 'deps/sigar/src/os/linux/linux_sigar.c' ],
          'include_dirs': [ 'deps/sigar/src/os/linux' ]
        }],
        [ 'OS=="win"', {
          'sources': [ 'deps/sigar/src/os/win32/win32_sigar.c' ],
          'include_dirs': [ 'deps/sigar/src/os/win32' ]
        }],
        ['OS=="mac"', {
          'sources': [ 'deps/sigar/src/os/darwin/darwin_sigar.c' ],
          'include_dirs': [ 'deps/sigar/src/os/darwin' ],
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'OTHER_CFLAGS': [
              '-DDARWIN',
              '-DDARWIN_HAS_LIBPROC_H'
            ]
          }
        }]
      ]
    }
  ]
}

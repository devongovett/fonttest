{
    'targets': [
        {
            'target_name': 'ragel',
            'type': 'executable',
            'cflags': ['-std=gnu++98'],
            'sources': [
                'ragel/ragel/cdcodegen.cpp',
                'ragel/ragel/cdfflat.cpp',
                'ragel/ragel/cdfgoto.cpp',
                'ragel/ragel/cdflat.cpp',
                'ragel/ragel/cdftable.cpp',
                'ragel/ragel/cdgoto.cpp',
                'ragel/ragel/cdipgoto.cpp',
                'ragel/ragel/cdsplit.cpp',
                'ragel/ragel/cdtable.cpp',
                'ragel/ragel/common.cpp',
                'ragel/ragel/cscodegen.cpp',
                'ragel/ragel/csfflat.cpp',
                'ragel/ragel/csfgoto.cpp',
                'ragel/ragel/csflat.cpp',
                'ragel/ragel/csftable.cpp',
                'ragel/ragel/csgoto.cpp',
                'ragel/ragel/csipgoto.cpp',
                'ragel/ragel/cssplit.cpp',
                'ragel/ragel/cstable.cpp',
                'ragel/ragel/dotcodegen.cpp',
                'ragel/ragel/fsmap.cpp',
                'ragel/ragel/fsmattach.cpp',
                'ragel/ragel/fsmbase.cpp',
                'ragel/ragel/fsmgraph.cpp',
                'ragel/ragel/fsmmin.cpp',
                'ragel/ragel/fsmstate.cpp',
                'ragel/ragel/gendata.cpp',
                'ragel/ragel/gocodegen.cpp',
                'ragel/ragel/gofflat.cpp',
                'ragel/ragel/gofgoto.cpp',
                'ragel/ragel/goflat.cpp',
                'ragel/ragel/goftable.cpp',
                'ragel/ragel/gogoto.cpp',
                'ragel/ragel/goipgoto.cpp',
                'ragel/ragel/gotable.cpp',
                'ragel/ragel/gotablish.cpp',
                'ragel/ragel/inputdata.cpp',
                'ragel/ragel/javacodegen.cpp',
                'ragel/ragel/main.cpp',
                'ragel/ragel/mlcodegen.cpp',
                'ragel/ragel/mlfflat.cpp',
                'ragel/ragel/mlfgoto.cpp',
                'ragel/ragel/mlflat.cpp',
                'ragel/ragel/mlftable.cpp',
                'ragel/ragel/mlgoto.cpp',
                'ragel/ragel/mltable.cpp',
                'ragel/ragel/parsedata.cpp',
                'ragel/ragel/parsetree.cpp',
                'ragel/ragel/rbxgoto.cpp',
                'ragel/ragel/redfsm.cpp',
                'ragel/ragel/rlparse.cpp',
                'ragel/ragel/rlscan.cpp',
                'ragel/ragel/rubycodegen.cpp',
                'ragel/ragel/rubyfflat.cpp',
                'ragel/ragel/rubyflat.cpp',
                'ragel/ragel/rubyftable.cpp',
                'ragel/ragel/rubytable.cpp',
                'ragel/ragel/xmlcodegen.cpp',
            ],
            'include_dirs': [
                'autoconf_generated',
	        'ragel/aapl',
	        'ragel/ragel'
            ]
        }
    ]
}

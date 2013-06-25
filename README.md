# ardeclare

An implementation of the interface provided by the cmdln module but
using argparse to provide the option/arg heavy parsing.

Credit for this code goes foremost to Shakeeb Alireza, code was
initially found: [argdeclare: declarative interface to argparse](http://code.activestate.com/recipes/576935-argdeclare-declarative-interface-to-argparse/)

# Usage

    from argdeclare import Commander, option_group, option, arg
    
    def test():
        # only for options which are repeated across different funcs
        common_options = option_group(
            option('-t', '--type', action='store', help='specify type of package'),
            arg('package', help='package to be (un)installed'),
            option('--log', '-l', action='store_true', help='log is on')
        )
        
        class Application(Commander):
            'a description of the test app'
            name = 'app1'
            version = '0.1'
            default_args = ['install', '--help']
            
            @option('--log', '-l', action='store_true', help='log is on')
            @arg('pattern', help="pattern to delete")
            def do_delete(self, options):
                "help text for delete subcmd"
                print(options)
    
            @option('-f', '--force', action='store_true',
                            help='force through installation')
            @common_options
            def do_install(self, options):
                "help text for install subcmd"
                print(options)
    
            @common_options
            def do_uninstall(self, options):
                "help text for uninstall subcmd"
                print(options)
    
        app = Application()
        app.cmdline()
    
    if __name__ == '__main__':
        test()


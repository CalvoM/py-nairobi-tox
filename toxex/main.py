import mlib_generator as mlibg
import ui

gen = mlibg.MadLibsGenerator()
cli = ui.UI(gen)
cli.run()

import gtk
from . import JsonschemaEditor


def main():
    main_window = gtk.Window()
    schema_editor = JsonschemaEditor(schema={}, data=None)

    main_window.add(schema_editor.widget)
    main_window.show()

    # Quit program when main window is closed.
    main_window.connect('destroy', lambda *args: gtk.main_quit())

    gtk.main()


if __name__ == '__main__':
    main()

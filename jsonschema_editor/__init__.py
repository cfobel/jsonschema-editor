from collections import OrderedDict

from pygtkhelpers.delegates import SlaveView
from pygtkhelpers.utils import gsignal
import gtk


class JsonschemaEditor(SlaveView):
    '''
    Slave widget that can added to another parent view.
    '''
    gsignal('changed', object)  # Emit when validated change applied to data.
    # TODO In validation code, add something like the following:
    #
    #     self.emit('changed', {'row': <index of changed row>,
    #                           'column_name': <column name>,
    #                           'original_value': <original value>,
    #                           'new_value': <new value>})
    #
    # Other code can then listen and react to this signal.
    #
    # For example:
    #
    #     schema_editor = JsonschemaEditor(...)
    #     ...
    #     schema_editor.connect('changed', on_changed)
    #
    # where `on_changed` is a function of the form:
    #
    #     def on_changed(jsonschema_editor, changed_info):
    #         # First argument is the `JsonschemaEditor` instance that emitted
    #         # the signal.
    #         print changed_info['row']
    #         print changed_info['column_name']
    #         print changed_info['original_value']
    #         print changed_info['new_value']
    #         print jsonschema_editor.to_frame()

    def __init__(self, schema, data=None):
        '''
        Args
        ----

            schema (dict) : jsonschema definition.
            data (pandas.DataFrame) : Initial data (optional).
        '''
        self.schema = schema
        self.data = data
        super(JsonschemaEditor, self).__init__()

    def create_ui(self):
        '''
        Called automatically during construction.  Prior to this call, a parent
        `gtk.VBox` widget named `self.widget` is automatically created.

        In general:

         1. Add all widgets to `self.widget` as needed.
         2. Show widgets as needed (e.g., `self.widget.show_all()`).

        Specifically for the jsonschema editor:

         1. Create `gtk.TreeView`.
         2. Create list store.
         3. Fill list store with data from `self.data` data frame.
         4. Create/add columns corresponding to properties from `self.schema`.
         5. Add callbacks to cell renderers to validate changes to the tree
            view.
        '''
        # Create `gtk.TreeView`.
        self.tree_view = gtk.TreeView()

        # TODO Create list store matching property data types from
        # `self.schema`.
        # ## Iterate through schema fields in a defined order ##
        #  - Order fields by `index` property (where it exists).
        #  - Note that `OrderedDict` maintains order that items are *inserted*.
        #  - Use:
        #      * `ordered_properties.iteritems()` to iterate through `(key,
        #        value)` pairs in order.
        #      * `ordered_properties.keys()` and `ordered_properties.values()`
        #        are in the order of insertion.
        ordered_properties = \
            OrderedDict(sorted(self.schema['properties'].items(),
                               key=lambda v: v[1].get('index', -1)))

        # TODO Fill list store with data from `self.data` data frame (if
        # necessary).
        if self.data is not None:
            pass

        # TODO Create/add columns corresponding to properties from
        # `self.schema`.
        pass  # TODO Use existing code...

        # TODO Add callbacks to cell renderers to validate changes to the tree
        # view.
        pass  # TODO Use existing code...

        # Add all widgets to `self.widget` as needed.
        self.widget.pack_start(child=self.tree_view, expand=True, fill=True,
                               padding=0)

        # Show widgets as needed.
        self.widget.show_all()

    def to_frame(self):
        '''
        Returns `pandas.DataFrame` with contents of `ListStore`.
        '''
        # TODO Create `pandas.DataFrame` containing contents of
        # `self.list_store`.
        pass


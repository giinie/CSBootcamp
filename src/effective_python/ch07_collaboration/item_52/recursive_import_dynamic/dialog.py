class Dialog(object):
    def __init__(self):
        pass


save_dialog = Dialog()


def show():
    import app  # Dynamic import
    save_dialog.save_dir = app.prefs.get('save_dir')
    print('Showing the dialog!')

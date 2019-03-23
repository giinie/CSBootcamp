import app


class Dialog(object):
    def __init__(self):
        pass


save_dialog = Dialog()


def show():
    print('Showing the dialog!')


def configure():
    save_dialog.save_dir = app.prefs.get('save_dir')

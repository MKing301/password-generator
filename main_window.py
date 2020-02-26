import sys
import random
import string
import json
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPlainTextEdit


class PasswordWindow(QMainWindow):
    """Password Window."""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle('Password List')
        self.setGeometry(30, 30, 900, 400)


class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Password Genearator')
        self.setGeometry(10, 10, 1000, 800)
        self._createMenu()
        self._createStatusBar()

    def _createMenu(self):
        """ Create menubar. """

        file_menu = self.menuBar().addMenu("File")

        # File Menu - New
        new_action = QAction("&New", self)
        new_action.setStatusTip('Create a new password.')
        new_action.setShortcut('Ctrl+Shift+N')
        new_action.triggered.connect(self.file_new)
        file_menu.addAction(new_action)

        # File Menu - Open
        open_action = QAction("Open", self)
        open_action.setStatusTip('Open password file.')
        open_action.setShortcut('Ctrl+Shift+O')
        open_action.triggered.connect(self.file_open)
        file_menu.addAction(open_action)

        # File Menu - Save
        save_action = QAction("&Save", self)
        save_action.setStatusTip('Save password file.')
        save_action.setShortcut('Ctrl+Shift+S')
        save_action.triggered.connect(self.file_save)
        file_menu.addAction(save_action)

        # File Menu - Delete
        delete_action = QAction("Delete", self)
        delete_action.setStatusTip('Delete password.')
        delete_action.triggered.connect(self.file_delete)
        file_menu.addAction(delete_action)

        file_menu.addSeparator()

        # File Menu - Exit
        exit_action = QAction("&Exit", self)
        exit_action.setStatusTip('Exit application.')
        exit_action.setShortcut('Ctrl+Shift+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # About Menu - Help
        about_action = QAction("About", self)
        about_action.setStatusTip('Brief summary about app.')
        about_action.triggered.connect(self.about_help)
        help_menu = self.menuBar().addMenu("Help")
        help_menu.addAction(about_action)

    def _createStatusBar(self):
        """ Create Status Bar """
        status = QStatusBar()
        status.showMessage("Status Bar Area")
        self.setStatusBar(status)

    def file_new(self):
        """ Display fields to capture user data to generate a password """
        # Text box to capture length of password being requested
        self.size_textbox = QLineEdit(self)
        self.size_textbox.move(100, 50)
        self.size_textbox.show()

        # Label for text to capture password length
        self.size_label = QLabel('Password Length', self)
        self.size_label.resize(self.size_label.minimumSizeHint())
        self.size_label.move(210, 50)
        self.size_label.show()

        # Radio button to request PIN
        self.pin_radiobtn = QRadioButton('PIN', self)
        self.pin_radiobtn.resize(self.pin_radiobtn.minimumSizeHint())
        self.pin_radiobtn.move(100, 100)
        self.pin_radiobtn.show()

        # Radio button to request alphanumeric password
        self.alphanum_radiobtn = QRadioButton('Alphanumeric', self)
        self.alphanum_radiobtn.resize(self.alphanum_radiobtn.minimumSizeHint())
        self.alphanum_radiobtn.move(100, 150)
        self.alphanum_radiobtn.show()

        ''' Radio button to request alphanumeric password w/ special characters
        password. '''
        self.special_radiobtn = QRadioButton(
            'Alphanumeric w/ special characters', self
            )
        self.special_radiobtn.resize(self.special_radiobtn.minimumSizeHint())
        self.special_radiobtn.move(100, 200)
        self.special_radiobtn.show()

        # Button to generate the password when clicked
        self.btn = QPushButton('Generate Password', self)
        self.btn.resize(self.btn.minimumSizeHint())
        self.btn.clicked.connect(self.on_generate_btn_clicked)
        self.btn.move(250, 275)
        self.btn.show()

        # Non-editable text box to display password or error.
        # This box is hide until password or error is returned.
        self.generated_pwd = QLineEdit(self)
        self.generated_pwd.move(60, 325)
        self.generated_pwd.setEnabled(False)
        self.generated_pwd.resize(700, 32)
        self.generated_pwd.hide()

    def file_open(self):
        """ Open file containing passwords. """
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fname = QFileDialog.getOpenFileName(
            self,
            'QFileDialog.getOpenFileNames()',
            '/home/mfsd1809/Dev/FullStackWebDeveloper/GUI/pass-gen/Files',
            'JSON Files (*.json)',
            options=options)
        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = json.load(f)
                self.pw = PasswordWindow()
                self.app_label = QLabel(self.pw)
                self.app_label.setText('Application - Password')
                self.app_label.resize(self.app_label.minimumSizeHint())
                self.app_label.move(20, 20)
                self.b = QPlainTextEdit(self.pw)
                count = 1
                for app, pwd in data.items():
                    self.b.insertPlainText(str(count) +
                                           '. ' +
                                           app +
                                           ' - ' +
                                           pwd +
                                           '\n')
                    count = count + 1
                self.b.setReadOnly(True)
                self.b.move(20, 50)
                self.b.resize(850, 250)
                self.pw.move(100, 150)
                self.pw.show()

    def file_save(self):
        """ Save application name and password to passwords file """
        app, okPressed = QInputDialog.getText(self,
                                              "Application Name",
                                              "Enter App Name:",
                                              QLineEdit.Normal,
                                              "")
        app = app.lower().strip()
        try:
            if okPressed and app != '' and self.generated_pwd.text() != '':
                # Read JSON file
                with open(
                    '/home/mfsd1809/Dev/FullStackWebDeveloper/GUI/pass-gen/'
                    'Files/passwords.json'
                        ) as r_file:
                    data = json.load(r_file)
                    # print(json.dumps(data, indent=4))

                # Add/Update JSON file
                data.update({app: self.generated_pwd.text()})

                # Write update to JSON file
                with open(
                    '/home/mfsd1809/Dev/FullStackWebDeveloper/GUI/pass-gen/'
                    'Files/passwords.json', 'w'
                        ) as w_file:
                    json.dump(data, w_file, indent=4)

                self.get_msg_box(QMessageBox.Information,
                                 'Success',
                                 'Password saved.')
            elif (okPressed and app == ''):
                self.get_msg_box(QMessageBox.Warning,
                                 'Insufficient Data',
                                 'You did not enter an app name.')
        except Exception:
            self.get_msg_box(QMessageBox.Warning,
                             'Insufficient Data',
                             'No password provided for the app you entered.')

    def file_delete(self):
        """ Delete application name and password from passwords file """
        app, okPressed = QInputDialog.getText(self,
                                              "Application Name",
                                              "Enter App Name:",
                                              QLineEdit.Normal,
                                              "")
        app = app.lower().strip()
        try:
            if okPressed and app != '':
                # Read JSON file
                with open(
                    '/home/mfsd1809/Dev/FullStackWebDeveloper/GUI/pass-gen/'
                    'Files/passwords.json'
                        ) as r_file:
                    data = json.load(r_file)
                    # print(json.dumps(data, indent=4))

                # Delete app/password from JSON file
                del data[app]

                # Write update to JSON file
                with open(
                    '/home/mfsd1809/Dev/FullStackWebDeveloper/GUI/pass-gen/'
                    'Files/passwords.json', 'w'
                        ) as w_file:
                    json.dump(data, w_file, indent=4)

                self.get_msg_box(QMessageBox.Information,
                                 'Success',
                                 'Password deleted.')
            elif (okPressed and app == ''):
                self.get_msg_box(QMessageBox.Warning,
                                 'Insufficient Data',
                                 'You did not enter an app name.')

        except Exception:
            self.get_msg_box(QMessageBox.Warning,
                             'Insufficient Data',
                             'No password provided for the app you entered.')

    def about_help(self):
        """ Display information about application when Help-->About menu item
            is clicked """
        self.get_msg_box(QMessageBox.Information,
                         'About',
                         'This application was created using Python and '
                         'PyQt5.  It is used to generate a password based '
                         'on the user input of length and selected type.')

    def get_msg_box(self, icon, title, msg):
        """ Message box"""
        self.mb = QMessageBox(self)
        self.mb.setIcon(icon)
        self.mb.setWindowTitle(title)
        self.mb.setText(msg)
        self.mb.setStandardButtons(QMessageBox.Ok)
        self.mb.show()

    def get_pin(self, size):
        """Generate random password, numbers only."""
        # Check if input an integer
        if(isinstance(size, int)):
            # Check if input is positive
            if(size < 0):
                self.get_response('You did not enter a positive integer!',
                                  'error')
            elif (size < 4):
                self.get_response('The number must be greater or equal to 4.',
                                  'error')
            else:
                digits = string.digits
                self.get_response(
                    ''.join(random.choice(digits) for i in range(size)),
                    'success')
        else:
            self.get_response('You did NOT enter an integer!', 'error')

    def get_alphanumeric_password(self, size):
        """ Generate random password, alphanumeric only """
        # Check if input an integer
        if(isinstance(size, int)):
            # Check if input is positive
            if(size < 0):
                self.get_response('You did not enter a positive integer!',
                                  'error')
            elif (size < 8):
                self.get_response('The number must be greater or equal to 8.',
                                  'error')
            else:
                letters_and_digits = string.ascii_letters + string.digits
                self.get_response(
                    ''.join(random.choice(
                        letters_and_digits) for i in range(size)
                        ),
                    'success')
        else:
            self.get_response('You did NOT enter an integer!', 'error')

    def get_alphanumeric_with_symbols_password(self, size):
        """ Generate random password, alphanumeric with symbols included """
        # Check if input an integer
        if(isinstance(size, int)):
            # Check if input is positive
            if(size < 0):
                self.get_response('You did not enter a positive integer!',
                                  'error')
            elif (size < 8):
                self.get_response('The number must be greater or equal to 8.',
                                  'error')
            else:
                letters_digits_symbols = (string.ascii_letters +
                                          string.digits +
                                          string.punctuation)
                self.get_response(
                    ''.join(random.choice(
                        letters_digits_symbols) for i in range(size)
                        ),
                    'success')
        else:
            self.get_response('You did NOT enter an integer!', 'error')

    def get_response(self, text, result_type):
        """ Display response from request; password or error in non-editable
            text box """
        self.generated_pwd.setText(text)
        if(result_type == 'error'):
            self.generated_pwd.setStyleSheet("color: rgb(255, 0, 0)")
        else:
            self.generated_pwd.setStyleSheet("color: rgb(0, 153, 0)")
        self.generated_pwd.show()

    def on_generate_btn_clicked(self):
        """ Execute request to generate password with validations """
        try:
            input = self.size_textbox.text().strip()
            if(input == ''):
                self.get_response('You did not enter a value for password '
                                  'length.',
                                  'error')
            else:
                input = int(input)
                if(self.pin_radiobtn.isChecked()):
                    self.get_pin(input)
                elif(self.alphanum_radiobtn.isChecked()):
                    self.get_alphanumeric_password(input)
                elif(self.special_radiobtn.isChecked()):
                    self.get_alphanumeric_with_symbols_password(input)
                else:
                    self.get_response('You must select a password option.',
                                      'error')
        except ValueError:
            self.get_response('You entered a string.',
                              'error')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

student_id = input('Enter your student ID: ')
username = input('Enter your username: ')
new_password = input('Enter your new password: ')
confirm_new_password = input('Confirm you new password: ')
common_words = ('huddersfield', 'justinbieber', 'cheese', 'canalside', student_id, username)

if new_password == confirm_new_password and len(new_password) in range (6,13) and new_password not in common_words:
    print('Password has successfully changed!')
else:
    print('Password change was unsuccessful!')

import pyautogui
import pyperclip
import pandas as pd
from time import sleep

pyautogui.PAUSE = 1

sleep(1)

# open a new tab and access the following link on GDrive
pyautogui.hotkey('ctrl', 't')
pyautogui.write('your_link_here')
pyautogui.press('enter')
sleep(5)

# clicks on the directory
pyautogui.click(1302, 278, 2)
sleep(3)

# downloads the xlsx archive
pyautogui.click(1404, 401)
pyautogui.click(1763, 168)
pyautogui.click(1580, 565, 2)
sleep(3)

# read the xlsx archive and print some informations on it
table = pd.read_excel(r'path_to_your_archive_here')
print(table)
invoicing = table['Valor Final'].sum()
amount = table['Quantidade'].sum()

#send an e-mail using GMail
pyautogui.hotkey('ctrl', 't')
pyautogui.write('gmail.com')
pyautogui.press('enter')
sleep(5)
pyautogui.click(995, 198)
sleep(3)
pyautogui.write('email_address@some_email.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('Relatório de vendas')
pyautogui.press('tab')
email = f'''
Prezados destinatários,
O faturamento foi de {invoicing:,.2f}.
A quantidade de vendas foi de {amount:,}.
Atts, Luiz.
'''
pyperclip.copy(email)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')

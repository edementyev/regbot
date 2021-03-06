from typing import Union

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove


async def send_remove_reply_keyboard(message: types.Message):
    remove_keyboard_stub: types.Message = await message.reply('...',
                                                              reply=False,
                                                              reply_markup=ReplyKeyboardRemove())
    await remove_keyboard_stub.delete()


def events_reply_keyboard(events_list,
                          admin_mode=False,
                          archived=False) -> Union[ReplyKeyboardMarkup, None]:
    max_buttons_in_row = 1
    keyboard = None
    row_list = []
    if len(events_list) > 0:
        i = 0
        for event in events_list:
            button = KeyboardButton(event.title)
            if len(row_list) == i:
                row_list.append([])
            row_list[i].append(button)
            if len(row_list[i]) == max_buttons_in_row:
                i += 1

    if admin_mode:
        if archived:
            row_list.append([button_back_to_events])
        else:
            row_list.append([button_create_new])
            row_list.append([button_view_archive])

    if len(row_list) > 0:
        keyboard = ReplyKeyboardMarkup()
        for row in row_list:
            keyboard.row(*row)
    return keyboard


button_create_new = KeyboardButton('Создать новое')
button_view_archive = KeyboardButton('Архив')

button_back_to_events = KeyboardButton('Вернуться к списку ивентов')

button_cancel = KeyboardButton('Отмена')
keyboard_cancel = ReplyKeyboardMarkup().row(button_cancel)

# Изменить статус ивента
button_status_decrease = InlineKeyboardButton('-', callback_data='-')
button_status_increase = InlineKeyboardButton('+', callback_data='+')
button_current_status = InlineKeyboardButton('', callback_data='status')
status_buttons_list = [button_status_decrease, button_current_status, button_status_increase]


def status_buttons(current_status: int):
    button_current_status.text = 'Статус: ' + str(current_status)
    return status_buttons_list


# Основное меню
button_view_enrolls = InlineKeyboardButton('Список регистраций', callback_data='view_enrolls')
button_publish = InlineKeyboardButton('Сообщение подписчикам', callback_data='publish')


def event_menu_keyboard(event_status: int):
    keyboard = InlineKeyboardMarkup()
    keyboard.row(button_view_enrolls)
    keyboard.row(button_publish)
    keyboard.row(*status_buttons(event_status))
    return keyboard


def append_keyboards(*keyboards) -> InlineKeyboardMarkup:
    result = InlineKeyboardMarkup()
    for keyboard in keyboards:
        for row in keyboard.inline_keyboard:
            result.row(*row)
    return result


# Просмотр регистраций
button_refresh = InlineKeyboardButton('Обновить', callback_data='refresh')
keyboard_refresh = InlineKeyboardMarkup().row(button_refresh)

button_rewind_back = InlineKeyboardButton('<<', callback_data='<<')
button_back = InlineKeyboardButton('<', callback_data='<')
button_forward = InlineKeyboardButton('>', callback_data='>')
button_rewind_forward = InlineKeyboardButton('>>', callback_data='>>')
scroll_buttons_list = [button_rewind_back, button_back, button_forward, button_rewind_forward]

keyboard_scroll = InlineKeyboardMarkup().row(*scroll_buttons_list)

# Сообщение подписчикам
button_publish_confirm = InlineKeyboardButton('Отправить', callback_data='publish_confirm')
button_publish_edit = InlineKeyboardButton('Редактировать', callback_data='publish_edit')
publish_buttons_list = [button_publish_confirm, button_publish_edit]

keyboard_publish = InlineKeyboardMarkup()
keyboard_publish.row(button_publish_confirm)
keyboard_publish.row(button_publish_edit)

button_turn_notifications_off = InlineKeyboardButton('Откл. уведомления', callback_data='turn_notifications_off')
button_turn_notifications_on = InlineKeyboardButton('Вкл. уведомления', callback_data='turn_notifications_on')
toggle_notifications_buttons_list = [button_turn_notifications_off, button_turn_notifications_on]
notifications_buttons_map = {
    True: button_turn_notifications_off,
    False: button_turn_notifications_on,
}
button_enroll = InlineKeyboardButton('Зарегистрироваться', callback_data='enroll')
button_show_all_events = InlineKeyboardButton('Весь список ивентов', callback_data='show_all_events')


def get_notifications_keyboard(flag):
    keyboard = InlineKeyboardMarkup()
    keyboard.row(button_enroll)
    keyboard.row(button_show_all_events)
    keyboard.row(notifications_buttons_map[flag])
    return keyboard

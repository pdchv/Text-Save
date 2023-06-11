import PySimpleGUI as sg
import functions

sg.theme("SystemDefault1")

text_box = sg.Multiline(key="input_box", expand_x=True, expand_y=True)
btn_save = sg.FileSaveAs("Save", default_extension='.txt', file_types=(('Text', '.txt'),),
                         key="FileBrowse", enable_events=True)

window = sg.Window("Simply Text", layout=[[text_box], [btn_save]], font=("Liberation Mono", 12), resizable=True,
                   default_element_size=(50, 20))

while True:
    event, values = window.read()

    match event:
        case "Save" | "FileBrowse":
            content = values["input_box"]
            filepath = values["FileBrowse"]
            functions.save_text(content, filepath)
        case sg.WIN_CLOSED:
            break

window.close()


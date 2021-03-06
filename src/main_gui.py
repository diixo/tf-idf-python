import tkinter as tk
import tkinter.filedialog as tkfd
import os
from tkinter.scrolledtext import ScrolledText
from tf_idf import tf_idf

table = tf_idf()

main_window = tk.Tk()
main_window.title("TD-IDF")
main_window.geometry("1250x620")


def open_filedialog():
    global folder
    folder = tkfd.askdirectory(initialdir=os.path.dirname(__file__) + '/..', )
    entry_dir_name.delete(0, tk.END)
    entry_dir_name.insert(0, folder)
    print(folder)
    return 0


def execute():
    table = tf_idf()
    text_output.delete('1.0', tk.END)
    folder_name = folder
    num_of_files = len([name for name in os.listdir(folder) if os.path.isfile(os.path.join(folder, name))]) + 1
    for x in range(1, num_of_files):
        file_name = folder_name + '/' + str(x).zfill(2) + '.txt'
        table.add_file(file_name)
    top_k = entry_top_k.get()
    top_k = int(top_k)
    for x in range(1, num_of_files):
        target_file = folder_name + '/' + str(x).zfill(2) + '.txt'
        var = 'Top ' + str(top_k) + ' of tf-idf in ' + os.path.basename(target_file) + ' : \n'
        text_output.insert('end', var)
        var = table.get_tf_idf(target_file, top_k)
        text_output.insert('end', var)
        var = '\n\n'
        text_output.insert('end', var)
    keyword = entry_keyword.get()
    var = 'tf-idf of key word "' + keyword + ' : \n'
    text_output.insert('end', var)
    var = table.similarities([keyword])
    for x in var:
        x[0] = os.path.basename(x[0])
    text_output.insert('end', var)
    return 0


if __name__ == "__main__":
    label_dir_name = tk.Label(main_window,
                              text='TXT Folder name:',
                              font=('Microsoft YaHei', 12),
                              width=15,
                              height=1,
                              ).grid(row=0, column=0)
    entry_dir_name = tk.Entry(main_window, width=100)
    entry_dir_name.grid(row=0, column=1)

    label_keyword = tk.Label(main_window,
                             text='Searching Keyword:',
                             font=('Microsoft YaHei', 12),
                             width=15,
                             height=1,
                             ).grid(row=2, column=0)
    entry_keyword = tk.Entry(main_window, width=100)
    entry_keyword.insert(0, '任我行')
    entry_keyword.grid(row=2, column=1)

    label_top_k = tk.Label(main_window,
                           text='Top K:',
                           font=('Microsoft YaHei', 12),
                           width=15,
                           height=1,
                           ).grid(row=3, column=0)
    entry_top_k = tk.Entry(main_window, width=100)
    entry_top_k.insert(0, '20')
    entry_top_k.grid(row=3, column=1)

    button_execute = tk.Button(main_window, text="Execute", width=15, height=1, command=execute).grid(row=3, column=2)
    button_file = tk.Button(main_window, text="Browse", width=15, height=1, command=open_filedialog).grid(row=0,
                                                                                                          column=2)

    text_output = ScrolledText(main_window, width=135, height=25, undo=True, font=('Microsoft YaHei', 12))
    text_output.grid(row=4, column=0, columnspan=4)
    text_output.tag_add("start", "1.8", "1.13")
    text_output.tag_config("start", background="black", foreground="white")

    main_window.mainloop()

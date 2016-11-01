try:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog
except ImportError:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import filedialog
import FunKiiU as fnku

PhotoImage=tk.PhotoImage

class RootWindow(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self)
        self.download_list=[]
        self.nb = ttk.Notebook(self)
        tab1 = ttk.Frame(self.nb)
        self.tab2 = ttk.Frame(self.nb)
        tab3 = ttk.Frame(self.nb)
        self.nb.add(tab1,text="Welcome")
        self.nb.add(self.tab2,text="Download")
        self.nb.add(tab3,text="Options")
        self.nb.pack(fill="both", expand=True)
        self.output_dir=tk.StringVar()
        self.retry_count=tk.IntVar(value=3)
        self.patch_demo=tk.BooleanVar(value=True)
        self.patch_dlc=tk.BooleanVar(value=True)
        self.skip_file=tk.BooleanVar(value=True)

        # Tab 1
        t1_frm1=ttk.Frame(tab1)   
        t1_frm2=ttk.Frame(tab1)
        t1_frm3=ttk.Frame(tab1)
        t1_frm4=ttk.Frame(tab1)
        t1_frm5=ttk.Frame(tab1)
        t1_frm6=ttk.Frame(tab1)
        self.img = PhotoImage(file='logo.gif')
        logo=ttk.Label(t1_frm1,image=self.img).pack()
        lbl=ttk.Label(t1_frm2,justify='center',text='This is a simple GUI by dojafoja that was written for FunKiiU.\nCredits to cearp for writing FunKiiU and cerea1killer for rewriting\n it in way that made writing a GUI much easier.').pack()
        lbl=ttk.Label(t1_frm3,justify='center',text='If you plan on using an online methond to obtain keys or tickets\n then FunKiiU will need to know the name of *that key site*. If you\nhaven\'t already provided the address to the key site, you MUST do so\nbelow before proceeding. You only need to provide this information once!').pack(pady=15)
        lbl=ttk.Label(t1_frm4,text='Enter the name of *that key site*. Something like wiiu.thatkeysite.com').pack(pady=15,side='left')
        lbl=ttk.Label(t1_frm5,text='http://').pack(pady=15,side='left')
        self.keysite_box=ttk.Entry(t1_frm5,width=40)
        self.keysite_box.pack(pady=15,side='left')
        btn=ttk.Button(t1_frm6,text='submit',command=self.submit_key_site).pack()
        t1_frm1.pack()
        t1_frm2.pack()
        t1_frm3.pack()
        t1_frm4.pack()
        t1_frm5.pack()
        t1_frm6.pack()
        
        # Tab2
        t2_frm1=ttk.Frame(self.tab2)   
        t2_frm2=ttk.Frame(self.tab2)
        t2_frm3=ttk.Frame(self.tab2)
        t2_frm4=ttk.Frame(self.tab2)
        t2_frm5=ttk.Frame(self.tab2)
        t2_frm6=ttk.Frame(self.tab2)
        lbl=ttk.Label(t2_frm1,text='Enter as many Title ID\'s as you would like to the list. Entering a key is optional and only needed if you are NOT using\nthe online keys or online tickets method. If you are NOT using one of the online methods, then you must provide\na key for every title you add to the list or it will fail.').pack(padx=5,pady=7)
        lbl=ttk.Label(t2_frm1,text='Title ID:').pack(padx=5,pady=7,side='left')
        self.id_box=ttk.Entry(t2_frm1,width=40)
        self.id_box.pack(padx=5,pady=5,side='left')
        btn=ttk.Button(t2_frm1,text='Add to list',command=self.add_to_list).pack(padx=5,pady=5,side='left')
        lbl=ttk.Label(t2_frm2,text='Key:').pack(padx=5,pady=7,side='left')
        self.key_box=ttk.Entry(t2_frm2,width=40)
        self.key_box.pack(padx=5,pady=5,side='left')
        lbl=ttk.Label(t2_frm3,text='Download list:').pack()
        dl_scroller=ttk.Scrollbar(t2_frm3,orient='vertical')
        dl_scroller.pack(side='right',fill='y')
        self.dl_listbox=tk.Listbox(t2_frm3,width=40,height=12)
        self.dl_listbox.pack(fill='y')
        self.dl_listbox.config(yscrollcommand=dl_scroller.set)
        dl_scroller.config(command=self.dl_listbox.yview)
        btn=ttk.Button(t2_frm4,text='Remove selected',command=self.remove_from_list).pack(padx=20,pady=10,side='left',anchor='w')
        btn=ttk.Button(t2_frm4,text='Clear list',command=self.clear_list).pack(padx=20,pady=10,side='left')
        lbl=ttk.Label(t2_frm5,text='Add an entry to the download list one at a time.\nWhen you are done, click on a download button\nbelow based on your preferred method. Don\'t\nforget to visit the options tab before you\ndownload.').pack(padx=20,pady=10)
        #btn=ttk.Button(t2_frm5,text='ALL',width=4,command=lambda:self.download_clicked(4)).pack(anchor='w')
        btn=ttk.Button(t2_frm6,text='Download using online tickets',width=30,command=lambda:self.download_clicked(1)).pack(padx=5,pady=10,side='left')
        btn=ttk.Button(t2_frm6,text='Download using online keys',width=30,command=lambda:self.download_clicked(2)).pack(padx=5,pady=10,side='left')
        btn=ttk.Button(t2_frm6,text='Download using entered keys',width=30,command=lambda:self.download_clicked(3)).pack(padx=5,pady=10,side='left')
        t2_frm1.grid(row=1,column=1,columnspan=2,sticky='w')
        t2_frm2.grid(row=2,column=1,sticky='w')
        t2_frm3.grid(row=3,column=2,rowspan=3,sticky='e')
        t2_frm4.grid(row=6,column=2,padx=10,sticky='e')
        t2_frm5.grid(row=3,column=1,sticky='w')
        #t2_frm6.grid(row=6,column=1,pady=10,sticky='w')
        t2_frm6.grid(row=8,column=1,columnspan=2,sticky='w')
        
        # Tab3
        t3_frm1=ttk.Frame(tab3)
        t3_frm2=ttk.Frame(tab3)
        t3_frm3=ttk.Frame(tab3)
        t3_frm4=ttk.Frame(tab3)
        t3_frm5=ttk.Frame(tab3)
        t3_frm6=ttk.Frame(tab3)
        t3_frm7=ttk.Frame(tab3)
        lbl=ttk.Label(t3_frm1,text='To use the default output directory, leave the entry blank').pack(padx=5,pady=10,side='left')
        lbl=ttk.Label(t3_frm2,text='Output directory').pack(padx=5,pady=5,side='left')
        self.out_dir_box=ttk.Entry(t3_frm2,width=35,textvariable=self.output_dir)
        self.out_dir_box.pack(padx=5,pady=5,side='left')
        btn=ttk.Button(t3_frm2,text='Browse',command=self.get_output_directory).pack(padx=5,pady=5,side='left')
        lbl=ttk.Label(t3_frm3,text='Retry count:').pack(padx=5,pady=5,side='left')
        self.retry_count_box=ttk.Combobox(t3_frm3,state='readonly',width=5,values=range(10),textvariable=self.retry_count)
        self.retry_count_box.set(3)
        self.retry_count_box.pack(padx=5,pady=5,side='left')
        lbl=ttk.Label(t3_frm4,text='Patch demo play limit:').pack(padx=5,pady=5,side='left')
        self.patch_demo_true=ttk.Radiobutton(t3_frm4,text='Yes',variable=self.patch_demo,value=True)
        self.patch_demo_false=ttk.Radiobutton(t3_frm4,text='No',variable=self.patch_demo,value=False)
        self.patch_demo_true.pack(padx=5,pady=5,side='left')
        self.patch_demo_false.pack(padx=5,pady=5,side='left')
        #self.patch_demo_box=ttk.Combobox(t3_frm3,state='readonly',width=5,values=('Yes','No'))
        #self.patch_demo_box.pack(padx=5,pady=10,side='left')
        #self.patch_demo_box.set('Yes')
        lbl=ttk.Label(t3_frm5,text='Patch DLC:').pack(padx=5,pady=5,side='left')
        #self.patch_dlc_box=ttk.Combobox(t3_frm4,state='readonly',width=5,values=('Yes','No'))
        #self.patch_dlc_box.pack(padx=5,pady=10,side='left')
        #self.patch_dlc_box.set('Yes')
        self.patch_dlc_true=ttk.Radiobutton(t3_frm5,text='Yes',variable=self.patch_dlc,value=True)
        self.patch_dlc_false=ttk.Radiobutton(t3_frm5,text='No',variable=self.patch_dlc,value=False)
        self.patch_dlc_true.pack(padx=5,pady=5,side='left')
        self.patch_dlc_false.pack(padx=5,pady=5,side='left')
        lbl=ttk.Label(t3_frm6,text='Existing files:').pack(padx=5,pady=5,side='left')
        self.file_skip_true=ttk.Radiobutton(t3_frm6,text='Skip',variable=self.skip_file,value=True)
        self.file_skip_false=ttk.Radiobutton(t3_frm6,text='Overwrite',variable=self.skip_file,value=False)
        self.file_skip_true.pack(padx=5,pady=5,side='left')
        self.file_skip_false.pack(padx=5,pady=5,side='left')      
        lbl=ttk.Label(t3_frm7,text='Download ALL titles on NUS except system titles:').pack(pady=70,side='left')
        btn=ttk.Button(t3_frm7,text='Go',width=4,command=lambda:self.download_clicked(4)).pack(pady=20,side='left')
        
        t3_frm1.grid(row=1,column=1,sticky='w')
        t3_frm2.grid(row=2,column=1,sticky='w')
        t3_frm3.grid(row=3,column=1,sticky='w')
        t3_frm4.grid(row=4,column=1,sticky='w')
        t3_frm5.grid(row=5,column=1,sticky='w')
        t3_frm6.grid(row=6,column=1,sticky='w')
        t3_frm7.grid(row=7,column=1,sticky='w')

    def sanity_check_input(self,val,chktype):
        try:
            if chktype == 'title':
                if len(val) == 16:
                    val=int(val,16)
                    return True
            elif chktype =='key':
                if len(val) == 32:
                    val=int(val,16)
                    return True
            else:
                return False
        except ValueError:
            return False
        
    def add_to_list(self):
        titleid = self.id_box.get().strip()
        if self.sanity_check_input(titleid,'title'):
            pass
        else:
            print('Bad Title ID. Must be a 16 digit hexadecimal.')
            return
        key=self.key_box.get().strip()
        if key == '': key=None
        else:
            if self.sanity_check_input(key,'key') or not key:
                pass
            else:
                print('Bad Key. Must be a 16 digit hexadecimal.')
                return
        entry=(titleid,key)
        if not entry in self.download_list: self.download_list.append(entry)
        self.populate_dl_listbox()

    def remove_from_list(self):
        try:
            index=self.dl_listbox.curselection()
            item=self.dl_listbox.get('active')
            for i in self.download_list:
                if i[0] == item:
                    self.download_list.remove(i)
            self.populate_dl_listbox()
        except IndexError as e:
            print('Download list is already empty')
            print(e)

    def clear_list(self):
        self.download_list=[]
        self.populate_dl_listbox()
        
    def populate_dl_listbox(self):
        self.dl_listbox.delete('0',tk.END)
        for i in self.download_list:
            self.dl_listbox.insert('end',i[0])

    def submit_key_site(self):
        site=self.keysite_box.get().strip()
        if fnku.hashlib.md5(site.encode('utf-8')).hexdigest() == fnku.KEYSITE_MD5:
            print('Correct key site, now saving...')
            config=fnku.load_config()
            config['keysite'] = site
            fnku.save_config(config)
            print('done saving, you are good to go!')
            self.nb.select(self.tab2)
        else:
            print('Wrong key site provided. Try again')

    def get_output_directory(self):
        out_dir=filedialog.askdirectory()
        self.out_dir_box.delete('0',tk.END)
        self.out_dir_box.insert('end',out_dir)
        print(self.id_box.get().strip())
    def download_clicked(self,dl_method):
        title_list=[]
        key_list=[]
        output_dir=self.output_dir.get().strip()
        if len(output_dir)==0:
            output_dir=None
        retry_count=self.retry_count.get()
        patch_demo=self.patch_demo.get()
        patch_dlc=self.patch_dlc.get()
        for i in self.download_list:
            if not i[0] in title_list:
                title_list.append(i[0])
            if i[1]:
                if not i[1] in key_list:
                    key_list.append(i[1])
        if dl_method == 1:
            print(title_list)
            fnku.main(titles=title_list,keys=key_list,onlinetickets=True,output_dir=output_dir,retry_count=retry_count,
                     patch_demo=patch_demo,patch_dlc=patch_dlc)
        elif dl_method == 2:
            fnku.main(titles=title_list,keys=key_list,onlinekeys=True,output_dir=output_dir,retry_count=retry_count,
                     patch_demo=patch_demo,patch_dlc=patch_dlc)
        elif dl_method == 3:
            fnku.main(titles=title_list,keys=key_list,output_dir=output_dir,retry_count=retry_count,
                     patch_demo=patch_demo,patch_dlc=patch_dlc)
        elif dl_method == 4:
            fnku.main(download_all=True,output_dir=output_dir,retry_count=retry_count,
                     patch_demo=patch_demo,patch_dlc=patch_dlc)
            
                
    
        
if __name__ == '__main__':
    root=RootWindow()
    root.title('FunKii-UI')
    root.resizable(width=False,height=False)
    root.mainloop()

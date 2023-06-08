import cv2 as cv
import numpy as np
import os, time
import json
from cut_images_tool import ui_window
import threading

class SharedVariable:
    def __init__(self, dat=None):
        self._value = dat
        self._lock = threading.Lock()

    def setvalue(self, dat):
        with self._lock:
            self._value = dat

    def getvalue(self):
        with self._lock:
            return self._value

    def get_value(self):
        with self._lock:
            return self._value
    pass

""" ------------------------------------------------------------------------------ """
class System:
    def __init__(self, qmain):
        self.win = ui_window.Ui_MainWindow(qmain)
        self.img_idx = SharedVariable(0)
        self.img_cut = SharedVariable(None)  # np.zeros([3,3], dtype=np.uint8)
        self.bt_auto_readnext = SharedVariable(True)
        self.bt_autosave = SharedVariable(False)
        self._image_autosave_name_format = '{base}__{idx}__{num}.jpg'
        self._image_autosave_name_oldname = ['', 0, 0]

        self.is_replace = False
        self.system_running = SharedVariable(False)
        self.system_to_running = SharedVariable(False)

        self.config_ui()
        pass

    def config_ui(self):

        self.btfn_read_autonext()
        self.win.pushButton_autonext.clicked.connect(self.btfn_read_autonext)

        self.win.pushButton_aboveimg.clicked.connect(self.btfn_read_above_image)
        self.win.pushButton_nextimg.clicked.connect(self.btfn_read_next_image)
        self.win.pushButton_start_system.clicked.connect(self.btfn_read_images_path)

        self.btfn_autosave()
        self.win.pushButton_autosave.clicked.connect(self.btfn_autosave)
        self.win.pushButton_cancel.clicked.connect(self.btfn_cancel_image_cut)
        self.win.pushButton_saveimg.clicked.connect(self.btfn_save_image_cut)

        # img = cv.imread('image/a01.png')
        # self._replay_show_image(img=img)
        # img = cv.imread('image/a02.jpg')
        # self._replay_show_image(img=img)
        # self._replay_show_image(imgpath='image/a01.png')
        # self._replay_show_image(imgpath='image/a02.jpg')
        # self.win.lineEdit_imgsave_path
        self.win.lineEdit_imgread_path.setPlaceholderText(r'输入图片存放的路径文件夹或者文件')  # .setPlaceholderText("Enter text here")
        self.win.lineEdit_imgsave_path.setPlaceholderText('设置用于保存裁剪图片的存放路径文件夹')
        self._set_images_save_name('a01.jpg')
        pass

    def _reset_state(self):
        self.imageread_path = None
        self.image_files_path = []
        self.imagesave_path = None
        self.imagesave_name = None
        self.img_idx = SharedVariable(0)
        self.img_cut = SharedVariable(None)  # np.zeros([3,3], dtype=np.uint8)

    def _replay_show_image(self, img=None, imgpath=None):
        if img is None and imgpath is None:
            print('No image data or path!')
            return
        element = self.win.label_img_show
        geometry = element.geometry()
        objectName = element.objectName()
        try:
            element.close()
            element.deleteLater()
        except:
            print('ERROR! _replay_show_image')
            pass
        myshow = ui_window.myWindow(self.win.groupBox)
        myshow.setGeometry(geometry)
        myshow.setObjectName(objectName)
        self.win.label_img_show = myshow
        self.win.label_img_show.getImg(img=img, imgpath=imgpath)
        self.win.label_img_show.show()
        # self.is_replace = True

    def _replay_show_label(self):
        element = self.win.label_img_show
        geometry = element.geometry()
        objectName = element.objectName()
        try:
            element.close()
            element.deleteLater()
        except:
            print('ERROR! _replay_show_image')
            pass
        myshow = ui_window.BorderLabel(self.win.groupBox)
        myshow.setGeometry(geometry)
        myshow.setObjectName(objectName)
        self.win.label_img_show = myshow
        self.win.label_img_show.show()

    def show_image(self, img=None, imgpath=None):
        if not self.is_replace:
            self. _replay_show_image(img=img, imgpath=imgpath)
        else:
            self.win.label_img_show.getImg(img=img, imgpath=imgpath)
            self.win.label_img_show.show()
        pass

    def _get_images_read_path(self):
        path = self.win.lineEdit_imgread_path.text()
        if path is None or len(path)<1:
            self.imageread_path = None
            self.image_files_path = []
        else:
            self.imageread_path = path
            if os.path.isfile(path): self.image_files_path = [path]
            else:
                files = os.listdir(path)
                self.image_files_path = [os.path.join(path, f) for f in files]
        print(f'{len(self.image_files_path)} images were found in: {path}')
        return path

    def _get_images_save_path(self):
        path = self.win.lineEdit_imgsave_path.text()
        if path is None or len(path) < 1:
            self.imagesave_path = None
        else:
            self.imagesave_path = path
        # print(f'New image will save in: {path}.')
        return path

    def _get_images_save_name(self):
        path = self.win.lineEdit_imgsave_name.text()
        if path is None or len(path) < 1:
            self.imagesave_name = None
        else:
            self.imagesave_name = path
            os.makedirs(self.imagesave_path, exist_ok=True)
            # print(f'New image name will save: {path}.')
        return path

    def _set_images_save_name(self, text):
        self.win.lineEdit_imgsave_name.setText(text)
        self.win.lineEdit_imgsave_name.show()
        return

    def _show_image_of_idx(self, idx=None):
        if idx is None: idx = self.img_idx.get_value()
        file = self.image_files_path[idx]
        # print(f'showing image file [{idx}]: ', file)
        img = cv.imread(file)
        self.img_Height, self.img_Width = img.shape[:2]
        # print(f'image height={self.img_Height}, width={self.img_Width}')
        self.show_image(img=img)

    def btfn_read_images_path(self):
        """ 系统启动首先函数 """
        if not self.system_running.getvalue():
            print(' system starting...')
            self._get_images_read_path()
            self._get_images_save_path()
            self._get_images_save_name()
            self.win.pushButton_start_system.setText('运行中')
            self.system_running.setvalue(True)
            self.system_to_running.setvalue(True)
            self.btfn_read_above_image()
        else:
            # print(' system is running.')
            self.win.pushButton_start_system.setText('读取')
            self.system_to_running.setvalue(False)
            self.system_running.setvalue(False)
            self._replay_show_label()
            self._reset_state()
        pass

    def btfn_read_above_image(self):
        if not self.system_running.getvalue(): return
        idx = self.img_idx.get_value()
        idx2 = idx-1 if idx-1>0 else 0
        self.img_idx.setvalue(idx2)
        # print(f'read image above. [{idx}]--[{idx2}]')
        if not self.bt_auto_readnext.get_value():
            self._show_image_of_idx()
            self.fn_auto_show_save()


    def btfn_read_next_image(self):
        if not self.system_running.getvalue(): return
        idx = self.img_idx.get_value()
        idx2 = idx+1 if idx+1<len(self.image_files_path) else len(self.image_files_path)-1
        self.img_idx.setvalue(idx2)
        # print(f'read image next. [{idx}]--[{idx2}]')
        if not self.bt_auto_readnext.get_value():
            self._show_image_of_idx()
            self.fn_auto_show_save()
        # else:


    def btfn_read_autonext(self):
        sta = self.bt_auto_readnext.get_value()
        if sta:
            self.bt_auto_readnext.setvalue(False)
            self.win.pushButton_autonext.setText('手动')
        # else:
        #     self.bt_auto_readnext.setvalue(True)
        #     self.win.pushButton_autonext.setText('自动')
        pass

    def btfn_autosave(self):
        sta = self.bt_autosave.get_value()
        if sta:
            self.bt_autosave.setvalue(False)
            self.win.pushButton_autosave.setText('手动保存模式')
        else:
            self.bt_autosave.setvalue(True)
            self.win.pushButton_autosave.setText('自动保存模式')
        pass

    def btfn_save_image_cut(self):
        if not self.system_running.getvalue(): return
        self._get_images_save_name()
        if self.imagesave_path is None: return
        file = os.path.join(self.imagesave_path, self.imagesave_name)
        img = self.img_cut.get_value()
        if img is not None:
            print('image cut save in:', file)
            cv.imwrite(file, img)

    def btfn_cancel_image_cut(self):
        if not self.system_running.getvalue(): return
        """ 重新显示 """
        self._show_image_of_idx()


    def fn_auto_show_save(self):
        def func():
            for i in range(40):
                # if self.bt_auto_readnext.get_value():
                #     self.btfn_read_next_image()
                #     self._show_image_of_idx()
                #
                if self.bt_autosave.get_value():
                    idx = self.img_idx.get_value()
                    basename = os.path.basename(self.image_files_path[idx])
                    basename = basename[:str(basename).rfind('.')]
                    if self._image_autosave_name_oldname[0] == basename and self._image_autosave_name_oldname[1] == idx:
                        self._image_autosave_name_oldname[2] = self._image_autosave_name_oldname[2] + 1
                    else:
                        self._image_autosave_name_oldname = [basename, idx, 0]
                    num = self._image_autosave_name_oldname[2]
                    new_name = self._image_autosave_name_format.format(base=basename, idx=idx, num=num)
                    self._set_images_save_name(new_name)
                else: break
                get_data = False
                ''' 等待绘制 '''
                while True:
                    try:
                        if self.win.label_img_show.get_state_ready():
                            get_data = True
                            break
                    except: pass
                    if not self.bt_autosave.get_value() or not self.system_to_running.get_value(): break
                    cv.waitKey(20)

                # print('=== mask finish.')
                if get_data:
                    pts = self.win.label_img_show.get_mask_positon()
                    [x1,y1], [x2, y2] = pts[0], pts[1]
                    x11, x22 = min(x1,x2), max(x1, x2)
                    y11, y22 = min(y1,y2), max(y1,y2)
                    idx = self.img_idx.get_value()
                    file = self.image_files_path[idx]
                    img = cv.imread(file)
                    mask_img = img[y11:y22, x11:x22,:]
                    self.img_cut.setvalue(mask_img)
                    self.btfn_save_image_cut()
                    cv.imshow('image', mask_img)
                    cv.waitKey(10)

                if not self.bt_autosave.get_value() or not self.system_to_running.get_value():
                    cv.destroyAllWindows()
                    break
        self.auto_save_thrad =threading.Thread(target=func)
        self.auto_save_thrad.setDaemon(True)
        self.auto_save_thrad.start()
        pass
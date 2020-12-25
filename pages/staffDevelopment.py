from base.basePage import Basepage
from selenium.webdriver.common.by import By
from pages.login_taidii import Login
import time



class StaffDevelopment(Basepage):

    # 单例模式
    # ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        super().__init__()
        # 员工管理
        self.staff_management = (By.CSS_SELECTOR,".td-sidebar ul>li:nth-of-type(3)")
        # 教师成长
        self.staffdevelopment = (By.CSS_SELECTOR,".td-sidebar ul>div:nth-of-type(3) li:nth-child(4)")
        # 职工培训
        self.staff_train = (By.CSS_SELECTOR,".td-navbar li:nth-child(2)")
        #创建课程
        self.create_course = (By.CSS_SELECTOR,".base-green-btn")
        #创建页面-标题框
        self.course_title = (By.ID,"course_title")
        #创建页面-选择线上课程
        self.online_course = (By.CSS_SELECTOR,"div>.js_course_create_type:nth-child(1)")
        #创建页面-线下课程
        self.offline_course = (By.CSS_SELECTOR,"div>.js_course_create_type:nth-child(2)")
        #创建页面-点击下一步
        self.next_button = (By.ID,"id_course_create_next")
        #学习期限框
        self.allotted_time = (By.ID,"id-learn-limit")
        #课程简介输入框
        self.course_introdution = (By.ID,"id_course_textarea")
        #添加课时
        self.add_course = (By.ID,"add_content")
        #点击视频、音频按钮
        self.video = (By.CSS_SELECTOR,".modal-body>.show_type_or_content>div.activity_create_type:nth-child(1)")
        #点击图片、文本文件上传
        self.picture = (By.CSS_SELECTOR,".modal-body>.show_type_or_content>div.activity_create_type:nth-child(2)")
       #选择后，点击下一步
        self.next_step = (By.ID,"id-next-content")

        #选择上传视频后
        #输入上传视频、音频或pdf的名称
        self.session_name = (By.ID,"id_show_type_or_content_1")
        #上传视频、音频、pdf按钮
        self.upload = (By.ID,"id_uploag_file_a")

        #点击保存
        self.course_save = (By.ID,"id-save-content")
        #点击发布
        self.publish = (By.CSS_SELECTOR,".course_set_title>.group>a:nth-child(4)")

        #获取全部列表
        self.get_courselist = (By.CSS_SELECTOR,"#js-other-course-list>div span.js-show-name")





    #进入教师成长模块
    def go_to_staff_development(self):
        self.move_to_ele(self.staff_management)
        self.ele_click(self.staffdevelopment)

    #直接进入职工培训界面
    def go_to_staff_train(self):
        self.go_to_staff_development()
        self.ele_click(self.staff_train)

    def create_online_course(self,coursename="自动默认课程名称",allotted=1,course_inf="自动随便",session_inf="自动视频"):
        self.ele_click(self.create_course)
        self.ele_input(self.course_title,coursename)
        self.ele_click(self.online_course)
        self.ele_click(self.next_button)
        self.ele_input(self.allotted_time,allotted)
        self.ele_input(self.course_introdution,course_inf)
        self.ele_click(self.add_course)
        self.ele_click(self.video)
        self.ele_click(self.next_step)
        self.ele_input(self.session_name,session_inf)
        self.upload_text(self.upload,"E:\\taidiiStaffdevelopment\\abca.mp4 \n\n")
        time.sleep(1)
        self.ele_click(self.course_save)
        time.sleep(0.5)
        self.js_execute("window.scroll(0,0)")
        self.ele_click(self.publish)
        return coursename
# staff = StaffDevelopment()
    def course_list(self):
        courlist = self.get_elements(self.get_courselist)
        res = [i.text for i in courlist]
        return res
        



if __name__ == "__main__":
    staff = StaffDevelopment()
    login_sys =Login()
    login_sys.login_sys()
    # staff.go_to_staff_development()
    staff.go_to_staff_train()
    staff.create_online_course()
    staff.course_list()








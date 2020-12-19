from base.base_page import Base
import page


"""
负责管理中心模块的逻辑
"""

class MCPage(Base):
    # 点击进入管理中心模块
    def click_MC(self):
        # 1.点击管理中心菜单
        self.click_ele(page.mc_center)




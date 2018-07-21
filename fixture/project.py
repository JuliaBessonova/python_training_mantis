

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def go_to_manage_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage Projects").click()

    def create(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()

    def fill_project_form(self):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("name")
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys("description")

    def submit_project_creation(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value="Add Project"]').click()

    def return_to_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[2]").click()






